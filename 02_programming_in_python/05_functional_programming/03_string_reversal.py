def string_reversal(str):
    if len(str) == 0:
        return str
    else:
        return string_reversal(str[1:]) + str[0]


str = "reversal"
print(string_reversal(str))
