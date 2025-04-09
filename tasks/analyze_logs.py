def analyze_logs(file_name):
    """
    Analyzes the log file and counts the number of errors, warnings, 
    and informational messages.

    Args:
        file_name (str): The name of the log file.

    Returns:
        dict: A dictionary containing counts of "ERROR", "WARNING", and "INFO".
    """
    counts = {"ERROR": 0, "WARNING": 0, "INFO": 0}
    try:
  
        with open(file_name, 'r') as log_file:
            for line in log_file:
          
                if "ERROR" in line:
                    counts["ERROR"] += 1
                elif "WARNING" in line:
                    counts["WARNING"] += 1
                elif "INFO" in line:
                    counts["INFO"] += 1
    except Exception as e:
        print(f"Error reading file {file_name}: {e}")
    return counts


def generate_report(input_file, output_file):
    """
    Generates a report of the log analysis and writes it to a new log file.

    Args:
        input_file (str): The name of the log file to analyze.
        output_file (str): The name of the file to write the report to.
    """
  
    counts = analyze_logs(input_file)
    
    try:
        
        with open(output_file, 'w') as report_file:
            report_file.write("Log Analysis Report\n")
            report_file.write("===================\n")
            report_file.write(f"Number of INFO messages: {counts['INFO']}\n")
            report_file.write(f"Number of WARNING messages: {counts['WARNING']}\n")
            report_file.write(f"Number of ERROR messages: {counts['ERROR']}\n")
        print(f"Report generated: {output_file}")
    except Exception as e:
        print(f"Error writing to file {output_file}: {e}")



log1_file = "log1.txt"
report_file = "log_report.txt"


counts = analyze_logs(log1_file)
print(f"Analysis for {log1_file}:")
print(f"INFO: {counts['INFO']}, WARNING: {counts['WARNING']}, ERROR: {counts['ERROR']}")


generate_report(log1_file, report_file)