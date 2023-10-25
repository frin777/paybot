import discord
from discord.ext import commands
from PySide6.QtCore import QThread, Signal
from discord import option
import database_module
import asyncio

session = database_module.Session()



class Buttons(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        
    @discord.ui.button(label="Отменить заявку", custom_id="button-1", style=discord.ButtonStyle.danger)
    async def gray_button(self, button, interaction):
        button.disabled = True
        button.label = "Отменено"
        embed = discord.Embed(
                description = f'**Заявка отменена**',
                colour = discord.Colour.from_rgb(255, 0, 0)
            )
        await interaction.response.edit_message(view=self, embed=embed)
        print(interaction.message.id)
        # await interaction.message.delete()
        user_id = self.update_order(interaction.message.id)
        # self.balance_change(user_id, '-', summ)
        if user_id:
            self.balance_change(user_id[0], '-', user_id[1])


    def balance_change(self, user, sign, amount):
        try:
            # Поиск пользователя по имени
            balance = session.query(database_module.User).filter_by(id=user).first()

            if balance:
                if sign == '+':
                    balance.balance = balance.balance + int(amount)
                elif sign == '-' and balance.balance >= 0:
                    balance.balance = balance.balance - int(amount)
                session.commit()
                print(f"Баланс пользователя {user} изменен {sign} {amount}")
                return 'ok'
            else:
                print(f"Пользователь с id {user} не найден.")

        except Exception as e:
            print(f"Ошибка при обновлении данных баланса: {e}")
            session.rollback()
        finally:
            session.close()

    def update_order(self, msg_id):
        session = database_module.Session()

        try:
            # Поиск пользователя по имени
            order = session.query(database_module.Order).filter_by(msg_id=msg_id).first()

            if order:
                if msg_id:
                    order.deleted = True
                session.commit()
                print(f"Ордер {order.id} отменен")
                return [order.user_id, order.amount]
            else:
                print(f"Ордер с сообщением {msg_id} не найден.")

        except Exception as e:
            print(f"Ошибка при обновлении данных ордера: {e}")
            session.rollback()
        finally:
            session.close()



class BotThread(QThread):
    message_signal = Signal(str, str)  # Signal for author and message
    log_signal = Signal(str)  # Signal for logging
    payment_signal = Signal(str, int, int, str)
    cancel_order_signal = Signal(int)

    def __init__(self, TOKEN):
        super().__init__()
        intents = discord.Intents.default()
        intents.messages = True
        intents.guilds = True
        self.bot = commands.Bot(command_prefix='/', intents=intents, activity = discord.CustomActivity(name="/help - Список комманд"))
        self.token = TOKEN

        @self.bot.event
        async def on_ready():
            log_message = f'Logged in as {self.bot.user}'
            self.log_signal.emit(log_message)

        @self.bot.event
        async def on_message_edit(before, after):
            session = database_module.Session()
            get_order_id = session.query(database_module.Order).filter_by(msg_id=after.id).first()
            self.cancel_order_signal.emit(get_order_id.id)
            # print(get_order_id.id)

        @self.bot.event
        async def on_message(message):
            if message.author != self.bot.user:
                self.message_signal.emit(str(message.author), message.content)

        @self.bot.slash_command(description="test pin")
        async def pay(ctx, summ: int, desc: str):
            user = self.find_user_by_name(ctx.author.name)
            if user:
                embed = discord.Embed(
                        description = f'**Заявка на оплату {summ} р успешно создана!**\n Счет: {user.card_number} ({user.bank_name}) \n Примечание: {desc}',
                        colour = discord.Colour.from_rgb(0, 255, 0)
                    )
                ord = self.add_order(0, user.id, ctx.channel.id, summ, desc, False)
                self.balance_change(user.id, '+', summ)
                self.payment_signal.emit(ctx.author.name, ord.id, summ, desc)
                # Отправляем сообщение
                response_message = await ctx.respond(embed=embed, view=Buttons())
                # Получаем ID отправленного сообщения
                msg_id = await response_message.original_response()
                self.update_order(ord.id, msg_id.id)
                
            else:
                embed = discord.Embed(
                        description = '**Ошибка, Сначала нужно добавить счет для оплаты**',
                        colour = discord.Colour.from_rgb(255, 0, 0)
                    )
                await ctx.respond(embed=embed)
        
        @self.bot.slash_command(name='setpayment', description="Добавить/Изменить счет для оплаты")
        @option("number", str, description="Счет")
        @option("payment_method", str, description="Название банка, платежной системы")
        async def set_payment(ctx, number:int, payment_method:str):
            ss = self.add_user(ctx.author.name, ctx.author.id, number, payment_method, False)
            if ss == 'have':
                upd = self.update_user_data(ctx.author.name, new_card_number=number, new_bank_name=payment_method)
                if upd == 'ok':
                    embed = discord.Embed(description = f'Счет **{number} ({payment_method})** обновлен', colour = discord.Colour.from_rgb(0, 255, 0))
                    await ctx.respond(embed=embed)
            if ss == 'ok':
                embed = discord.Embed(description = f'Счет **{number} ({payment_method})** успешно добавлен', colour = discord.Colour.from_rgb(0, 255, 0))
                await ctx.respond(embed=embed)


        @self.bot.slash_command()
        async def dm(ctx, user: discord.User, *, message=None):
            message = message or "This Message is sent via DM"
            try:
                await user.send(message)
                await ctx.send(f"Message sent to {user.name}!")
            except discord.Forbidden:
                await ctx.send(f"Couldn't send a DM to {user.name}. They might have DMs disabled for non-friends or from this server.")
            except Exception as e:
                await ctx.send(f"An error occurred: {str(e)}") 


    def add_order(self, msg_id, user_id, chat_id, amount, desc, deleted=False):
        """Добавляет пользователя в базу данных"""
        session = database_module.Session()

        try:
            new_order = database_module.Order(msg_id=msg_id, user_id=user_id, chat_id=chat_id, amount=amount, desc=desc, deleted=deleted)
            session.add(new_order)
            session.commit()
            print(f"Ордер {new_order.id} успешно добавлен!")
            return new_order
        except Exception as e:
            print(f"Ошибка при добавлении ордера: {e}")
            session.rollback()  # Откатываем изменения в случае ошибки
        finally:
            session.close()  # Закрываем сессию в любом случае


    def balance_change(self, user, sign, amount):
        try:
            # Поиск пользователя по имени
            balance = session.query(database_module.User).filter_by(id=user).first()

            if balance:
                if sign == '+':
                    balance.balance = balance.balance + amount
                elif sign == '-' and balance.balance >= 0:
                    balance.balance = balance.balance - amount
                session.commit()
                print(f"Баланс пользователя {user} изменен {sign} {amount}")
                return 'ok'
            else:
                print(f"Пользователь с id {user} не найден.")

        except Exception as e:
            print(f"Ошибка при обновлении данных баланса: {e}")
            session.rollback()
        finally:
            session.close()

    def update_order(self, order_id, msg_id):
        """Обновляет номер карты и банк для пользователя по имени"""
        session = database_module.Session()

        try:
            # Поиск пользователя по имени
            order = session.query(database_module.Order).filter_by(id=order_id).first()

            if order:
                if msg_id:
                    order.msg_id = msg_id
                session.commit()
                print(f"Msg_id изменен на {order.msg_id}")
                return 'ok'
            else:
                print(f"Пользователь с id {order_id} не найден.")

        except Exception as e:
            print(f"Ошибка при обновлении данных ордера: {e}")
            session.rollback()
        finally:
            session.close()
    

    def add_user(self, username, user_id, card_number, bank_name=None, banned=False):
        """Добавляет пользователя в базу данных"""
        session = database_module.Session()

        try:
            new_user = database_module.User(username=username, userid=user_id, card_number=card_number, bank_name=bank_name, balance=0, banned=banned)
            session.add(new_user)
            session.commit()
            print(f"Пользователь {username} успешно добавлен!")
            return 'ok'
        except Exception as e:
            print(f"Ошибка при добавлении пользователя: {e}")
            session.rollback()  # Откатываем изменения в случае ошибки
            return 'have'
        finally:
            session.close()  # Закрываем сессию в любом случае

    def update_user_data(self, username, new_card_number=None, new_bank_name=None):
        """Обновляет номер карты и банк для пользователя по имени"""
        session = database_module.Session()

        try:
            # Поиск пользователя по имени
            user = session.query(database_module.User).filter_by(username=username).first()

            if user:
                # Изменение атрибутов пользователя, если они предоставлены
                if new_card_number:
                    user.card_number = new_card_number
                if new_bank_name:
                    user.bank_name = new_bank_name

                session.commit()
                print(f"Данные пользователя {username} успешно обновлены!")
                return 'ok'
            else:
                print(f"Пользователь с именем {username} не найден.")

        except Exception as e:
            print(f"Ошибка при обновлении данных пользователя: {e}")
            session.rollback()
        finally:
            session.close()

    def find_user_by_name(self, username):
        """Поиск пользователя по имени"""
        session = database_module.Session()

        try:
            user = session.query(database_module.User).filter_by(username=username).first()
            return user
        except Exception as e:
            print(f"Ошибка при поиске пользователя: {e}")
        finally:
            session.close()

    def run(self):
        self.bot.run(self.token)

    def send_message(self, channel_id, message):
        future = asyncio.run_coroutine_threadsafe(self._send_message(channel_id, message), self.bot.loop)
        try:
            future.result()  # wait for the result of the coroutine
        except Exception as e:
            print(f"Error occurred while sending message: {e}")


    async def _send_message(self, channel_id, message):
        try:
            channel = await self.bot.fetch_channel(channel_id)
            if not channel:
                print(f"Channel with ID {channel_id} not found.")
                return

            await channel.send(message)
            print(f"Message sent to channel ID {channel_id}: {message}")
        except Exception as e:
            print(f"Error sending message: {e}")


    def edit_message(self, channel_id, message_id):
        future = asyncio.run_coroutine_threadsafe(self._edit_message(channel_id, message_id), self.bot.loop)
        try:
            future.result()  # wait for the result of the coroutine
        except Exception as e:
            print(f"Error occurred while editing message: {e}")

    async def _edit_message(self, channel_id, message_id):
        try:
            channel = await self.bot.fetch_channel(channel_id)
            if not channel:
                print(f"Channel with ID {channel_id} not found.")
                return

            message = await channel.fetch_message(message_id)
            if not message:
                print(f"Message with ID {message_id} not found in channel {channel_id}.")
                return
            embed = discord.Embed(description = f'Заявка отменена ботом', colour = discord.Colour.from_rgb(255, 0, 0))
            await message.edit(content=None, embed=embed, view=None)
            print(f"Message with ID {message_id} in channel {channel_id} edited")
        except Exception as e:
            print(f"Error editing message: {e}")