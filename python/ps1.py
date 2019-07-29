alphabet = "abcdefghijklmnopqrstuvwxyz"
longest = ""
substring = ""

for char in s:
    if char in alphabet or char == substring[-1]:
        substring += char
        for i in range(len(alphabet)+1):
            if not(char in alphabet[i:]):
                alphabet = alphabet[i:]
                break
    else:
        substring = "" + char
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(alphabet)+1):
            if not(char in alphabet[i:]):
                alphabet = alphabet[i:]
                break
    if len(substring) > len(longest):
        longest = substring
print("Longest substring in alphabetical order is: " + longest)
