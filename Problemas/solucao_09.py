def prescriptionChecker(prescription, stock):
    avalible = True
    stock = list(stock)
    for i in range(len(prescription)):
        if (prescription[i] in stock):
            stock.pop(stock.index(prescription[i]))
        else:
            avalible = False
    return avalible