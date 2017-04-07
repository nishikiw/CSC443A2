import json

filename = "inverted_index.json"

if __name__ == '__main__':
    
    dict_mySolution = {}
    dict_solution = {}
    
    my_solution = open("my_solutions/"+filename)
    solution = open("solutions/"+filename)
    
    for line in my_solution:
        record = json.loads(line)
        key = record[0]
        value = set(record[1])
        dict_mySolution[key] = value
    
    wrong = 0
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