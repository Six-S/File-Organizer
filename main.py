#File organizer
#Written by: Six-S
import os, time, shutil

start = time.time()
print ('[INFO] File sorting began at: ', time.ctime(int(start)))

#FIXME
#user will be what we use to distinguish directories
#ex: destination/user/Documents/example.txt
user = 'user'

#FIXME
#Let's get our directory
directory = os.fsencode('entryPoint/')

#Our legal file extensions. This dict serves two purposes:
#Determine if The Archive supports y file extension
#Determine where file x should go since it is of y file extension
legal_file_extensions = {
    'py': 'destination/Development',
    'html': 'destination/Development',
    'txt': 'destination/Documents',
    'directory': 'destination/'
}

if __name__ in '__main__':
    #Move through our files one at a time.
    for file in os.listdir(directory):
        filename = os.fsdecode(file)

        #Full directories don't have file extensions.
        try:
            file_extension = filename.split('.')[1]
        except IndexError:
            file_extension = 'directory'

        #If file_extension is legal, move file into specified location
        print ('[INFO] Attempting to sort: {}'.format(filename))
        if file_extension in legal_file_extensions:
            shutil.move(os.fsdecode(directory) + filename, legal_file_extensions[file_extension])
        else: 
            print ('[WARN] Unsupported file type: ', file_extension)
    
    end = time.time()
    print ('[INFO] File sorting completed at: {}'.format(time.ctime(int(end))))
    print ('[INFO] Process took: {}'.format(end - start))
