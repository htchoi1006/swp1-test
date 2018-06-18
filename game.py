from findnumber import Findnumber

fn = Findnumber()

def new_game(d):
	try:
		count = int(d.get('count', [''])[0])
	except:
		return {'code': 'error', 'msg': 'count not given'}

	fn.new_game(count)

	return {'code': 'success'}


def guess(d):
	try:
		guess = int(d.get('guess', [''])[0])
	except:
		return {'code': 'error', 'msg': 'wrong guess parameter'}

	answer = fn.compare(guess)
	trial = fn.gettrial()

	return {'code': 'success', 'compare': answer, 'trial': trial}
