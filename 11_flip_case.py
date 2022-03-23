def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    #swap to_swap in phrase to lowercase or uppercase
    #if to_swap.lower in phrase = to_swap.upper 
    #if to_swap.upper in phrase = to_swap.lower


    new_phrase = ''

    for char in phrase:
        if char.lower() == to_swap.lower():
            new_phrase += char.swapcase()
        else:
            new_phrase += char
    return new_phrase

    # char = a 
    # if a == a or  a == A
    # then char swapcase 