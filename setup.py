import subprocess
subprocess.run(['pwd'])
subprocess.run(['rm', 'db.sqlite3'])
subprocess.run(['python', 'manage.py', 'migrate'])
subprocess.run(['python', 'manage.py', 'convert'])