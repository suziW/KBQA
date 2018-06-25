"""
ge result from dbpidia use sparql query

"""

from SPARQLWrapper import SPARQLWrapper, JSON


class Search():
    def __init__(self, URL):
        self.sparql = SPARQLWrapper(URL)

    def sult(self, query):
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        return [result for result in results["results"]["bindings"]]
        # return results