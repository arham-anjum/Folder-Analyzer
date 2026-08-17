"""
Folder Analyzer Tool - Scan data
Author: M.Arham Anjum
Started: August 13, 2026
Version: v1.0
"""

def scan_data(path):
    """Recursively scan a folder and return all files."""
        
    file_list = []
    for items in path.iterdir(): 
        if items.is_file():
            file_list.append(items)
        if items.is_dir():
            nested_files = scan_data(items)
            file_list.extend(nested_files)
    
    return file_list

