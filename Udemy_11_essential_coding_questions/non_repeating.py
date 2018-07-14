from collections import OrderedDict
from operator import itemgetter


def non_repeating(given_string):
    if len(given_string) > 0:
        my_dict = OrderedDict()

        for ii in range(len(given_string)):
            if given_string[ii] in my_dict:
                my_dict[given_string[ii]] += 1
            else:
                my_dict[given_string[ii]] = 1

        if 1 in my_dict.values():
            # sort the dict
            sorted_dict = sorted(my_dict.items(),key = itemgetter(1))
            return sorted_dict[0][0]
        else:
            return None

    else:
        return None


print(non_repeating("abcab")) # should return 'c'
print(non_repeating("abab")) # should return None
print(non_repeating("aabbbc")) # should return 'c'
print(non_repeating("aabbdbc")) # should return 'd'