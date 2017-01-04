"""
This script runs the BeaconServer application using a development server.
"""

from os import environ
from BeaconServer import app

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)
