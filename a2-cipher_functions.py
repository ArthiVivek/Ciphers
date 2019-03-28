# Functions for running an encryption or decryption algorithm

ENCRYPT = 'e'
DECRYPT = 'd'

# Write your functions after this comment.  Do not change the statements above
# this comment.  Do not use import, open, input or print statements in the
# code that you submit.  Do not use break or continue statements.

def clean_message (msg):
    """ (str) -> str

    Return copy of msg that only consists of capitalized alphabetcial letters.

    >>> clean_message ('123peaches')
    'PEACHES'
    >>> clean_message ('pickle-pie')
    'PICKLEPIE'
    """
    clean_msg = ''

    for letter in msg:
        if letter.isalpha():
            clean_msg = clean_msg + letter.upper()

    return clean_msg

def encrypt_letter (letter, keystream):
    """ (str, int) -> str

    Precondition: len(letter) == 1 and letter.isupper() and a vaid keystream
    value is given.

    Apply the given keystream to letter and return the encrypted letter.

    >>> encrypt_letter ('C', 4)
    'G'
    >>> encrypt_letter ('F', 2)
    'H'
    """

    difference = ord (letter) - ord ('A')

    new_ord = (difference + keystream) % 26

    return chr (new_ord + ord ('A'))

def decrypt_letter (letter, keystream):
    """ (str, int) -> str

    Precondition: len (letter) == 1 and letter.isupper() and a vaid keystream
    value is given.

    Return the decrypted letter found using the keystream.

    >>> decrypt_letter ('W', 2)
    'U'
    >>> decrypt_letter ('K', 10)
    'A'
    """

    difference = ord (letter) - ord ('A')

    new_ord = (difference - keystream) % 26

    return chr (new_ord + ord ('A'))

def swap_cards (deck, index):
    """(list of int, int) -> NoneType

    Precondition: 0 <= index <= len (deck)

    Modify deck so that the values at position index and index + 1 are swapped.

    >>> swap_cards ([1, 3, 5, 9, 21], 3)
    >>> deck
    [1, 3, 5, 21, 9]

    >>> swap_cards ([1, 2, 3, 4, 5], 4)
    >>> deck
    [5, 2, 3, 4, 1]
    """
    # Case 1 is if the card at index is the last card
    if index == (len(deck) - 1):
        temp1 = deck[index]
        temp2 = deck[0]
        deck[0] = temp1
        deck[index] = temp2

    # For every other case
    else:
        temp1 = deck [index]
        temp2 = deck [index + 1]
        deck [index] = temp2
        deck [index + 1] = temp1

def get_small_joker_value (deck):
    """ (list of int) -> int

    Precondition: len(deck) > 1

    Return the value of the second greatest integer in deck.

    >>> get_small_joker_value ([3, 8, 12, 21])
    12
    >>> get_small_joker_value ([3, 5, 1, 8, 6])
    6
    """

    deck2 = []

    for i in deck:
        if i != max (deck):
            deck2.append(i)

    return max (deck2)

def get_big_joker_value (deck):
    """ (list of int) -> int

    Precondition: len(deck) > 0

    Return the highest value in deck.

    >>> get_big_joker_value ([3, 7, 9, 10])
    10
    >>> get_big_joker_value ([9, 3, 34, 2])
    34
    """

    return max (deck)

def move_small_joker (deck):
    """ (list of int) -> NoneType

    Modify the deck so that the position of small_joker and the card that
    follows it are swapped.

    >>> move_small_joker ([5, 17, 12, 6, 2])
    >>> deck
    [5, 17, 6, 12, 2]

    >>> move_small_joker ([14, 1, 6, 26, 15])
    >>> deck
    [15, 1, 6, 26, 14]
    """

    small_joker = get_small_joker_value (deck)

    index = deck.index(small_joker)

    swap_cards (deck, index)

def move_big_joker (deck):
    """ (list of int) -> Nonetype

    Modify the deck so that the position of big_joker is moved two positions
    down towards the bottom of the deck.

    >>> move_big_joker ([5, 17, 12, 6, 2])
    >>> deck
    [5, 12, 6, 17, 2]

    >>> move_big_joker ([14, 1, 6, 26, 15])
    >>> deck
    [26, 1, 6, 15, 14]
    """

    count = 0
    big_joker = get_big_joker_value(deck)

    # Swaps big_joker with the card beside it two times
    while count <= 1:
        index = deck.index(big_joker)
        swap_cards(deck, index)
        count = count + 1

def triple_cut(deck):
    """ (list of int) -> Nonetype

    Perform a triple cut on the deck.

    >>> triple_cut ([5, 17, 12, 6, 2])
    >>> deck
    [6, 2, 17, 12, 5]

    >>> triple_cut ([14, 1, 6, 26, 15])
    >>> deck
    [26, 15, 14, 1, 6]
    """

    big_joker = get_big_joker_value(deck)
    small_joker = get_small_joker_value(deck)

    # Case 1 is if small_joker is found closer to the top of the deck.
    if deck.index(big_joker) > deck.index(small_joker):
        
        # Store deck portion above small_joker in deck1. 
        deck1 = deck[:deck.index(small_joker)]
        
        # Store deck potion below the big_joker in deck2. 
        deck2 = deck[deck.index(big_joker) + 1 :]
        
        # Swap the positions of the contents of deck1 and deck2. 
        deck[deck.index(big_joker) + 1 :] = deck1
        deck[:deck.index(small_joker)] = deck2

    # Case 2 is if big_joker is found closer to the top of the deck.
    elif deck.index(big_joker) < deck.index(small_joker):
        deck1 = deck[:deck.index(big_joker)]
        deck2 = deck[deck.index(small_joker) + 1 :]

        deck[deck.index(small_joker) + 1 :] = deck1
        deck[:deck.index(big_joker)] = deck2

