import csv

datnes_nosaukums=input("Nolasi un izdrukā otro kolonnu!")

with open(datnes_nosaukums, newline='x', encoding='utf-8') as csvfile:
    csvlasitajs: csv.reader(csvfile)
for rinda in csvlasitajs:
    print(rinda)

except StopIteration:
print("Datne ir tukša.")
except Exception as 
print(f"Notikusi kļūda:")