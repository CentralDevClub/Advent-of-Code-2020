with open('input.txt') as file:
    s = [i.strip() for i in file.readlines()]


class Seats:
    def __init__(self, seats):
        self.seats = seats
        self.width = len(self.seats[0])
        self.height = len(self.seats)

    def show(self):
        for line in self.seats:
            print(line)
        print()

    def countOccupied(self):
        print(''.join(self.seats).count('#'))

    def update_state(self):
        stateChanged = False
        newSeats = []
        for y,line in enumerate(self.seats):
            newLine = ''
            for x,seat in enumerate(line):
                occupied = 0
                for i in [-1,0,1]:
                    for j in [-1,0,1]:
                        if (i != 0 or j != 0) and y+i >= 0 and y+i < self.height and x+j >= 0 and x+j < self.width and self.seats[y+i][x+j] == '#':
                            occupied += 1

                if seat == 'L' and occupied == 0:
                    newLine += '#'
                    stateChanged = True
                elif seat == '#' and occupied >= 4:
                    newLine += 'L'
                    stateChanged = True
                else:
                    newLine += seat

            newSeats.append(newLine)

        self.seats = newSeats
        return stateChanged

    def update_state_8_direction(self):
        stateChanged = False
        newSeats = []
        for y,line in enumerate(self.seats):
            newLine = ''
            for x,seat in enumerate(line):
                occupied = 0
                directions = [
                    {'x':1,'y':0},{'x':-1,'y':0},
                    {'x':1,'y':1},{'x':-1,'y':-1},
                    {'x':1,'y':-1},{'x':-1,'y':1},
                    {'x':0,'y':1},{'x':0,'y':-1}
                ]

                for d in directions:
                    posX = x + d['x']
                    posY = y + d['y']
                    while (posX >= 0 and posY >= 0 and posX < self.width and posY < self.height):
                        if self.seats[posY][posX] == '#':
                            # print(posX,posY)
                            occupied += 1
                            break
                        if self.seats[posY][posX] == 'L':
                            break
                        posX += d['x']
                        posY += d['y']


                if seat == 'L' and occupied == 0:
                    newLine += '#'
                    stateChanged = True
                elif seat == '#' and occupied >= 5:
                    newLine += 'L'
                    stateChanged = True
                else:
                    newLine += seat

            newSeats.append(newLine)

        self.seats = newSeats
        return stateChanged


# Part 1
seats = Seats(s)
stateChanging = seats.update_state()
while stateChanging:
    stateChanging = seats.update_state()
seats.countOccupied()

seats = Seats(s)
stateChanging = seats.update_state_8_direction()
while stateChanging:
    stateChanging = seats.update_state_8_direction()
seats.countOccupied()