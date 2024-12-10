x = 5

try:
    if(x < 10):
        raise Exception("low value")
except Exception: 
    print(Exception)
finally:
    print("program completed !")

# if(x < 10):
#     raise Exception("low value")