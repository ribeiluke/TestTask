import os

def get_file_names(path:str):
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        # List all files in the folder
        files = os.listdir(path)

        # Filter out directories, if needed
        files = [f for f in files if os.path.isfile(os.path.join(path, f))]

        return files
    except Exception as e:
        print(e)
        return e

def get_file_content(file_path:str):
    file_content = []
    with open(file_path) as f:
        file_content = f.readlines()
    return file_content

def write_file_content(file_path:str, content:list):
    with open(file_path, 'w') as f:
        f.writelines(content)

def make_file(file_path:str):
    with open(file_path, 'w') as f:
        f.write('')

def update_file(file_path:str, content:str):
    with open(file_path, 'a') as f:
        f.write(content + "\n\n")
    print(content + "\n")

def remove_file(file_path:str):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File {file_path} has been deleted.")

def get_default_log_path():
    # Get the current file's absolute path
    current_file_path = os.path.abspath(__file__)

    # Get the project directory from parent directory (Files) to create default_log.txt file
    parent_directory_path = os.path.dirname(current_file_path)
    project_directory_path = os.path.dirname(parent_directory_path)
    log_file_path = project_directory_path + "/default_log.txt"

    return log_file_path
