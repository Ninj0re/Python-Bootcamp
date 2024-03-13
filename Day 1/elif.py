# Estü harf notu sistemi
# bu kısım harf notunun 0 ile 100 arasında olduğunu gösteriyor
note = -1
while note < 0 or note > 100:
    note = int(input("Ders notu gir: "))

# If, elif ve else birbirine bağlı zincir if statementlar
# Burası ana kod kısımı
if note >= 84:
    print("AA")
elif 77 <= note:
    print("AB")
elif 71 <= note:
    print("BA")
elif 66 <= note:
    print("BB")
elif 61 <= note:
    print("BC")
elif 56 <= note:
    print("CB")
elif 50 <= note:
    print("CC")
elif 46 <= note:
    print("CD")
elif 40 <= note:
    print("DC")
elif 30 <= note:
    print("DD")
else:
    print("FF")
