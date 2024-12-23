from flask import Flask, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/mongo-reise-project"
mongo = PyMongo(app)

@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    tasks = list(mongo.db.tasks.find({}, {"_id": 0}))
    return jsonify(tasks)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
