from urllib.parse import *


def app(environ, start_response):
    """Simplest possible application object
    :param start_response:
    :param environ:
    """
    params = parse_qs(environ['QUERY_STRING'])
    response = [];
    for param in params:
        params_str = param + "=" + params[param][0] + "\n"
        response.append(params_str.encode())
        print(param + "=" + params[param][0])
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        # ('Content-Length', str(len("".join(list))))
    ]
    start_response(status, response_headers)
    return response
