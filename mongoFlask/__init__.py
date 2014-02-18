from flask import Flask
app = Flask(__name__)

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "articles"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

db = MongoEngine(app)

if __name__ == '__main__':
    app.run()