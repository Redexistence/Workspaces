N = int(input())
peppers_SHU_dict = {
    "Poblano": 1500,
    "Mirasol": 6000,
    "Serrano": 15500,
    "Cayenne": 40000,
    "Thai": 75000,
    "Habanero": 125000
}
T = 0
for i in range(N):
    T += peppers_SHU_dict[str(input())]
    
print(T)