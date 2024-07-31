# kiit-gpt - > project ppt - > https://drive.google.com/file/d/1BTcM2hFooTTh-ivUO3rev-qFYbJ8OUmQ/view
<img src="https://github.com/Nayankumar4986/kiit-gpt/blob/main/kiit%201.png" width="2800" height="400" alt="Image Description">



Certainly! Let's break down the code you provided step by step.

### Imports and Initial Setup

```python
from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
```

- `Flask`: The main class from the Flask framework to create a web application.
- `render_template`: A Flask function to render HTML templates.
- `jsonify`: A Flask function to return a JSON response.
- `request`: A Flask object that contains all the data sent by the client in an HTTP request.
- `PyMongo`: A Flask extension to simplify working with MongoDB.

### Flask App Configuration

```python
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://nayank092:Nayan%4059464986@cluster0.ujpfx8c.mongodb.net/Kiitgpt"
mongo = PyMongo(app)
```

- `app = Flask(__name__)`: Creates a new Flask web application instance.
- `app.config["MONGO_URI"]`: Sets the MongoDB connection URI to connect to your MongoDB Atlas cluster.
- `mongo = PyMongo(app)`: Initializes the PyMongo instance with your Flask app to enable MongoDB operations.

### Home Route

```python
@app.route('/')
def home():
    chats = mongo.db.chats.find({})
    myChats = [chat for chat in chats]
    return render_template("index.html", myChats=myChats)
```

- `@app.route('/')`: Defines the route for the home page. When the user visits the root URL, this function will be called.
- `chats = mongo.db.chats.find({})`: Retrieves all documents from the `chats` collection in the MongoDB database.
- `myChats = [chat for chat in chats]`: Converts the MongoDB cursor object into a list of chat documents.
- `return render_template("index.html", myChats=myChats)`: Renders the `index.html` template, passing the list of chats (`myChats`) to be displayed on the page.

### API Route

```python
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
```

- `@app.route('/api', methods=["GET", "POST"])`: Defines the route for the API endpoint, supporting both GET and POST methods.
- `if request.method == "POST"`: Checks if the request method is POST.
  - `question = request.json.get("question")`: Retrieves the `question` from the JSON payload of the POST request.
  - `chat = mongo.db.chats.find_one({"question": {"$regex": question, "$options": "i"}})`: Searches for a document in the `chats` collection where the `question` field matches the provided question (case-insensitive).
  - `if chat`: If a matching document is found:
    - `data = {"result": chat['answer']}`: Creates a response JSON with the answer from the database.
  - `else`: If no matching document is found:
    - `data = {"result": f"Answer not found for '{question}'. Adding to the database..."}`: Creates a response JSON indicating the question was not found and is being added.
    - `mongo.db.chats.insert_one({"question": question, "answer": f"Answer from openai for '{question}'"})`: Inserts the new question and a placeholder answer into the database.
  - `return jsonify(data)`: Returns the response JSON to the client.

- `data = {"result": "Thank you so much for the kind words! ...}`: Default response for GET requests.
- `return jsonify(data)`: Returns the default response JSON to the client.

### Running the Flask App

```python
if __name__ == '__main__':
    app.run(debug=True, port=3000)
```

- `if __name__ == '__main__'`: Ensures that the Flask app runs only if this script is executed directly (not imported as a module).
- `app.run(debug=True, port=3000)`: Starts the Flask web server in debug mode on port 3000.

### Summary
- The code sets up a Flask web application with MongoDB integration using PyMongo.
- It has two routes: the home route (`/`) for rendering a webpage with chat data and an API route (`/api`) for handling Q&A functionality.
- The home route fetches all chat records from MongoDB and displays them using a template.
- The API route processes POST requests to find answers to questions in the MongoDB collection or adds new questions if not found.







### Certainly! Let’s break down the JavaScript code step by step:

### `postData` Function

```javascript
async function postData(url = "", data = {}) {
  const response = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });
  return response.json();
}
```

- **Function Purpose**: `postData` is an asynchronous function designed to send a POST request to a specified URL with a given data payload and then return the JSON response.

- **Parameters**:
  - `url`: The endpoint to which the POST request will be sent.
  - `data`: The data to be sent in the request body, which is expected to be an object.

- **Inside the Function**:
  - `await fetch(url, {...})`: Sends a POST request to the specified URL with the following options:
    - `method: "POST"`: Specifies the HTTP method as POST.
    - `headers: {"Content-Type": "application/json"}`: Sets the content type of the request to JSON.
    - `body: JSON.stringify(data)`: Converts the data object into a JSON string for the request body.
  - `return response.json()`: Waits for the response from the server and parses it as JSON.

### `reloadPage` Function

```javascript
function reloadPage() {
    location.reload();
}
```

- **Function Purpose**: `reloadPage` is a function that reloads the current page.

- **Inside the Function**:
  - `location.reload()`: This method reloads the current document, effectively refreshing the page.

### `sendButton` Event Listener

```javascript
sendButton.addEventListener("click", async () => {
  // questionInput used as question in video check before using
  const questionInput = document.getElementById("questionInput").value;
  if (questionInput !== null) {
    questionInput.value = "";
  }
  document.querySelector(".right2").style.display = "block";
  document.querySelector(".right1").style.display = "none";

  const question1 = document.getElementById("question1");
  const question2 = document.getElementById("question2");
  question1.innerHTML = questionInput;
  question2.innerHTML = questionInput;

  let result = await postData("/api", {"question": questionInput});
  solution.innerHTML = result.result;
});
```

- **Event Listener Purpose**: This code sets up an event listener for a button (presumably `sendButton`) that will trigger when the button is clicked. The click event will execute an asynchronous function.

- **Inside the Event Listener**:
  - `const questionInput = document.getElementById("questionInput").value;`: Retrieves the value from the input field with the ID `questionInput`.
  - `if (questionInput !== null) { questionInput.value = ""; }`: If the input value is not null, it clears the input field.
  - `document.querySelector(".right2").style.display = "block";`: Shows an element with the class `right2`.
  - `document.querySelector(".right1").style.display = "none";`: Hides an element with the class `right1`.
  - `const question1 = document.getElementById("question1");`: Gets the element with the ID `question1`.
  - `const question2 = document.getElementById("question2");`: Gets the element with the ID `question2`.
  - `question1.innerHTML = questionInput;`: Sets the inner HTML of the `question1` element to the value of `questionInput`.
  - `question2.innerHTML = questionInput;`: Sets the inner HTML of the `question2` element to the value of `questionInput`.
  - `let result = await postData("/api", {"question": questionInput});`: Sends the question to the `/api` endpoint using the `postData` function and waits for the result.
  - `solution.innerHTML = result.result;`: Sets the inner HTML of the `solution` element to the result obtained from the API response.

### Summary

- The `postData` function sends a POST request with JSON data and returns the server’s response in JSON format.
- The `reloadPage` function reloads the current page.
- The event listener on `sendButton` handles the click event by sending a question to the server, updating the UI to reflect the question, and displaying the response from the server.

This code snippet is likely part of a frontend application where users can input questions, send them to a backend service, and display the answers or responses in the UI.


