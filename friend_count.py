import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: person's name
    # value: pair of friends in order
    personA = record[0]
    personB = record[1]
    if personA < personB:
        str = personA + personB
    else:
        str = personB + personA
    mr.emit_intermediate(personA, str)
    mr.emit_intermediate(personB, str)

def reducer(key, list_of_values):
    # key: person's name
    # value: list of pair of friends
    total = 0
    mr.emit((key, len(list_of_values) - len(set(list_of_values))))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)