import onepunch

feed = 1
battle = 2
quit = 3
saitama = onepunch.OnePunch("Saitama", "punch")
kami = onepunch.OnePunch("Kamikaze", "sword")
tornado = onepunch.OnePunch("Tornado", "psychic")

def main():
    print("░█████╗░███╗░░██╗███████╗░░░░░░██████╗░██╗░░░██╗███╗░░██╗░█████╗░██╗░░██╗  ███╗░░░███╗░█████╗░███╗░░██╗")
    print("██╔══██╗████╗░██║██╔════╝░░░░░░██╔══██╗██║░░░██║████╗░██║██╔══██╗██║░░██║  ████╗░████║██╔══██╗████╗░██║")
    print("██║░░██║██╔██╗██║█████╗░░█████╗██████╔╝██║░░░██║██╔██╗██║██║░░╚═╝███████║  ██╔████╔██║███████║██╔██╗██║")
    print("██║░░██║██║╚████║██╔══╝░░╚════╝██╔═══╝░██║░░░██║██║╚████║██║░░██╗██╔══██║  ██║╚██╔╝██║██╔══██║██║╚████║")
    print("╚█████╔╝██║░╚███║███████╗░░░░░░██║░░░░░╚██████╔╝██║░╚███║╚█████╔╝██║░░██║  ██║░╚═╝░██║██║░░██║██║░╚███║")
    print("░╚════╝░╚═╝░░╚══╝╚══════╝░░░░░░╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝")
    print("Choose a hero!")
    name = input("Name: ")
    weap = input("Weapon: ")
    hero = onepunch.OnePunch(name, weap)
    menu(hero)

def menu(hero):
    print()
    print("1: Feed hero")
    print("2: Battle heroes")
    print("3: Quit")
    choice = int(input("What would you like to do? Enter number choice: "))
    if choice == 1:
        feedHero(hero)
    elif choice == 2:
        battleHero(hero)
    elif choice == 3:
        print("Bye!")

def feedHero(hero):
    hero.feed()
    menu(hero)

def battleHero(hero):
    print("   ⠀⣠⣶⡾⠏⠉⠙⠳⢦⡀⠀⠀⠀⢠⠞⠉⠙⠲⡀⠀")
    print("⠀⠀⠀⣴⠿⠏⠀⠀⠀⠀⠀⠀⢳⡀⠀⡏⠀⠀⠀⠀⠀⢷")
    print("⠀⠀⢠⣟⣋⡀⢀⣀⣀⡀⠀⣀⡀⣧⠀⢸⠀⠀⠀⠀⠀ ⡇")
    print("⠀⠀⢸⣯⡭⠁⠸⣛⣟⠆⡴⣻⡲⣿⠀⣸⠀⠀OK⠀ ⡇")
    print("⠀⠀⣟⣿⡭⠀⠀⠀⠀⠀⢱⠀⠀⣿⠀⢹⠀⠀⠀⠀⠀ ⡇")
    print("⠀⠀⠙⢿⣯⠄⠀⠀⠀⢀⡀⠀⠀⡿⠀⠀⡇⠀⠀⠀⠀⡼")
    print("⠀⠀⠀⠀⠹⣶⠆⠀⠀⠀⠀⠀⡴⠃⠀⠀⠘⠤⣄⣠⠞⠀")
    print("⠀⠀⠀⠀⠀⢸⣷⡦⢤⡤⢤⣞⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⠀⠀⢀⣤⣴⣿⣏⠁⠀⠀⠸⣏⢯⣷⣖⣦⡀⠀⠀⠀⠀⠀⠀")
    print("⢀⣾⣽⣿⣿⣿⣿⠛⢲⣶⣾⢉⡷⣿⣿⠵⣿⠀⠀⠀⠀⠀⠀")
    print("⣼⣿⠍⠉⣿⡭⠉⠙⢺⣇⣼⡏⠀⠀⠀⣄⢸⠀⠀⠀⠀⠀⠀")
    print("⣿⣿⣧⣀⣿.........⣀⣰⣏⣘⣆⣀⠀⠀")
    print()
    print("Choose another hero to fight!")
    name2 = input("Name: ")
    weap2 = input("Weapon: ")
    print()
    opp = onepunch.OnePunch(name2, weap2)
    hero.battle(opp)
    menu(hero)

main()



