import csv


print("\n")

print("""

▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██ ▄▄▀██ ▄▄▄ ██ ███ ████ ▄▄▄ ██ ▄▄▄█ ▄▄▀██ ▄▄▀██ ▄▄▀██ ██ ████ ▄▄▄██ ▀██ ██ ▄▄ █▄ ▄██ ▀██ ██ ▄▄▄
██ █████▄▄▄▀▀███ █ █████▄▄▄▀▀██ ▄▄▄█ ▀▀ ██ ▀▀▄██ █████ ▄▄ ████ ▄▄▄██ █ █ ██ █▀▀██ ███ █ █ ██ ▄▄▄
██ ▀▀▄██ ▀▀▀ ███▄▀▄█████ ▀▀▀ ██ ▀▀▀█ ██ ██ ██ ██ ▀▀▄██ ██ ████ ▀▀▀██ ██▄ ██ ▀▀▄█▀ ▀██ ██▄ ██ ▀▀▀
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀

""")
print("\n\n\n")
try:
    while True:
        path = input("Enter the PATH ")
        # Removing "" from the path
        path = path.replace('"', '')
        spred = open(path, "r")
        reader = csv.reader(spred)
        x = 0
        print("\n\n\n\n\n\n")

        # read the entity name :
        z = int(0)
        for y in reader:
            while True:
                try:
                    for i in range(len(y)):

                        print(y[z], "[", z, "]")
                        z += 1
                except IndexError:
                    break
            break
            # for x in y:

        # -------------------------

        search = int(input(
            "\nType what column you want to search in it\n"))

        keyWord = input("Enter a keyword: \n")
        # Searcher

        x = 0
        for i in reader:
            x += 1

            if i[search].find(keyWord) > -1:
                print("----------- \n \nI found one! \nAnd it's in Line:", x)

except:
    print("")
