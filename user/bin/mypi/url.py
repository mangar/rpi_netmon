import os
import platform

# 
# 
# 
def check_url(_url):
    val = False
    
    val = ping(_url)
    if val:
        print '  OK - ', _url, '\n\n'
    else:
        print '  !! - ', _url, '\n\n'

    return val;



def ping(host):
    response = os.system("ping -c 3 " + host)
    if response == 0:
        return True
    else:
        return False