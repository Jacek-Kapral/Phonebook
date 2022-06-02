import os
f = open("Phonebook.txt", "w")

class Phonebook:
    def __init__(self):
        self.phonebook = {}
        self.phonebook_file = 'Phonebook.txt'

    def loadAll(self):
        self.phonebook.clear()

        file = open(self.phonebook_file, 'r')
        for line in file.readlines():
            name, number = line.strip().split()
            self.phonebook[name] = number
        file.close()

    def addEntry(self):
        self.loadAll()

        name = input("Wpisz imię: ")
        number = input("Wpisz numer: ")

        new_entry = name + '\t' + number + '\n'

        file = open(self.phonebook_file, 'a')
        file.write(new_entry)
        file.close()

    def readAll(self):
        self.loadAll()

        for name, number in self.phonebook.items():
            print(name, " : ", number)
        if len(self.phonebook) == 0:
            print("Książka telefoniczna nie ma żadnych wpisów")

    def deleteEntry(self):
        self.loadAll()

        entry_to_delete = input("Wpisz imię kontaktu do skasowania: ")
        if entry_to_delete in self.phonebook.keys():
            del self.phonebook[entry_to_delete]
            file = open(self.phonebook_file, 'w')
            for name, number in self.phonebook.items():
                string = name + '\t' + number + '\n'
                file.write(string)
            file.close()
            print("Kontakt skasowany")

        else:
            print("Kontakt nie znaleziony")

    def exitProgram(self):
        os._exit

    def menu(self):
        print("""\
       -Menu Książki Telefonicznej-
1) Wszystkie wpisy
2) Dodaj wpis
3) Skasuj wpis
4) Exit\n""")
        choice = input("Wybierz: ")
        choice_menu = {'1': self.readAll,
                       '2': self.addEntry,
                       '3': self.deleteEntry,
                       '4': self.exitProgram}
        if choice not in choice_menu.keys():
            print("Zły wybór.")
        else:
            choice_menu[choice]()

Book_1 = Phonebook()
Book_1.menu()