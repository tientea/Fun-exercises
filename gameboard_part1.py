def horizontal():
    print(" --- " * size)

def vertical():
    print("|    " * (size + 1))
    
if __name__=="__main__":
    size = int(input("Give me a size for your board:"))
    
    for i in range(size):
        horizontal()
        vertical()
    print(horizontal())