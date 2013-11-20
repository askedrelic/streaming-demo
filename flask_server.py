from flask import Flask, stream_with_context, Response
from time import sleep
import subprocess

app = Flask(__name__)

@app.route('/stream')
def streamed_response():
    def generate():
        proc = subprocess.Popen(
            'echo 1 && sleep 3 && echo 2 && sleep 3 && echo 3',
            shell=True,
            stdout=subprocess.PIPE,
        )
        while proc.poll() is None:
            output = proc.stdout.readline()
            yield output + "\r\n;"
        # for i in xrange(1,10):
        #     yield '%s<br>\n' % i
        #     sleep(1)
    return Response(stream_with_context(generate()))

app.run(host='0.0.0.0', port=8000, debug=True)
