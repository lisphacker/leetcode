class Solution:
    def gen_numbers(self, n, i, digits, number, output):
        if i == n:
            output.append(number.copy())
            return
        
        for d in digits:
            number.append(d)
            self.gen_numbers(n, i + 1, digits, number, output)
            number.pop()
            
    def findStrobogrammatic(self, n: int) -> List[str]:
        houtput = []
        
        inv = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }
        
        self.gen_numbers((n + 1) // 2, 0, '01689', [], houtput)
        
        s = (n // 2) - 1
        l = n // 2
        
        for h in houtput:
            for i in range(l):
                h.append(inv[h[s - i]])
            
        if n != 1:
            houtput = list(filter(lambda s: s[0] != '0', houtput))
            
        s = n // 2
        if n % 2 == 1:
            houtput = list(filter(lambda ss: ss[s] not in '69', houtput))
        
        for i in range(len(houtput)):
            houtput[i] = ''.join(houtput[i])
        
        return houtput