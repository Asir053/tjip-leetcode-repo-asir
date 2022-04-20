#O(t*log(s)),O(t)
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_dict={}
        for i in t:
            if i in t_dict:
                t_dict[i]+=1
            else:
                t_dict[i]=1
        i=0
        j=0
        count=len(t)
        ans=""
        val=float("inf")
        while j<len(s):
            if count==0:
                if val>j-i+1:
                    val=j-i+1
                    ans=s[i:j+1]
                if s[i] in t_dict:
                    t_dict[s[i]]+=1
                    if t_dict[s[i]]>0:
                        count+=1
                i+=1
                while i<len(s) and s[i] not in t_dict:
                    i+=1
            else:
                if s[j] in t_dict:
                    t_dict[s[j]]-=1
                    if t_dict[s[j]]>=0:
                        count-=1
            if count!=0:
                j+=1
        return ans
        
