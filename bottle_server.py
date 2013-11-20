import bottle
import subprocess
from time import sleep

@bottle.route('/stream')
def stream():
    proc = subprocess.Popen(
        'echo 1 && sleep 3 && echo 2 && sleep 3 && echo 3',
        shell=True,
        stdout=subprocess.PIPE,
    )
    while proc.poll() is None:
        output = proc.stdout.readline()
        yield output + "\r\n"
    # for i in xrange(1,10):
    #     yield '%s<br>\n' % i
    #     sleep(1)

bottle.debug(True)
bottle.run(host='0.0.0.0', port=8000, reloader=True)
