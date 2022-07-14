def main():
    exp = list(map(int,input().split('+')))
    exp.sort()
    print('+'.join(map(str,exp)))
main()
