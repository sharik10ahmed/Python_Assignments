try:
    ans = 10 / 2
except:
    print("Error happened.")
else:
    print("Success! Answer is", ans)
finally:
    print("This runs no matter what.")