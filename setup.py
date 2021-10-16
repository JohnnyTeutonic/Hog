from setuptools import find_packages, setup

setup(
    name='Hog_example',
    version='0.1',
    packages=find_packages(include=['hog_example.py']),
    url='https://github.com/JohnnyTeutonic/Hog',
    license='MIT',
    author='Jonathan Reich',
    author_email='jonathanreich100@gmail.com',
    description='minimal example of hog descriptor for Python 3.6',
    classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
])
