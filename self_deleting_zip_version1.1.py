import os
import time
import zipfile
import logging

def self_delete():
    """Deletes the current directory and its contents after a delay."""
    try:
        time.sleep(120)  # Delay for 120 seconds (adjust as needed)
        
        script_path = os.path.join(os.getcwd(), os.path.basename(__file__))
        os.remove(script_path)  # Delete the Python script itself

        logging.info(f"Script '{script_path}' deleted successfully.")
        
        os.removedirs(os.getcwd())  # Delete the current directory and its contents
    except Exception as e:
        logging.error(f"Error during self-deletion: {e}")

def trigger_on_extraction():
    """Triggers the self-delete function when the zip file is extracted."""
    try:
        with zipfile.ZipFile(__file__, 'r') as zip_ref:
            zip_ref.extractall()  # Extract the zip file
        
        logging.info("Extraction successful.")
        self_delete()
    except Exception as e:
        logging.error(f"Error during extraction: {e}")

if __name__ == '__main__':
    logging.basicConfig(filename='script_log.txt', level=logging.INFO)
    logging.info("Script started.")

    try:
        trigger_on_extraction()
    except Exception as e:
        logging.error(f"Error during script execution: {e}")
    finally:
        logging.info("Script execution completed.")
