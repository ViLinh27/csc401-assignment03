#textAndFiles.py

#####week3#######

#iteration/loops-see controlStructures.py
#review
#text and files
#quizzes will be due soon---------------not timed---used to practice for exams
##########yes there are trickquestions in quizzes

'''
print v return
print is for user
print displays answer
return makes asnwer user available for other code
return gerneally better
return= "the answer is"
return terminates a function(hence any loops in that function)

cant technically return multiple things but you can collect those things to
return containter of multiple things

print displays answer
return  means "the answer is"and the function calls and evaualues to the returned value


arguments v parameters

def f(a,b):
    print(a,b)

>>>f(2,3)

a, b are parameters, local variables inside function

2,3 are arguments fed to function

arguments are substituted for paramters
i.e. a=2,b=3

'''

#######functions vs methods######
'''
functions are called directly
print()
abs()
max()

methods have caling objects(lst=[])
lst.append(3)
lst.pop()
'''

##############more on str################

'''
str(ings) are immutable
-cant change them
-but you can make new ones based on old ones


consider the .split() method. It splits squences of words (ususally on spaces
or new line characters

Essentially splits a sentence(string) into its words into a list of words

>>> #replace
>>> s = 'hello'
>>> s.replace('e', 'E')
'hEllo'
>>>


format() method
letter = ''Dear {} ,dfalsdfslkfjalsdfas;d,kd;laksjf;{}''
>>> letter
'Dear {} ,dfalsdfslkfjalsdfas;d,kd;laksjf;{}'
>>> letter.format('Jane',100)
'Dear Jane ,dfalsdfslkfjalsdfas;d,kd;laksjf;100'
>>>


#4.24 format doesn't solve whole prob, use loop


check 8.pm if you want to learn about optional methods like sep and end=
sep defaults to ' '
end efaults to '\n'

'''


#############files ##################
'''
8:10pm

open(<filename>, mode='r')
    opens file with name<filename>
     and returns a file object

     filename is relative to working folder/directory
     easiest to place in the same folder as your module

modes
    'r'ead - default
    'w'rite
    'a'ppend

file methods

    read()= returns contents as single str

    readlines()- rads contents as a list of strings

    write(s) - writes single str to file

    close()- closes the file, should always close files!!!!!!!!!

working with files a lot: look up "with


hint, keep these straight:
1-file name, a string
2-file objet
3- contenets of file,, string or lists of st
'''

######file example ############

'''
make this work:
>>>numchars('out.txt')
????

'''


def numchars(filename):
    file = open(filename)
    contents = file.read()
    file.close()

    n = len(contents)
    return n


##############dictionaries##########
count{}
'''
works differently than lists because it uses keys instead of indexes
each key in dictionary has a value

'''









