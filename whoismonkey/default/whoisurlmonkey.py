#!/usr/bin/env python

import os
import json
from flask import Flask, request, jsonify, make_response


app = Flask(__name__)


def queryDomain(domain):
    cmd = 'pwhois --json %s' % domain
    a = os.popen(cmd).read()
    j = json.loads(a)
    return j


@app.route('/query/', methods=['GET'])
def lookupDomain():
    domain = request.args.get('domain')
    x = queryDomain(domain)
    return make_response(jsonify({'Query': x}))


if __name__ == '__main__':
     app.run(host='0.0.0.0'  ,debug= True)

#app.run(port=4300, debug=True)
