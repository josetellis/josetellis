from SystemDriveFinder import SystemDriveFinder
from SearchManager import SearchManager

class SearchForm:

    def __init__(self):
        pass

    def show(self):

        # Accept the choice from user to search in all drives or active drives
        print("Do you want to search in 1. All Drives 2. Active Drives")
        choice = int(input())
        
        #-- Locate the drives in the system based on the choice of the user
        drive_finder = SystemDriveFinder()
        
        # Once you get the object then called the method to get the drives
        drives = drive_finder.find_drives()

        #-- Display the drives in the system
        for drive in drives:
            print("Drives in the local system", drive)
        
        print(drives)
        
        #-- Accept the filename to be searched
        print("Enter the file to be searched")
        file_name = input()

        #-- Search for file in the drives
        search_manager = SearchManager()
        search_results = search_manager.search(file_name, drives)

        # Iterate through the results and display the paths found
        for result in search_results:
            # for file_path in result.file_paths:
            #     print(file_path)
            print(result)

if __name__=='__main__':
    obj=SearchForm()
    obj.show()


    