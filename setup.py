# setup.py
from setuptools import setup, find_packages
import os

def get_version():
    with open(os.path.join("mifos_iac", "__init__.py")) as f:
        for line in f:
            if line.startswith("__version__"):
                return line.split("=")[1].strip().replace('"', '').replace("'", "")
            

setup(
    name="mifos-gazelle-iac-cli-prototype",  
    version=get_version(),
    author="Mifos Gazelle IaC Prototype Contributors",
    description="Mifos Gazelle aligned IaC security CLI prototype",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/mifos-gazelle-iac-cli-prototype", 
    packages=find_packages(),
    install_requires=[
        "click",
        "rich",
        "reportlab",
        "requests"
    ],
    entry_points={
        'console_scripts': [
            'mifos-iac=mifos_iac.cli:main',
            'mifos-gazelle-iac=mifos_iac.cli:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)