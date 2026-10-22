class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        list_s = list(s)
        list_t = list(t)
        hash_table_s = {}
        hash_table_t = {}

        for i in list_s:
            if i in hash_table_s.keys():
                hash_table_s[i] += 1
            else:
                hash_table_s.update({i:1})

        for i in list_t:
            if i in hash_table_t.keys():
                hash_table_t[i] += 1
            else:
                hash_table_t.update({i:1})

        return hash_table_s == hash_table_t

            