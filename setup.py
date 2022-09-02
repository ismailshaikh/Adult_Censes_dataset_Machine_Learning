from setuptools import setup
from typing import List


def get_requirements_list()->List[str]:
    pass

# Declaring variables for setup funtions
PROJECT_NAME = "income-census"
VERSION = "0.0.1"
AUTHOR =  "Mohammed Ismail"
DESCRIPTION = "This is my internship Project "
PACKAGES = ["housing"]

setup(
name = PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requires = get_requirements_list()
)