# Testing cli interactivity

import sys

# here, we set the variable text 
# to the result of the user's input
# "prompt" is the string which determines 
# what the user is prompted with
text = raw_input("prompt")

# okay, this works to print out the user's input 
# but it prints each as it's own line. I want just
# one line.
print "You said " 
print text
print ", right?"

new_text = raw_input("Let's try that again. Say summit, I dare you.")

print "Oh, I see, you meant to say",
print new_text,
print ",right?"
