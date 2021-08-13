# Simple python application to emulate an information provider, with a client consuming the data it streams.

**Python 3.6 or later is required.**

The only external library used is [Websockets](https://websockets.readthedocs.io/en/stable/) for python.

## **How to use**:

Creating a virtual environment is recommended:

> python -m venv my_venv_path'

Copy/extract/clone the repository files in an empty folder, navegate with the console and type:

> pip install websockets

To start, run on your console

> python server.py

This will create a socket and wait for connections at _ws://localhost:3000_

Then, on a different console, run

> python client.py

The server should start gathering data from the local db - **db.sqlite3** in this case - and stream it through the socket. It will send 5 random rows from the db at the same time, in random intervals from 1 to 5 seconds, until the client closes the connection.

The client will recieve the data and finally will save it on it's own database, **market_saved_data.sqlite3**, located in the same folder.
