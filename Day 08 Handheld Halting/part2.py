with open('input.txt') as file:
    console = file.readlines()
    console = [c[:-1] for c in console]
    console = [{c.split()[0]:int(c.split()[1])} for c in console]


class Program:
    def __init__(self, commands):
        self.commands = commands
        self.pointer = 0
        self.accumulator = 0
        self.history = set()

    def run(self):
        while True:
            # Infinite Loop control
            if self.pointer in self.history:
                break
            self.history.add(self.pointer)

            if self.pointer == len(self.commands):
                print(f'Terminates! Acc : {self.accumulator}')
                break
            com = list(self.commands[self.pointer].items())[0]
            if com[0] == 'nop':
                self.pointer += 1
            elif com[0] == 'acc':
                self.pointer += 1
                self.accumulator += com[1]
            elif com[0] == 'jmp':
                self.pointer += com[1]


# Part 2
for i in range(len(console)):
    current_console = console.copy()
    c, val = list(console[i].items())[0]
    if c == 'nop':
        current_console[i] = {'jmp': val}
    elif c == 'jmp':
        current_console[i] = {'nop': val}
    prog = Program(current_console)
    prog.run()
