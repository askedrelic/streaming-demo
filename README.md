# Streaming Small Responses with Python

Client/server code for streaming HTTP responses.

Server to send a long streaming response written in Bottle and Flask: `bottle_server.py` or `flask_server.py`

Client written in Requests to consume a slow streaming response and print output line by line: `client.py`

# Installation

Clone the repo into a new directory, create a virtualenv, activate it, and install the correct versions.

    $ git clone https://github.com/askedrelic/streaming-demo
    $ cd streaming-demo/
    $ virtualenv .
    $ source bin/activate
    $ pip install -r requirements.txt

Now you can run the server the current shell, but you will need another shell to run the client.

    $ python bottle_server.py
    $ python client.py