def insert_top_to_bottom(deck):
    """ (list of int) -> Nonetype

    Move the number of cards indicated by the bottom card value from the top to
    the bottom of the deck placing them above the bottom card. If the bottom
    card is the big_joker, the value of the small_joker is used instead.

    >>> insert_top_to_bottom ([1, 2, 3, 4, 5])
    >>> deck
    [1, 2, 3, 4, 5]

    >>> insert_top_to_bottom ([2, 5, 4, 1, 3])
    >>> deck
    [1, 2, 5, 4, 3]
    """
    bottom_card = deck[-1]
    big_joker = get_big_joker_value(deck)
    small_joker = get_small_joker_value(deck)
     
    if bottom_card != big_joker:
        bottom_card2 = bottom_card
    elif bottom_card == big_joker:
        bottom_card2 = small_joker

    mini_deck = deck[:bottom_card2]
    index = 0
    while index < bottom_card2:
        deck.remove(deck[0])
        index = index + 1
    deck.remove(deck[-1])

    for card in mini_deck:
        deck.append(card)
    deck.append(bottom_card)

def get_card_at_top_index(deck):
    """ (list of int) -> int

    Return the value of the card at the index indicated by the value of the top
    card. If the top card is the big_joker, the value of the small_joker is used
    instead.

    >>> deck = [1, 2, 3, 4, 5]
    >>> get_card_at_top_index(deck)
    2
    
    >>> get_card_at_top_index (deck)
    3
    """
    big_joker = get_big_joker_value(deck)
    small_joker = get_small_joker_value(deck)


    if deck[0] != big_joker:
        keystream = deck[deck[0]]

    elif deck[0] == big_joker:
        keystream = deck[small_joker]

    return keystream

def get_next_keystream_value(deck):
    """ (list of int) -> int

    Repeat 5 steps of the algorithm until a valid keystream value is produced.
    
    >>> deck = [1, 2, 3, 4, 5]
    >>> get_next_keystream_value(deck)
    2
    >>> get_next_keystream_value (deck)
    3
    """

    big_joker = get_big_joker_value (deck)
    small_joker = get_small_joker_value (deck)
    num = glue_steps_together (deck)

    while num in [big_joker, small_joker]:
        num = glue_steps_together (deck)

    return num

def glue_steps_together (deck):
    """ (list of int) -> list of int

    Connect all five steps of the algorithm to return a keystream value
    
    >>> deck = [2, 5, 4, 1, 3]
    >>> glue_steps_together (deck)
    1
    
    >>> glue_steps_together (deck)
    2
    """
    move_small_joker (deck)
    move_big_joker (deck)
    triple_cut (deck)
    insert_top_to_bottom (deck)

    return get_card_at_top_index (deck)

def process_messages (deck, messages, cipher_type):
    """ (list of int, list of str, str) -> list of str

    Return a list of the message that has been altered by the cipher_type using
    deck.

    >>> process_messages ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
    16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28],
    ['compsci108', 'ismyfav'], 'e')

    >>> process_messages ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
    16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28], ['KEXXYBN', 'JMTONAY'],
    'd')
    """
    cleanmessage = []
    for message in messages:
        cleanmessage.append(clean_message(message))
    temp = ""
    testlist = []
    if cipher_type == DECRYPT:
        for message in cleanmessage:
            temp = ""
            for letter in message:
                temp+= decrypt_letter(letter, get_next_keystream_value(deck))
            testlist.append(temp)
    elif cipher_type == ENCRYPT:
        for message in cleanmessage:
            temp = ""
            for letter in message:
                temp+= encrypt_letter(letter, get_next_keystream_value(deck))
            testlist.append(temp)
            
    return testlist

def read_messages (file):
    """ (file open for reading) -> list of str

    Return a list that contains each message without a newline character.
    """

    message_list = []

    for message in file:
        message_list.append(message.strip('\n'))

    return message_list

def is_valid_deck (deck):
    """ (list of int) -> bool

    Return True if and only if deck is valid. Otherwise, return False.

    >>> is_valid_deck ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
    16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28])
    True

    >>> is_valid_deck ([1, 2, 3, 4, 5, 5, 100, 6, 7, 8, 9, 10])
    False
    """

    deck_checker = []
    card = 1
    while card in range(len(deck) + 1):
        if card not in deck_checker and card in deck:
            deck_checker.append(card)
        card = card + 1
    return len(deck) == len(deck_checker) and len(deck) >= 3

def read_deck (file):
    """ (file open for reading) -> list of int

    Return a list of int in the same order as they appear in the file.
    """

    deck = []

    for num in file:

        temp = num.strip('\n').split(" ")
        for card in temp:
            if card != '':
                deck.append(int(card))
    return deck