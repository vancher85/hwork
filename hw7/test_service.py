import json
import random

import requests
from flask import Flask, abort, Response

app = Flask(__name__)


@app.route('/users/<user_id>/bans/', methods=['GET'], strict_slashes=False)
def user_bans(user_id):
    user = requests.get('http://{0}/spa/accounts/{1}/'.format(SPA_HOST, user_id)).json()
    if not user.get('id'):
        abort(Response(json.dumps({'exception': 'USER NOT FOUND IN SPA!'})))
    return {'user': user['id'], 'bans': [{'type': 'permanent', 'id': random.randint(1, 1000)}]}


@app.route('/spa/accounts/<user_id>/', methods=['GET'], strict_slashes=False)
def spa_mock(user_id):
    return {
        'id': int(user_id),
        'name': "Sker",
        'state': 15728945,
        'created_at': 1343998793,
        'activated_at': 1343998793,
        'bigworld_id': None,
        'warplane_id': int(user_id),
        'warship_id': None,
        'blitz_id': None,
        'externals': []
    }


if __name__ == '__main__':
    SPA_HOST = 'spa.ru.wott.iv'
    #SPA_HOST = '127.0.01:8080'
    app.run(host='0.0.0.0', port=8080)