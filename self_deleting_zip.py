import os
import time
import zipfile

def self_delete():
    """Deletes the current directory and its contents after a delay of 120 seconds."""
    time.sleep(120)  # Delay for 120 seconds
    os.remove(os.path.join(os.getcwd(), os.path.basename(__file__)))  # Delete the Python script itself
    os.removedirs(os.getcwd())  # Delete the current directory and its contents

def trigger_on_extraction():
    """Triggers the self-delete function when the zip file is extracted."""
    with zipfile.ZipFile(__file__, 'r') as zip_ref:
        zip_ref.extractall()  # Extract the zip file
    self_delete()

if __name__ == '__main__':
    trigger_on_extraction()
