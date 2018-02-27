import os
import platform

# 
# 
# 
def check_url(_url):
    val = False
    
    val = ping(_url)
    if val:
        print '  OK - ', _url
    else:
        print '  !! - ', _url

    return val;



def ping(host):
    response = os.system("ping -c 1 " + host)
    if response == 0:
        return True
    else:
        return False