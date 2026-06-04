def freq(txt):
    dict={}
    for i in txt:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    return dict