from bottle import route, run
import requests

@route('/port/<port>')
def port(port):
    r = requests.get(f'http://localhost:{port}/')
    return r.content

run(host="0.0.0.0", port=8080)
