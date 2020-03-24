#hw3py, collaborator: Anh Nguyen

#######from hwtest
from hw3 import *

#4.24----double check this
def cheer(mascot):
    mascot=mascot.upper()
    mc = mascot.capitalize()
    print('How do you spell winner?')
    print('I know, I know!')
    for i in list(mascot):
        print(i, end=' ')
    print("!\nAnd that's how you spell winner!")
    print('Go '+mc+'!')

#4.25
#addition assignment += from :
#https://python-reference.readthedocs.io/en/latest/docs/operators/addition_assignment.html

def vowelCount(strinput):#######not very effective but still right idea
#############think count method
	strinput = strinput.casefold()
	vchecker = 'aeiou'

	acount=0
	ecount=0
	icount = 0
	ocount= 0
	ucount = 0
	for vl in strinput:
		if vl in vchecker and vl=='a':########all ifs independent of eachtoter
			acount+=1
		if vl in vchecker and vl=='e':
			ecount+=1
		if vl in vchecker and vl=='i':
			icount+=1
		if vl in vchecker and vl=='o':
			ocount+=1
		if vl in vchecker and vl =='u':
			ucount+=1
	print('a, e, i, o, and u appear, respectively, '+str(acount)+', '+str(ecount)+', '+str(icount)+', '+str(ocount)+', '+str(ucount)+' times.')


''' more effective code:
def vowelCount(strinput):
	strinput = strinput.casefold()
	vcheck = 'aeiou'
	for v in strinput:
		if v in vcheck:
			ac=strinput.count('a')
			ec=strinput.count('e')
			ic=strinput.count('i')
			oc = strinput.count('o')
			uc=strinput.count('u')
			return ac,ec,ic,oc,uc

		
>>> vowelCount('yes')
(0, 1, 0, 0, 0)
>>> vowelCount('oohawehagsrhf')
(2, 1, 0, 2, 0)
>>> 
'''

#4.26
def crypto(fILe):
    msg = open('crypto.txt', 'r')
    lines = msg.read()
    newmsg = lines.replace('secret', 'xxxxxx')
    print(newmsg)
    msg.close()

#4.28
def links(fIle):
    fILe = open(fIle, 'r')
    char = fILe.read()
    lct=char.count('</a>')#counts the ending anchor tags for hyperlinks
    #print(lct)
    return lct
    fILe.close()
    

#4.31-double check
#removing punctuation source: https://www.geeksforgeeks.org/removing-punctuations-given-string/
def duplicate(fILe):
    hasdbl=open(fILe, 'r')

    exFl = hasdbl.read()#this is READING CHARACTERS, TRY SPLITTING IT
    pcts= '!()-[]{};\,<>./?'

    for i in exFl.lower():#thorough but aggressive method,
        if i in pcts:
            exFl = exFl.replace(i, "")#changes string to get rid of pcts

    #print(exFl)#checks if everything looks good
	
    #make string into list of words.
    wordList = exFl.split()# this will split by space making list of words
    #make a counter thing
    for itm in range(len(wordList)):
        #print(itm,wordList[itm])
        wct = wordList.count(wordList[itm])
	#make boolean to see if file has duplicates
	#print(wct,wordList[itm])
        if wct>1:
            return True
    return False
    hasdbl.close()
#COUNT METHOD COUNTS WORDS. THERE ARE STAGES


if __name__=='__main__':
    import doctest
    print( doctest.testfile('hw3TEST.py'))



    

    

   
    
