
import os
import time
os.system("cls")

while True:

    c_dir = 0
    c_file = 0
    f_size = 0
    f_path = 0
    x_path = 0
    #size = 0
    total_bytes = 0
    
    f_path = str(input("Enter a directory path >> "))
    print('\n')
    
    try:
        n = f_path[-2]
        x_path = f_path[-1]
    except:
        pass
    
    if f_path == '':
        print("Blank entries are not allowed since they produce no results."'\n')
        #pass

    elif x_path != '\\':
        print("Not a valid entery, also, make sure to end the path with ''\\''."'\n')
        #pass
    
    elif n == '\\':
        print("More than one ''\\'' is not allowed."'\n')
        #pass
            
    else:
        try:   
            dir_render = os.listdir(f_path)
                          
            print("***********************************************************************"'\n')
                                
            for dir in dir_render:
                                
                x =(dir)
                time.sleep(.12)

                f_ext = x.rfind('.')
                file_or_not = (x[f_ext])

                full_path = (f_path + x)

                f_size = os.path.getsize(full_path)

                if file_or_not != '.':
                    print(f_path + "\u001b[32m" + x + "\u001b[37m","<DIR>", "\u001b[34m", "\u001b[37m"'\n')
                    c_dir +=1
                else:
                    print(f_path + "\u001b[35m" + x + "\u001b[34m",   f_size,"Bytes","\u001b[37m"'\n')
                    c_file +=1
                    total_bytes = total_bytes + f_size
            print("***********************************************************************")
            print("Found [", c_dir,"] directories" + " and [",c_file,"] files." + " Total directory byte size: [", total_bytes,"bytes]"'\n')
        except:
            print("Invalid path, enter a true path before continuing.")
                            
