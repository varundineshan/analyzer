from bottle import route, run, template,static_file,error,request
import pandas as pd
import json

@route("/")
def index_page():
	return static_file("index.html", root = "staticfiles/views")



def splitdata(data):
	df = pd.DataFrame(columns=['A', 'B'])
	for i in range(5):
		df.loc[i, 'A'] = i
		df.loc[i, 'B'] = i * 5

	return df
def setreturn(df):
	k = []

	for row_index, row in df.iterrows():
		k.append({"tag":row["A"],"value":row["B"]})
		print(k)
	return k 

@route("/countword",method="POST")
def posted_words():
	if request.method ==  "POST":
		textdata =  json.loads(request.body.read())
		splitreturn = splitdata(textdata["data"])
		finalresponse = setreturn(splitreturn)
		return  json.dumps(finalresponse)


@route('<filename:path>')
def static_content(filename):
	return static_file(filename,root="staticfiles")



@error(404)
def mistake404(code):
    return 'Sorry, this page does not exist!'



run(host='localhost', port=8080,debug=True)