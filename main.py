import datetime

# from to leave arrive aviacompany

# flights = [
#     ['vno','kns' '']
#
# specific_Date_time = datetime.datetime(2019,10,15,14,14,14)
#
#
# ]

#
# import datetime
#
# # Skrydžio informacija: išvykimo ir atvykimo vietos, aviakompanija
# skrydziai = [
#     ['VNO',
#      'KNS',
#      datetime.datetime(year=2024, month=10, day=15, hour=14, minute=30, second=0),
#      datetime.datetime(year=2024, month=10, day=15, hour=14, minute=30, second=0)
#     ]
# ]
#
# # Nustatyti konkrečią datą ir laiką: metai, mėnuo, diena, valanda, minutė, sekundė
# konkreci_data_laikas = datetime.datetime(year=2024, month=10, day=15, hour=14, minute=30, second=0)
#
# print(konkreci_data_laikas)
# print(skrydziai[0][3])
#
#
# while True:
#         print('1. sarašas 2. įdėti 3.redaguoti 4.trinti')
#         opt = input()
#         match opt:
#             case 1:
#                 print('sarasas')
#             case 2:
#                 print('įdėti')
#
#             case 3:
#                 print('redaguoti')
#             case 4:
#                 print('trinti')



# 1 versija

# import random
# class UserAccount:
#     def __init__(self, username: str, password: str = None, email: str = None):
#         self.username = username
#         self.password = password or self.generate_random_password(12)
#         self.email = email
#
#     def __str__(self):
#         return f'Username: {self.username}, Password: {self.password}, Email: {self.email}'
#
#     def generate_random_password(length: int) -> str:
#         symbols = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890!#*.,"
#         return ''.join(random.choice(symbols) for _ in range(length))
#
#
# class UserManager:
#     def __init__(self):
#         self.accounts = []
#
#     def create_account(self, username: str, email: str, password: str = None):
#         account = UserAccount(username, password, email)
#         self.accounts.append(account)
#         print(f'Sukurtas vartotojas: {account}')
#
#     def read_accounts(self):
#         if not self.accounts:
#             print("Nėra sukurtų vartotojų.")
#         else:
#             print("\nSukurtų vartotojų sąrašas:")
#             for account in self.accounts:
#                 print(account)
#
#     def update_account(self, username: str, new_password: str = None, new_email: str = None):
#         account = self.find_account(username)
#         if account:
#             if new_password:
#                 account.password = new_password
#             if new_email:
#                 account.email = new_email
#             print(f'Vartotojo "{username}" informacija atnaujinta: {account}')
#         else:
#             print(f'Vartotojas su vardu "{username}" nerastas.')
#
#     def delete_account(self, username: str):
#         account = self.find_account(username)
#         if account:
#             self.accounts.remove(account)
#             print(f'Vartotojas "{username}" ištrintas.')
#         else:
#             print(f'Vartotojas su vardu "{username}" nerastas.')
#
#     def find_account(self, username: str):
#         return next((acc for acc in self.accounts if acc.username == username), None)
#
#
# def main():
#     user_manager = UserManager()
#
#     options = {
#         1: ("Sukurti vartotoją", user_manager.create_account),
#         2: ("Rodyti vartotojus", user_manager.read_accounts),
#         3: ("Atnaujinti vartotoją", lambda: user_manager.update_account(
#             input("Įveskite vartotojo vardą: ").strip(),
#             input("Įveskite naują slaptažodį: ").strip(),
#             input("Įveskite naują el. pašto adresą: ").strip()
#         )),
#         4: ("Ištrinti vartotoją", lambda: user_manager.delete_account(
#             input("Įveskite vartotojo vardą: ").strip()
#         )),
#         5: ("Išeiti", None)
#     }
#
#     while True:
#         print(f'{"-" * 26}')
#         print(f'|Profilio valdymo sistema|')
#         print(f'{"-" * 26}')
#         print("\nPasirinkite veiksmą:")
#         for key, (desc, _) in options.items():
#             print(f"{key} - {desc}")
#
#         try:
#             action = int(input("Įveskite numerį pasirinkimui: "))
#             if action == 5:
#                 print("Programa baigta.")
#                 break
#             if action in options:
#                 if action == 1:
#                     username = input("Įveskite vartotojo vardą: ").strip()
#                     email = input("Įveskite el. pašto adresą: ").strip()
#                     password = input(
#                         "Įveskite slaptažodį (arba paspauskite Enter, kad būtų sukurtas automatiškai): ").strip() or None
#                     user_manager.create_account(username, email, password)
#                 else:
#                     options[action][1]()
#             else:
#                 print("Neteisingas pasirinkimas.")
#         except ValueError:
#             print("Prašome įvesti skaičių.")
#
#
# if __name__ == '__main__':
#     main()

