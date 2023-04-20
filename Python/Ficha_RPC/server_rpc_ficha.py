from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()
    class MyFuncs:
        def mul(self, x, y):
            return x * y

        def adder(self,x,y):
            return x + y

        def div(self,x,y):
            return x / y

        def sub(self):
            return x - y

        def pot(self,y,x):
            return double(x ^ y)
    server.register_instance(MyFuncs())

