# VeeamTestTask

Description:

Implement a program that synchronizes two folders: source and replica. 

The program should maintain a full, identical copy of source folder at replica folder. 

Solve the test task by writing a program in one of these programming languages:  Python C/C++ C#  

Synchronization must be one-way: after the synchronization content of the replica folder should be modified to exactly match content of the source folder;  

Synchronization should be performed periodically.  File creation/copying/removal operations should be logged to a file and to the console output;  

Folder paths, synchronization interval and log file path should be provided using the command line arguments;  

It is undesirable to use third-party libraries that implement folder synchronization;  

It is allowed (and recommended) to use external libraries implementing other well-known algorithms. For example, there is no point in implementing yet another function that calculates MD5 if you need it for the task – it is perfectly acceptable to use a third-party (or built-in) library.


Step 1:

    git clone https://github.com/ribeiluke/VeeamTestTask.git

Step 2:

    python3 -m venv ./.venv/

Step 3:

    source .venv/bin/activate

Step 4:

    pip install -e .

Step 5 - run commmand

run command syntax:
    
    python3 main.py --sourceFolder /path/to/sourceFolder/ --replicaFolder /path/to/replicaFolder/ --logPath /path/to/logFile --interval integer

Example run command:

    python3 main.py --sourceFolder /home/lukenyr/Documents/Python/VeeamTestTask/ --replicaFolder /home/lukenyr/Documents/Python/VeeamTestTask/replica/ --logPath /home/lukenyr/Documents/Python/VeeamTestTask/log.txt --interval 1

Bonus:

Program includes a help command to reduce learning curve. Help command:
    
    python3 main.py -h
