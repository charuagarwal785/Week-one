def print_formatted(number):
    # your code goes here
    w = len(format(number, 'b'))
    for i in range(1, number+1):
        d=format(i,'d').rjust(w,' ')
        o=format(i,'o').rjust(w,' ')
        x=format(i,'x').rjust(w,' ').upper()
        b=format(i,'b').rjust(w,' ')
        print(f"{d} {o} {x} {b}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
