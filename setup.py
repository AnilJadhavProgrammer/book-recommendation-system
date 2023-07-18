from setuptools import setup, find_packages
  
with open("README.md",'r',encoding="utf-8") as f:
    long_desciption = f.read()

REPO_NAME= "Book recommender system"
AUTHOR_USER_NAME ="Anil Jadhav"
SRC_RRPO ="src"
LIST_OF_REQUIRMENTS= ['numpy','streamlit']


setup(
    name=SRC_RRPO,
    version='3.10.5',
    author='Anil Jadhav',
    long_desciption=long_desciption,
    long_desciption_content_type="text/markdown",
    author_email='aniljadhav8412@gmail.com',
    packages=[SRC_RRPO],
    description='This project help to the which types of book you read. when you read one book he suggeste you next which book you are read.',
    url='https://github.com/AnilJadhavProgrammer/Book_recommender_system',
    install_requires=LIST_OF_REQUIRMENTS,
    
)
