from wsgiref.simple_server import make_server


def app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]

    start_response(status, headers)

    return [b"Wassap World! its my first simple wsgi server."]


with make_server('', 8000, app) as server:
    print("server already started http://localhost:8000...")
    server.serve_forever()
