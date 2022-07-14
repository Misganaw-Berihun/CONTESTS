def main():
    s = input()
    visited = set()
    cnt = 0
    for i in range(len(s)):
        if s[i] not in visited:
            visited.add(s[i])
            cnt += 1
    if cnt % 2:
        print("IGNORE HIM!")
    else:
        print("CHAT WITH HER!")
main()