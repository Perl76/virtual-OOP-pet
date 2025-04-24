from pet import Pet

def main():
    pet_name = input("What’s your pet’s name? ")
    my_pet = Pet(pet_name)

    my_pet.get_status()
    my_pet.eat()
    my_pet.play()
    my_pet.sleep()
    my_pet.train("roll over")
    my_pet.train("sit")
    my_pet.get_status()
    my_pet.show_tricks()

if __name__ == "__main__":
    main()
