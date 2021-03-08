from pythonds.basic import Stack

def infixToPostfixEval(infixExpre):
    prec = {}
    prec["!"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixExpre.split()

    #infix to postfix
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    postfixExpre = (" ".join(postfixList))

    #postfix to eval
    operandStack = Stack()
    tokenList = postfixExpre.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        #seperate statements for factorial
        elif token == "!":
            operand1 = operandStack.pop()
            result = doFactorial(operand1)
            operandStack.push(result)
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    
    return postfixExpre, operandStack.pop()

#performs calculations for */+-
def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

#performs calculations for factorials
def doFactorial(op1):
    total =1
    for i in range(1, int(op1)+1):
        total = total * i
    return total
