from urllib2 import urlopen

# 
# 
# 
def check_url(_url):
    val = False
    try: 
        request = urlopen(_url)
        val = True
        print("  OK - " + _url)
    except:
        print("  ERROR - " + _url)
    
    return val;