def unique(l: list):
    # Convert the list to a set to remove duplicates, then back to a list
    return list(set(l))


METADATA = {} 
def check(unique): 
    assert unique([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123] 
    
check(unique)