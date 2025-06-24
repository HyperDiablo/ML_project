from setuptools import find_packages,setup 
from typing import List
 
def get_Requirements(file_path:str)->List[str]:
    Requirements=[]
   

    with open (file_path) as file_obj:
        Requirements=file_obj.readlines()
        Requirements=[req.replace('/n',"")for req in Requirements]

    return Requirements    





setup(
name ='Mlproject',
version='0.0.1',
author='Atharva',
author_email='atharvatashildar120903@gmail.com',
packages= find_packages(),
install_requires=get_Requirements('Requirements.txt')

)