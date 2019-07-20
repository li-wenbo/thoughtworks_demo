import multiprocessing
import os
import os

# server
pidfile = 'gun.pid'
backlog = 512
bind = "0.0.0.0:{}".format(os.environ.get('HTTP_PORT'))

# log
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(L)s ' \
                    '"%({X-Forwarded-Proto}i)s" "%({X-Forwarded-For}i)s" "%({X-Real-IP}i)s"'
accesslog = '-'

errorlog = '-'
loglevel = 'debug'

# worker
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "gevent"
worker_connections = 1024
