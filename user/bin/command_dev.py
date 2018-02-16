from urllib.request import urlopen
import mypi.led


mypi.led.error()

mypi.led.success()






print ("\n------------------------------\n\n")

print ("\n- test 1")

try: 
    request = urlopen("http://google.com")
    print("  Google OK!")
except:
    print("  Error - Google")



print ("\n- test 2")
try: 
    request = urlopen("http://facebook.com")
    print("  Facebook OK!")
except:
    print("  Error - Facebook")

print ("\n------------------------------\n\n")


# while loop_value == 1:
#     print ("test 2")
#     try: 
#         urlopen("http://google.com")
#     except error.URLError as e:
#         print(e.reason)
#         f.write( "Network currently down." )
#     time.sleep(5)
# else:
#     print( "Up and running." )


# print("Hello World!")

# loop_value = 1
# while (loop_value == 1):
#     try:
#         urlopen("http://google.com")
#     except urllib2.URLError, e:
#         f.write( "Network currently down." )
#     else:
#         print( "Up and running." )
#         #The code to upload a file to my server goes here
#         loop_value = 0

