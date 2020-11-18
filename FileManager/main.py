import os
import shutil

FOLDER = input('Enter a directory to tide up \n')
TEMPFOLDER = r'C:\temp_folder'

files = os.listdir(FOLDER)

## Web , Python , Movie , Picture , document , music ,  


web = ['.html', '.js', '.css', '.json', '.htm', '.xml', '.php']
python = ['.py']
movie = [ '.mp4', '.webm', '.mkv', '.flv', '.vob', '.ogv', '.ogg']
picture = ['.png', '.jpg', '.gif', '.jpeg', '.tiff', '.ico', ]
document = ['.zip', '.pdf', '.esp', '.ai', '.swf', '.psd', '.txt', '.docx', '.log']
music = ['.mp3', '.m4a']

list = ['Web', 'Python', 'Video', 'Images', 'Document', 'Music', 'Unknown']

for item in list:
    os.mkdir(TEMPFOLDER+'\\'+item)
    
for file in files:
    file = file.lower()
    
    for item in web:
        if file.endswith(item):
            shutil.move(FOLDER+'\\'+file, TEMPFOLDER+'\\'+'Web')
            break
    for item in python:
        if file.endswith(item):
            shutil.move(FOLDER+'\\'+file, TEMPFOLDER+'\\'+'Python')
            break
    for item in movie:
        if file.endswith(item):
            shutil.move(FOLDER+'\\'+file, TEMPFOLDER+'\\'+'Video')
            break
    for item in picture:
        if file.endswith(item):
            shutil.move(FOLDER+'\\'+file, TEMPFOLDER+'\\'+'Images')
            break
    for item in document:
        if file.endswith(item):
            shutil.move(FOLDER+'\\'+file, TEMPFOLDER+'\\'+'Document')
            break
    for item in music:
        if file.endswith(item):
            shutil.move(FOLDER+'\\'+file, TEMPFOLDER+'\\'+'Music')
            break
    
    try:
        shutil.move(FOLDER+'\\'+file, TEMPFOLDER+'\\'+'Unknown')
    except:
        pass
        
    
     
    
for item in list:
    shutil.move(TEMPFOLDER+'\\'+item, FOLDER)