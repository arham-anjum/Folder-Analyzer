"""
Folder Analyzer Tool
Author: M.Arham Anjum
Started: August 13, 2026
Version: v1.0
"""

from Models.Get_data import get_data
from Models.Scan_data import scan_data
from Models.Print_data import print_data

def main():
    """Run the Folder Analyzer application."""

    print("\n🎉Welcome to Folder Analyzer Tool!\n")
    # Keep the application running until the user chooses to exit.
    while True:
        try:
            p = get_data()
            scanned = scan_data(p)
            print_data(p, scanned)
            while True:
                user = input("Do You Want to Use Again? (Yes or No) : ").lower().strip().replace(" ", "")
                if user == "no":
                    input("\nThanks for Using. See you Soon :)")
                    print("Good Bye!\n")
                    break
                    
                elif user == "yes":
                        break
                else:
                    print("Invalid Input!\n")

            if user == "no":
                break

                
        except Exception as e:
                print(f"Error: {e}\n")

if __name__ == "__main__":
    main()

