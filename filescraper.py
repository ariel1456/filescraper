import requests                                                                     
from bs4 import BeautifulSoup as bs  
import os                                                                               

wantet_path = input("enter the path you want to save the results in\n>")
def imagedown(url,path, folder):                                        
    try:
        os.chdir(path+f"\{folder}")  
        os.mkdir("images")    
    except:
        pass
    r = requests.get(url)     
    soup = bs(r.text, 'html.parser')                
    images = soup.find_all("img")                 
    for image in images:                 
        try:
            link = image.get('src')     
            img_name = link.split("/")[-1] 
        except:
            pass
        try:
            with open(path+"\{folder}\images\{img_name}",'wb') as f:                
                try:
                    im = requests.get(link)           
                    f.write(im.content)              
                except:
                    pass
        except:
            pass
    print("all images downloaded")  

def pdfdown(url,path,  folder): 
    link_list = []  
    unique = []   
    try:
        os.chdir(path+"\{folder}")    
        os.mkdir("files")  
    except:
        pass
    r = requests.get(url)     
    soup = bs(r.text, "html.parser")       
    for a in soup.find_all("a"):      
        links = a.get("href")     
        if ".pdf" in str(links) or ".txt" in str(links): 
            link_list.append(str(links))     
            for y in link_list:                       
                if y not in unique:                
                    unique.append(y)           
            for z in unique:  
                pdf_name = z.split('/')[-1] 
                try:
                    with open(path+f"\{folder}\files\{pdf_name}",'wb') as f:
                        try:
                            im = requests.get(z)  
                            f.write(im.content) 
                        except:
                            pass
                except:
                    pass
    print("all files downloaded")  

while 1:  
    url = input("enter the url you want to scrape\n>")  
    folder = input("enter a name for a new folder\n>")
    try:
        os.chdir(wanted_path) 
        os.mkdir(folder) 
    except:
        pass
    r = requests.get(url)  
    soup = bs(r.text, "html.parser") 
    for a in soup.find_all('a'): 
        links = a.get('href') 
        if "https" in str(links): 
            print(links)  
        txt_file = folder + " links.txt"  
        with open(wanted_path+f"\{folder}\{txt_file}", 'a') as f: 
            f.write(str(links)+"\n") 
    pdfdown(url,wanted_path, folder) 
    imagedown(url,wanted_path folder) 
    print("a file containing all links including links without https//: created in your folder ") 
    again = input("""you want to scan another url
y= yse
n =no
>""") 
    if again == "y": #if the content of variable again equal "y" do:
        continue 
    elif again == "n": #if the content of the variable again equal "n" do:
        break 
    else: #if the content of again do not equal "y" or "n" do:
        print("error") #print on screen "error"
        break 
