# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 07:31:26 2020

@author: kgitn
"""

'''
removal of repeated adjacent characters
'''

class Solution(object):
    def removeDuplicates(self, S):
        st=[]     
        i=0       
        while i<len(S):
            if len(st)!=0 and st[-1]==S[i]:
                i=i+1
                st.pop(-1)
                
            else:
                st.append(S[i])
                i=i+1
        return ''.join(i for i in st)
a=Solution()
print(a.removeDuplicates('aabbbccddesckck'))
