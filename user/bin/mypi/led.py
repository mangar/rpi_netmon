import time
import myos
import os


if os.uname()[1] == "raspberry":
    import RPi.GPIO as GPIO 


def working():
    
    if os.uname()[1] != "raspberry":
        print("[ working ] - Request sent")    
    else:
        print("Running on a RPi")
    

    # osName = os.uname()
    # print 'OS Name: ', osName[4]
    # print 'OS Name: ', osName[1]
    # print 'OS Name: ', osName

    # print 'isRPi? ', mypy.myos.isRPIi()



    


def error():
    print("[ error ] - Error")
    

def success():
    print("[ success ] - Success")

def success_flashing():
    print("[ success_flashing ] - Almost Success")
    


def error_tech():
    print("[ error_tech ] - Error Tech")



def isRPi():
    isR = False
    if os.uname()[1] == "raspberrypi":
        isR = True
    return isR



# 
# 
# 
def flash_led(checks):
    count = len(checks)
    count_fail = 0
    count_ok = 0

    for i in range(len(checks)):
        if checks[i] == True:
            count_ok += 1
        else:
            count_fail += 1

    print("- Count Fail: " + str(count_fail))
    print("- Count OK  : " + str(count_ok))

    # success
    if count_fail == 0:
        success()

    # error or some error
    else:
        
        # almost success
        if count_ok > count_fail:
            success_flashing()

        # error
        elif count_fail >= count_ok:
            error()

