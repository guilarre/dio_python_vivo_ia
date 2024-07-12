import os, shutil

# os.mkdir('./exemplo')

# file = open("./exemplo.txt", 'w')
# file.write("Teste!!\n\nEu sou uma esponja.")
# file.close()

# file = open("./exemplo.txt", 'r')
# print(file.read())
# file.close()

# os.rename("./exemplo.txt", "esponja.txt")

# remover_me = open("remover-me.txt", 'x').close()
os.remove("./remover-me.txt")

# shutil.move("./esponja.txt", './exemplo')