import os
import subprocess
import threading

class UIConverter:

    def __init__(self, root_dir='.'):
        self.root_dir = root_dir
        self.ui_dir = os.path.join(root_dir, 'ui')

        if not os.path.exists(self.ui_dir):
            os.makedirs(self.ui_dir)

    def _convert_file(self, ui_file_path):
        py_file_name = os.path.basename(ui_file_path).replace('.ui', '_ui.py')
        py_file_path = os.path.join(self.ui_dir, py_file_name)

        command = f"pyside6-uic {ui_file_path} -o {py_file_path}"
        subprocess.call(command, shell=True)
        print(f"Converted {ui_file_path} to {py_file_path}")

        # After converting, change the import statement
        self._replace_import(py_file_path)

    def _replace_import(self, py_file_path):
        with open(py_file_path, 'r') as file:
            file_data = file.read()

        # Replace the target string
        file_data = file_data.replace('import images_rc', 'import Ui.images_rc')

        with open(py_file_path, 'w') as file:
            file.write(file_data)

    def convert_all_files(self):
        threads = []

        for dirpath, _, filenames in os.walk(self.root_dir):
            for filename in filenames:
                if filename.endswith('.ui'):
                    ui_file_path = os.path.join(dirpath, filename)

                    # Create a thread for each file and start it
                    t = threading.Thread(
                        target=self._convert_file, args=(ui_file_path,))
                    t.start()
                    threads.append(t)

        # Wait for all threads to complete
        for t in threads:
            t.join()

if __name__ == "__main__":
    converter = UIConverter()
    converter.convert_all_files()
