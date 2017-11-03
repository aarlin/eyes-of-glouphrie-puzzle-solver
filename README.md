## Runescape Eyes of Glouphrie Puzzle Solver
Python GUI implementation to help players solve the puzzle lock using the shapes they have in their inventory.      
Images taken from http://2007.runescape.wikia.com/    

I started playing Old School Runescape recently and came upon this quest 
I did this quest when I was younger but had trouble trying to get the correct amount to unlock the machine. In order to aid me and potentially other people, I decided I'd make a program to help me see if I have the solution in my inventory  

I also wanted to work with some Python GUI. This was my first time implementing with Tkinter  

## What should you do before running program?
You should try to get as many shapes from Brimstail using drop trick method.  
Another way is to try to exchange big shape values for smaller shapes.  
The idea is get a coverage of values so when you try the locks, you can be sure to get a solution.  

## How to run the program and compatability 
Runs with Linux environment and works with Windows environment using cx_Freeze to turn files into a executable.    

### Windows: 
Please refer to the [release page](https://github.com/Fompei/eyes-of-glouphrie-calculator/releases) for Windows executable.   

Go to release page:  
Download build.zip  
Unzip file and open folder  
Two ways to open program  
1. Access folder directory eog-solver > build > exe.win32-2.7 > Run eyescalc.exe as Admin  
2. Access folder directory eog-solver > dist > Eyes of Glouphrie Calculator-1.0-win32.msi  
After downloading msi file, go to folder where downloaded; usually C:\Programs Files (x86)\Eyes of Glouphrie Calculator and run eyescalc.exe  

### Unix:   
Change directory to the location of eyescalc.py    
Run command `python eyescalc.py`      
There might be some dependencies that you'll have to install  
`apt-get install python-tk`  
`pip install Pillow`  
afterwards run `python eyescalc.py`. Python 2.7 is required  

If you want to build the python files into Windows, run  
`pip install cx_Freeze`   
`python setup.py build` or `python setup.py bdist_msi`  


## Type of Problem
The premise of this calculator involved adding shapes that held a numerical weight into a lock. The lock only opened itself with a certain weight.  
This is a variation of the subset sum problem.  

Our shapes that we hold in our inventory will be our array/list of numbers.  Our locks are the sum we are trying to find. 
Unlike the subset sum problem, we are restricted to a number of shapes allowed to open the lock.  
That is to say, if one lock has a limit of two shapes, we are lookng for a pair in the array that equals that lock weight  

## Screenshots
![alt tag](https://raw.githubusercontent.com/fompei/eyes-of-glouphrie-puzzle-solver/master/screenshots/linux_gui.png) 
![alt tag](https://raw.githubusercontent.com/Fompei/eyes-of-glouphrie-calculator/master/screenshots/windows_gui.png)
![alt tag](https://raw.githubusercontent.com/fompei/eyes-of-glouphrie-puzzle-solver/master/screenshots/sample_solution.png)  