import subprocess
import os


if os.path.exists('db.sqlite3'):
    os.remove('db.sqlite3')

subprocess.run(['python', 'crawl_food/crawl.py'])
subprocess.run(['python', 'manage.py', 'makemigrations',
                'account', 'cart', 'orders', 'shop'])
subprocess.run(['python', 'manage.py', 'migrate'])
subprocess.run(['python', 'manage.py', 'convert'])