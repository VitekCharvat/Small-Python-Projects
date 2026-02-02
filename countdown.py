import time

def countdown():
    try:
        countTime = int(input("second to countdown:"))
        while countTime != 0:
            print(countTime)
            time.sleep(1)
            countTime -= 1
    except ValueError:
        print("please enter a whole number")
countdown()