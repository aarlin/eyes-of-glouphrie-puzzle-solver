## Runescape Eyes of Glouphrie Quest Calculator
Python GUI implementation to help players calculate the shapes they have in their inventory.    
Images taken from http://2007.runescape.wikia.com/  

I started playing Old School Runescape recently and came across this quest   
I did this quest when I was younger, and when I was doing it again I had trouble trying to get the correct amount to unlock the machine. In order to aid me and possibly others, I decided I'd make a program to help me see if I have the solution in my inventory  

I also wanted to work with some Python GUI. This was my first time implementing with Tkinter  

## What should you do before running program?
You should try to get as many shapes from Brimstail using drop trick method.  
Another way is to try to exchange big shape values for smaller shapes.  
The idea is get a coverage of values so when you try the locks, you can be sure to get a solution.  

## How to run the program and Compatability 
Runs with Linux environment  
Works with Windows environment using cx_Freeze to turn files into a executable. Please refer to the [release page](https://github.com/Fompei/eyes-of-glouphrie-calculator/releases) for Windows executable.    

### Windows: 
Access the files:  
build > exe.win32-2.7 > eyescalc.exe   

### Unix:   
Change directory to files  
Run command `python eyescalc.py`      
There might be some dependencies that you'll have to install; possibly PIL and tkinter  

## Type of Problem
The premise of this calculator involved adding shapes that held a numerical weight into a lock. The lock only opened itself with a certain weight.  
This is a variation of the subset sum problem.  

Our shapes that we hold in our inventory will be our array/list of numbers.  Our locks are the sum we are trying to find. 
Unlike the subset sum problem, we are restricted to a number of shapes allowed to open the lock.  
That is to say, if one lock has a limit of two shapes, we are lookng for a pair in the array that equals that lock weight  



## Screenshot
![alt tag](https://raw.githubusercontent.com/Fompei/eyes-of-glouphrie-calculator/master/linux_gui.png)  
![alt tag](https://raw.githubusercontent.com/Fompei/eyes-of-glouphrie-calculator/master/windows_gui.png)  