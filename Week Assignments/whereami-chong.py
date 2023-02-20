#Open file and create split input
file_in = open('whereami.in')
data = file_in.read().strip().split('\n')

#Int all the data and set answer and well as mailbox point
n = int(data[0])
mailboxes = data[1]
ans=n

#Determine the mailboxs for unique configuration
for k in range(1, n + 1):
	sequences = set()
  #Add mailboxes as needed for unique lcoationing
	for i in range(n - k + 1):
		sequences.add(mailboxes[i : i + k])
  #Stop if the necessary mailbox amount is found
	if len(set(sequences)) == (n - k + 1):
		ans = k
		break

#open and write out answer!
fileOut = open("whereami.out",'w')
fileOut.write(str(ans))
fileOut.close()