from django.http import HttpResponse, HttpResponseBadRequest

route_table = {}
def route(path, methods, **kwargs):
    def decor(fn):
        def wrapper(request):
            if request.method not in methods:
                return HttpResponseBadRequest(f"Endpoint `/api/{path}` only supports methods: {methods}")

            if "arg_shape" in kwargs:
                args, err = validate_req_args(request, kwargs["arg_shape"])

                if err:
                    return make_err_response(err)
                
                return fn(request, args)

            return fn(request)

        route_table[path] = route_table

        return wrapper

    return decor    

# validate_req_args extracts and validates request arguments in accordance with
# a given shape defined a dictionary where the key corresponds to the argument
# name and the value is a tuple whose first element is a validation function and
# whose second argument is a default value.  If this field is none, then the
# request argument is required.  If the validator is None, then no validation is
# performed.
def validate_req_args(request, arg_shape):
    args = {}

    for name, spec in arg_shape:
        if name in request.GET:
            if not spec[0]:
                args[name] = request.GET[name]
            else:
                result, err = spec[0](request.GET[name])
    
                if err:
                    return (None, f"{name} must {err}")
                else:
                    args[name] = result
        elif spec[1]:
            args[name] = spec[1]
        else:
            return (None, f"Missing required request argument: `{name}`")

    return (args, None)

# validate_int is a validation function used to validate and extract integer
# request arguments
def validate_int(a):
    if a.isdigit():
        return (int(a), None)

    return (None, "be an integer")

# validate_enum is a validation function used to validate and extract request
# arguments that belong to a finite set of values
def validate_enum(*possible_values):
    def validator(a):
        if a in possible_values:
            return (a, None)

        return (None, f"be one of {possible_values}")

    return validator

# make_err_response returns an response that is an error
def make_err_response(err):
    return HttpResponse({"status": False, "error": err})

# make_message returns a simple message response
def make_message(message):
    return HttpResponse({"status": True, "message": message})