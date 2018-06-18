from cgi import parse_qs
import json
from game import new_game, guess


def application(environ, start_response):
    error = False

    if environ['REQUEST_METHOD'] != 'POST':         #만약 포스트 요청이 아닐경우
        response = {'code': 'error', 'msg': 'wrong HTTP method'}    #에러메세지를 담은 dictionary
        error = True

    if not error:
        try:            #environ['PATH_INFO']로부터 요청된 기능(API) 파악
            path = environ['PATH_INFO'].split('/')
            if len(path) == 2:
                method = path[1]
            else:
                response = {'code': 'error', 'msg': 'wrong API path'}
                error = True
        except:
            response = {'code': 'error', 'msg': 'wrong API path'}
            error = True

    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', '0'))
    except ValueError:
        request_body_size = 0

    request_body = environ['wsgi.input'].read(request_body_size)
    d = parse_qs(request_body)

    if not error:       #요청된 API에 따라 적절한 게임 드라이버 함수를 호출한다.
        if method == 'new':
            response = new_game(d)
        elif method == 'guess':
            response = guess(d)
        else:
            response = {'code': 'error', 'msg': 'non-existent API method'}

    status = '200 OK'
    response_body = json.dumps(response)        #json 형태를 가지는 HTTP response를 출력한다.

    response_headers = [
        ('Content-Type', 'application/json'),
        ('Content-Length', str(len(response_body)))
    ]

    start_response(status, response_headers)

    return [response_body]


if __name__ == '__main__':      #localhost/8051이라는 서버를 만들고 유지한다.
    httpd = make_server(
            'localhost',
            8051,
            application
    )

    httpd.serve_forever()
