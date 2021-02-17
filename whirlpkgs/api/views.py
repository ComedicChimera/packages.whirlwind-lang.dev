from .util import route, validate_int, validate_enum, make_message

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
@route("query", ["GET"], arg_shape={
    "search-string": (None, None),
    "count": (validate_int, None),
    "category": (validate_enum("all", "com", "std"), "all"),
    "ordering": (validate_enum("ranking", "stars", "recent"), "ranking")
})
def query(request, args):
    return make_message(args["search-string"])
