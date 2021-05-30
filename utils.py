from sys import stdin

def getch():
    ch = stdin.read(1)
    stdin.flush()
    return ch

if __name__ == "__main__":
    while True:
        ch = getch()
        print(ch)
