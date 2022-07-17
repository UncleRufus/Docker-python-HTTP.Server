#!/usr/bin/env python

# Imports
import urls, settings
import http.server
import json


class HostHTTPServer(http.server.SimpleHTTPRequestHandler):
    """
    Локальный сервер слущающий порт 9999
    """
    def do_GET(self):
        path = self.path.split('/')

        if path[1] in urls.urlpatterns.keys():
            message = json.dumps(urls.urlpatterns[path[1]]()._asdict())
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(message, "utf8"))
            return

        else:
            message = 'Url not found 404'
            self.send_response(404, message)
            self.wfile.write(bytes(message, "utf8"))



if __name__=='__main__':
    server = http.server.HTTPServer((settings.HOST, settings.PORT), HostHTTPServer)
    try:
        server.serve_forever()

    except KeyboardInterrupt:
        server.server_close()
        print('Сервер остановлен вручную')

