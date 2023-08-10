for T in range(int(input())):
    in_list = input().split(" ")
    N = int(in_list[0])  # no of days of work
    W = int(in_list[1])  # total salary for working N days
    A = input().split(" ")  # list of wages for each day for N days
    for _ in range(len(A)):
        A[_] = int(A[_])
    A.sort(reverse=True)

    print(A)
    salary = 0
    work = 0
    for i in A:
        salary += i
        work += 1
        if salary >= W:
            break

    print(N - work)
