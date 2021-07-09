# FileSearchProgram
This is a little Python project I've been working on due to running into issues with Windows native file search system. 

# Basic Information
Since I have no real formal coding experience and have relied on books and YouTube channels for learning, I figured I might try and take some of what I've learned and do something with it. The end result is the FileSearchProgram (not a good name, open to suggestions). I started working on this program as a way to sift through mods for The Sims 4, Skyrim, and Fallout 4 which had been effectively just dumped into a singular folder following a hard drive failure. The purpose of this project is to take the "Search" function from Windows Explorer and combine it with a tool to move all desired files. As I learn more about different modules and ways to code, I will make desired changes to this program in the hopes of making it more useful and to showcase what I've learned. 

# Dependencies
As of right now, there is a dependency for running the program, and that is the TQDM module. It is not a hard requirement as the program will work fine if you either delete or hashtag lines 4, 61, and 62. I say its not a hard requirement as I just found it to be interesting and threw it in. 

# Notes on Usage
The program was written to work with Windows or Linux based systems, though it works better on Windows than Linux. I don't have any versions of MacOS to demo on, but if I had to hazard a guess I would say it _should_ work like it does on Linux. Part of the problem that I've run into which I will learn more about and address is case-sensitivity between OSs. In Windows, any input given will work, regardless of case. This is not the same with Linux as **_case-sensitivity is a must._** Again, I am not sure as to why, I will research and address it as I learn more about it.

Another problem which is only apparent in Linux is the wildcard functionality. In Windows, wildcard functionality works as intended in cases of before and/or after a file name. Wildcard only works before a file type, though it is a bit reduntant since you can just input a wildcard in the file name section. This doesn't seem to be the case with Linux during my testing, as it required more specific terms rather than before or after wildcards. Both before and after seemed to work just fine. 

# How To Use
The program will ask for a desired location where the files you want to search through are located. Simply put the exact location of the folder where the files are located.

Windows: users/wrek-noir/Documents/Test

Linux: /home/wrek-noir/Documents/Test

It will then notify you that the desired folder is now selected and ask what file type you wish to search for. Input a file type when prompted.

Example: .jpg

The program will then ask for the name of the file or files that is to be searched. 

Example: Paris 

Example: *Paris

Example: Paris*

Example: \*Paris\*


For this explanation, we'll use the last example. It will then return all files that match the criteria of \*Paris*\.jpg by listing them out and counting the number of matches. 

The program will then prompt for a desired destination for the files.

Windows: users/wrek-noir/Pictures/Paris

Linux /home/wrek-noir/Pictures/Paris

A status bar will display (again, it's just an aesthetic thing that can be removed if desired) and the files will be moved. The program will ask if there there's anything else to search for, type "y" if yes, "n" if no. 

# Future Plans
There's a couple of things I'd like to do once I get some more understanding under my belt and explore some module documentation. The first thing is taking care of the issues with case-sensitivity, both on Linux and Windows. I haven't run into too much issue with case-sensitivity in Windows, but I've only tested it on a couple of thousand files so I'm not entirely sure if I've just been lucky or its a non-issue. Hopefully, whatever solution I can come up with for Linux will also work for Windows.

A problem that I had initially when I started testing this on Linux (which I tested on Debian, Ubuntu, and a derivivate of each) was the way that I wrote the variable dealing with combining the path and files. I fixed this by using the platform module which has fixed the problem and I don't see it breaking in the future, though I'm really just waiting.

At the end of the program when it asks if there's anything else to look for, I want to see about writing a piece of code of some kind that would allow the program to return to the source folder if desired, as it became incredibly tedious having to keep entering the same source path again and again. 
