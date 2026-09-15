# BUG: Added the missing colon, changed < to <=, to include 5, and used an f-string for the finnal output.
count = 1
total = 0

while count <= 5:
    total = total + count
    count = count + 1

    print(f"sum of 1 to 5 is: {total}")