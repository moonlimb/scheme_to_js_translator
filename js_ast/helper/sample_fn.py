fibonacci

def pythagorean(a, b):
    c = a * a + b * b
    return Math.sqrt(c)
    

def fib_two(inp):
    if inp <= 0:
        return 0
    if inp == 1:
        return 1
    return fib_two(inp - 1) + fib_two(inp - 2)


def number_of_words_per_letter(string_list):
    letter_dict = {}
    for word in string_list:
        if word:
            letter_dict.setdefault(word[0], []).append(word)
    return letter_dict


def palindrome(inp):
    best_i, best_j = 0, 0
    # this one iterates forwards
    for i in range(len(inp)):
        # this one iterates backwards
        for j in range(len(inp), i, -1):
            # this if statement checks to see if the list is the same backwards and forwards
            if inp[i:j] == inp[i:j][::-1]:
                # this moves j one movement forward, best i and best j are counters for the palandrone 
                # sequence. so if we run into mom it will make note of what where to increment in I 
                #and where to increment for j. 
                if j - i > best_j - best_i:
                    best_i = i
                    best_j = j
    # return the part of the list that matches backwards and forwards
    return inp[best_i:best_j]

    def reverse_order(inp):
    size = len(inp)
    for i in range(len(inp)/2):
        temp = inp[i]
        inp[i] = inp[size-i-1]
        inp[size-i-1] = temp
        
    return inp
