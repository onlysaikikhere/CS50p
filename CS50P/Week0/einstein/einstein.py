mass=int(input("enter mass"))
if mass >= 0 :
    def energy(mass):
        return mass*90000000000000000
    print (energy(mass))
else:
    print("mass cannot be negative")
    exit()

