# Given a list of strings, return the count of the number of strings
# where the string length is 2 or more and the first and last chars of
# the string are the same.
# 
def match_ends(words):
    count = 0

    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            count = count + 1
    return count


# Given a list of strings, return a list with the strings in sorted
# order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields ['xanadu',
# 'xyz', 'aardvark', 'apple', 'mix']
# 
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
# 
def front_x(words):
    xlist = []
    blist = []

    for word in words:
        if word.startswith('x'):
            xlist.append(word)
        else:
            blist.append(word)
    return sorted(xlist) + (blist)


# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# 
# e.g.
# [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# 
# Hint: use a custom key= function to extract the last element from
# each tuple.
def last_num(last): return last[-1]
def sort_last(tuples):
    return sorted(tuples, key=last_num)



def test_match_ends():
    from nose.tools import assert_equal 
    assert_equal(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    assert_equal(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    assert_equal(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

def test_front_x():
    from nose.tools import assert_equal 
    assert_equal(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
                 ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    assert_equal(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
                 ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    assert_equal(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
                 ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])


def test_sort_last():
    from nose.tools import assert_equal 
    assert_equal(sort_last([(1, 3), (3, 2), (2, 1)]),
                 [(2, 1), (3, 2), (1, 3)])
    assert_equal(sort_last([(2, 3), (1, 2), (3, 1)]),
                 [(3, 1), (1, 2), (2, 3)])
    assert_equal(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
                 [(2, 2), (1, 3), (3, 4, 5), (1, 7)])
    


def main():
    test_match_ends()
    test_front_x()
    test_sort_last()

if __name__ == '__main__':
    main()
