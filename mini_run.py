# Testing cli interactivity

import sys

# "prompt" is the string which determines 
# what the user is prompted with
prompt = "Hi, and welcome to my little text adventure. There's not much here yet -- right now, this greeting and your response is all. \n"

# "text" is where we store the user's response to the prompt
text = raw_input(prompt)

#Here we echo back what the user said
print "You said", 
print text,
print ", right?"

