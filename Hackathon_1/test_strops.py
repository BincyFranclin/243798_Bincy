import my_package as strop
    
s = input("Enter the main string: ")
r = input("Enter the substring to search for: ")
    
count, spans = strop.getspan(s, r)
print(f"Span and count of substring '{r}' in '{s}': {spans}{count}")

# Test other functions
print("Reversed words:", strop.reverseWords(s))
print("String without punctuation:", strop.removePunctuation(s))
print("Word count:", strop.countWords(s))
print("Character frequency map:", strop.characterMap(s))
print("Title case:", strop.makeTitle(s))
print("Normalized spaces:", strop.normalizeSpaces(s))
print("Transformed string:", strop.transform(s))
print("Permutation of the string", strop.get_permutations('abc'))