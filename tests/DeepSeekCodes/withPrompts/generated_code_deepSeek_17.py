from typing import List


def parse_music(music_string: str) -> List[int]:
    notes = music_string.split()
    beats = []
    for note in notes:
        if note == 'o':
            beats.append(4)
        elif note == 'o|':
            beats.append(2)
        elif note == '.|':
            beats.append(1)
    return beats


METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(parse_music): 
    assert parse_music('') == [] 
    assert parse_music('o o o o') == [4, 4, 4, 4] 
    assert parse_music('.| .| .| .|') == [1, 1, 1, 1] 
    assert parse_music('o| o| .| .| o o o o') == [2, 2, 1, 1, 4, 4, 4, 4] 
    assert parse_music('o| .| o| .| o o| o o|') == [2, 1, 2, 1, 4, 2, 4, 2] 
    
check(parse_music)