import pip

def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package])  

def main():   
    file1 = open('package.txt', 'r') 
    Lines = file1.readlines() 

    for line in Lines: 
        import_or_install(line)
     
if __name__ == "__main__":
    main()