from collections import defaultdict

def main():
    n = int(input())
    names_dict = defaultdict(int)
    for i in range(n):
        user_name = input()
        if user_name not in names_dict:
            names_dict[user_name] = 1
            print("OK")
        else:
            print(user_name + str(names_dict[user_name]))
            names_dict[user_name] += 1
main()
        

        