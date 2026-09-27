def infextopre (slef, root):
    operaotr = Stack()
    output = Stack()

    for i in expr[::-1]:
        if i == ")":
            operaotr.push(i)
        elif i == "(":
            while not operaotr.isep and operaotr.peek() != ")":
                output.oush(operatior.pop())
            if  not operaotr.isep and operaotr.peek() == ")":
                operator.pop()
        elif i.alnum():
            output.psuh(i)
        else:
            while ( not operton. ismpety and operaot.peek != ")" and (PRECENDENCE[i] < PrcENDENCE[oeprator] or
                                                                  (PRECEN[i] == PRECEn[operaore] and i != "**"))):
                output.push(opertator.pop())
            oepqtor.psuh(i)

        while orpator.