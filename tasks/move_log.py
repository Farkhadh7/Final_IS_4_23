import os
import shutil

def move_log_files(source_folder, processed_folder):
    """
    Moves all log files from the source folder to the processed folder.

    Args:
        source_folder (str): Path to the folder containing the log files.
        processed_folder (str): Path to the "Processed" folder where the log files will be moved.
    """
    try:
      
        if not os.path.exists(processed_folder):
            os.makedirs(processed_folder)
            print(f"Created folder: {processed_folder}")

        
        for file_name in os.listdir(source_folder):
            
            if file_name.endswith(".txt"):  
                source_path = os.path.join(source_folder, file_name)
                destination_path = os.path.join(processed_folder, file_name)

          
                shutil.move(source_path, destination_path)
                print(f"Moved: {file_name} -> {processed_folder}")

    except Exception as e:
        print(f"Error while moving files: {e}")



source_folder = "./"  
processed_folder = "./Processed"


move_log_files(source_folder, processed_folder)