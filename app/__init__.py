from sanic import Sanic, response

app = Sanic()

@app.route("/headers")
async def index(request):
	return response.json(request.headers)

@app.route("/json", methods=['POST'])
async def post_json(request):
    return response.json({"received": True, "message": request.json})

@app.route("/query_string")
async def query_string(request):
    return response.json({"parsed": True, "args": request.args, "url": request.url, "query_string": request.query_string})

@app.route("/file")
async def post_json(request):
    test_file = request.files.get('file')

    file_parameters = {
        'body': test_file.body,
        'name': test_file.name,
        'type': test_file.type,
    }
    return response.json({ "received": True, "file_names": request.files.keys(), "test_file_parameters": file_parameters })

if __name__ == '__main__':
	app.run()
