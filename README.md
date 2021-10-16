# Hog
Minimal example of a Hog Descriptor written in Python 3.
### Installation Instructions
```
python3 setup.py install
```
### Importing the module files:
```
import numpy as np
from hog_example import hogImg
```
### Example usage:
with default paramaters:
```
hog = hogImg(arr=np.random.randint(1, 101, size=(19,19)))
output = hog.do_work()"""
```
You can specify 'ppc' and 'cpc' in the constructor:
```
hog = hogImg(arr=hog_example.np.random.randint(1,101,size=(19,19)), ppc=(3,3), cpc=(5,5))
```
