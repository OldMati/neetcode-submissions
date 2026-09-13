class Solution:
    def decodeString(self, s: str) -> str:
        # for each 3[str]:
        # first decode the string inside, then multiply it 3 times and add to current string
        # to decode everything: 
        # iterate over s[i:j+1], if encountered number, find opening (l) and closing (r) brackets, recurse on (l+1) (r-1)
        # then add the returned array s times to current array
        # return current array


        def _decode(i): # decode string from i until closing bracket
            cur = []
            idx = i
            while idx < len(s):
                if s[idx] == ']':
                    idx += 1
                    break

                elif s[idx].isnumeric():
                    end_of_num = idx
                    while s[end_of_num].isnumeric():
                        end_of_num += 1
                    mul=int(s[idx:end_of_num])

                    temp, idx = _decode(end_of_num + 1)

                    for _ in range(mul):
                        cur.extend(temp)

                else:
                    cur.append(s[idx])
                    idx += 1

            return cur, idx
        

        return ''.join(_decode(0)[0])