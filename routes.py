from flask import jsonify,request,Blueprint
from werkzeug.exceptions import NotFound, BadRequest, Conflict, UnprocessableEntity
# from models import get_all_tasks, get_task_by_id,update_task,delete_task, tasks
from db import db
from bson import ObjectId

tasks_bp = Blueprint("tasks", __name__)



#========== first page =============
@tasks_bp.route("/")
def home():
    return jsonify({
        "message" : "Welcome to my API"
    })

#============ show all tasks ===========
@tasks_bp.route("/tasks", methods =["GET"])
def get_tasks():
    collection_tasks = db["tasks"]
    tasks = list(collection_tasks.find())
    
    for task in tasks:
        task["_id"] = str(task["_id"])
    return jsonify(tasks)

#============ finde task by ID =============
       
@tasks_bp.route("/tasks/<task_id>")         
def get_task_from_id(task_id):
    if ObjectId.is_valid(task_id) == False:
        raise BadRequest("ID must be vaild ObjectId ")
    
    collection_tasks = db["tasks"]
    tasks = list(collection_tasks.find())
    for task in tasks:
        task["_id"] = str(task["_id"])
        
    for task in tasks:
        if task["_id"] == task_id:
            return task
    raise NotFound(f"Task with id -{task_id}- not found")
 
       
       
#==============Create Task=====================       

@tasks_bp.route("/tasks", methods= ["POST"])    
def create_task_route():
    body = request.get_json(silent=True)
    if body is None:
        raise BadRequest("Missing JSON body")
    if body is None:
        raise BadRequest("Missing JSON body")
    
    if body == {}:
        raise BadRequest("Request body must be full JSON")
    
    title = body["title"]                
    if not isinstance(title, str): 
        raise BadRequest("Title must be a string")
    
    if not title.strip():
        raise UnprocessableEntity("Title cannot be empty")
    
    if "title" not in body:
        raise BadRequest("title is required")
    
    new_task = {
        "title": title.strip(),
        "completed": False
    }
    
    db.tasks.insert_one(new_task)
    
    new_task["_id"] = str(new_task["_id"])
    return jsonify({
        "success": True,
        "data": new_task
    }), 201
    # return jsonify(new_task),201


#===============Update Task by ID=====================

@tasks_bp.route("/tasks/<task_id>", methods= ["PUT"])    
def update(task_id):
    body = request.get_json(silent=True)
    
    if ObjectId.is_valid(task_id) == False:
        raise BadRequest("ID must be vaild ObjectId ")
     
    is_exist = db.tasks.find_one(
            {"_id": ObjectId(task_id)}
        )
    if is_exist == None:
        raise NotFound(f"Task with id -{task_id}- not found")

    if body is None:
        raise BadRequest("Missing JSON body")
   
    title = body.get("title")
    if title:
        if not isinstance(title, str):
            raise BadRequest("Title must be a string")
    
    completed = body.get("completed")
    if completed:
        if not isinstance(completed, bool):
            raise BadRequest("completed must be bool.")
                  
    
    if "title" in body:
        new_title= body["title"]
        db.tasks.update_one(
            {"_id": ObjectId(task_id)},
            {"$set": {"title":new_title}}
        )
    
    if "completed" in body:
        new_completed= body["completed"]
        db.tasks.update_one(
            {"_id": ObjectId(task_id)},
            {"$set": {"completed":new_completed}}
        )
    
    collection_tasks = db["tasks"]
    tasks = list(collection_tasks.find())
    for task in tasks:
        task["_id"] = str(task["_id"])
        
    for task in tasks:
        if task["_id"] == task_id:
            return task
    
  
                  
    
@tasks_bp.route("/tasks/<task_id>", methods= ["DELETE"])
def delete(task_id):
    if ObjectId.is_valid(task_id) == False:
        raise BadRequest("ID must be vaild ObjectId ")
    
    deleted_task = db.tasks.find_one_and_delete({"_id": ObjectId(task_id)})
    
    if deleted_task == None:
        raise NotFound("Task with id -{task_id}- not found")
    return "task deleted successfully "
    
  

    
    
    