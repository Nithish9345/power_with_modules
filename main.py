class PowerModules:
    def power_mod(self, a, x, p):
        result = 1
        a = a % p
        for i in range(1, x+1):
            result = (result * a) % p
        return result

object = PowerModules()
print(object.power_mod(a= int(input()), x= int(input()), p= int(input())))