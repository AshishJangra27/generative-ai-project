import os
import glob

def combine_logs(log_folder_path):
    """
    Combine all log files from a specific log folder into one giant string
    
    Args:
        log_folder_path (str): Full path to the log folder (e.g., "logs/folder_name" or just "folder_name")
    
    Returns:
        str: Combined content of all log files in the folder
    """
    # Handle both full path and folder name only
    if not log_folder_path.startswith("logs/"):
        log_folder_path = os.path.join("logs", log_folder_path)
    
    # Check if the folder exists
    if not os.path.exists(log_folder_path):
        print(f"Error: Log folder '{log_folder_path}' does not exist.")
        return ""
    
    # Find all markdown files in the folder
    markdown_files = glob.glob(os.path.join(log_folder_path, "*.md"))
    
    if not markdown_files:
        print(f"No markdown files found in '{log_folder_path}'")
        return ""
    
    # Sort files by name to maintain consistent order
    markdown_files.sort()
    
    combined_content = ""
    
    for file_path in markdown_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                combined_content += content + "\n\n" + "="*100 + "\n\n"
                
            print(f"Added content from: {os.path.basename(file_path)}")
            
        except Exception as e:
            print(f"Error reading file {file_path}: {str(e)}")
    
    print(f"Successfully combined {len(markdown_files)} files from '{log_folder_path}'")
    return combined_content
