with open('03.txt') as f:
    lines = f.read()
    # a = lines.split()
    t = list(lines)
    print(t[32768])
    # result = ""
    # for i in range(len(t)):
    #     if i % 2000 == 0:
    #         result += t[i]
    # print(str(len(t))+"_"+result)