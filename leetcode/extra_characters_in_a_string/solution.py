from typing import List
import re

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
      sorted_dictionary = list(reversed(sorted(dictionary, key=len)))
      masks = []
      for word in sorted_dictionary:
         mask = re.sub(word, '|' * len(word), s)
         masks.append(mask)

      final_mask = ['x' for i in range(len(s))]
      for mask in masks:
        for i in range(len(mask)):
          if mask[i] == '|':
            final_mask[i] = '|'

      return len(list(filter(lambda c: c != '|', final_mask)))

solver = Solution()
#assert solver.minExtraChar("sayhelloworld", ["hello","world"]) == 3
#assert solver.minExtraChar("leetscode", ["leet","code","leetcode"]) == 1

print(solver.minExtraChar('azvzulhlwxwobowijiyebeaskecvtjqwkmaqnvnaomaqnvf', ["na","i","edd","wobow","kecv","b","n","or","jj","zul","vk","yeb","qnfac","azv","grtjba","yswmjn","xowio","u","xi","pcmatm","maqnv"]))
#assert solver.minExtraChar('azvzulhlwxwobowijiyebeaskecvtjqwkmaqnvnaomaqnvf', ["na","i","edd","wobow","kecv","b","n","or","jj","zul","vk","yeb","qnfac","azv","grtjba","yswmjn","xowio","u","xi","pcmatm","maqnv"]) == 15
assert solver.minExtraChar('aakodubkrlauvfkzje', ["ix","qoqw","ax","ar","v","hxpl","nxcg","thr","kod","pns","cdo","euy","es","rf","bxcx","xe","ua","vws","vumr","zren","bzt","qwxn","ami","rrbk","ak","uan","g","vfk","jxmg","fhb","nqgd","fau","rl","h","r","jxvo","tv","smfp","lmck","od"]) == 9
assert solver.minExtraChar('kevlplxozaizdhxoimmraiakbak', ["yv","bmab","hv","bnsll","mra","jjqf","g","aiyzi","ip","pfctr","flr","ybbcl","biu","ke","lpl","iak","pirua","ilhqd","zdhx","fux","xaw","pdfvt","xf","t","wq","r","cgmud","aokas","xv","jf","cyys","wcaz","rvegf","ysg","xo","uwb","lw","okgk","vbmi","v","mvo","fxyx","ad","e"]) == 9
