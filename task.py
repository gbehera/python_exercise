import random

all = input ("Enter all the task you have separated with a ','!\n")
task= all.split(",")

print ("This are the task in your tasks list:")
print (task)

x=random.choice(task)
print ("This the task '%s' selected on Random! I hope you will complete and won't disappoint me!" %(x))