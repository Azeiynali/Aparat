from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    if request.form.get("key"):
        print(request.form.get("key"))
        f = open("log.txt", "a")
        f.write(request.form.get("key"))
        f.close()
        return "1"

    f = open('log.txt', 'r')
    fc = f.read()
    return fc

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)