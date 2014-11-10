# Load our initial list of files
FileList = open('./FileList.txt').read().splitlines()

# Let's also display it to make sure we have loaded the right list
print FileList

# FileLoadLoop.py
# Part of the PythonTips series on deparkes.co.ukqa
# Duncan Parkes

# We will loop through the different items in this newly load list.
# After each iteration we will check to see if the list has been updated, and
# load the new list if it has.
file_count = 0
FileList_length = len(FileList)
while file_count < FileList_length:
	print "Running script on %s" % (FileList[file_count])
	print "Modify the file now, if you want"
	a=raw_input()
	
	# not sure why there is this while loop here
	# check this actually needs to be here.
	# use a try - except block to catch any failure to load the file
	while True:
		try:
			file_list_new = open('./FileList.txt').read().splitlines()
			if FileList != file_list_new:
				FileList = file_list_new
				print(FileList)
				print('New list loaded successfully');
			break
		except ValueError:
			print('Error loading new file\nWill try again next time.')
	FileList_length = len(FileList)
	file_count = file_count + 1
       
        
print "Press return to continue"
a=raw_input()