from Files.find import get_file_content, write_file_content, make_file, update_file, remove_file
from datetime import datetime
import time

def setup_sync(args, source_file_names, replica_file_names):
    for file_name in source_file_names:
        source_file_path = args.sourceFolder + file_name
        replica_file_path = args.replicaFolder + file_name

        if file_name not in replica_file_names:
            log_data = f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - Created {file_name} on replica folder."
            make_file(replica_file_path)
            update_file(args.logPath, log_data)
            time.sleep(1)

        source_content = get_file_content(source_file_path)
        replica_content = get_file_content(replica_file_path)
        if source_content != replica_content:
            log_data = f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - Copied content on {file_name} from source folder to replica folder."
            update_file(args.logPath, log_data)
            write_file_content(replica_file_path, source_content)
            time.sleep(1)


def sync(args, source_file_names, replica_file_names):
    for source_file_name, replica_file_name in zip(source_file_names, replica_file_names):
            source_file_path = args.sourceFolder + source_file_name
            replica_file_path = args.replicaFolder + source_file_name

            if source_file_name not in replica_file_names:
                log_data = f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - Created {source_file_name} on replica folder."
                make_file(replica_file_path)
                update_file(args.logPath, log_data)
                time.sleep(1)

            source_content = get_file_content(source_file_path)
            replica_content = get_file_content(replica_file_path)
            if source_content != replica_content:
                log_data = f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - Copied content on {source_file_name} from source folder to replica folder."
                update_file(args.logPath, log_data)
                write_file_content(replica_file_path, source_content)
                time.sleep(1)
            
            if replica_file_name not in source_file_names:
                log_data = f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} - Removed {replica_file_name} from replica folder."
                replica_file_path = args.replicaFolder + replica_file_name
                remove_file(replica_file_path)
                update_file(args.logPath, log_data)
                time.sleep(1)