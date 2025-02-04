'''log_analysis.py - Analyze a network gateway log file using regular expressions.
COMP 593 Scripting Applications - Winter 2025 (Week 5)
Louis Bertrand <louis.bertrand@flemingcollege.ca>

Usage:
    python log_analysis <logfile>
    where <logfile> is the file name or path to the log file.

### STUDENTS: PLEASE ADD THE STANDARD ACADEMIC INTEGRITY STATEMENT.###
# This program is strictly my own work. Any material beyond course learning
# materials that is taken from the Web or other sources is properly cited,
# giving credit to the original author(s).

'''

### Imports
import sys  # Need for sys.argv command line parameters
import os  # Need for path handling

def main():
    log_file = get_log_file_path_from_cmd_line()  # Get the file name (Step 3)
    print(f"Analyzing file:\n  {log_file}")  # Test step 3 (we can comment out later)

# TODO: Step 3
def get_log_file_path_from_cmd_line():
    '''Return the command line parameter giving the file name or path,
    exit with error message if no parameter or if parameter is not a file.
    '''
    if len(sys.argv) > 1:  # there is at least one argument after the program name itself
        # Get the path
        filename = sys.argv[1]
        if os.path.isfile(filename):  # Check if it's a file
            return os.path.abspath(filename)  # Expand to full path in file system
        else:
            print("Name specified on the command line is not a file. Exiting...")
            exit(0)  # Exit status code is only used in Linux/Unix systems, just leave at zero
    else:
        print("No file name specified on the command line. Exiting...")
        exit(0)  # Exit status code is only used in Linux/Unix systems, just leave at zero
    # No return statement here, all paths through the if-else statements
    # end in a return or an exit. The return statement would be "dead code".

# TODO: Steps 4-7
def filter_log_by_regex(log_file, regex, ignore_case=True, print_summary=False, print_records=False):
    """Gets a list of records in a log file that match a specified regex.

    Args:
        log_file (str): Path of the log file
        regex (str): Regex filter
        ignore_case (bool, optional): Enable case insensitive regex matching. Defaults to True.
        print_summary (bool, optional): Enable printing summary of results. Defaults to False.
        print_records (bool, optional): Enable printing all records that match the regex. Defaults to False.

    Returns:
        (list, list): List of records that match regex, List of tuples of captured data
    """
    return

# TODO: Step 8
def tally_port_traffic(log_file):
    return

# TODO: Step 9
def generate_port_traffic_report(log_file, port_number):
    return

# TODO: Step 11
def generate_invalid_user_report(log_file):
    return

# TODO: Step 12
def generate_source_ip_log(log_file, ip_address):
    return

if __name__ == '__main__':
    main()