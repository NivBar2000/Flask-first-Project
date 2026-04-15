from flask import jsonify,request,Blueprint
from werkzeug.exceptions import NotFound, BadRequest, Conflict, UnprocessableEntity
from models import get_all_tasks, get_task_by_id,create_task,update_task,delete_task, tasks
import uuid

tasks_bp = Blueprint("tasks", __name__)




@tasks_bp.route("/")
def home():
    return jsonify({
        "message" : "Welcome to my API"
    })
 
@tasks_bp.route("/tasks", methods =["GET"])
def get_tasks():
    return jsonify(get_all_tasks())
       
@tasks_bp.route("/tasks/<task_id>")         
def get_task_from_id(task_id):
    task = get_task_by_id(task_id)
    if task == None:
        raise NotFound(f"Task with id {task_id} not found")
    return(task)
       
       
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
    
    return jsonify(create_task(body)),201


#===============Update Task by ID=====================

@tasks_bp.route("/tasks/<task_id>", methods= ["PUT"])    #! בעיה בפונקציה לא עובד כמו שצריך
def update(task_id):
    body = request.get_json(silent=True)
    title = body["title"]
    
    if body is None:
        raise BadRequest("Missing JSON body")
    
    if body == {}:
        raise BadRequest("Request body must be full JSON")

    if not isinstance(title, str):
        raise BadRequest("Title must be a string")
    
    completed = body["completed"]
    if not isinstance(completed, bool):
        raise BadRequest("completed must be bool.")
        
    updated_task = update_task(body, task_id)

    if updated_task is None:
        raise NotFound(f"Task with id {task_id} not found")
    
    return update_task

    
           
            
    
@tasks_bp.route("/tasks/<task_id>", methods= ["DELETE"])
def delete(task_id):
    deleted_task= delete_task(task_id)
    if deleted_task == None:
        raise NotFound(f"Task with id {task_id} not found")
    
    return jsonify(deleted_task)
    
    
    