import math
with open('input.txt') as file:
	commands = [[i.strip()[0],int(i.strip()[1:])] for i in file.readlines()]


class Waypoint:
	def __init__(self,facing):
		self.point_of_compass = ['N','E','S','W']
		self.coor = [0,0]
		self.wx = 10
		self.wy = 1

	def show_pos(self,manhattan=False):
		print(f'Ship Coordinates : {self.coor}, Waypoint Coordinates : {self.wx,self.wy}')
		if manhattan:
			print(f'Manhattan Disctance of Ship : {abs(self.coor[0])+abs(self.coor[1])}')
		return self

	def rotate(self, direction, degree):
		if direction == 'L':
			angle = degree * math.pi / 180
		elif direction == 'R':
			angle = -degree * math.pi / 180

		new_wx = self.wx * math.cos(angle) - self.wy * math.sin(angle)
		new_wy = self.wx * math.sin(angle) + self.wy * math.cos(angle)
		self.wx = round(new_wx)
		self.wy = round(new_wy)

	def move(self, distance, direction):
		if direction == 'E':
			self.wx += distance
		elif direction == 'W':
			self.wx -= distance
		elif direction == 'N':
			self.wy += distance
		elif direction == 'S':
			self.wy -= distance
		elif direction == 'F':
			self.coor[0] += distance * self.wx
			self.coor[1] += distance * self.wy

	def go(self,command,scale):
		if command in self.point_of_compass+['F']:
			self.move(distance=scale,direction=command)
		elif command in ['L','R']:
			self.rotate(command,scale)


# Part 2
waypoint = Waypoint('E')
waypoint.show_pos()

for command in commands:
	waypoint.go(command[0],command[1])
	waypoint.show_pos()
waypoint.show_pos(True)