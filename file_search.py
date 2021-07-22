import fnmatch
import os
import shutil
import glob
import platform
from tqdm import tqdm
from time import sleep

while True: #This is used for several loops that exist throughout the program.
    path = input("Where do you want to go? \n") #This takes an input for a desired directory. 

    isdir = os.path.isdir(path) #Creates a variable for a check to see if the directory exists.
    
    if isdir == False: #If statement to notify user that directory does not exist, and to prompt for the directory again.
        print("No such directory exists. Check the destination again, please. \n")
        continue
            
    os.chdir(path) #Sets our working directory to the inputed path from above.

    current_path = os.getcwd() #Creates a variable for the current directory.

    print('\n') #Just creates a bit of separation, this will be seen frequently thoughout. 

    print("Congrats, we are now at %s." % current_path) #This confirms whether or not we are in the desired directory. 

    source_path = os.listdir() #This creates a variable containg a list of all entries in a given directory.
                               #Our path is left blank as it is self referential.
    print('\n')

    file_type = input("What kind of file do you want to search for? \n") #This asks what part of a file type that the user
                                                                         #would like to search for and assigns it to a variable.
                                                                       
    print('\n')

    file_name = input("And what's the name of the file we're looing for? \n") #Creates and assigns a variable with the name of the file. 

    f_file = ((file_name)+(file_type)) # Joins the file name and file type to a singluar value.

    print('\n')

    for file in source_path:  #This for loop is where the program scans through the directoy looking for matches.
        if fnmatch.fnmatch(file, f_file):  #By using fnmatch, the program searches for the f_file s
            print(file) # This can be removed if desired, I have it included as it reports back anything matching f_file so I can see if something has been picked up by mistake.
            
        
    count = len(fnmatch.filter(source_path, f_file)) # Counts the total number of matches in the directory. Can be removed if desired.

    print('\n')

    print("There's a total of " + str(count) + " " + file_type + "(s) that match the search term " + file_name +".") #Simply outputs how many files match the initial criteria. Can be removed. MUST BE REMOVED IF LINE 41 IS REMOVED.

    if platform.system() == 'Windows': #This runs a check to see if the OS is Windows or not as this is what I originally designed the script for. 
        source_files = (path +  '\\' + f_file) #This combines the working directory and the f_file variable into a singluar value to let glob know what files are where in a Windows OS.
    else:
        source_files = (path +  '//' + f_file) #Performs the same function as line 48, but for Linux and Unix systems.

    print('\n')

    target_path = input("Where are we moving the " + file_type + "(s) to? \n") #Asks for the desired target directory.

    for file in glob.glob(source_files): #Gets all the files in the source_files variable as selected paths for moving.
        shutil.move(file, target_path) #Moves all the files from source_files to target_path.

    print('\n')

    for i in tqdm(range(100)): #This for loop is just a super simple visual timer. Can be removed if desired.
        sleep(0.02)

    print('\n')

    while True: #I won't get too into this, this is just a loop checking to see if the user wants to do the program over again to search for other files or just close it out. 
        answer = (str(input('Would you like to look for something else? (y/n): \n')))
        if answer in ('y', 'n'):
            break
        print("Invalid input.")
    if answer == 'y':
        continue
    else:
        print("Done.")
        break
        

