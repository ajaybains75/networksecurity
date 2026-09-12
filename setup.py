from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    """
    This function will return the list of requirements
    """
    try:
        with open("requirements.txt", "r") as file:
            #read lines from the file
            lines=file.readlines()
            requirement_list:List[str]=[]
            ## process the lines to remove empty lines and comments
            for line in lines:
                requirements=line.strip()
                ##ignore empty lines and comments and -e
                if requirements and not requirements.startswith("#") and not requirements.startswith("-e"):
                    requirement_list.append(requirements)
    except FileNotFoundError:
        print("requirements.txt file not found. Please make sure it exists in the project directory.")

    return requirement_list

setup(
    name="Network Security",
    version="0.1.0",
    author="Ajay Bains",
    author_email="ajay.bains@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements() 
)
