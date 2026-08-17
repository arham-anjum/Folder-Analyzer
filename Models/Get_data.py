"""
Folder Analyzer Tool - Get data
Author: M.Arham Anjum
Started: August 13, 2026
Version: v1.0
"""

from pathlib import Path

def get_data():
    """Get and validate the folder path from the user."""

    path = Path(input("Enter Path: ").strip())

    if not path.exists():
        print(f"\nFolder not found! \n")
        print("Try Again!\n")
        
    elif path.is_file():
        print("\nIt is a file. I deal with folders only!\n")
    elif path.is_dir():
        return path
    else:
        input("Invalid Input!")
        
    
