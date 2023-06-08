import subprocess
import sys

def install_dependencies():
    dependencies = [
        'discord.py==1.7.3',
        'requests',
        'colorama',
        'psutil',
        'pyperclip'
    ]

    for dependency in dependencies:
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', dependency])
            print(f"{dependency} successfully installed.")
        except subprocess.CalledProcessError as e:
            print(f"Error while installing {dependency}: {str(e)}")

if __name__ == '__main__':
    print("Install dependencies...")
    install_dependencies()
    print("Done.")