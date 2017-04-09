import MapReduce
import sys

mr = MapReduce.MapReduce()

"""
Second round of matrix multiplication.
Assume A = M_{ij}, B = M_{jk}, we want to compute A * B
Input is the result json file multiply1.json from first round of matrix multiplication
"""

# =============================
# Do not modify above this line

def mapper(record):
    # key: (i, j)
    # value: multiplication result of A_ij * B_jk.
    j = record[0]
    i = record[1][0]
    k = record[1][1]
    value = record[1][2]
    mr.emit_intermediate((i, k), value)

def reducer(key, list_of_values):
    # key: (i, j)
    # list_of_values: list of multiplication results of A_ij * B_jk.
    
    mr.emit((key[0], key[1], sum(list_of_values)))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
