def load_savegame(filename):
    with open(filename, 'r') as savegame:
        text = savegame.read()
        lines = text.split('\n')
        for line in lines:
            print('line: ' + line)

load_savegame('filetest.py')
