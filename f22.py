import random
import string
import math


def randomword():
	length=random.randrange(3,20)	
	return ''.join(random.choice(string.ascii_uppercase) for i in range(length))

def check(code,guessed):
	correct=""
	wrong=""
	for x in guessed:
		if x in code:
			if code.index(x)==guessed.index(x):
				correct+=x
			else:
				wrong+=x
	if len(correct)==0:
		correct="NO SUCH WORDS"
	if len(wrong)==0:
		wrong="NO SUCH WORDS"
								
	print("Characters that are correct but in correct positions are:",correct)
	print("Characters that are correct but in wrong positins are:",wrong)
x=list(randomword())
print("Length of generated code is:",len(x))
ntr=round(math.sqrt(len(x)))
print("Number of attempts allowed =",ntr)
cnt=0
print(x)
flag=0
while(cnt!=ntr):
	y=list(input().upper())
	if y==x:
		print("You Guessed the code right!!")
		flag=1
		break
	check(x,y)
	cnt+=1
if flag!=1:
	print("Sorry Better Luck Next time")	

