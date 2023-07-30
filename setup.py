from setuptools import setup
from typing import List

#Declaring variables for setup function
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Braja"
DESCRIPTION = "This is house prediction ML project"
PACKAGES = ["Housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"

def get_requirement_list()->List[str]:
    """
    Description: This finction is going to return list of requirements
    mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readline()

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirement_list()
)
