def intToRoman(num):
    strNum = str(num)
    roman = ""
    for pos, i in enumerate(reversed(strNum)):
        if pos == 0:
            if int(i) < 4:
                roman += (int(i) * 'I')
            elif int(i) == 4:
                roman += 'IV'
            elif int(i) == 5:
                roman += 'V'
            elif int(i) > 5 and int(i) < 9:
                roman += 'V'
                roman += (int(i) - 5) * 'I'
            elif int(i) == 9:
                roman += 'IX'
        elif pos == 1:
            if int(i) < 4:
                roman = (int(i) * 'X') + roman
            elif int(i) == 4:
                roman = 'XL' + roman
            elif int(i) == 5:
                roman = 'L' + roman
            elif int(i) > 5 and int(i) < 9:
                #roman = 'L' + roman
                roman = 'L' + (int(i) - 5) * 'X' + roman
            elif int(i) == 9:
                roman = 'XC' + roman
        elif pos == 2:
            if int(i) < 4:
                roman = (int(i) * 'C') + roman
            elif int(i) == 4:
                roman = 'CD' + roman
            elif int(i) == 5:
                roman = 'D' + roman
            elif int(i) > 5 and int(i) < 9:
                #roman = 'D' + roman
                roman = 'D' + (int(i) - 5) * 'C' + roman
            elif int(i) == 9:
                roman = 'CM' + roman
        elif pos == 3:
            if int(i) < 4:
                roman = (int(i) * 'M') + roman
            elif int(i) == 4:
                roman = 'CD' + roman
            elif int(i) == 5:
                roman = 'D' + roman
            elif int(i) > 5 and int(i) < 9:
                #roman = 'D' + roman
                roman = 'D' + (int(i) - 5) * 'C' + roman
            elif int(i) == 9:
                roman = 'CM' + roman
        elif pos == 4:
            roman = (int(i) * 'M') + roman
    return roman


print(intToRoman(int(input())))