import json

class C1:
	title = '1'
	text = '2'
	author = '3'

class Model(C1):

	def save(self):
		d = {}
		with open('use.json', 'w') as f:
			d = list(filter(lambda x: not x.startswith('_'), dir(C1)))
			json.dump(d, f)
		
s = Model()
s.save()


'''class C1:
	title = '1'
	text = '2'
	author = '3'

class Model(C1):

	def save(self):
		d = {}
		with open('use.json', 'w') as f:
			d = dict(C1)
			json.dump(d, f)
		
s = Model()
s.save()'''