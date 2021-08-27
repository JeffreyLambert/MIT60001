# Problem Set 4A
# Name: Jeff lambert
# Collaborators:
# Time Spent: x:xx


def insert_letter_into_sequence(sequence, letter):
    """
    Returns a list with letter inserted into all possible parts of sequence
    Args:
        sequence (str): Sequence where letter will be inserted
        letter (str): Letter to be inserted into sequence

    Returns:
        list: Returns list of sequence with letters inserted in various positions
    """
    sequence_list = list(sequence)
    sequence_length = len(sequence) + 1
    output_list = []
    for i in range(sequence_length):
        new_list = sequence_list[:]
        new_list.insert(i, letter)
        output_list.append(''.join(new_list))
    return output_list


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

    try:

        seq_length = len(sequence)
        seq_list = list(sequence)

        # Check base case where sequence length is 1
        if seq_length <= 1:
            return seq_list
        else:
            # Held out letter will be inserted into results from previous iteration of function
            previous_run = get_permutations(sequence[1:])
            first_letter = seq_list[0]
            output_list = []

            # For every permutation of the shorter sequence, insert held out letter into that sequence
            for seq in previous_run:
                new_output = insert_letter_into_sequence(seq, first_letter)
                output_list.extend(new_output)

            return output_list

    except TypeError:
        print("Sequence must be a string")

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    example1 = 'abc'
    expected1 = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    print('Input:', example1)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example1))
    print('Test Result:', expected1.sort() == get_permutations(example1).sort())
    print()

    example2 = ''
    expected2 = ['']
    print('Input:', example2)
    print('Expected Output:', [''])
    print('Actual Output:', get_permutations(example2))
    print('Test Result:', expected2.sort() == get_permutations(example2).sort())
    print()

    example3 = 1
    expected3 = None
    print('Input:', example3)
    print('Expected Output:', None)
    print('Actual Output:', get_permutations(example3))
    print('Test Result:', expected3 is None)
    print()