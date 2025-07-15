n = int(input())
tuples_list = [tuple(map(int, input().split())) for _ in range(n)]
unique_tuples = set(tuples_list)
print(len(unique_tuples))