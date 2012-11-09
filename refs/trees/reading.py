
'''
Accepts a variable inp, convert inp to an int and assign that value to variable base.
Returns a value rounded up or down depending on if the difference is >= 0.5.
'''
def rounding(inp):
    base = int(inp)
    if inp - base >= 0.5:
        return base+1
    else:
        return base

'''
Line counting function - pass a string or block of text. If string is empty (''), return 0.
If there is at least one line in text, return count=1; for each newline, add 1 to count. Return
the number of lines (count) at the end of the loop.
'''
def line_count(inp):
    if not inp:
        return 0
    count = 1
    for char in inp:
        if  char == "\n":
           count  += 1    
    return count

'''
this is the pythagorean theorem. Using two sides (a & b) we can caculate the third side of a 
right triangle. The square root of c=a^2 + b^2 is the side.
'''
def pythagorean(a, b):
    c = a * a + b * b
    return Math.sqrt(c)
    
'''
Pass a string, dict, list, tuple (anything that is indexable). Get the length of that variable.
Divide that length by 2, and make that length/2 the range for the loop. Exp: len(word)=4, range=2, 
i=0, i=1 once the loop runs.

this function will take the last half of the string and put it in the front to reverse the word. 
ex: word becomes drow however if it is an odd number string it doesn't work too well 
ex: erica becomes aceri 
'''
def reverse_order(inp):
    size = len(inp)
    for i in range(len(inp)/2):
        temp = inp[i]
        inp[i] = inp[size-i-1]
        inp[size-i-1] = temp
        
    return inp

'''
Open a text file and split words on spaces into a list word_string. Create an empty dictionary.
Loop through list word_string; check to see if word is in dictionary - if not, set its value to 0,
so key = word, value = 0. Then increment num by one, and reset value to num. If the word is in 
the dict, then just increment its value by one. Finally, iterate over the dict and print the keys
and values. You should have a word count (ie key = a word, value = number of times that word appears.)
'''
def word_count():
    text = open("sample_input.txt")
    word_string = text.split()
    howdy = dict()
    for word in word_string:
        num = howdy.get(word, 0)
        num += 1
        howdy[word] = num
    
    for k, v in howdy.iteritems():
        print "%s:\t%d"%(k, v)

'''
Pass in something that is indexable (list, string, etc). Set boolean variable swapped = True;
Start loop and set swapped to False (since it hasn't been swapped yet). Look at first item in list,
and compare it to second item in list. If first has greater value, move it to second position, and 
move second position value to first position. Set swapped to True, and iterate over the next pair. 
This ends up looking like a sorting function, and should stop when the items are in order from lowest
to highest.
'''
def sort(inp):
    swapped = True
    while swapped == True:
        swapped = False
        for item in range(len(inp)-1):
            if inp[item] > inp[item+1]:
                tmp = inp[item]
                inp[item] = inp[item+1]
                inp[item+1] = tmp
                swapped = True

'''
this is the fibonacci sequence. the input will determine how many times the function
calculates the next number in the sequence. The fibonacci sequence takes the sum of the 
previous 2 numbers to make up the value of the next number. 
'''

def fibonacci_generator(inp):
    a, b = 0, 1
    for i in range(inp):
        a, b = b, a + b
    return a

'''
This function returns the fibonacci sequence by doing the following:
If number <=0, return 0. If number is greater than 1, return number minus 1.
For numbers greater than 1, recursively call the function as such:
inp = 2
fib_two(2) = fib_two(1) + fib_two(0) = 1
fib_two(3) = fib_two(2) + fib_two(1) = 1 + 1 = 2
....
fib_two(5) = fib_two(4) + fib_two(3) = 3 + 2 = 5
fib_two(6) = fib_two(5) + fib_two(4) = 5 + 3 = 8
... 
'''

def fib_two(inp):
    if inp <= 0:
        return 0
    if inp == 1:
        return 1
    return fib_two(inp - 1) + fib_two(inp - 2)

'''
Compare two indexable items. If they are not of equal length, return False. If they are of equal length:
Iterate based on length. Compare index of inp1 to index of inp2. If they are not equal, return False. 
If they are equal, return True. 
'''
def compare_items(inp1, inp2):
    if len(inp1) == len(inp2):
        for i in range(len(inp1)):
            if inp1[i] != inp2[i]:
                return False
        return True
    return False

'''
Takes two dictionaries as arguments, and create a new empty dictionary. 
Iterate through first dictionary, and check to see if the key in inp1 exists in inp2.
If it does, add it to the new dictionary as a key, and assign it the value of value in
inp1 plus the value of inp2's key. At the end, return the new dictionary. This function
will pull out all duplicate keys and either adds the values in the case of numbers or 
concatenates strings.
'''
def dict_combinator(inp1, inp2):
    new_dict = {}
    for k, v in inp1.items():
        if k in inp2:
            new_dict[k] = v + inp2[k]
    return new_dict

'''
Takes one indexable arg, and creates new empty dictionary. Loop through inp; if s is not null,
then add the first element of s as a key in outp, and make its default value an empty list. Append 
s to that empty list. For ex: our inp = ('one', 'two', 'three') s[0] = o and s = one it iteriates 
through each item so our dictionary ends up being a list of keys with one letter and all the values 
that begin with the letter of our key.
'''
def number_of_words_per_letter(string_list):
    letter_dict = {}
    for word in string_list:
        if word:
            letter_dict.setdefault(word[0], []).append(word)
    return letter_dict

'''
Pass in list, and set two variables to 0. Counts down (subtracts one) range 
on length input to zero. 
'''
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

'''
'''

def mystery13(inp_a, inp_e):
    # only loops if a is an iterable item with more than one element
    while len(inp_a) > 1:
        # if inp_e equals the element at half the length of inp_a, return true
        if inp_e == inp_a[len(inp_a) / 2]:
            return True
        # otherwise, check to see if inp_e is greater than element at half length of inp_a
        # inp_a now only contains values from 0 until half of length of inp_a.
        elif inp_e < inp_a[len(inp_a) / 2]:
            inp_a = inp_a[:len(inp_a) / 2]
        # if inp 
        else:
            inp_a = inp_a[len(inp_a) / 2 + 1:]
 
    return len(inp_a) > 0 and inp_e == inp_a[0]

def mystery_m(inp1, inp2):
    i, j = 0, 0 # counters
    outp = []   
    while i < len(inp1) and j < len(inp2):
        # compare first indices of both lists
        if inp1[i] <= inp2[j]:
            # if first index of first var is less than or equal to first index of second var, add to empty
            # list and add one to our first var counter
            outp.append(inp1[i])
            i += 1
        # # if first index of first var is greater than or equal to first index of second var, add the 
        # second var's first index to empty list and add one to our second var counter
        if inp1[i] >= inp2[j]:
            outp.append(inp2[j])
            j += 1
    # if i or j length is less than inp1 or inp2 respectively, then add the rest of the list from 
    # i or j to the end of the list, and output.
    if i < len(inp1):
        outp.extend(inp1[i:])
    elif j < len(inp2):
        outp.extend(inp2[j:])

    return outp

def mystery_s(inp):
    if len(inp) < 2:
        return inp
    # fh = first half (from 0 to length of input / 2) sh = second half (from length of inp / 2 to end)
    fh = mystery_s(inp[:len(inp) / 2])
    sh = mystery_s(inp[len(inp) / 2:])

    # pass fh
    return mystery_m(fh, sh)
