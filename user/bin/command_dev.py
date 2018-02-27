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

    # Global
    checks.append(mypi.url.check_url("google.com"))
    checks.append(mypi.url.check_url("facebook.com"))
    checks.append(mypi.url.check_url("twitter.com"))
    # BR
    checks.append(mypi.url.check_url("uol.com.br"))
    checks.append(mypi.url.check_url("globo.com"))
    checks.append(mypi.url.check_url("mangar.com.br"))

    checks.append(mypi.url.check_url("esse_dominio_nao_existe_deve_falhar_no_teste.com.br"))
    
    mypi.led.flash_led(checks)

main()