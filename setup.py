from setuptools import find_packages, setup

setup(
    name='Hog_example',
    version='0.1',
    packages=find_packages(include=['hog_example.py']),
    py_modules=['hog_example'],
    url='https://github.com/JohnnyTeutonic/Hog',
    license='MIT',
    author='Jonathan Reich',
    author_email='jonathanreich100@gmail.com',
    description='minimal example of a hog descriptor for Python 3.6 and above',
    install_requires=['numpy', 'numba'],
    classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
])
