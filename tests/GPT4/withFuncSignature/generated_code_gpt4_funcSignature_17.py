def parse_music(music_string: str) -> List[int]:
    # Mapping of note names to integers
    note_to_int = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7}

    # Parse the string and convert each note to its corresponding integer
    return [note_to_int[note] for note in music_string if note in note_to_int]

# Example usage
music_str = "ABCDEF"
result = parse_music(music_str)

METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(parse_music): 
    assert parse_music('') == [] 
    assert parse_music('o o o o') == [4, 4, 4, 4] 
    assert parse_music('.| .| .| .|') == [1, 1, 1, 1] 
    assert parse_music('o| o| .| .| o o o o') == [2, 2, 1, 1, 4, 4, 4, 4] 
    assert parse_music('o| .| o| .| o o| o o|') == [2, 1, 2, 1, 4, 2, 4, 2] 
    
check(parse_music)