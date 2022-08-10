# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) == 1:
        return [sequence]
    else:
        if len(sequence) == 2:
            new = sequence[1] + sequence[0]
            return [sequence, new]
        else:
            first = sequence[:-1]
            second = sequence[-1]
            result = []
            for i in get_permutations(first):
                listStr = list(i)
                for position in range(len(listStr)+1):
                    listStr.insert(position, second)
                    newStr = ''.join(listStr)
                    result.append(newStr)
                    del listStr[position]
            return result



if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    # print('Actual Output:', get_permutations(example_input), 'Length', len(get_permutations(example_input)))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    example_input = 'but'
    print('Input:', example_input)
    print('Expected output:', ['but','btu','ubt', 'utb', 'tbu', 'tub'])
    print('Actual Output:', get_permutations(example_input))

    example_input = 'ok'
    print('Input:', example_input)
    print('Expected output:', ['ok','ko'])
    print('Actual Output:', get_permutations(example_input))
