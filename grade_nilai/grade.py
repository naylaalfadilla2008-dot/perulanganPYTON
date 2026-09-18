nilai = int(input("Masukkan nilai: "))

if nilai >= 90 and nilai <= 100:
    grade = "A"
elif nilai >= 80:
    grade = "B"
elif nilai >= 70:
    grade = "C"
elif nilai >= 60:
    grade = "D"
else:
    grade = "E"

print("Grade:", grade)