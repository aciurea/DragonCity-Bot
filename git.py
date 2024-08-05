import subprocess

def update_project():
    process = subprocess.check_output(['git', 'pull'])

    print(process)