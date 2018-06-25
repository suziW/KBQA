import argparse
parser = argparse.ArgumentParser(description='search related things(movie,music or book) you might wanna know')
parser.add_argument('input', type = str,
                    help = 'input what u wanna search')
parser.add_argument('-s','--specify_search', type = str, choices=['movie', 'music', 'book'],
                    help = 'specify a search type')
args = parser.parse_args()
search_result = args.input
if args.specify_search == 'movie':
    print(search_result, args.specify_search)
elif args.specify_search == 'music':
    print(search_result, args.specify_search)
elif args.specify_search == 'book':
    print(search_result, args.specify_search)
else:
    print(search_result, "all")
