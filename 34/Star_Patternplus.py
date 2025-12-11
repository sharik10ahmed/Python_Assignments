for i in range(1,5):
    for j in range(1,13):
        if j>=5-i:
            print("          *",)
        else:
            print("",end='')
    print()