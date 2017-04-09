import json

filename = "multiply.json"

lists = ["join.json", "friend_count.json", "unique_trims.json", "friend_count.json", "multiply.json"]

if __name__ == '__main__':
    
    wrong = 0
    
    my_solution = open("my_solutions/"+filename)
    solution = open("solutions/"+filename)
    
    if filename in lists:
        
        print("Checking1 "+filename)
        
        my_solution_lines = []
        solution_lines = []
        
        for line in my_solution:
            my_solution_lines.append(", ".join(str(x) for x in json.loads(line)))
            
        for line in solution:
            solution_lines.append(", ".join(str(x) for x in json.loads(line)))
        
        if set(my_solution_lines) != set(solution_lines):
            print("redundant: %s" % ", ".join(set(my_solution_lines) - set(solution_lines)))
            print("miss: %s" % ", ".join(set(solution_lines) - set(my_solution_lines)))
            wrong += 1
    
    else:
    
        print("Checking2 "+filename)
        
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
            if key in dict_mySolution and value != dict_mySolution[key]:
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