# 2 Versija
# import random
#
# class UserAccount:
#     def __init__(self, username: str, password: str = None, email: str = None):
#         self.username = username
#         self.password = password or self.generate_random_password(12)
#         self.email = email
#
#     def __str__(self):
#         return f'Username: {self.username}, Password: {self.password}, Email: {self.email}'
#
#     def generate_random_password(length: int) -> str:
#         symbols = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890!#*.,"
#         return ''.join(random.choice(symbols) for _ in range(length))
#
# class UserManager:
#     def __init__(self):
#         self.accounts = []
#
#     def create_account(self, username: str, email: str, password: str = None):
#         account = UserAccount(username, password, email)
#         self.accounts.append(account)
#         print(f'Sukurtas vartotojas: {account}')
#
#     def read_accounts(self):
#         if not self.accounts:
#             print("Nėra sukurtų vartotojų.")
#         else:
#             print("\nSukurtų vartotojų sąrašas:")
#             for account in self.accounts:
#                 print(account)
#
#     def update_account(self, username: str, new_password: str = None, new_email: str = None):
#         account = self.find_account(username)
#         if account:
#             if new_password:
#                 account.password = new_password
#             if new_email:
#                 account.email = new_email
#             print(f'Vartotojo "{username}" informacija atnaujinta: {account}')
#         else:
#             print(f'Vartotojas su vardu "{username}" nerastas.')
#
#     def delete_account(self, username: str):
#         account = self.find_account(username)
#         if account:
#             self.accounts.remove(account)
#             print(f'Vartotojas "{username}" ištrintas.')
#         else:
#             print(f'Vartotojas su vardu "{username}" nerastas.')
#
#     def find_account(self, username: str):
#         return next((acc for acc in self.accounts if acc.username == username), None)
#
# def main():
#     user_manager = UserManager()
#
#     while True:
#         print("\n1. Sukurti vartotoją\n2. Rodyti vartotojus\n3. Atnaujinti vartotoją\n4. Ištrinti vartotoją\n5. Išeiti")
#         try:
#             option = int(input("Pasirinkite veiksmą: "))
#             if option == 1:
#                 username = input("Įveskite vartotojo vardą: ").strip()
#                 email = input("Įveskite el. paštą: ").strip()
#                 password = input("Įveskite slaptažodį arba spauskite Enter, kad būtų sukurtas automatiškai: ").strip() or None
#                 user_manager.create_account(username, email, password)
#             elif option == 2:
#                 user_manager.read_accounts()
#             elif option == 3:
#                 username = input("Įveskite vartotojo vardą: ").strip()
#                 new_password = input("Naujas slaptažodis (palikite tuščią, jei nenorite keisti): ").strip() or None
#                 new_email = input("Naujas el. paštas (palikite tuščią, jei nenorite keisti): ").strip() or None
#                 user_manager.update_account(username, new_password, new_email)
#             elif option == 4:
#                 username = input("Įveskite vartotojo vardą: ").strip()
#                 user_manager.delete_account(username)
#             elif option == 5:
#                 print("Programa baigta.")
#                 break
#             else:
#                 print("Neteisingas pasirinkimas. Bandykite dar kartą.")
#         except ValueError:
#             print("Prašome įvesti skaičių.")
#
# if __name__ == '__main__':
#     main()


# Užduotis.  CRUDas objektui kuris turi BENT 3 parametrus, šie turi būti bent dviejų skirtingų duomenų tipų.

#Profilio tvarkyklė

import datetime

vartotoju_profiliai = []

def spausdinti_meniu():
    print('--------------------------------')
    print('1. Peržiūrėti visus profilius')
    print