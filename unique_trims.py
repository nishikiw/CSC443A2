import MapReduce
import sys

"""
DNA sequence in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: DNA nucleotides
        
    key = record[1]
    # remove last 10 characters from nucleotides
    key = key[:-10]
    mr.emit_intermediate(key, 1)

def reducer(key, list_of_values):
    # key: DNA nucleotides
    # value: list of occurrence counts
  
    mr.emit((key))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)


