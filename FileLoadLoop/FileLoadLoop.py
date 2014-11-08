# Load our initial list of files
FileList = open('./FileList.txt').read().splitlines()
print FileList
# For updating the strain list while the python script is running
# wait_string = raw_input('Please update file strains.txt and press enter.')

file_count = 0

FileList_length = len(FileList)
while file_count < FileList_length:
	print "Running script on %s" % (FileList[file_count])
	print "Modify the file now, if you want"
	a=raw_input()
	
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
       
        
    # For debugging. If I run this script in a windows command window the following will stop the window from closing before I can read the error message.
print "Press return to continue"
a=raw_input()