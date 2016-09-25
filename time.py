import time
import msvcrt
finish=10
count=0
n=0
print "press enter key to get started"
raw_input()
s_time=time.time()
while(1):
	key=msvcrt.getch()
	if key=='d':
		count=count+1
		print "-->",
		if count==finish:
			break
print "HINT:press s to go down because u reached end of the path"

finish=15
count=0
'''raw_input()'''
while(1):
	key=msvcrt.getch()
	if key=='s':
		count=count+1
		print "\t\t\t\t\t|"
		if count==finish:
			break
print "Enter d to move right",

finish=10
count=0
'''raw_input()'''
while(1):
	key=msvcrt.getch()
	if key=='d':
		count=count+1
		if n==0:
			print "\t\t\t",
			n=n+1
		print "-->",
		if count==finish:
			break

time_elapsed=time.time()-s_time
print "CONGRATES YOU HAVE FINISHED THE GAME"
print "Time taken is "+str(time_elapsed)
	