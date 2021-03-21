from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Membatasi jalur yang akan digunakan
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Membuat server
server = SimpleXMLRPCServer(("localhost", 8000), requestHandler=RequestHandler)
server.register_introspection_functions()

# Membuat fungsi pow() 
server.register_function(pow)

# Membuat fungsi tambah dengan nama add
def adder_function(x,y):
    return x + y
server.register_function(adder_function, 'add')

# Membuat instansiasi yang dipublikasikan sebagai metod XML-RPC
class MyFuncs:
    def div(self, x, y):
        return x // y

server.register_instance(MyFuncs())

# jalankan looping untuk server
server.serve_forever()