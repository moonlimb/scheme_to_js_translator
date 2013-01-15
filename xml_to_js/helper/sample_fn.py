
def pythagorean(a, b):
    c = a * a + b * b
    return Math.sqrt(c)
    

def fib_two(input):
    if input <= 0:
        return 0
    if input == 1:
        return 1
    return fib_two(input - 1) + fib_two(input - 2)


def number_of_words_per_letter(string_list):
    letter_dict = {}
    for word in string_list:
        if word:
            letter_dict.setdefault(word[0], []).append(word)
    return letter_dict


def palindrome(input):
    best_i, best_j = 0, 0
    # this one iterates forwards
    for i in range(len(input)):
        # this one iterates backwards
        for j in range(len(input), i, -1):
            # this if statement checks to see if the list is the same backwards and forwards
            if input[i:j] == input[i:j][::-1]:
                # this moves j one movement forward, best i and best j are counters for the palandrone 
                # sequence. so if we run into mom it will make note of what where to increment in I 
                #and where to increment for j. 
                if j - i > best_j - best_i:
                    best_i = i
                    best_j = j
    # return the part of the list that matches backwards and forwards
    return input[best_i:best_j]

def reverse_order(input):
    size = len(input)
    for i in range(len(input)/2):
        temp = input[i]
        input[i] = input[size-i-1]
        input[size-i-1] = temp
        
    return input
