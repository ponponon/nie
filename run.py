from nie import nopen
from mark import BASE_DIR


with nopen(BASE_DIR/'') as file:
    content = file.read()
    
with open(BASE_DIR/'001.jpg','rb') as file:
    
    
    content = file.read()


with open(BASE_DIR/'001.txt','r') as file:
    
    
    content = file.read()