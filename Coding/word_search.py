import copy
from pprint import pprint

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        ops = {
            'left':(0, -1),
            'right':(0, 1),
            'up':(-1, 0),
            'down':(1, 0)
        }
  

        def _get_first_idx(word):
            res = []
            for i in range(len(board)):
                if word[0] in board[i]:
                    if board[i].count(word[0]) == 1: 
                        res.append((i, board[i].index(word[0])))
                    else:
                #multiple char in the same row
                        tmp = copy.deepcopy(board[i])
                        tmp_res = []
                        while tmp.count(word[0]):
                            tmp_res.append((i, tmp.index(word[0])+len(tmp_res)))
                            tmp.remove(word[0])
                        res.extend(tmp_res)
            return res

                
        
        def search(word, idx, last_idx = []):
            #last_idx = []
            for i in range(1, len(word)):
                char = word[i]
                print(char)
                print(idx, last_idx)
                res_track = []
                print("before the try, indx value is ", idx)
                for _op in ops:
                    try:
                        print(_op, ops[_op])
                        track_idx = None
                        track_idx = (idx[0] + ops[_op][0],idx[1] + ops[_op][1])
                        move = board[track_idx[0]][track_idx[1]]
                        #print('track:', track_idx)
                        if track_idx:
                            if not track_idx in last_idx and min(track_idx) >= 0 and \
                                not track_idx == idx:
                                print('track:', track_idx, 'idx:', idx)
                                res_track.append((move, track_idx))
                    except:
                        pass

                print("before track:", res_track)                
                if char in [x[0] for x in res_track]:
                    tmp_track_idx = []
                    for char_idx in [x for x in res_track if x[0] == char]:
                        _, char2_idx = char_idx
                        tmp_track_idx.append(idx)
                        idx = char2_idx
                        last_idx = last_idx + tmp_track_idx
                        print("after track:", idx, last_idx)
                        print(word[i:])
                        return search(word[i:], idx, last_idx)
                    
                else:
                    return False

            return True
        
        
        res = []
        for word in words:
            res_idx = _get_first_idx(word)
            print('idx choice:', res_idx)
            if len(res_idx) == 1: 
                if search(word, res_idx[0]) and word not in res:
                    res.append(word)
            else:
                for idx in res_idx:
                    if search(word, idx):
                        if word not in res:
                            res.append(word)

                        
        print('idx choice:', res_idx)
        return res
            
                    
                
                    
            
ans = Solution()
board = [["a","b","c"],["a","e","d"],["a","f","g"]]
words = ['eaabcdgfa']
print(ans.findWords(board, words))

for x in board:
    print(x)