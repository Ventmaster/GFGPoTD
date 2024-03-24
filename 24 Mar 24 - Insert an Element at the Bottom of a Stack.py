# 24 March 2024
# Insert an Element at the Bottom of a Stack

class Solution:
    def insertAtBottom(self,st,x):
        # code here
        st.insert(0, x)
        return st
