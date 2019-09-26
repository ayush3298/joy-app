from flask import Flask, render_template, request, redirect, url_for, Response, make_response
from database import database
import pyduktape
import uuid

app = Flask(__name__)
db = database()


@app.route('/')
def index():
    res = make_response(render_template('index.html'))
    res.set_cookie('key', str(uuid.uuid4()))
    return res


@app.route("/data", methods=["GET", "POST"])
def get_data():
    if request.method == "POST":
        r = request
        try:
            context = pyduktape.DuktapeContext()
            data = request.form.get('data')
            context.eval_js_file("js/crypto.js")
            context.set_globals(data=data)
            context.set_globals(key=str(request.cookies.get('key')))
            decrypter = '''function mytest(encrypted_data){var bytes = CryptoJS.AES.decrypt(encrypted_data, key);
                                                    var plaintext = bytes.toString(CryptoJS.enc.Utf8);return plaintext}'''
            context.eval_js(decrypter)
            decrypted_data = context.eval_js('(mytest(data));')
            data = {data.split('=')[0]: data.split('=')[1] for data in decrypted_data.split('&')}
            if db.insert_data(data['name'], data['color'], data['dog_or_cat']):
                return render_template('index.html')
            return Response(str('Already Exists'), status=500)

        except Exception as e:
            print(e)
            return Response(str(e), status=500)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
