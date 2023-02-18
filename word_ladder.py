#!/bin/python3

from collections import deque
import copy


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny',
    'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty',
    'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    with open(dictionary_file, 'r') as f:
        working_dict = f.read()

    dictionary = list(working_dict.split())

    if start_word == end_word:
        return [start_word]
    if len(start_word) != len(end_word):
        return None
    stack = []
    stack.append(start_word)
#    dictionary.remove(start_word)
    queue = deque([])
    queue.append(stack)

    while len(queue) != 0:
        working_stack = queue.popleft()
        dictionary_iterate = copy.copy(dictionary)
        for word in dictionary_iterate:
            if _adjacent(working_stack[-1], word):
                if word == end_word:
                    working_stack.append(word)
                    print("working_stack=", working_stack)
                    return working_stack
                stack1 = copy.copy(working_stack)
                stack1.append(word)
                queue.append(stack1)
                dictionary.remove(word)
    return None

def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''

    if len(ladder) < 1:
        return False
    for i in range(0, len(ladder) - 1):
        if not _adjacent(ladder[i], ladder[i + 1]):
            return False
    return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''

    if len(word1) != len(word2):
        return False
    else:
        dif = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                dif += 1
#           print("dif=", dif)
    return dif == 1
