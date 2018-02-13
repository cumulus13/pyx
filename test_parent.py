import test_child
import debug as debugger
debugger.DEBUG = True
debug = debugger.debug

def test(data):
	debug(data = data)
	
test("HELLO DATA")