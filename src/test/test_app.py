from src.app import ping

def test_ping():
	assert ping() == 'pong'
