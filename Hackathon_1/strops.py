def getspan(s, r):
    """Returns the start and end index (span) of substring ss in string s"""
    count = 0
    spans = []
    start = 0
    #process
    while True:
        start = s.find(r, start)
        if start == -1:
            break
        end = start + len(r)
        spans.append((start, end))
        count += 1
        start += 1  # Move to the next character to find subsequent occurrences
    return count, spans

def reverseWords(s):
    """
    Reverses the order of words in a given string.
    """
    words = s.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

def removePunctuation(s):
    """
    Removes punctuation characters from the given string 
    """
    punctuation_chars = "!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    translator = str.maketrans('', '', punctuation_chars)
    return s.translate(translator)

def countWords(s):
    """
    Counts the number of words in a given string.
    """
    return len(s.split())

def characterMap(s):
    """
    Creates a mapping of characters to their frequencies in the given string.
    """
    char_map = {}
    for char in s:
        if char in char_map:
            char_map[char] += 1
        else:
            char_map[char] = 1
    return char_map

def makeTitle(s):
    """
    Converts the given string to title case (each word capitalized).
    """
    return s.title()

def normalizeSpaces(s):
    """
    Normalizes spaces in the given string by replacing multiple spaces with a single space.
    """
    return ' '.join(s.split())

def transform(s):
    """
    Reverses the string and swaps case
    """
    return s[::-1].swapcase()

def get_permutations(s, step=0):
    """ 
    Returns all permutations of the string s as a list
    """
    permutations = []  
    
    if step == len(s):
        return [''.join(s)]      
    
    for i in range(step, len(s)):
        s_list = list(s)
        s_list[step], s_list[i] = s_list[i], s_list[step]
        
        permutations += get_permutations(s_list, step + 1)
    
    return permutations

