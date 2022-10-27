from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/getJson', methods = ['GET'])
def getJson():
    if(request.method == 'GET'):
        data = {
            "slackUsername": "idyValour",

            "backend": True,
            "age":27,
            "bio": "Build and Host serve"
        }

        return jsonify(data)

if __name__=='__main__':
    app.run(debug=True)
