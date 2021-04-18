import hash_table_chain as htc

def load_factor(h):
    count = 0
    for b in h.bucket:
        count+= len(b)
    return count/len(h.bucket)

def longest_bucket(h):
    count = 0
    for b in h.bucket:
        if len(b) > count:
            count = len(b)
    return count

def check(h):
    for i in range(len(h.bucket)):
        for rec in h.bucket[i]:
            if h.h(rec.key) != i:
                return False
    return True

def has_duplicates(L):
    # O(n)
    h = htc.HashTableChain(len(L))
    for i in L:
        if h.insert(i,[]) == -1:
            return True
    return False


def has_duplicates_v1(L):
    # O(n^2)
    for i in range(len(L)):
        if L[i] in L[i+1:]:
            return True
    return False
        
def has_duplicates_v2(L):
    # O(n log n)
    L.sort()
    for i in range(1,len(L)):
        if L[i] == L[i+1:]:
            return True  
    return False

if __name__ == "__main__":
    h = htc.HashTableChain(9)
    
    players = ['Bellinger','Betts', 'Hernandez', 'Pederson', 'Pollock', 'Taylor']
    numbers= [35, 50, 14, 31, 11, 3]

    for i in range(len(players)):
        h.insert(numbers[i],players[i])
        
    h.print_table()

    print(load_factor(h))  # 0.66666666666666
    
    print(longest_bucket(h)) # 2
    
    print(check(h)) # True
    h.bucket[2][0].key = 2302
    h.print_table()
    print(check(h)) # False
    
    L1 = [1,4,2,5,6,7,8,39,20,45]
    L2 = [1,4,2,5,6,7,8,39,20,45,9,13,5,34]
    
    print(has_duplicates(L1)) # False
    print(has_duplicates(L2)) # True

