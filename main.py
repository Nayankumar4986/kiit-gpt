# from flask import Flask, render_template, jsonify, request
# from flask_pymongo import PyMongo

# app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb+srv://nayank092:Nayan%4059464986@cluster0.ujpfx8c.mongodb.net/Kiitgpt"
# mongo = PyMongo(app)


# @app.route('/')
# def home():
#     chats = mongo.db.chats.find({})
#     myChats = [chat for chat in chats]
#     print(myChats)
#     return render_template("index.html", myChats=myChats)


# @app.route('/api', methods=["GET", "POST"])
# def qa():
#     if request.method == "POST":
#         print(request.json)
#         question = request.json.get("question")
#         chat = mongo.db.chats.find_one({"question": question})
#         print(chat)
#         if chat:
#             data = {"result": f"{chat['answer']}"}
#             return jsonify(data)
#         else:
#             data = {"result": f"Answer of {question}"}
#             mongo.db.chats.insert_one(
#                 {"question": question, "answer": f"Answer from openai for {question}"})
#             return jsonify(data)
#         # data={"result": f"Answer of {question}"}
#         # return jsonify(data)
#     data = {"result": "Thank you so much for the kind words! I'm here to assist you with any questions or tasks you have, so please feel free to ask anything you'd like help with. How can I assist you today?"}

#     return jsonify(data)


# app.run(debug=True)

from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://nayank092:Nayan%4059464986@cluster0.ujpfx8c.mongodb.net/Kiitgpt"
mongo = PyMongo(app)


@app.route('/')
def home():
    chats = mongo.db.chats.find({})
    myChats = [chat for chat in chats]
    return render_template("index.html", myChats=myChats)


@app.route('/api', methods=["GET", "POST"])
def qa():
    if request.method == "POST":
        question = request.json.get("question")
        chat = mongo.db.chats.find_one(
            {"question": {"$regex": question, "$options": "i"}})
        if chat:
            data = {"result": chat['answer']}
        else:
            data = {
                "result": f"Answer not found for '{question}'. Adding to the database..."}
            mongo.db.chats.insert_one(
                {"question": question, "answer": f"Answer from openai for '{question}'"})
        return jsonify(data)

    data = {"result": "Thank you so much for the kind words! I'm here to assist you with any questions or tasks you have, so please feel free to ask anything you'd like help with. How can I assist you today?"}
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, port=3000)
