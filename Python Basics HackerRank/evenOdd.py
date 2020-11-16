def is_even (n):
    if n%2 == 0:
        return "even"
    else:
        return "odd"

if __name__ == "__main__":
    n = int (input())
    print (is_even(n))