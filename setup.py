from setuptools import setup, find_packages
 
VERSION = '0.0.1'
DESCRIPTION = 'A pakage to perform physics operation'
with open("README.txt", "r") as f:
    LONG_DESCRIPTION = f.read()


# Setting up
setup(
    name="physicsNutshell",
    version=VERSION,
    author="Rajib Paul",
    url="https://github.com/rajib3728/physicsNutshell.git",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['physics', 'Physicsnutshell', 'physicsNutshell', 'PHYSICSNUTSHELL', 'physicsnutshell'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
