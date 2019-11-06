#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image
import os

size_512 = (512,512)

for f in os.listdir("."):
    if f.endswith(".jpg"):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)
        
        i.thumbnail(size_512)
        i.save("20Images/{}_512{}".format(fn, fext))
    


# In[ ]:




