from urllib2 import urlopen
import os
import platform

# 
# 
# 
def check_url(_url):
    val = False
    # try: 
    #     request = urlopen(_url)
    #     val = True
    #     print("  OK - " + _url)
    # except:
    #     print("  !! - " + _url)
    
    print ' --> ', ping(_url)
    
    return val;


def ping(host):
    response = os.system("ping -c 1 " + host)
    if response == 0:
        return True
    else:
        return False