import psutil, os

class SystemDriveFinder:

    def __init__(self):
        pass


    def find_drives(self):
        # Write the Logic to get all the drives in the system (Active or Inactive)
        print("This is the find drives method of System Drive Finder class")
        
        drives = []
        for x in range(65,91):
            if os.path.exists(chr(x)+ ":"):
                drives.append(chr(x))

        return drives


        # disks = psutil.disk_partitions()
        # drives = []

        # for i in disks:
        #     drives.append(i[0])
        
        # return drives
if __name__=='__main__':
    obj=SystemDriveFinder()
    print(obj.find_drives())


     