# from gettext import find
from setuptools import setup,find_packages
from typing import List


# Declaring variables for setup funtions
PROJECT_NAME = "income-census"
VERSION = "0.0.2"
AUTHOR =  "Mohammed Ismail"
DESCRIPTION = "This is my internship Project "
PACKAGES = ["income_census"]
REQUIREMENT_FILE_NAME = "requirements.txt"



def get_requirements_list()->List[str]:
    """
    Description :  This function going to return list of requirement
    mention in requirement.txt file

    return This function is going to return a list which contain name 
    of libraries mentioned in requirements.txt file
    
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove('-e .\n')
        # print(requirement_file)



setup(
name = PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
# packages=PACKAGES,
packages=find_packages(),
install_requires = get_requirements_list()
)



