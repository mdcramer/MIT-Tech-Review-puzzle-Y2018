# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 09:52:46 2018

@author: mcramer

https://cs.nyu.edu/~gottlieb/tr/

Y2018. How many integers from 1 to 100 can you form using the 
digits 2, 0, 1, and 8 exactly once each, along with the operators 
+, -, * (multiplication), / (division), and ˆ (exponentiation)? We 
desire solutions containing the minimum number of operators; 
among solutions having a given number of operators, those using 
the digits in the order 2, 0, 1, 8 are preferred. Parentheses may 
be used; they do not count as operators. A leading minus sign, 
however, does count as an operator.
"""
import itertools

operators = ["+", "-", "*", "/", "^", ""] # last one is no operator
num_equations = 0
best = {}
for i in range(1, 101): # initialize dict of best equations
    best[i] = ""

#def get_operands(equation):
#    s = re.split('\+|\-|\*|\/|\^|\(|\)', equation) # split at operators
#    while "" in s: # remove all empty strings
#        s.remove("")
#    return s

def num_operators(equation):
    count = 0
    for c in equation:
        if c in operators:
            count += 1
    return count

def store_best(equation, ans):
    global best
    if best[ans] == "":
        best[ans] = equation
    else:
        if num_operators(equation) < num_operators(best[ans]):
            best[ans] = equation
        elif num_operators(equation) == num_operators(best[ans]):
            if len(equation) <= len(best[ans]): # eliminates uncessary parenthesis
                best[ans] = equation

def run_evaulation(equation):
    global num_equations
    ans = 0
    try:
        ans = eval(equation.replace("^", "**"))
    except ZeroDivisionError: # catches divide by zero errors
        pass
    except SyntaxError: # catches errors where number has leading zero
        pass
    except: # catches errors with misplaced parenthesis
        pass
    if (type(ans).__name__ == 'int' and 1 <= ans <= 100):
        num_equations += 1
        num_ops = num_operators(equation)
        print("%s = %d with %d operators" % (equation, ans, num_ops))
        store_best(equation, ans)

def find_solutions(n1, n2, n3, n4):    
    for a in ["", "-"]: # leading minus possible
        for b in operators: # first operator
            for c in operators: # second operator
                for d in operators: # third operator
                    equation = a+n1+b+n2+c+n3+d+n4
                    run_evaulation(equation)
                    
                    # one set of parenthesis with two digits
                    run_evaulation("("+a+n1+b+n2+")"+c+n3+d+n4)
                    run_evaulation(a+"("+n1+b+n2+")"+c+n3+d+n4)
                    run_evaulation(a+n1+b+"("+n2+c+n3+")"+d+n4)
                    run_evaulation(a+n1+b+n2+c+"("+n3+d+n4+")")
                    
                    # one set of parenthesis with three digits
                    run_evaulation("("+a+n1+b+n2+c+n3+")"+d+n4)
                    run_evaulation(a+"("+n1+b+n2+c+n3+")"+d+n4)
                    run_evaulation(a+n1+b+"("+n2+c+n3+d+n4+")")
                    
                    # two sets of parenthesis with two digits each
                    run_evaulation("("+a+n1+b+n2+")"+c+"("+n3+d+n4+")")
                    run_evaulation(a+"("+n1+b+n2+")"+c+"("+n3+d+n4+")")

perm = list(itertools.permutations(["2", "0", "1", "8"]))
perm = list(reversed(perm)) # put 2, 0, 1, 8 at end
for i in perm:
    find_solutions(i[0], i[1], i[2], i[3])
   
#find_solutions("2", "0", "1", "8")
print("There are %d possible equations\n" % num_equations)

for k, v in best.items(): # output best equations for each integer
    if v != "":
        print("%d = %s" % (k, v))