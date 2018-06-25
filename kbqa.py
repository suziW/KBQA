# -*- coding: utf8 -*-

"""
help.doc
"""
import argparse
from SPARQLWrapper import SPARQLWrapper, JSON

parser = argparse.ArgumentParser(description='search related things(movie,music or book) you might wanna know')
parser.add_argument('input', type = str,
                    help = 'input what u wanna search')
parser.add_argument('-s','--specify_search', type = str, choices=['movie', 'music', 'book'],
                    help = 'specify a search type')
args = parser.parse_args()

sparql = SPARQLWrapper("http://dbpedia.org/sparql")
query = """select distinct(?film) ?f_name
            where {
                ?film rdf:type dbo:Film;
                      rdfs:label ?f_name.
                filter regex(?f_name,"love") 
            }
            group by ?film
            limit 10
"""
sparql.setQuery(query)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

output = []
for result in results["results"]["bindings"]:
    print(result["film"]["value"],'#'*3,result['f_name']['value'])



# if args.specify_search == 'movie':
#     print(search_result, args.specify_search)
# elif args.specify_search == 'music':
#     print(search_result, args.specify_search)
# elif args.specify_search == 'book':
#     print(search_result, args.specify_search)
# else:
#     print(search_result, "all")
