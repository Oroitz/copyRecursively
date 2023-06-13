#/usr/bin/python

import os
import shutil

# Define kind of slash ('\' for Windows systems and '/' for Linux/Unix/MacOS systems)

if os.name == 'nt':
	slash = '\\'
else:
	slash = '/'

# If override is True, if there is any file with the same name in a directory it'll be overrided
# WARNING: if the override option is in true make sure the original file is not in a subdirectory of the given root directory or it'll be deleted

override = False

# Function for copy a file in a directory

def paste_recursively(ref_file, filename, directory):
	
	exist = False
	
	# Saves in a list the elements of the given directory
	
	dirs = os.listdir(directory)
	
	for file in dirs:
		
		# If the element of the directory is a subdirectory, the function is reloaded to copy the file there
		
		if  os.path.isdir(directory + slash +  file):
			paste_recursively(ref_file, filename, directory + slash + file)
		
		# If the file has the same name as the copying file, if override option is in True it is removed
		
		if file == filename:
			if override == False:
				exist = True
			else:
				os.remove(directory + slash +  file)
	
	# If override option is in False and there is no file with the same name, the original file is copied in the given directory
	
	if exist == False:
		
		shutil.copyfile(ref_file, directory + slash + filename)
		print('Pasting in ' + directory)

# Function to define the file to copy and the root directory for

def copypaste_recursively():
	
	# File to copy

	#ref_file = ''
	ref_file = input('Give the file directory to copy: ')
	
	# Check if the file exists and it's not a directory
	
	if not os.path.isfile(ref_file):
		if os.path.isdir(ref_file):
			print("Error: the given file is a directory")
		else:
			print("Error: the file does not exist")
		exit()

	# Root directory where the files will be copied

	#root_dir = ''
	root_dir = input('Give the root directory where the files will be copied recursively: ')
	
	# Check if the directory exists and it's not a file
	
	if not os.path.isdir(root_dir):
		if os.path.isfile(root_dir):
			print("Error: the given directory is a file")
		else:
			print("Error: the directory does not exist")
		exit()
	
	# If file is not in the same directory as execution directory the file's name is saved in the variable file
	
	if slash in ref_file:
		slash_pos = 0
		for n in range(0, len(ref_file)):
			if ref_file[n] == slash:
				slash_pos = n
		filename = ref_file[slash_pos:len(ref_file)]
	
	# If the give file is only the name its relative directory is defined
	
	else:
		filename = ref_file
		ref_file = '.' + slash + filename
	
	# If the root directory has no slash it is added
	
	if root_dir[len(root_dir)-1] != slash:
		directory = root_dir + slash
	else:
		directory = root_dir
	
	# The function to copy the file is loaded
	
	paste_recursively(ref_file, filename, root_dir)

copypaste_recursively()
