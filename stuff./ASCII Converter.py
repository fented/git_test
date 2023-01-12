import sys
# import this



#choose between encode or decode
chrlist = "99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125"
chrsplit = chrlist.split(", ")

print(chrsplit)






print("For Text to ASCII, type \"1\"")
question = input("For ASCII to text, type \"2\": ")
if question := 1:
    ordlist = input("Paste your text, format: 1, 2, 3")
    ordsplit = ordlist.split(", ")
    ordord = int(ord(ordsplit[0]))
    ordlist.remove(0)
    print(ordord)