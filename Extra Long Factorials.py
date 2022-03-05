def mult_dec(A, B):
    mult = []

    for i in range(len(B) - 1, -1, -1):
        multBin = ""
        leftOver = 0
        for ii in range(len(A) - 1, -1, -1):
            B_A = int(B[i]) * int(A[ii]) + leftOver
            leftOver = int(B_A / 10)
            multBin = str(B_A % 10) + multBin
            if ii == 0:
                multBin = str(leftOver) + multBin

        mult.append(multBin)

    for i in range(1, len(mult)):
        for ii in range(i):
            mult[i] += "0"

    for i in range(len(mult)):
        while len(mult[i]) != len(mult[-1]):
            mult[i] = "0" + mult[i]

    out = ""
    leftOver = 0

    for i in range(len(mult[0]) - 1, -1, -1):
        sum = 0 + leftOver
        for ii in range(len(mult)):
            sum += int(mult[ii][i])
        leftOver = int(sum / 10)
        rowOut = str(sum % 10)
        out = rowOut + out
        if i == 0:
            out = str(leftOver) + out

    out = out.lstrip("0")
    return out


def find_factor(n):
    X = str(n)
    for i in range(n, 1, -1):
        X = mult_dec(X, str(i - 1))
    return X


print(find_factor(100))
