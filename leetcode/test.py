
def main(ans1, ans2):
    if len(ans1) > 15 and len(ans2) > 15:
        return (ans1 if len(ans1) > len(ans2) else ans2)
    elif not len(ans1) > 15 and not len(ans2) > 15:
        return "default ans"
    else:
        return max(ans1, ans2)


res = main(''.join(['_' for _ in range(5)]), ''.join(['_' for _ in range(100)]))
print(res)