# -*- coding: utf8 -*-

"""
help.doc
"""
import argparse
import depida

parser = argparse.ArgumentParser(description='search related things(movie,music or book) you might wanna know')
parser.add_argument('input', type = str,
                    help = 'input what u wanna search')
parser.add_argument('-s','--type', type = str, choices=['movie', 'music', 'book'],
                    help = 'specify a search type, none input will search all three things')
args = parser.parse_args()

search = depida.Search("http://dbpedia.org/sparql")
query1 = """select distinct ?publication ?p_name
            where {
                ?publication rdf:type dbo:%s;
                      rdfs:label ?p_name.
                filter regex(?p_name,"%s") 
            }
            group by ?publication
            limit 10
"""%(args.specify_search, args.input)

results = search.sult(query)
print(results)



# if args.specify_search == 'movie':
#     print(search_result, args.specify_search)
# elif args.specify_search == 'music':
#     print(search_result, args.specify_search)
# elif args.specify_search == 'book':
#     print(search_result, args.specify_search)
# else:
#     print(search_result, "all")
