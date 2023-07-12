# ^ for and
# | for or
# > for implies
# = for equivalence 
# ! for negation





def andConn(value1, value2):
    if value1 == 'T' and value2 == 'T':
        return 'T'
    else:
        return 'F'


def orConn(value1, value2):
    if value1 == 'F' and value2 == 'F':
        return 'F'
    else:
        return 'T'


def impliesConn(value1, value2):
    if value1 == 'T' and value2 == 'F':
        return 'F'
    else:
        return 'T'


def equivalenceConn(value1, value2):
    if ( value1 == 'T' and value2 == 'T' ) or ( value1 == 'F' and value2 == 'F'):
        return 'T'
    else:
        return 'F'


def negationConn(value1):
    if value1 == 'T':
        return 'F'
    else:
        return 'T'



def bool_combination(number):
    if not number:
        return [[]]
    result = []
    for combination in bool_combination(number-1):
        result.append(combination + ['T'])
        result.append(combination + ['F'])
    return result


def TablePrint():
    print()

  
    nbatoms = len(atomslist)

    print('  ', end='')


    for a in atomslist:
        print(a, ' |  ', end='')

    
    print('Ans')
    print('--------'*nbatoms)


    to_print = '  '
    k = 0
    
    for i in range(0, nbatoms * (2 ** (nbatoms)), nbatoms):
        k = (i//nbatoms)
        for j in range(0, nbatoms):
            to_print += overalltruthlist[i+j] + '  |  '
        to_print += answerlist[k]
        print(to_print)
        print('--------'*nbatoms)
        to_print = '  '


def checkifValid(listofanswers):
    t_number = 0
    f_number = 0
    for element in listofanswers:
        if element == 'T':
            t_number += 1
        else:
            f_number += 1
    if f_number == 0:
        print("The formula is valid")
    elif t_number != 0:
        print("The formula is satisfiable")
    else:
        print("The formula is not valid nor satisfiable")



connectors = ['^','|','>','=','!']
atomslist = []
truthlist = []
overalltruthlist = []
answerlist = []


proposition = input()


for i in range(0, len(proposition)):
    if proposition[i].isalpha() and proposition[i] not in atomslist:
        atomslist.append(proposition[i])


combination_list = bool_combination(len(atomslist))

ok = 1


for i in range(0, 2**len(atomslist)):


    proposition_copy = proposition
    
    for j in range(0, len(atomslist)):
        truthlist.append(combination_list[i][j])
        overalltruthlist.append(combination_list[i][j])

    
    for j in range(0, len(proposition_copy)):
        if proposition_copy[j].isalpha():
            for l in range(0, len(atomslist)):
                if proposition_copy[j] == atomslist[l]:
                    proposition_copy = proposition_copy.replace(proposition_copy[j], truthlist[l], 1)
                
    
    isValid = True

    while isValid:
        
        open_parenthesis = 0
        closed_parantesis = 0
        is_valid = False

       
        if len(proposition_copy) == 1 and proposition_copy.isalpha():
            print(proposition_copy)
            answerlist.append(proposition_copy)
            break
        
        for index in range(0, len(proposition_copy)):
            if proposition_copy[index] == '(':
                open_parenthesis = index
        
        for index in range(open_parenthesis, len(proposition_copy)):
            if proposition_copy[index] == ')':
                closed_parantesis = index
                break
        
        
        if closed_parantesis - open_parenthesis == 3 and proposition_copy[open_parenthesis+1] == '!' and proposition_copy[open_parenthesis+2].isalpha():
            current_proposition_copy = '(' + proposition_copy[open_parenthesis+1] + proposition_copy[open_parenthesis+2] + ')'
            replacement = negationConn(proposition_copy[open_parenthesis+2])
            print(current_proposition_copy, " is valid and we can replace it with it's truth value under the current interpretation, precisely ", replacement)
            proposition_copy = proposition_copy.replace(current_proposition_copy, replacement, 1)
            print("We are left with: ", proposition_copy)
            is_valid = True

        
        elif closed_parantesis - open_parenthesis == 4 and proposition_copy[open_parenthesis+1].isalpha() and proposition_copy[open_parenthesis+2] in connectors and proposition_copy[open_parenthesis+3].isalpha():
            current_proposition_copy = '(' + proposition_copy[open_parenthesis+1] + proposition_copy[open_parenthesis+2] + proposition_copy[open_parenthesis+3] + ')'
            
            if proposition_copy[open_parenthesis+2] == '^':
                replacement = andConn(proposition_copy[open_parenthesis+1],proposition_copy[open_parenthesis+3])
                print(current_proposition_copy, " is valid and we can replace it with it's truth value under the current interpretation, precisely ", replacement)
                proposition_copy = proposition_copy.replace(current_proposition_copy, replacement, 1)
                print("We are left with: ", proposition_copy)
                is_valid = True
            
            elif proposition_copy[open_parenthesis+2] == '|':
                replacement = orConn(proposition_copy[open_parenthesis+1],proposition_copy[open_parenthesis+3])
                print(current_proposition_copy, " is valid and we can replace it with it's truth value under the current interpretation, precisely ", replacement)
                proposition_copy = proposition_copy.replace(current_proposition_copy, replacement, 1)
                print("We are left with: ", proposition_copy)
                is_valid = True
            
            elif proposition_copy[open_parenthesis+2] == '>':
                replacement = impliesConn(proposition_copy[open_parenthesis+1],proposition_copy[open_parenthesis+3])
                print(current_proposition_copy, " is valid and we can replace it with it's truth value under the current interpretation, precisely ", replacement)
                proposition_copy = proposition_copy.replace(current_proposition_copy, replacement, 1)
                print("We are left with: ", proposition_copy)
                is_valid = True 
            
            elif proposition_copy[open_parenthesis+2] == '=':
                replacement = equivalenceConn(proposition_copy[open_parenthesis+1],proposition_copy[open_parenthesis+3])
                print(current_proposition_copy, " is valid and we can replace it with it's truth value under the current interpretation, precisely ", replacement)
                proposition_copy = proposition_copy.replace(current_proposition_copy, replacement, 1)
                print("We are left with: ", proposition_copy)
                is_valid = True
        
        
        else:
            current_proposition_copy = ''
            for i in range(open_parenthesis, closed_parantesis):
                current_proposition_copy += proposition_copy[i]
            print(current_proposition_copy, ' is invalid, which means the whole proposition is not a wff and we cannot compute the truth value of it ')
            ok = 0
            break

    
    for j in range(0, len(atomslist)):
        del truthlist[-1]

if ok == 1:
    TablePrint()
    checkifValid(answerlist)

'''Superman exercise

“If Superman were able and willing to prevent evil, he would do so. If
Superman were unable to prevent evil, he would be impotent; if he were
unwilling to prevent evil, he would be malevolent. Superman does not
prevent evil. If Superman exists, he is neither impotent nor malevolent.”

If Superman were able and willing to prevent evil, he would do so.
((A^W)>P)

If Superman were unable to prevent evil, he would be impotent
((!A)>I)

if he were unwilling to prevent evil, he would be malevolent
((!W)>M)

Superman does not prevent evil.
(!P)

If Superman exists, he is neither impotent nor malevolent.
(E>(!(I|M)))

If we combine everything, we can write the formula as:
((((((A^W)>P)^((!A)>I))^((!W)>M))^(!P))^(E>(!(I|M))))
'''

