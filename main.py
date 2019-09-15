# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_flex_quickstart]
import logging

from flask import Flask, request

app = Flask(__name__)

db = dict()
db['odometer'] = None
db['fuel_level'] = None
db['longitude'] = None
db['latitude'] = None

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'GET': # for use by frontend
        param = str(request.args.get('param', '')) #args: key, default
        return str(db.get(param, 'error'))

    elif request.method == 'POST': # for inputting incoming data to db
        req_data = request.get_json()
        name = str(req_data['name'])
        value = req_data['value']

        if name in db:
            db[name] = value
            return name + ' value set to ' + str(value)
        else:
            return 'unable to insert value'

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_flex_quickstart]
