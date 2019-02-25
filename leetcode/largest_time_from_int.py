#py3

class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        #全排列四个int看组成的时间是否合法再和最大的比较。
        def _sec(t):
            assert len(t) == 4, "you got a wrong time format!"
            return (t[0]*10 + t[1])*3600 + (t[2]*10 + t[3])*60
        
        
        
        f_hour = [0, 1, 2]
        s_hour = [x for x in range(10)]
        
        f_min = s_hour
        s_min = s_hour
        
        max_time = _sec([2, 3, 5, 9])
        min_time = 0
        
        candidate_f_hour = [x for x in A if x in f_hour]
        candidate_oth_3 = [x for x in A if x in s_hour]
     
        res = [0,0,0,0]
        
        for f_h in range(4):
            useset = []
            useset.append(f_h)
            print('1', useset)
            for s_h in [x for x in range(4) if x != f_h]:
                useset.append(s_h)
                print('2',useset)
                for f_min in [x for x in range(4) if x not in [f_h, s_h,6]]:
                    useset.append(f_min)
                    print('3',useset)
                    for s_min in [x for x in range(4) if x not in [f_h, s_h, f_min]]:
                        print('4',useset)
                        tmp = [f_h, s_h, f_min, s_min]
                        tmp = [A[x] for x in tmp]
                        print('tmp:', tmp)
                        if min_time < _sec(tmp) < max_time:
                            res = tmp
                            min_time = _sec(tmp)
                        else:
                            res = ''
        
        if not res:
            return res

        res = [str(x) for x in res]
                            
        return res[0] + res[1] + ':' + res[2] + res[3]

ans = Solution()
res = ans.largestTimeFromDigits([1,9,6,0])
print(res)