with open('input.txt') as file:
	commands = [[i.strip()[0],int(i.strip()[1:])] for i in file.readlines()]


class Ship:
	def __init__(self,facing):
		self.point_of_compass = ['N','E','S','W']
		self.facing = facing
		self.coor = [0,0]

	def show_pos(self,manhattan=False):
		print(f'Ship Coordinates : {self.coor}, Facing : {self.facing}')
		if manhattan:
			print(f'Manhattan Disctance of Ship : {abs(self.coor[0])+abs(self.coor[1])}')
		return self

	def rotate(self, direction, degree):
		if direction == 'R':
			new_direction = (self.point_of_compass.index(self.facing) + (degree//90))%4
			self.facing = self.point_of_compass[new_direction]
		elif direction == 'L':
			new_direction = (self.point_of_compass.index(self.facing) - (degree//90))%4
			self.facing = self.point_of_compass[new_direction]

	def move(self, distance, direc = ''):
		direction = self.facing if direc == '' else direc
		if direction == 'E':
			self.coor[0] += distance
		elif direction == 'W':
			self.coor[0] -= distance
		elif direction == 'N':
			self.coor[1] -= distance
		elif direction == 'S':
			self.coor[1] += distance

	def go(self,command,scale):
		if command in self.point_of_compass:
			self.move(distance=scale,direc=command)
		elif command in ['L','R']:
			self.rotate(command,scale)
		elif command == 'F':
			self.move(distance=scale)
			

# Part 1			
ship = Ship('E')
ship.show_pos()

for command in commands:
	ship.go(command[0],command[1])
ship.show_pos(True)