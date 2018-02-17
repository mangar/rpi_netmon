
def working():
    print("[ working ] - Request sent")


def error():
    print("[ error ] - Error")
    

def success():
    print("[ success ] - Success")

def success_flashing():
    print("[ success_flashing ] - Almost Success")
    


def error_tech():
    print("[ error_tech ] - Error Tech")



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

