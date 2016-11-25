#This code is written in pyhton3 please use python3 to run this code.
import random
import string
import math
def randomword():
	length=random.randrange(3,20)	
	return ''.join(random.choice(string.ascii_uppercase) for i in range(length))

def check(code,guessed):
	d={}
	correct=""
	wrong=""
	print("generated code is :",''.join(code))
	for x in range(0,len(guessed)):
		for y in range(0,len(code)):
			if code[y]==guessed[x]:
				if y in d.keys():
					continue
				if x==y:
					correct+=guessed[x]
					d[y]=code[y]
	for x in range(0,len(guessed)):
		for y in range(0,len(code)):
			if code[y]==guessed[x]:
				if y in d.keys():
					continue				
				if x!=y:
					wrong+=guessed[x]					
					d[y] = code[y]
	return correct,wrong
def comp(code,maxx):
	compgess=''.join(random.choice(string.ascii_uppercase) for i in range(maxx))
	if compgess==code:
		print("computer wins!")
	(correct,wrong)=check(code,compgess)
	
	if len(correct)==0:
		correct="NO SUCH WORDS"
	if len(wrong)==0:
		wrong="NO SUCH WORDS"				
	print("Characters that are correctly guessed by computer and are in correct positions are:",correct)
	print("Characters that are correctly guessed by computer but are in wrong positins are:",wrong)
generated=list(randomword())
print("Length of generated code is:",len(generated))
ntr=round(math.sqrt(len(generated)))
print("Number of attempts allowed =",ntr)
cnt=0
flag=0
print("generated code is :",''.join(generated))
while(cnt!=ntr):
	y=list(input().upper())
	if y==generated:
		print("You Guessed the code right!!")
		flag=1
		break
	(correct,wrong)=check(generated,y)
	if len(correct)==0:
		correct="NO SUCH WORDS"
	if len(wrong)==0:
		wrong="NO SUCH WORDS"				
	print("Characters that are correct but in correct positions are:",correct)
	print("Characters that are correct but in wrong positins are:",wrong)
	print("Computer player stats are:--------")
	comp(generated,len(generated))
	cnt+=1
if flag!=1:
	print("Sorry Better Luck Next time")	
