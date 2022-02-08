def contains(word,letters):
    if letters == "":
        return True
    word = word.strip()
    for letter in letters:
        if letter not in word:
            return False
    return True

def not_contain(word,letters):
    if letters == "":
        return True
    word = word.strip()
    for letter in letters:
        if letter in word:
            return False
    return True


def right_place(word,letters):
    if letters == "":
        return True
    word = word.strip()
    for i in range(len(word)):
        if letters[i] != "." and word[i] != letters[i]:
            return False
    return True


def no_wrong_place(word,letters):
    if letters == "":
        return True
    word = word.strip()
    for i in range(len(word)):
        if contains(word[i],letters[i]) == True:
            if letters[i] != "." and word[i] == letters[i]:
                return False
    return True




f = open('words.txt', 'r')

words = []

for word in f:
    words.append(word.strip())


guesses = 6

for i in range(guesses):

    one = input("\n1. Write letters in word: ")
    two = input("2. Write letters not in word: ")
    three = input("3. Write letters in correct position: ")
    four = input("4. Write letters in incorrect position: ")

    lst = []

    for word in words:
        if contains(word,one) == True:
            if not_contain(word,two) == True:
                if right_place(word,three) == True:
                    if no_wrong_place(word,four) == True:
                        lst.append(word.strip())

    words = sorted(lst)

    print(words)


    if len(words) == 1:
        print("Solved! Word is: {}.".format(words[0].strip()))
        break
