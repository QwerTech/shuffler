import random
import re
import string
from os import listdir
from os import rename
from os.path import isfile, join

SHUFFLE_SEPARATOR = '.'

ALPHABET = string.ascii_uppercase + string.digits  # + r"""!#$%&'()+-;=@[]^_`{}~"""

SIZE = 2

targetDirToShuffle = 'D:\\Music1\\'

erasePatterns = {' - ': '-',
                 ' & ': '&',
                 '\s*\(.*\)': '',
                 ', ': ',',
                 '  ': ' ',
                 '\. ': '.',
                 '\.\.': '.'}


def randomString(size=SIZE, chars=ALPHABET):
  return ''.join(random.choice(chars) for _ in range(size))

def clean(name):
  for source, target in erasePatterns.items():
    name = re.sub(source, target, name)
  return name


if __name__ == '__main__':
  print('Capacity ' + str(len(ALPHABET) ** SIZE))
  dir = targetDirToShuffle
  files = [f for f in listdir(dir) if
                    isfile(join(dir, f))]
  for f in files:
    rename(dir + f, dir + randomString() + SHUFFLE_SEPARATOR + f)

  files = [f for f in listdir(dir) if
           isfile(join(dir, f))]

  for f in files:
    cleaned = clean(f)
    if cleaned != f:
      print()
      print(f)
      print(cleaned)
      rename(dir + f, dir + cleaned)
