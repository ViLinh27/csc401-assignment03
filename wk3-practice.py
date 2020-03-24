#hw3.py practice exercises

#4.17
'''
Translate each part into a python statement using approdiate string methods
a)assign to variable message string 'The secret of this message is that it is
secret.'
b) assignto variable length the the length of string message, using operator
len().
c)assign to variable count the number of times the substring 'secret' appears in
string message,using string method count().
d)assign to variable censored a copy of string message with every occurence of
substring 'secret'replaced by 'xxxxxx', using string method replace().
'''
#a)
message='The secret of this message is that it is secret.'
#b)
length = len(message)
#c
count = message.count('secret')
#d
censored = message.replace('secret','xxxxxx')

#4.18------------------------------------
'''
suppose variable s has been assigned in this way:
s=''''''It was the best of times, it was the worst of times; it was the age of
wisdom,it was the age of foolishness;it was the epoch of belief,it was the epoch
of incredulity;it was...''''''

Do the following in order:
a)Write a sequence of statements that produce a copy f s, named newS, in which
characters ., ,, ;, and \n have been replaced by blank spaces.
b)Remove leading and trailing blank spaces in newS(and name the new string newS).
c)Make all the characters in newS lowercase(and name new string newS).
d)compute the number of occurences in newS of string 'it was'.
e)change every occurence of was to is( and the new string newS).
f)Split newS into a list of words and name the list listS.
'''
s='''It was the best of times, it was the worst of times; it was the age of
wisdom,it was the age of foolishness;it was the epoch of belief,it was the epoch
of incredulity;it was...'''
#a
newS=((s.replace('.',';')).replace(';',',')).replace(',',' ')
#b----------------------check this one
#
#c
newS=newS.lower()
#d
pcount=newS.count('it was')
#e
newS=newS.replace('was','is')
#f
listS=newS.split()
#4.19
'''
write python statements that print the next formatted outputs using the already
assigned variables first, middle and last:
>>>first = 'Marlena'
>>>last = 'Sigel'
>>>middle = 'Mae'

a)Sigel, Marlena Mae
b)Sigel, Marlena M.
c)Marlena M. Sigel
d)M. M. Sigel
e)Sigel, M.
'''
first = 'Marlena'
last = 'Sigel'
middle = 'Mae'

print(last+', '+first,middle)
print(last+', '+first,middle[0]+'.')
print(first,middle[0]+'.',last)
print(first[0]+'.',middle[0]+'.',last)
print(last+',',first[0]+'.')

#4.20
'''
Given string values for the sender, recepient, and subject of an email, write
a string format expression that uses variables sender,recipeient, and subject and that
prints as shown here:
>>>sender= 'tim@abc.com'
>>>recipient = 'tom@xyz.org'
>>>subject = 'Hello!'
print(???)

From: tim@abc.com
To:tom@xyz.org
Subject: Hello!
'''
sender = 'tim@abc.com'
recipient = 'tom@xyz.org'
subject = 'Hello!'
print('From:',sender)
print('To:',recipient)
print('Subject:',subject)
