def count_errors(file_name):
    """
    Counts the number of lines containing the word "ERROR" in the specified log file.

    Args:
        file_name (str): The name of the log file.

    Returns:
        int: The count of lines containing "ERROR".
    """
    error_count = 0
    try:
 
        with open(file_name, 'r') as log_file:
            for line in log_file:
      
                if "ERROR" in line:
                    error_count += 1
    except Exception as e:
        print(f"Error reading file {file_name}: {e}")
    return error_count


def count_warnings(file_name):
    """
    Counts the number of lines containing the word "WARNING" in the specified log file.

    Args:
        file_name (str): The name of the log file.

    Returns:
        int: The count of lines containing "WARNING".
    """
    warning_count = 0
    try:

        with open(file_name, 'r') as log_file:
            for line in log_file:
            
                if "WARNING" in line:
                    warning_count += 1
    except Exception as e:
        print(f"Error reading file {file_name}: {e}")
    return warning_count



log1_file = "log1.txt"
log2_file = "log2.txt"


print(f"Number of errors in {log1_file}: {count_errors(log1_file)}")
print(f"Number of errors in {log2_file}: {count_errors(log2_file)}")


print(f"Number of warnings in {log1_file}: {count_warnings(log1_file)}")
print(f"Number of warnings in {log2_file}: {count_warnings(log2_file)}")