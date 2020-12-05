class Seat:
    def __init__(self, ss):
        self.seat = ss
        self.selected = []
        self.rows = list(range(128))
        self.cols = list(range(8))

    @staticmethod
    def split(array):
        return [array[:len(array)//2], array[len(array)//2:]]

    @staticmethod
    def select(array, selection):
        if selection == 'F':
            return array[0]
        elif selection == 'B':
            return array[1]
        elif selection == 'L':
            return array[0]
        elif selection == 'R':
            return array[1]

    def get_selection(self, array,selection):
        selected_seat = self.split(array)
        if selection == 'row':
            selection_array = self.seat[:-3]
        elif selection == 'col':
            selection_array = self.seat[-3:]

        for i in selection_array:
            selected_seat = self.select(selected_seat, i)
            selected_seat = self.split(selected_seat)

        for i in selected_seat:
            if i:
                return i[0]


with open('seat.txt') as file:
    seats = file.readlines()
    seats = list(map(lambda x: x[:-1], seats))

all_id = []
card = {'id':0}
for s in seats:
    seat = Seat(s)
    row, col = seat.get_selection(seat.rows, 'row'), seat.get_selection(seat.cols, 'col')
    id = row * 8 + col
    all_id.append(id)
    card['id'] = max(all_id)

    if id == card['id']:
        card['row'] = row
        card['col'] = col

    # print(s)
    # print(f"Row : {row}")
    # print(f"Col : {col}")
    # print(f"ID  : {id}")
    # print()

# Part 1
print(f'My Card : {card}')

# Part 2
all_id = sorted(all_id)
for i in range(len(all_id)):
    if all_id[i+1] - all_id[i] > 1:
        print(all_id[i]+1)
        break
