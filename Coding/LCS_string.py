#string


def lcs_string(s1, s2):
    l1, l2 = len(s1), len(s2)
    dp = [['' for _ in range(l2+1)] for _ in range(l1+1)]
    string = ''
    for i in range(1, l1+1):
        for j in range(1, l2+1):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            if s1[i-1] == s2[j-1]:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1]+s1[i-1])
            string = max(string, dp[i][j])
    return string


#print(lcs_string("leetcode", 'delete'))


def lcs_Continue_string(s1, s2):
    l1, l2 = len(s1), len(s2)
    dp = [['' for _ in range(l2+1)] for _ in range(l1+1)]
    string = ''
    for i in range(1, l1):
        for j in range(1, l2):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]+s1[i-1]
        string = max(string, max(dp[i], key=len), key = len)
    return string

q = '海战开始，泰国海军一共损失了三艘什么艇？'
a = ' 海战开始时从东面进入的两艘布干维尔级巡防舰合力击沉了一艘鱼雷 艇，此战法军没有损失，泰国海军一共损失了三艘鱼雷艇及吞武里号浅水重炮艇 ，阿育陀耶大城号后来被拖到日本修复。'

lcs = lcs_Continue_string(q, a)
print(lcs)
print(lcs + a.split(lcs)[1])

