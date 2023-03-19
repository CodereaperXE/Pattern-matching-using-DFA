

def construct_state_set(val):

	temp1=[]
	temp2=[]

	count=0

	while(count<len(val)):
		for i in range(0,len(val)):
			if(val[i]==val[count]):
				temp2.append((val[i],"next"))
			else:
				if(val[i]==val[0] and count==1):
					temp2.append((val[i],"stay"))
				else:
					temp2.append((val[i],0))

		temp1.append(temp2.copy())
		temp2.clear()
					
		count+=1
	
	return temp1


def state_machine(pattern,string):
	rules=construct_state_set(pattern)
	print("Displaying Rule Set [[(element,condition)state-conditions]]")
	print("---------------------------------------------------------")
	print(rules)
	print("---------------------------------------------------------")
	max_states=len(pattern)
	state=0
	count=0
	flag=False
	for element in string:
		i=0
		while(i<max_states):
			if(element==rules[state][i][0]):
				if(rules[state][i][1]=="next"):
					state+=1
					break
				elif(rules[state][i][1]==0):
					state=0
					break
				elif(rules[state][i][1]=="stay"):
					break
				else:
					state=0
					break
			else:
				i+=1
		count+=1

		if(state==max_states):
			state=0
			print("Pattern found in index "+str(count-max_states))
			flag=True
	if(not flag):
		print("Pattern not found")


print("Deterministic finite automata pattern matching-Built by Rishab Budale-19/3/2023")
pattern=str(input("Enter the pattern to search "))
text=str(input("Enter the text to search "))
state_machine(pattern,text)
