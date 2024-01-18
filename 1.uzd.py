import csv

datnes_nosaukums=input("Nolasi un izdrukā!")

with open(datnes_nosaukums, newline='x', encoding='utf-8') as csvfile:
    csvlasitajs: csv.reader(csvfile)
for rinda in csvlasitajs:
    print(rinda)

except StopIteration:
print("Datne ir tukša.")
except Exception   
print(f"Notikusi kļūda:")