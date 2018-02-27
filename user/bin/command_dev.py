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

    checks.append(mypi.url.check_url("12312qwdqwefd.com"))
    checks.append(mypi.url.check_url("wdfsd231324.com"))
    checks.append(mypi.url.check_url("twitter.com"))
    checks.append(mypi.url.check_url("uol.com.br"))
    checks.append(mypi.url.check_url("globo.com"))
    
    mypi.led.flash_led(checks)

main()