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

    checks.append(mypi.url.check_url("http://google.com"))
    checks.append(mypi.url.check_url("http://facebook.com"))
    checks.append(mypi.url.check_url("http://rga.com"))
    checks.append(mypi.url.check_url("http://uol.com.br"))

    mypi.led.flash_led(checks)

main()
