# 
# RED   - Error
# GREEN - Success
#       - Flashing: 1 or more problems   
#       - 2 Flashing in a row: requesting data
# 
import mypi.led
import mypi.url

# 
# 
# 
def main():
    checks = []

    mypi.led.working()

    checks.append(mypi.url.check_url("http://googless.com"))
    checks.append(mypi.url.check_url("http://facebooksss.com"))
    checks.append(mypi.url.check_url("http://twitter.com"))
    checks.append(mypi.url.check_url("http://uol.com.br"))
    checks.append(mypi.url.check_url("http://globo.com"))
    
    mypi.led.flash_led(checks)

main()