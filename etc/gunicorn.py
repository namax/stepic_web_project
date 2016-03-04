# CONFIG = {
#     # 'mode': 'wsgi',
#     'working_dir': '/Projects/python/stepic_web_tech/stepic_web_project',
#     'python': '/usr/bin/python3',
#     'args': (
#         '--bind=0.0.0.0:8080',
#         '--workers=2',
#         '--timeout=60',
#         'hello:app',
#     ),
# }
# for django /usr/local/bin/gunicorn -b :8000 -w 4 ask.wsgi:application

command = '/usr/bin/gunicorn'
pythonpath = '/home/box/web'
bind = '0.0.0.0:8080'
workers = 2
