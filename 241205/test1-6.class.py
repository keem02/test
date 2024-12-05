class Car(object): #앞 부분을 대문자로 사용합니다. ref.(object)없어도 된다
	MaxSpeed = 300
	MaxPeople = 5
	def move(self, x):
		print(x, '의 스피드로 움직이고 있습니다.')
	def stop(self):
		print('멈췄습니다.')

k5 = Car()
k3 = Car()
k5.move(10)
k5.stop()
k3.move(5)
k3.stop()

print(k5.MaxSpeed)
print(k3.MaxSpeed)