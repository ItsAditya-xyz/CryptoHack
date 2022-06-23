cipher = '''XUMB GOZZCH JCIHYYL MCGCFUL'''
# replace the cipher with your own login cipher!

allChars = f'''ABCDEFGHIJKLMNOPQRSTUVWXYZ'''
shiftLimit = 20
for shift in range(0, shiftLimit):
    cipherShifted = ''
    for char in cipher:
        if char == ' ':
            cipherShifted += ' '
            continue
        charIndex = allChars.find(char)
        charIndex += shift
        if charIndex > len(allChars) - 1:
            charIndex -= len(allChars)
        cipherShifted += allChars[charIndex]
    print(cipherShifted + '\n')

# This will print all the possible solutions. Just choose that whose words makes sense