class Student : 
	def __init__(self, name, score):
		self.name = name
		self.score = score
	def do_hw(self,hw):
		print('我在做作業',hw)
	def study(self):
		print('我在讀書')
		self.score += 5
	def sleep(self):
		print('0')

s1 = Student('Roy',80)
s2 = Student('Chris', 85)
s2.study()
students = [s1,s2]
for s in students:
	print(s.name,s.score)

class Desk :
	def __init__(self,colar) :
		self.colar = colar
		print('我被造出來了')
	def re_colar(self,new_colar):
		self.colar = new_colar
d = Desk('blue')
d.re_colar('red')
print(d.colar)