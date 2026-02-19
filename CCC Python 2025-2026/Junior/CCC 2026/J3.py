def win(c1, c2):
    if c1 == c2:
        return 0
    if c1 == 'R' and c2 == 'G':
        return 1
    if c1 == 'G' and c2 == 'B':
        return 1
    if c1 == 'B' and c2 == 'R':
        return 1
    return 2

def calculate(n, m):
    n_eat = 0
    m_eat = 0
    
    n_ind = 0
    m_ind = 0    
    while n_ind < len(n) and m_ind < len(m):
        result = win(n[n_ind], m[m_ind])
        
        if result == 0:
            n_eat += 1
            m_eat += 1
            n_ind += 1
            m_ind += 1
        elif result == 1:
            n_eat += 1
            m_ind += 1
        else:
            m_eat += 1  
            n_ind += 1
    
    n_eat += len(n) - n_ind
    m_eat += len(m) - m_ind    
    return n_eat, m_eat

n = input().strip()
m = input().strip()

n_eat, m_eat = calculate(n, m)
print(n_eat)
print(m_eat)