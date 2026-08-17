"""
Folder Analyzer Tool - Print data
Author: M.Arham Anjum
Started: August 13, 2026
Version: v1.0
"""

from collections import Counter

def print_data(p, scanned):
    """Display the folder summary and file list."""

    print("\nFolder Summary:")
    print("==============")
    
    print(f"\nFolder Name: {p.name}")
    print(f"Number of Files: {len(scanned)}\n")
    
    count = Counter()
    for file in scanned:
        count[file.suffix] += 1
    for key, value in count.items():
        if key == "":
            key = " Without Extension"
        print(f"{key}: {value}")

    input("\nTo view files Press Enter Key✨ \n")

    for index, file in enumerate(scanned, start = 1):
        files = file.name
        print(f"\t{index}. {files}")
        
    print("\n")

