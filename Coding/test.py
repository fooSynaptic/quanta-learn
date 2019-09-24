def infer():
    s = "1(2(4()(#))())(3(#)())"
    i = 0
    ans = ''
    while i < len(s):
        if s[i] == '#' and s[i+2:i+4] == '()':
            ans += s[i+1]
            i += 4
        ans += s[i]
        i += 1
    return ans.replace('()','').replace('#','')

print(infer())