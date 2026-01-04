def count_distributions(n, k):
    """
    Count ways to distribute n pieces of pie to k people
    where each person gets at least as many as the person before them.
    """
    memory = {}
    
    def dynamic_programming(remaining_pieces, remaining_people, min_pieces):
        
        if remaining_people == 0:
            return 1 if remaining_pieces == 0 else 0
        
        if remaining_pieces < remaining_people * min_pieces:
            return 0
        
        if (remaining_pieces, remaining_people, min_pieces) in memory:
            return memory[(remaining_pieces, remaining_people, min_pieces)]
        
        count = 0
        # Try giving the current person x pieces (where x >= min_pieces)
        for x in range(min_pieces, remaining_pieces - remaining_people + 2):
            count += dynamic_programming(remaining_pieces - x, remaining_people - 1, x)
        
        memory[(remaining_pieces, remaining_people, min_pieces)] = count
        return count
    
    return dynamic_programming(n, k, 1)

n = int(input())
k = int(input())

print(count_distributions(n, k))