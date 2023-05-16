text = str(input())
vsum = 0

# a	e	i	o	u

for i in range(0, len(text)):
    if text[i] == "a":
        vsum += 1

    if text[i] == "e":
        vsum += 2

    if text[i] == "i":
        vsum += 3

    if text[i] == "o":
        vsum += 4

    if text[i] == "u":
        vsum += 5

print(vsum)

