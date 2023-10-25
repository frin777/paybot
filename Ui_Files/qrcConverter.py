import os
import subprocess

class QrcToPyConverter:
    def __init__(self, directory='.', output_directory='.'):
        self.directory = directory
        self.output_directory = output_directory
        # Ensure the output directory exists
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)
    
    def _find_qrc_files(self):
        """Find all .qrc files in the directory and its subdirectories."""
        qrc_files = []
        for root, _, files in os.walk(self.directory):
            for file in files:
                if file.endswith('.qrc'):
                    qrc_files.append(os.path.join(root, file))
        return qrc_files
    
    def convert(self):
        """Convert all .qrc files to .py files."""
        qrc_files = self._find_qrc_files()

        if not qrc_files:
            print("No .qrc files found!")
            return

        for qrc in qrc_files:
            output_py_name = os.path.basename(qrc).replace('.qrc', '_rc.py')
            output_py = os.path.join(self.output_directory, output_py_name)
            command = ['pyside6-rcc', '-o', output_py, qrc]
            subprocess.run(command)
            print(f"Converted {qrc} to {output_py}")

if __name__ == '__main__':
    # Specify the output directory where .py files should be saved
    converter = QrcToPyConverter(output_directory='./Ui')
    converter.convert()
