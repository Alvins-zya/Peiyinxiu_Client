#coding=utf-8
import re
from Peiyinxiu_Client import API

import string


test = API.Person_senter().gold()[1]
print(test)


if test >180:
    print(1)
else:
    print(2)