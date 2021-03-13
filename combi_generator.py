import itertools

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
chars_as_string = "abcdefghijklmnopqrstuvwxyz"


def convert(s):
    new = ""
    for x in s:
        new += x
    return new

def generate_all(length):
    main_lists = []

    for l in itertools.permutations(chars_as_string, length):
        main_lists.append(l)

    return main_lists

combinations = generate_all(4)
#print(type(combinations))
print(len(combinations))
#for c in combinations:
    #print(convert(c))
