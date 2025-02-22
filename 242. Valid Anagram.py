# I COULD NOT SOLVE THIS PROBLEM IMPLEMENTING HASHMAPS. I HAD TO LOOK UP THE SOLUTION. I WILL COME BACK TO THIS PROBLEM LATER.

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t): # If the lengths of the strings are not equal, then they are not anagrams of each other.
        return False

    return sorted(s) == sorted(t) # The sorted function sorts the characters in the string alphabetically. If the sorted strings are equal, then the strings are anagrams of each other.
