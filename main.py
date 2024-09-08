import argparse
from Files.find import get_file_names, check_log_path
from Files.syncronization import setup_sync, sync
from datetime import datetime
import time

def run():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="Process some file paths.")

    # Add an argument with a name
    parser.add_argument('--sourceFolder', type=str, help='Path to the source folder')
    parser.add_argument('--replicaFolder', type=str, help='Path to the replica folder')
    parser.add_argument('--interval', type=int, help='interval in minutes used to syncronize both folders')
    parser.add_argument('--logPath', type=str, help='Path to the log file')

    # Parse the arguments
    args = parser.parse_args()
    if not args.sourceFolder:
        log_data = f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - Missing path to source folder. Please submit one using --sourceFolder parameter."
        check_log_path(args=args, log_data=log_data)
        return None
    
    if not args.replicaFolder:
        log_data = f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - Missing path to replica folder. Please submit one using --replicaFolder parameter."
        check_log_path(args=args, log_data=log_data)
        return None
    
    if not args.interval:
        log_data = f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - Missing interval parameter. Will use 60 minutes as default."
        args.interval = 60
        check_log_path(args=args, log_data=log_data)

    while True:
        source_file_names = get_file_names(args.sourceFolder)
        replica_file_names = get_file_names(args.replicaFolder)
        if isinstance(source_file_names, Exception) or isinstance(replica_file_names, Exception):
            break

        if len(replica_file_names) == 0:
            setup_sync(args=args, source_file_names=source_file_names, replica_file_names=replica_file_names)
        else:
            sync(args=args, source_file_names=source_file_names, replica_file_names=replica_file_names)
        time.sleep(args.interval * 60)
    
if __name__ == "__main__":
    run()