import sys
from math import cos, radians

def make_dot_string(x):
    return " " * int(10 * cos(radians(x)) + 10) + "o"
#assert make_dot_string(90) == '          o'
#assert make_dot_string(180) == 'o'
def main():
    
    for i in range(10000000):
        s = make_dot_string(i)
        
        print(s)


    


if __name__ == "__main__":
    main();