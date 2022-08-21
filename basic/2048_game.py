import random
nums = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
dir_map = ["up", "down", "left", "right"]
N = 5
table = [[0 for _ in range(N)] for _ in range(N)]
WIN = False

def table_get(t):
    global table
    return table[t[0]][t[1]]

def table_set(t, v):
    global table
    table[t[0]][t[1]] = v

def move_line(pos):
    global table
    global WIN
    for i in range(N-1, -1, -1):
        if table_get(pos[i]) == 0:
            continue
        for j in range(i+1, N):
            if table_get(pos[j-1]) == table_get(pos[j]):
                table_set(pos[j], table_get(pos[j])*2)
                table_set(pos[j-1], 0)
                if table_get(pos[j]) == 2048:
                    WIN = True
                break
            elif table_get(pos[j]) == 0:
                table_set(pos[j], table_get(pos[j-1]))
                table_set(pos[j-1], 0)
            else:
                break

def add_random_num():
    global table
    while True:
        i = random.randrange(N)
        j = random.randrange(N)
        if table[i][j] == 0:
            table[i][j] = random.choice(nums[:4])
            break

def table_print():
    global table
    for l in table:
        for x in l:
            print(x, end='\t')
        print()

def move(d):
    global table
    for i in range(N):
        if d == 'up':
            move_line([(j , i) for j in range(N-1, -1, -1)])
        elif d == 'down':
            move_line([(j , i) for j in range(N)])
        elif d == 'left':
            move_line([(i , j) for j in range(N-1, -1, -1)])
        elif d == 'right':
            move_line([(i , j) for j in range(N)])
        else:
            print("bad")
    add_random_num()

def run():
    for _ in range(3):
        add_random_num()
    table_print()
    print("PLAY")
    while not WIN:
        d = dir_map[int(input())]
        move(d)
        print(d)
        table_print()
    print("WON")

run()
