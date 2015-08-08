# Gets data from both boards
b1 = 0
b2 = 0

from gattlib import GATTRequester

req = GATTRequester("EA:02:7F:9E:5F:7C", False)
req1 = GATTRequester("EC:C7:D5:05:67:BF", False)

def initialize():
	try:
	    req.connect(True)
	    req.disconnect()
	    print "connected 1"

	    req1.connect(True)
	    req1.disconnect()
	    print "connected 2"
	    return True

	except:
		print "Error connecting"
		try:
		    print "disconnect 1"
		    req.disconnect()
		except Exception, e:
		    pass
		try:
		    print "disconnect 2"
		    req1.disconnect()
		except Exception, e:
		    pass

def check_answers():
	try:
		   req.connect(True)
		   data=req.read_by_handle(0x000e)
		   b1 = ord(data[0])
		   req.disconnect()

		   req1.connect(True)
		   data=req1.read_by_handle(0x000e)
		   b2 = ord(data[0])
		   req1.disconnect()
		   return b1, b2
	except:
		try:
		    print "disconnect 1"
		    req.disconnect()
		except Exception, e:
		    pass
		try:
		    print "disconnect 2"
		    req1.disconnect()
		except Exception, e:
		    pass
