with open('dummy.txt') as file:
	lines = [int(i) for i in file.readlines()[0].split(',')]


class Game:
	def __init__(self,line):
		self.last_number = line[-1]
		self.turn = len(line)
		self.starting = {turn+1:number for turn,number in enumerate(line)}
		self.memory = {}

	def find_duplicate(self,array,value):
		return [i for i,v in enumerate(array) if v == value]

	def play_to(self,turn):
		turn -= self.turn
		for i in range(turn):
			self.turn += 1
			# print(f'Turn : {self.turn} --> {self.last_number}')
			line = list(self.memory.values())
			if self.last_number in line:
				prev_index = self.find_duplicate(list(self.starting.values())+line,self.last_number)
				if len(prev_index) > 1:
					diff = [i+1 for i in prev_index[-2:]]
					new_number = abs(diff[0]-diff[1])
					# print(f'{diff[1]} - {diff[0]}')
					if self.last_number == 1 and new_number == 1:
						self.memory[self.turn] = 0
						self.last_number = 0
					else:
						self.memory[self.turn] = new_number
						self.last_number = new_number
				else:
					self.memory[self.turn] = 0
					self.last_number = 0
			else:
				self.memory[self.turn] = 0
				self.last_number = 0
			# print(self.memory)


game = Game(lines)
game.play_to(30000000)
print(game.last_number)