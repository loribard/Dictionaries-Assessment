"""Dictionaries Assessment

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

    unique_words_dictionary = {}  #initialize dictionary

    phrase_by_words = phrase.split() #split the phrase into words and make a list of the words

    for word in phrase_by_words:   #iterate through the list
        unique_words_dictionary[word] = unique_words_dictionary.get(word,0) + 1 #make a dictionary counting how many of each word
    
    return unique_words_dictionary


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon
    
    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25 
    (it was a bad year for Christmas melons -- supply is low!)

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25
        
        >>> get_melon_price('Tomato')
        'No price found'
    """

    melon_name_price_dict = {}  #initilaize dictionary

    # input data...list of melons and their prices
    list_melon_names_prices = [["Watermelon",2.95],
    ["Cantaloupe", 2.50],
    ["Musk", 3.25],
    ["Christmas", 14.25]]

    for melon in list_melon_names_prices: #iterate over list of melons
        melon_name_price_dict[melon[0]] = melon[1] #make a dictionary of melons and prices

    if melon_name in melon_name_price_dict.keys(): #check to see if melon is in dictionary
        return melon_name_price_dict[melon_name] #print the price of the mlon
    else:
        return "No price found" #if no melon name in dictionary, return no price found


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
    """
   
    word_length_dictionary = {}     #initilaize a dictionary to keep word lengths
    list_tuples = []                #initilaize a list to hold the tuples

    for word in words:              #start iterating through the words
        length = len(word)
        #print length, word
        word_length_dictionary[length] =  word_length_dictionary.get(length,[]) #get the current key value
        word_length_dictionary[length].append(word)    #add the word to the length key

    for key in word_length_dictionary.keys():     #iterate over the dictionary
        word_length_dictionary[key].sort()         #sort each value (list of words) alphabetically
        list_tuples.append((key,word_length_dictionary[key])) #make each dictionary key, value a tuple


    return list_tuples
    

def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """
    #make a dictionary with the data
    pirate_dictionary = ({
     'sir':'matey'
    ,'hotel':'fleabag inn'
    ,'student':'swabbie'
    ,'man':'matey'
    ,'professor':'foul blaggart'
    ,'restaurant':'galley'
    ,'your':'yer'
    ,'excuse':'arr'
    ,'students':'swabbies'
    ,'are':'be'
    ,'restroom':'head'
    ,'my':'me'
   ,'is':'be'
    })
        
    #initialize the string
    string = ''
    #break up the phrase into words
    words = phrase.split(" ")
    #make a list that will contain all the new words
    new_phrase = []

    #iterate through the list of words in the phrase
    for word in words:
        #if the word has a translation, use that translation, otherwise, use the word
        if word in pirate_dictionary.keys():
            new_phrase.append(pirate_dictionary[word])
        else:
            new_phrase.append(word)

    #add all the words to the string with spaces between the words
    for word in new_phrase:
        string += word + " "

    #print out the string without the last blank space
    return string[:-1]     


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """
 
    names_firstchar_lastchar = {}  #initilaize the set
    
    for name in names: #make a dictionary with names as keys, and first and last letters as values
        names_firstchar_lastchar[name] = [name[0],name[-1]]

    #print names_firstchar_lastchar,names

    word = names[0] #the first word chose is the first word in the list
    #print word
    list_of_words = [word] #need to start the chain with the first word
    lenghth_of_remaining = len(names_firstchar_lastchar.keys()) #we're going to keep going until the lengh doesn't go down

    end_letter = names_firstchar_lastchar[word][1] #the first letter we'll look for
    #print end_letter

    # once you take the word, delete it from the dictionary
    #   del names_firstchar_lastchar[word]
    # go in order of the list of names:
    # if first letter matches last letter
    # new word
    # take last letter

    del names_firstchar_lastchar[word] #need to delete the first word from the dictionary
    old_length = lenghth_of_remaining + 1 #need to get condition going so it keeps going while we keep finding words

    while lenghth_of_remaining < old_length:
        old_length = lenghth_of_remaining
        #print "New Dictionary",names_firstchar_lastchar
        for name in names:
            
            #print name
            if name in names_firstchar_lastchar:
                if names_firstchar_lastchar[name][0] == end_letter:
                    #print "END letter match", name, end_letter
                
                    list_of_words.append(name)
                    end_letter = names_firstchar_lastchar[name][1]
                    del names_firstchar_lastchar[name]
                    lenghth_of_remaining -= 1
                    break  #because we need to get out of this loop and start at names agian
                    #print "Going for another round"
            
                


    return list_of_words
      

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
