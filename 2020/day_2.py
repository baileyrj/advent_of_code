import re

def identify(data_row):
    '''
    Parse the data row format of '1-3 a: abcde' to a reasonable dict 
    '''
    regex = re.compile(r'(\d+)-(\d+) (.): (.+)$')
    match = regex.search(data_row)

    return {
        'first': int(match.group(1)),
        'second': int(match.group(2)),
        'letter': match.group(3),
        'text': match.group(4)
    }

def is_valid_1(first, second, letter, text):
    return first <= text.count(letter) <= second

def is_valid_2(first, second, letter, text):
    return (text[first - 1] == letter) != (text[second - 1] == letter)
    
def count_valid_text():
    with open('data/day_2_input.txt', 'r') as f:
        entries = list(map (identify, f.read().splitlines()))

        valid_1_alg = lambda x: is_valid_1(**x)
        valid_2_alg = lambda x: is_valid_2(**x)
        x = filter(valid_2_alg, entries)

        return len(list(x))

print(count_valid_text())
