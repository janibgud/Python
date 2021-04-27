
import zipfile
import time
import os
os.system("cls")

wordlist = str(input("Enter the path and file name for the password list >> ")) 
w_list = wordlist.split('\\')[-1]
print("Word list loaded:","\u001b[33m",w_list,"\u001b[37m",'\n')

zip_file = str(input("Enter the path and file name for the file to be cracked >> ")) 
z_file = zip_file.split('\\')[-1]
print("Zip file loaded:","\u001b[34m",z_file,"\u001b[37m",'\n')
zip_file = zipfile.ZipFile(zip_file)
n_words = len(list(open(wordlist, "rb")))

print("Total passwords to test:", n_words,'\n')
print("One moment, loading engine...",'\n')
time.sleep(3)
print("Ready!"'\n')
time.sleep(1)
print("Searching for the password...",'\n')

with open(wordlist, "rb") as wordlist:
    #count = n_words
    jcount = 0
    percent = 0
    
    for words in wordlist:
        
        #count -=1
        jcount +=1
        time.sleep(.0001)
        percent = 100 * jcount / n_words
            
        percent = (round(percent, 3))
        

        print(" COMPLETED:","\u001b[32m",percent,"\u001b[37m", flush=True,end='\r')
            
        #print("       REMAINING TESTS:",count,'/',n_words,flush=True, end='\r')
            
        #print("       WORD CHECKED: ",jcount,flush=True, end='\r')
            

        try:
            
            zip_file.extractall(pwd=words.strip())
            
        except:
            
            continue
        
        else:
            
            print("[+] Password found ->","\u001b[31m",words.decode().strip())
            print("\u001b[37m")
            exit(0)
print("[!] Password not found, try other wordlist.")




    
            
        
   
        
        
     
            
        
     

        
        
