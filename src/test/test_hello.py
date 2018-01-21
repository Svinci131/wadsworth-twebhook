from src.hello import handler

def test_handler():
	resp = handler({}, {})
	assert resp['statusCode'] == 200

'''
	It should parse ...
'''