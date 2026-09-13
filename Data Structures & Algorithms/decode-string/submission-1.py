class Solution:
    def decodeString(self, s: str) -> str:
        # for each 3[str]:
        # first decode the string inside, then multiply it 3 times and add to current string
        # to decode everything: 
        # iterate over s[i:j+1], if encountered number, find opening (l) and closing (r) brackets, recurse on (l+1) (r-1)
        # then add the returned array s times to current array
        # return current array


        def _decode(i, j):
            print(f'analysing {s[i:j+1]}')
            cur = []
            idx = i
            while idx <= j:
                if s[idx].isnumeric():
                    print(f'{s[idx]} is numeric')
                    end_of_num = idx
                    while s[end_of_num].isnumeric():
                        end_of_num += 1
                        
                    mul=int(s[idx:end_of_num])
                    print("mul: ", mul)

                    l = end_of_num + 1 # opening bracket
                    opened = 1
                    r = l + 1
                    while opened > 0: # need all brackets to be closed
                        if s[r] == ']':
                            opened -= 1
                        elif s[r] == '[':
                            opened += 1
                        r += 1

                    print(f'decoding {s[l:r]}, {l=} {r=}\n')

                    temp = _decode(l, r - 2)

                    print(f'\ndecoded: {temp}')

                    for _ in range(mul):
                        cur.extend(temp)
                    idx = r
                else:
                    cur.append(s[idx])
                    idx += 1
            print(cur)
            return cur
        

        return ''.join(_decode(0, len(s)-1))


        