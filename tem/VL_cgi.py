from time import localtime
print('Content-Type: text/html; char-set-urt-8\n')
print('<html> <body>\n')
print('<h2>Die aktuelle Uhrzeit</h2>\n')
print(f'Es ist {localtime()[3]} Uhr und {localtime()[4]} Minuten.\n')
print('</body> </html>\n')

from http.server import HTTPServer, CGIHTTPRequestHandler

serveradresse = ('', 8080)
server = HTTPServer(serveradresse, CGIHTTPRequestHandler)

server.serve_forever()