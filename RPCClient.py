import xmlrpc.client as xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:8000')
print (s.pow(2,5))  # mengembalikan nilai x pangkat y
print (s.add(2,18))  # mengembalikan nilai x + y
print (s.div(17,8))  # mengembalikan nilai x div y

# list fungsi yang disediakan oleh server
print (s.system.listMethods())