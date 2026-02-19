n = int(input())
gold_players = 0

for _ in range(n):
    points = int(input())
    fouls = int(input())
    
    rating = (points * 5) - (fouls * 3)
    
    if rating > 40:
        gold_players += 1

if gold_players == n:
    print(f"{gold_players}+")
else:
    print(gold_players)