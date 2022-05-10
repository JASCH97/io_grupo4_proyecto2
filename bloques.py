import sys

def blockTowerBruteForce(BlockList):
    print("Fuerza Bruta")

def blockTowerDynamic(BlockList):
    print("Dinamico")


# save the first argument (second position in argv list) to a variable
arg1 = sys.argv[1]
arg2 = sys.argv[2]

a_file = open(arg2, "r")

list_of_lists = []
for line in a_file:
  stripped_line = line.strip().replace(",","")
  line_list = stripped_line.split()
  list_of_lists.append(line_list)

a_file.close()

print(list_of_lists)

if arg1 == "1":
    blockTowerBruteForce(list_of_lists)
elif arg1 == "2":
    blockTowerDynamic(list_of_lists)
else:
    print("Choose an algorythm")