# database_module.py
from sqlalchemy import create_engine, Column, Integer, String, Boolean, Sequence
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship, backref
from sqlalchemy import ForeignKey

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    userid = Column(Integer, nullable=False)
    card_number = Column(String(50), nullable=False)
    bank_name = Column(String(100), nullable=True)
    balance = Column(Integer, nullable=False)
    banned = Column(Boolean, default=False)

    # Отношение к заказам. При удалении пользователя, связанные заказы также удаляются.
    orders = relationship('Order', backref='user', cascade='all, delete-orphan')

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, Sequence('order_id_seq'), primary_key=True)
    msg_id =  Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)  # Внешний ключ на таблицу users
    chat_id = Column(Integer, nullable=False)
    amount = Column(String(50), nullable=False)
    desc = Column(String(50), nullable=False)
    deleted = Column(Boolean, default=False)


# Создание базы данных в файле (в данном случае SQLite, сохраненная в файле mydatabase.db)
engine = create_engine('sqlite:///base.db')
Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)



def GetAllUsers():
    session = Session()
    try:
        users = session.query(User).all()
        if users:
            return users
    except Exception as e:
        print(f"Ошибка получения списка пользователя: {e}")
        session.rollback()
    finally:
            session.close()

def GetOneUser(id):
    session = Session()
    try:
        user = session.query(User).filter_by(id=id).first()
        if user:
            return user
    except Exception as e:
        print(f"Ошибка получения пользователя: {e}")
        session.rollback()
    finally:
            session.close()


def GetAllOrders():
    session = Session()
    try:
        orders = session.query(Order).all()
        if orders:
            return orders
    except Exception as e:
        print(f"Ошибка получения списка ордеров: {e}")
        session.rollback()
    finally:
            session.close()

def GetOneOrder(id):
    session = Session()
    try:
        user = session.query(Order).filter_by(id=id).first()
        if user:
            return user
    except Exception as e:
        print(f"Ошибка получения ордера: {e}")
        session.rollback()
    finally:
            session.close()
