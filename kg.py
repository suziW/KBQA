# -*- coding: utf8 -*-

"""
help.doc
"""
import argparse
import dbpidia

parser = argparse.ArgumentParser(description='search related things(Film, Game, Book) you might wanna know')
parser.add_argument('input', type = str,
                    help = 'input what u wanna search')
parser.add_argument('type', type = str, choices=['Film', 'Game', 'Book'],
                    help = 'specify a search type, none input will search all three things')
args = parser.parse_args()

search = dbpidia.Search("http://dbpedia.org/sparql")


query = """select ?publication sample(?p_name)
            where {
                ?publication rdf:type dbo:%s;
                      rdfs:label ?p_name.
                filter regex(?p_name,"%s") 
            }
            group by ?publication
            order by desc(count(?publication))
            limit 10
""" % (args.type, args.input)

result = search.sult(query)
for i in result:
    print(i['publication']['value'], i['callret-1']['value'])
# print(result)