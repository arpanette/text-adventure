# Here I prepare to store a list of items. For now, this is unused;
# I can edit this list as the player has items added and removed
# from their inventory.
list_of_items = []

# >0 means the item is not in inventory
oops = 0

# response when item is not present in inventory
absent = "You don't have that, you dingleberry. Ask about something you actually have."

# Prompt is what the user will be told before input.
prompt = "Let's talk about your stuff. What items do you want to hear about? Right now, you only have a key, a map, and mirror. \n \n"

# Text is the user's input.
text = raw_input(prompt)

# We're using try in order to catch any errors and deal with them.
try:
	# we open the inventory file
	inv = open('inv.txt')

	# We will iterate over the inventory file's lines using a for loop.
	for each_item in inv:

		# Gotta catch errors in the loop, too!
		try: 
			# We split each line into the item's name and the item's description
			(item, desc) = each_item.split(':',1)

			# if the item is not in the player's inventory
			if item != text:
				oops += 1

			# if the item is in the player's inventory
			else:

				# set oops in deep negative so iteration on items in the list that don't match the query won't cause false positives
				oops -= 6000000  
				# print the item's description
				print desc
					
		# raise an exception if the for loop shits the bed
		except ValueError:

			# the error message
			print "Something went wrong in the for loop :( "
		# if the item isn't present

except IOerror:
	print "Uh...looks like your inventory file is misplaced or named incorrectly."

if oops > 0:
		# print absence message
		# (maybe have a few, randomly pick one
		# so it's a little less rote)
		print absent

else:
	pass
	# should close file here
	# not quite sure if it works right, commenting out for first tests
	# inv.close()

