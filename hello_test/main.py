from urllib.parse import *


def app(environ, start_response):
    """Simplest possible application object
    :param start_response:
    :param environ:
    """
    print(environ['QUERY_STRING'])
    params = parse_qs(environ['QUERY_STRING'], keep_blank_values=True)
    response = [];
    print(params)
    if len(params):
        for param in params:
            for value in params[param]:
                params_str = param + "=" + value + "\n"
                response.append(params_str.encode())
                print(param + "=" + params[param][0])
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        # ('Content-Length', str(len("".join(list))))
    ]
    start_response(status, response_headers)
    return response
