import MapReduce
import sys


"""
Join query in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    attributes = record.split()
    key = attributes[1]
    tale_name = attributes[0]
    # (key, tale_name, attributes[2:]
    value = (table_name, attributes)
    mr.emit_intermediate(key, value)
    
    

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    order_tuples =[]
    line_tuples =[]
    for v in list_of_values:
        if(v[0] == "order"):
            order_tuples.append(v[1])
        else:
            line_tuples.append(v[1])
    
    for order in order_tuples:
        for line in line_tuples:
            output = list(order) + list(line)
            mr.emit(key, output);
    


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
