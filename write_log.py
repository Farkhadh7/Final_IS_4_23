def write_log(file_name, message):
    """
    Appends a message to the specified log file.

    Args:
        file_name (str): The name of the log file.
        message (str): The message to write to the log file.
    """
    try:
      
        with open(file_name, 'a') as log_file:
            log_file.write(message + '\n')
        print(f"Message logged to {file_name}: {message}")
    except Exception as e:
        print(f"Error writing to log file: {e}")


write_log("log1.txt", "INFO: Task started")
write_log("log1.txt", "ERROR: File not found")
write_log("log1.txt", "INFO: Task completed")