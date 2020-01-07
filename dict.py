# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

counts = {}
words = []

name = input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"
name = "mbox-short.txt"
handle = open(name)

for line in handle:
    if not line.startswith("From: "):
        continue
    line = line.split()
    words.append(line[1])

for word in words:
    counts[word] = counts.get(word, 0) + 1 
   
bigvalue = None
bigkey= None
for key,value in counts.items() :
    if value > bigvalue:
        bigvalue = value
        bigkey = key   

print(bigkey, bigvalue)