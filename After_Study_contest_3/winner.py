from collections import defaultdict
def main():
    n = int(input())
    dict = defaultdict(int)
    dict2 = defaultdict(int)
    user_input = []
    for i in range(n):
        line = input()
        name, score = line.split()
        user_input.append(line)
        score = int(score)
        dict[name] += score
    max_score = max(dict.values())
    for j in range(n):
        name, score = user_input[j].split()
        score = int(score)
        dict2[name] += score
        if dict2[name] >= max_score and dict[name] == max_score:
            print(name)
            break
main()
