# Anthony Gringeri
# acgringeri
# Algorithms, Project 1
# This project implements and compares algorithms using anagrams

import sys
import itertools
import timeit

# exhausts all possibilities before reporting true or false -- very inefficient
def bruteForceAlgorithm(string1, string2):
    matches = 0
    # assemble a list of all possible permutations of the first given string
    permutations = (list(map("".join, itertools.permutations(string1))))
    # go through list and check if there is a match
    for x in permutations:
        if string2 == x:
            matches = matches + 1
    # check if there was a match
    if matches > 0:
        return True
    # if not, the two strings are not anagrams
    return False

def myAlgorithm(string1, string2):
    # checks if the 2 strings are the same length (excluding spaces)
    if ((len(string1) - string1.count(' ')) != (len(string2) - string2.count(' '))):
        return False

    #create dictionaries for both strings with initial letter counts
    counts1 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
               'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

    counts2 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0,
               'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

    # go through each string and add one occurence for each time a character appears
    for c1 in string1:
        if (   (c1 == 'a') or (c1 == 'b') or (c1 == 'c') or (c1 == 'd') or (c1 == 'e') or (c1 == 'f') or (c1 == 'g')
            or (c1 == 'h') or (c1 == 'i') or (c1 == 'j') or (c1 == 'k') or (c1 == 'l') or (c1 == 'm') or (c1 == 'n')
            or (c1 == 'o') or (c1 == 'p') or (c1 == 'q') or (c1 == 'r') or (c1 == 's') or (c1 == 't') or (c1 == 'u')
            or (c1 == 'v') or (c1 == 'w') or (c1 == 'x') or (c1 == 'y') or (c1 == 'z')):

            counts1[c1] = counts1[c1] + 1

    for c2 in string2:
        if ((c2 == 'a') or (c2 == 'b') or (c2 == 'c') or (c2 == 'd') or (c2 == 'e') or (c2 == 'f') or (c2 == 'g')
            or (c2 == 'h') or (c2 == 'i') or (c2 == 'j') or (c2 == 'k') or (c2 == 'l') or (c2 == 'm') or (c2 == 'n')
            or (c2 == 'o') or (c2 == 'p') or (c2 == 'q') or (c2 == 'r') or (c2 == 's') or (c2 == 't') or (c2 == 'u')
            or (c2 == 'v') or (c2 == 'w') or (c2 == 'x') or (c2 == 'y') or (c2 == 'z')):

            counts2[c2] = counts2[c2] + 1

    # compare the two dictionaries; if they are the same, they are anagrams
    if (counts1 == counts2):
        return True

    # if this is evaluated then they are NOT anagrams
    return False

# time the Brute Force algorithm and return time elapsed
def effAnaBF(s1, s2):
    start1 = timeit.default_timer()
    bruteForceAlgorithm(s1, s2)
    end1 = timeit.default_timer()
    return (end1 - start1)

# time the better algorithm and return time elapsed
def effAnaBtr(s1, s2):
    start2 = timeit.default_timer()
    myAlgorithm(s1, s2)
    end2 = timeit.default_timer()
    return (end2 - start2)

def main():
    print("This program tests whether two strings are anagrams.")
    print("\nIf two strings are anagrams, they contain the same letters -- but not necessarily in the same "
          "arrangement.")
    print("\nNote: For strings larger than 12 characters, the brute force approach might not finish.\n")

    testNumber = input("To test both algorithms, enter 0.\n"
                       "To test just the Brute Force Algorithm, enter 1.\n"
                       "To test just my algorithm, enter 2.\n"
                       "Enter a value: ")

    if (testNumber == "0"):
        print("Testing both algorithms...\n")

        string1 = input("Enter the first string: ")
        string2 = input("Enter the second string: ")

        bruteForceTime = effAnaBF(string1, string2)
        betterTime = effAnaBtr(string1, string2)

        if (bruteForceAlgorithm(string1, string2) == True):
            print("\nThe Brute Force Algorithm determined that '" + string1 + "' and '" + string2 + "' ARE anagrams.")
        else:
            print(
                "\nThe Brute Force Algorithm determined that '" + string1 + "' and '" + string2 + "' ARE NOT anagrams.")

        print("Time elapsed for Brute Force Algorithm: ")
        print("{:15.10f}".format(bruteForceTime))

        if (myAlgorithm(string1, string2) == True):
            print("\nMy algorithm determined that '" + string1 + "' and '" + string2 + "' ARE anagrams.")
        else:
            print("\nMy algorithm determined that '" + string1 + "' and '" + string2 + "' ARE NOT anagrams.")

        print("Time elapsed for my algorithm: ")
        print("{:15.10f}".format(betterTime))

        print("")

    elif (testNumber == "1"):
        print("Testing just the Brute Force Algorithm...\n")

        string1 = input("Enter the first string: ")
        string2 = input("Enter the second string: ")

        bruteForceTime = effAnaBF(string1, string2)

        if (bruteForceAlgorithm(string1, string2) == True):
            print("\nThe Brute Force Algorithm determined that '" + string1 + "' and '" + string2 + "' ARE anagrams.")
        else:
            print(
                "\nThe Brute Force Algorithm determined that '" + string1 + "' and '" + string2 + "' ARE NOT anagrams.")

        print("Time elapsed for Brute Force Algorithm: ")
        print("{:15.10f}".format(bruteForceTime))

        print("")

    elif (testNumber == "2"):
        print("Testing just my algorithm...\n")

        string1 = input("Enter the first string: ")
        string2 = input("Enter the second string: ")

        betterTime = effAnaBtr(string1, string2)

        if (myAlgorithm(string1, string2) == True):
            print("\nMy algorithm determined that '" + string1 + "' and '" + string2 + "' ARE anagrams.")
        else:
            print("\nMy algorithm determined that '" + string1 + "' and '" + string2 + "' ARE NOT anagrams.")

        print("Time elapsed for my algorithm: ")
        print("{:15.10f}".format(betterTime))

        print("")

    else:
        print("Please enter a valid value and try again. Exiting...\n")

    exit(0)

# execute main method
main()



