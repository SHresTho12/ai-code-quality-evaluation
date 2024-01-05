
from typing import List


def parse_music(music_string: str) -> List[int]:
  """
  Parses a music string into a list of integers representing notes.

  Args:
      music_string: The string containing the music notation.

  Returns:
      A list of integers representing the notes in the music string.
  """

  # Split the string into a list of tokens, handling both spaces and commas:
  tokens = music_string.split(",") if "," in music_string else music_string.split()

  # Convert each token to an integer and return the list:
  return [int(token) for token in tokens]


METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(parse_music): 
    assert parse_music('') == [] 
    assert parse_music('o o o o') == [4, 4, 4, 4] 
    assert parse_music('.| .| .| .|') == [1, 1, 1, 1] 
    assert parse_music('o| o| .| .| o o o o') == [2, 2, 1, 1, 4, 4, 4, 4] 
    assert parse_music('o| .| o| .| o o| o o|') == [2, 1, 2, 1, 4, 2, 4, 2] 
    
check(parse_music)