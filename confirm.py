import json

filename = "join.json"

lists = ["join.json"]

if __name__ == '__main__':
    
    wrong = 0
    
    my_solution = open("my_solutions/"+filename)
    solution = open("solutions/"+filename)
    
    if filename in lists:
        
        print(filename + " generates lists")
        
        my_solution_lines = []
        solution_lines = []
        
        for line in my_solution:
            record = set(json.loads(line))
            my_solution_lines.append(record)
            
        for line in solution:
            record = set(json.loads(line))
            solution_lines.append(record)
        
        for mine in my_solution_lines:
            if mine not in solution_lines:
                print("redundant: %s" % ", ".join(mine))
                wrong += 1
                
        for real in solution_lines:
            if real not in my_solution_lines:
                print("miss: %s" % ", ".join(real))
                wrong += 1
    
    else:
    
        dict_mySolution = {}
        dict_solution = {}
        
        for line in my_solution:
            record = json.loads(line)
            key = record[0]
            value = set(record[1])
            dict_mySolution[key] = value
        
        for line in solution:
            record = json.loads(line)
            key = record[0]
            value = set(record[1])
            if key not in dict_mySolution or value != dict_mySolution[key]:
                print("mine: (%s, [%s])" % (key, ",".join(value)))
                print("true: (%s, [%s])" % (key, ",".join(dict[key])))
                wrong += 1
            dict_solution[key] = value
            
        if set(dict_mySolution.keys()) != set(dict_solution.keys()):
            print("miss in my solution:")
            print(set(dict_solution.keys()) - set(dict_mySolution.keys()))
            print("redundant in my solution:")
            print(set(dict_mySolution.keys()) - set(dict_mySolution.keys()))
            wrong += 1
    
    if wrong == 0:
        print("ALL CORRECT!")
    
    my_solution.close()
    solution.close()