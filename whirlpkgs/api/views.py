from django.http import HttpResponse

# packages.whirlwind-lang.dev REST API

# `/query` - API Endpoint
# Search package database based on specific search parameters
# Request Parameters:
#   search-string: string ; `Search term(s)`
#   count: int ; `Max number of results to return`
#   category: string ; options = ["all", "com", "std"], default = "all"
#   ordering: string ; options = ["ranking", "stars", "recent"], default = "ranking"
# Response Shape:
#   status: bool ; `Indicates if request was successful`
#   results: [Package] ; `Array of serialized package models`
def query(request):
    return HttpResponse("API Response 1")
