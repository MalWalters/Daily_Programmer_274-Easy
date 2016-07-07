# Open declaration and cypher text files.
dec_words = open("declaration_of_independence.txt", encoding="utf-8").read().split()
cypher_index = open("cypher.txt").read().split(',')

for cypher in cypher_index:
    print(dec_words[int(cypher)-1][0],end='')
