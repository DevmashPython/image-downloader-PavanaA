import urllib
import re
import os
def downloadimgs():
	r= open('link.txt','r')
	for line in r:
		line= line[:-1]
		urllib.urlretrieve(line,os.path.basename(line))
	r.close()
geturl = "http://"+raw_input("enter url:\thttp://")
f = urllib.urlopen(geturl)	
html=f.read() 
a=re.compile('<img.*src="(.*\.jpg)"',re.IGNORECASE)	
n=a.findall(html) 
if not n: 
	exit("no images") 
file1=open('link.txt','w+') 
for i in n: 
 	i=geturl+"/"+i 
 	print i 
 	file1.write(i+"\n") 
file1.close() 
print "\nAll links saved in link.txt\n" 
while(1): 
 	ch = raw_input("Do you want to download all the images?(s/n)") 
 	if ch=='n' or ch=='N': 
 		exit( notdownloaded) 
	elif ch=='s' or ch=='S': 
 		downloadimgs() 
 		exit("Download Complete") 
 	else: 
		print "invalid choice...re-enter choice"  