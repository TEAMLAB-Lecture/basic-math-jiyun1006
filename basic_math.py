#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#######################
# Basic Math          #
#######################

"""
여기서 간단한 수학을 하는 프로그램을 만들것입니다. 
"""


def get_greatest(number_list):
    greatest_number = max(number_list)
    return greatest_number


def get_smallest(number_list):
    smallest_number = min(number_list)
    return smallest_number


def get_mean(number_list):
    mean = sum(number_list) / len(number_list)
    return mean


def get_median(number_list):
    number_list.sort()

    if len(number_list)%2 == 0:
        temp = len(number_list)//2
        ans = (number_list[temp] + number_list[temp-1])/2

    else:
        temp = len(number_list)//2
        ans = number_list[temp]
    return ans


# In[17]:


a=[39, 54, 32, 11, 99, 5]

a.sort()

if len(a)%2 == 0:
    temp = len(a)//2
    ans = (a[temp] + a[temp-1])/2
    
else:
    temp = len(a)//2
    ans = a[temp]
    
print(ans)

