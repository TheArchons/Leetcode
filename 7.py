def isNegative(num):
    if num < 0:
        return True
    else:
        return False

def removeLeadingZeros(strNum):
    strLen = len(strNum)
    for i in range(strLen):
        if strNum[strLen-i-1] != '0':
            return strNum[:strLen-i]

def reverse(x):
    if x == 0:
        return 0
    strX = removeLeadingZeros(str(x))
    strLen = len(strX)
    if isNegative(x):
        if strLen > 11:
            return 0
        elif strLen == 11:
            #check if over 32 bit
            maxSize = str(-2**31)
            revStr = strX[::-1]
            if revStr == maxSize:
                return revStr
            for i in range(strLen):
                if i == strLen-1:
                    break
                if int(strX[strLen - i - 1]) < int(maxSize[i+1]):
                    strX = strX[1:]
                    return '-' + strX[::-1]
                elif int(strX[strLen - i - 1]) > int(maxSize[i+1]):
                    return 0
        else:
            strX = strX[1:]
            return '-' + strX[::-1]
    else:
        if strLen > 10:
            return 0
        elif strLen == 10:
            #check if over 32 bit
            maxSize = str(2**31-1)
            revStr = strX[::-1]
            if revStr == maxSize:
                return revStr
            for i in range(strLen):
                if int(strX[strLen - i - 1]) < int(maxSize[i]):
                    #strX = strX[1:]
                    return revStr
                elif int(strX[strLen - i - 1]) > int(maxSize[i]):
                    return 0
            return 0
        else:
            #strX = strX[1:]
            return strX[::-1]
input = int(input())
print(reverse(input))