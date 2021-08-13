Simple python application to emulate an information provider, with a client consuming the data it streams.

Python 3.6 or later is required.
The only external library used is (Websockets)[http://google.com] for python.

To start, run on console/bash 'server.py', it'll create a socket and wait for connections at 'ws://localhost:3000'

Then, on a different console, run the file 'client.py'.

The server should start gathering data from the local db - db.sqlite3 in this case - and stream it through the socket. It will send 5 random rows from the db at the same, in random intervals from 1 to 5 seconds, until the client closes the connection.

The client will recieve the data, display it on the console and finally will save it on it's own database, 'market_saved_data.sqlite3'.
