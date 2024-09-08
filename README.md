# VeeamTestTask

Step 1:

    git clone https://github.com/ribeiluke/VeeamTestTask.git

Step 2:

    python3 -m venv ./.venv/

Step 3:

    source .venv/bin/activate

Step 4:

    pip install -e .

Step 5 - run commmand

command syntax:
    
    python3 main.py --sourceFolder /path/to/sourceFolder/ --replicaFolder /path/to/replicaFolder/ --logPath /path/logFile --interval integer

Example Run command:

    python3 main.py --sourceFolder /home/lukenyr/Documents/Python/VeeamTestTask/ --replicaFolder /home/lukenyr/Documents/Python/VeeamTestTask/replica/ --logPath /home/lukenyr/Documents/Python/VeeamTestTask/log.txt --interval 1

Bonus:

Program includes a help command to reduce learning curve.

Help command:
    
    python3 main.py -h
