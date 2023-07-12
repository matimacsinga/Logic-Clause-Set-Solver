import re
# & is AND
# | is OR
# ! is NOT

def resolutionMethod(clause_list):
    for current_clause in clause_list:
        for clause in clause_list:

            if clause == current_clause:
                continue

            else:
                for literal in current_clause:

                    if '!' in literal:
                        searched = literal.replace('!','')

                        if searched in clause:
                            resolvent = []
                            for l in current_clause:
                                if l != literal and l != searched:
                                    resolvent.append(l)
                            for l in clause:
                                if l != literal and l != searched:
                                    resolvent.append(l)
                            resolvent.sort()
                            for lit in resolvent:
                                if len(lit) == 1:
                                    neg = '!' + lit
                                    if neg in resolvent:
                                        resolvent = 0
                                        break
                                else:
                                    neg = lit.replace('!','')
                                    if neg in resolvent:
                                        resolvent = 0
                                        break
                            if resolvent == []:
                                return 'unsatisfiable'
                            if resolvent not in clauses and resolvent != 0:
                                clauses.append(resolvent)
                                resolutionMethod(clauses)
                            
                            
                    else:
                        searched = '!' + literal

                        if searched in clause:

                            resolvent = []
                            for l in current_clause:
                                if l != literal and l != searched:
                                    resolvent.append(l)
                            for l in clause:
                                if l != literal and l != searched:
                                    resolvent.append(l)
                            resolvent.sort()
                            for lit in resolvent:
                                if len(lit) == 1:
                                    neg = '!' + lit
                                    if neg in resolvent:
                                        resolvent = 0
                                        break
                                else:
                                    neg = lit.replace('!','')
                                    if neg in resolvent:
                                        resolvent = 0
                                        break
                            if resolvent == []:
                                return 'unsatisfiable'
                            if resolvent not in clauses and resolvent != 0:
                                clauses.append(resolvent)
                                resolutionMethod(clauses)
    return 'satisfiable'
                            


formula = input()
clauses = []

while formula != "":

    first_and = formula.find('&')

    if first_and == -1:
        if len(formula) <= 2:
            temp_list = []
            temp_list.append(formula)
            temp_list.sort()
            if temp_list not in clauses:
                clauses.append(temp_list)
        else:
            potential = ''
            for i in range(0, len(formula)):
                potential = potential + formula[i]
            closed_paranthesis = potential.find(')')
            temp_list = []    

            for i in range(1, closed_paranthesis):
                if potential[i].isalpha() and ( potential[i+1] == "|" or potential[i+1] == ')' ) and '!'+potential[i] not in temp_list:
                    temp_list.append(potential[i])
                if potential[i] == '!' and potential[i+1].isalpha() and (potential[i]+potential[i+1]) not in temp_list:
                    temp_list.append(potential[i]+potential[i+1])
            if temp_list not in clauses:
                clauses.append(temp_list)
        formula = ""
    
    else:
        potential = ''
        for i in range(0, first_and):
            potential = potential + formula[i]
        
        if len(potential) <= 2:
            temp_list = []
            temp_list.append(potential)
            temp_list.sort()
            if temp_list not in clauses:
                clauses.append(temp_list)

        else:
            closed_paranthesis = potential.find(')')
            temp_list = []    

            for i in range(1, closed_paranthesis):
                if potential[i].isalpha() and ( potential[i+1] == "|" or potential[i+1] == ')' ) and '!'+potential[i] not in temp_list:
                    temp_list.append(potential[i])
                if potential[i] == '!' and potential[i+1].isalpha() and (potential[i]+potential[i+1]) not in temp_list:
                    temp_list.append(potential[i]+potential[i+1])
            if temp_list not in clauses:
                clauses.append(temp_list)

        new_formula = ''
        for i in range(first_and+1, len(formula)):
            new_formula = new_formula + formula[i] 
        formula = new_formula


for clause in clauses:
    if clause == []:
        clauses.remove([])

print(resolutionMethod(clauses))

print(len(clauses))




    
        
