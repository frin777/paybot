import subprocess
import sys
import os

def compile_with_nuitka(script_name, output_name=None, icon_path=None, app_name=None, file_description=None, file_version=None, product_version=None, standalone=True):
    """
    Compile a Python script using Nuitka.
    """
    # Compile using Nuitka
    command = [sys.executable, '-m', 'nuitka', '--follow-imports', script_name, '--windows-disable-console']
    if standalone:
        command.append('--standalone')
    
    # Enable the PySide6 plugin for Nuitka
    command.append('--enable-plugin=pyside6')

    # Specify output name if provided
    if output_name:
        output_dir = os.path.dirname(script_name)  # Get the directory of the script
        command.append(f'--output-dir={output_dir}')
        command.append(f'--output-filename={output_name}')

    # Add icon if provided
    if icon_path:
        command.append(f'--windows-icon-from-ico={icon_path}')

    # Set application name, file description, and version if provided
    if app_name:
        command.append(f'--windows-company-name={app_name}')
        command.append(f'--windows-product-name={app_name}')
        if file_description:
            command.append(f'--windows-file-description={file_description}')
        if file_version:
            command.append(f'--windows-file-version={file_version}')
        if product_version:
            command.append(f'--windows-product-version={product_version}')

    subprocess.run(command, check=True)

    print(f"Compilation of {script_name} completed!")

if __name__ == "__main__":
    script_to_compile = "main.py"  # Name of your main Python script
    icon_to_use = "Ui_Files/icon20.ico"  # Replace with the path to your .ico file
    application_name = "RT"  # Replace with your desired application name
    file_desc = "RT"  # Replace with your desired file description
    file_version = "1.0"  # Replace with your desired file version
    product_version = file_version  # Replace with your desired product version
    output_exe_name = "RT.exe"  # Desired name for the compiled executable
    compile_with_nuitka(script_to_compile, output_exe_name, icon_to_use, application_name, file_desc, file_version, product_version)
