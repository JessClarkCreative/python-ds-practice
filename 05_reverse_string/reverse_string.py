def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    reversed_phrase = ''
    for char in phrase:
        reversed_phrase = char + reversed_phrase
    return reversed_phrase
