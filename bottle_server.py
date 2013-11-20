import bottle
from bottle import *

from time import sleep
import subprocess

@route('/stream')
def stream():
    proc = subprocess.Popen(
        'ls && sleep 1 && ls && sleep 2 && ls && ls && sleep 5',
        shell=True,
        stdout=subprocess.PIPE,
    )
    while proc.poll() is None:
        output = proc.stdout.readline()
        yield output + "\r\n;"
    # for i in xrange(1,10):
    #     yield '%s<br>\n' % i
    #     sleep(1)

bottle.debug(True)
run(host='0.0.0.0', port=8000, reloader=True)
