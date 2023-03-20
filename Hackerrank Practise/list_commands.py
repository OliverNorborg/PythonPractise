# Hackerrank

if __name__ == '__main__':
    N = int(input())
    list1 = []
    for _ in range(N):
        s = list(input().split())
        action = s[0]
        if action == "insert":
            position = int(s[1])
            number = int(s[2])
            list1.insert(position, number)
        if action == "print":
            print(list1)
        if action == "remove" :
            number = int(s[1])
            list1.remove(number)
        if action == "append":
            number = int(s[1])
            list1.append(number)
        if action == "sort":
            list1.sort()
        if action == "pop":
            list1.pop()
        if action == "reverse":
            list1.reverse()
        
        
            
            
