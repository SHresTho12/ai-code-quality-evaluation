def how_many_times(string: str, substring: str) -> int:
    count = start = 0
    while start < len(string):
        pos = string.find(substring, start)
        if pos != -1:
            start = pos + 1
            count += 1
        else:
            break
    return count


METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(how_many_times): 
    assert how_many_times('', 'x') == 0 
    assert how_many_times('xyxyxyx', 'x') == 4 
    assert how_many_times('cacacacac', 'cac') == 4 
    assert how_many_times('john doe', 'john') == 1 
    
check(how_many_times)