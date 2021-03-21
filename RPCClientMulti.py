import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
multicall = xmlrpc.client.MultiCall(proxy)
multicall.add(8, 2)
multicall.subtract(7, 3)
multicall.multiply(2, 3)
multicall.divide(12, 3)
result = multicall()

#print "%d, %d, %d, %d" % tuple(result)iiih/hlk6tgv  ngdt rcbn v,                                                                    wa
print("8+2=%d, 7-3=%d, 2*3=%d, 12//3=%d" % tuple(result))

