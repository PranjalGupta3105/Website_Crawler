import os


def create_project_directory(directory):
    if not os.path.exists(directory):
        print("....creating directory.....")
        os.makedirs(directory)
    else:print("The Directory Already Exists")



def create_data_files(project_name,base_url):
    queue=project_name+"/queue.txt"
    crawled=project_name+"/crawled.txt"
    if not os.path.isfile(queue):
        write_file(queue,base_url)
    if not os.path.isfile(crawled):
        write_file(crawled,'')

def write_file(file_path,data):
    f=open(file_path,'w')
    f.write(data)
    f.close()


#Adding the links to the file (appending here)
def append_onto_file(path,data):
    with open(path,'a') as file:
        file.write(data+"\n")
        file.close()

#deleting the content of the file
def delete_all_from_file(path):
    with open(path,'w') as file:
        pass


# converting a file to a set
def file_to_set(file_name):
    results=set()
    with open(file_name,'rt') as readfile:
        for line in readfile:
            results.add(line.replace('\n',''))
    return results

# converting a set to file
def set_to_file(links,file):
    delete_all_from_file(file)
    for link in links:
        append_onto_file(file,link)

