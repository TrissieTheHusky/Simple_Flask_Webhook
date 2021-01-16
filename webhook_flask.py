#!/usr/bin/python3

# Version 1.0
# Author: trojand
# Details: https://trojand.com/simple-webhook-with-flask
# This script listens for and accepts POST requests with data in JSON format

from flask import Flask, request
from datetime import datetime
import json
app = Flask(__name__)


@app.route('/webhook', methods=["POST"])
def webhook():

    try:
        data = request.get_json(force=True)

        if request.content_length < 500:
            logfile = open("webhook.log", 'a')
            logfile.write("Timestamp: "+str(datetime.now()) + "\n")
            logfile.write("Remote Address: "+str(request.remote_addr) + "\n")
            logfile.write(str(request.headers)+json.dumps(data, indent=1)+"\n")
            logfile.write(
                "=============================================================================\n")
            logfile.close()
            return 'CSP Report received.\n'
        else:
            return "Request size too large.\n."
    except Exception as e:
        print("Data not JSON format\n %s" % e)


if __name__ == '__main__':
    # To run on dev/test mode, uncomment below:
    # app.run(host="127.0.0.1", port=29999, debug=False)
    # To run on production (uWSGI), use uncomment below:
    app.run()
