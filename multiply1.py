import MapReduce
import sys

mr = MapReduce.MapReduce()

"""
RUN STEPS:
python multiply1.py input/matrix.json > matrix1.json
python multiply2.py matrix1.json > multiply.json


First round of matrix multiplication.
Assume A = M_{ij}, B = M_{jk}, we want to compute A * B
Natural join matrix A and B on j
"""

# =============================
# Do not modify above this line

def mapper(record):
    # key: j 
    # value: a tuple (matrix name, i or k depends on matrix name, value)
    matrix = record[0]
    i = record[1]
    j = record[2]
    value = record[3]
    if matrix == "a":
        mr.emit_intermediate(j, (matrix, i, value))
    else:
        mr.emit_intermediate(i, (matrix, j, value))

def reducer(key, list_of_values):
    # key: j
    # list_of_values: list of tuples
    
    A = []
    B = []
    
    for tuple in list_of_values:
        if tuple[0] == "a":
            A.append(tuple)
        else:
            B.append(tuple)
            
    for a in A:
        for b in B:
            mr.emit((key, (a[1], b[1], a[2]*b[2])))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
