import functions_framework
from flask import Request, Response, abort, send_file
from util import generator


@functions_framework.http
def entrypoint(request: Request) -> Response:
    args = request.args
    if len(args) > 0:
        if "type" in args and "data" in args:
            type = args["type"].lower()
            data = args["data"].lower()
            if type == "qrcode" or type == "code128":
                try:
                    return send_file(
                        generator.generate_code(type=args["type"], data=args["data"]), mimetype="image/png"
                    )
                except Exception as err:
                    abort(500)
                    print(err)
            else:
                return f"Code type unsupported, given: {type}", 400
        else:
            return "Insufficient or unsupported arguments", 400
    else:
        return "No arguments given", 400
