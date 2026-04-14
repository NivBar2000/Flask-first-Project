from flask import Flask,jsonify,request
import uuid

app = Flask(__name__)

tasks= [
{
    "id" : str(uuid.uuid4()),
    "title":"learn flask",
    "completed": False
},

{
    "id" : str(uuid.uuid4()),
    "title":"build API",
    "completed": False
},

{
    "id" : str(uuid.uuid4()),
    "title":"Test with postman",
    "completed": True
}
]

str(uuid.uuid4())
task_id_counter = 4 

@app.route("/")
def home():
    return jsonify({
        "message" : "Welcome to my API"
    })
    
    
@app.route("/tasks", methods =["GET"])
def get_tasks():
    return jsonify(tasks)
       
@app.route("/tasks/<task_id>")
def get_task_by_id(task_id):
    # task_id = int(task_id)
    
    for task in tasks:
        if task["id"] == task_id:
            return jsonify(task)
    return jsonify({
        "message" : "Not found"
            }),404
       

@app.route("/tasks", methods= ["POST"])
def echo():
    global task_id_counter
    body = request.json
    
    if not bool(body) :
        return jsonify({
            "success" : False,
            "error" : "json body required"
        }), 400
    
    new_task = {
        "completed" : False,
        "id" : str(uuid.uuid4()),
        "title" : body["title"]
    }
    
    task_id_counter += 1 
    tasks.append(new_task)
    return jsonify(new_task),201

@app.route("/tasks/<task_id>", methods= ["PUT"])
def update(task_id):
    # task_id = int(task_id)
    body = request.json
    
    if not bool(body) :
        return jsonify({
            "success" : False,
            "error" : "json body required"
        }), 400
        
    for task in tasks:
        if task["id"] == task_id:
            if "title" in body:
                task["title"] = body["title"]
            if "completed" in body:
                task["completed"] = body["completed"]
            
            return jsonify(task)

    return jsonify({
        "message" : "task Not found"
            }),404
    
@app.route("/tasks/<task_id>", methods= ["DELETE"])
def delete(task_id):
    # task_id = int(task_id)
    
    for task in tasks:
        if task["id"] == task_id:
           tasks.remove(task)
           return jsonify(tasks)

    return jsonify({
        "message" : "task Not found"
            }),404
    
    
        
    
    
if __name__  == "__main__":
    app.run(debug=True)