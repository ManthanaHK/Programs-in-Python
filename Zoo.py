zoodata = [['Lion','Elephant','Girrafe'],['Borwn-Gold','Gray-Black','Yellow']]
animals,color = zoodata

print('Enter the animal name:')
animalname=input()
print('The color of '+animalname+' is '+zoodata[1][animals.index(animalname)])

print('Do you want know about all the animals? \nIf you want, enter /yes/.')
reply = input()
if reply == 'yes':
	for i in range(1):
	   for j in range(3):
		   print('The color of '+zoodata[i][j]+' is '+zoodata[i+1][j])
else:
	print('Thanks for visiting :-)')
