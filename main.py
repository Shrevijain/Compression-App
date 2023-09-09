file = open("members.txt",'r');
content = file.readlines()
file.close()
content.append("Shrevi Jain" + "\n")

file=open("members.txt",'w')
file.writelines(content)
file.close()
