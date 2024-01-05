from typing import List

def parse_music(music_string: str) -> List[int]:
    """Parse a string of musical notes and return a list of integers representing the beats each note lasts.

    Args:
    music_string (str): A string representing musical notes in ASCII format.

    Returns:
    List[int]: A list of integers corresponding to the number of beats each note lasts.

    Examples:
    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
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
