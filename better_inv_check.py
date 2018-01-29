
# Now we're going to read the items present in the inventory file to generate the prompt based on what the user actively has. 
# Also, I added an ownership flag to the inventory format and added logic to check that flag in this file.


# We're using try in order to catch any errors and deal with them.
try:
	# we open the inventory file
	inv = open('inv.txt')



	# Here I prepare to store a list of items. For now, this is unused;
	# I can edit this list as the player has items added and removed
	# from their inventory.
	list_of_items = []

	#iterate through list
	for each_item in inv:
		#gotta catch errors
		try:
			(item, owned, desc) = each_item.split(':',2)
			if owned == "1":
				list_of_items.append(item)
		except ValueError:
			print "Something went awry trying to populate user's inventory list"
	#reset the file pointer so I can read from the beginning in my next use of inv.txt
	inv.seek(0)

	# make list into string
	owned_items = ", ".join(list_of_items)

	# >0 means the item is not in inventory
	oops = 0

	# response when item is not present in inventory
	absent = "You don't have that, you dingleberry. Ask about something you actually have."

	# Prompt is what the user will be told before input. The list of items is appended to the greeting, as is the newline after.
	prompt = "Let's talk about your stuff. What items do you want to hear about? Right now, your bag contains: "
	prompt += owned_items
	prompt += "\n" 
	

	# Text is the user's input.
	text = raw_input(prompt)


	# We will iterate over the inventory file's lines using a for loop.
	for each_item in inv:

		# Gotta catch errors in the loop, too!
		try: 
			# We split each line into the item's name and the item's description
			(item, owned, desc) = each_item.split(':',2)

			# if the item is not in the inventory file
			if item != text:
				oops += 1

			# if the item is in the inventory file
			else:
				# if the player owns the item
				if owned == "1":
					# set oops in deep negative so iteration on items in the list that don't match the query won't cause false positives
					oops -= 6000000  
					# print the item's description
					print desc
				# if the player does not own the item
				else: 					
					oops += 1
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

#close inventory file
inv.close()

