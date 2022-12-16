from FileSearcher import FileSearcher
from threading import Thread

class SearchManager:

    def __init__(self):
        pass

    def search(self, file_name, drives):
        print("This is a search method of search manager")

        # search_result = []
        searcher_threads = []
        file_serachers = []
        # print(drives)
        # Iterate through the drives 
        for drive in drives:
            print(drive)
            file_searcher = FileSearcher()
            file_searcher.search_for_file(file_name,drive)
            # search_result.append(file_searcher)
            # Append the results to the search_results list  

            # Creating a thread and starting them with the file searcher object
            search_thread = Thread()
            search_thread.start()

            # 4. Adding the file searcher and thread objects into a collection
            # to later join and get results
            file_serachers.append(file_searcher)
            searcher_threads.append(search_thread)

             # 5. Iterate through all the threads and join the threads
        for searcher_thread in searcher_threads:
            searcher_thread.join()

        # 6. Iterate through the file searchers and get the results
        search_results = []
        for file_searcher in file_serachers:
            search_results.append(file_searcher.file_name)

        print(search_results)
        
        

if __name__=='__main__':

    obj=SearchManager()
    d=obj.search("hcl.txt","c://")
    d1=obj.search("hcl.txt","d://")
    print(d)
    print(d1)



        
       