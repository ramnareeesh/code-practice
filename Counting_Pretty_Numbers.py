

for i in range(int(input())):
    in_list = input().split(" ")
    L = int(in_list[0])
    R = int(in_list[1])
    pretty = 0
    for i in range(L, R+1):
        if i % 10 in [2, 3, 9]:
            pretty += 1
    print(pretty)