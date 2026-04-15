from flask import Flask

from routes import tasks_bp
from errors import error_bp

app = Flask(__name__)


app.register_blueprint(tasks_bp)
app.register_blueprint(error_bp)

    
    
if __name__  == "__main__":
    app.run(debug=True)





# @app.errorhandler(NotFound)
# def handle_type_error(e):
#     return jsonify({
#         "error": str(e)
#     }), 404

# @app.errorhandler(BadRequest)
# def handle_type_error(e):
#     return jsonify({
#         "error": str(e)
#     }), 400
    
# @app.errorhandler(UnprocessableEntity)
# def handle_type_error(e):
#     return jsonify({
#         "error": str(e)
#     }), 422

# @app.route("/")
# def home():
#     return jsonify({
#         "message" : "Welcome to my API"
#     })
    
    
# @app.route("/tasks", methods =["GET"])
# def get_tasks():
#     return jsonify(tasks)
       
# @app.route("/tasks/<task_id>")
# def get_task_by_id(task_id):
    
#     for task in tasks:
#         if task["id"] == task_id:
#             return jsonify(task)
#     return jsonify({
#         "message" : "Not found"
#             }),404

       
       
# #==============Create Task=====================       

# @app.route("/tasks", methods= ["POST"])
# def create_task():
#     body = request.get_json()
#     if body == {}:
#         raise BadRequest("Request body must be full JSON")
    
#     title = body["title"]                
#     if not isinstance(title, str): 
#         raise BadRequest("Title must be a string")
    
#     if not title.strip():
#         raise UnprocessableEntity("Title cannot be empty")
    
#     new_task = {
#         "completed" : False,
#         "id" : str(uuid.uuid4()),
#         "title" : body["title"]
#     }
    
#     tasks.append(new_task)
#     return jsonify(new_task),201


# #===============Update Task by ID=====================

# @app.route("/tasks/<task_id>", methods= ["PUT"])
# def update(task_id):
#     body = request.get_json()
    
#     if body == {}:
#         raise BadRequest("Request body must be full JSON")
    
#     title = body["title"]
#     if not isinstance(title, str):
#         raise BadRequest("Title must be a string")
    
#     completed = body["completed"]
#     if not isinstance(completed, bool):
#         raise BadRequest("completed must be bool.")
        
#     for task in tasks:
#         if task["id"] == task_id:
#             if "title" in body:
#                 task["title"] = body["title"]
#             if "completed" in body:
#                 task["completed"] = body["completed"]
            
#             return jsonify(task)

#     return jsonify({
#         "message" : "task Not found"
#             }),404
    
# @app.route("/tasks/<task_id>", methods= ["DELETE"])
# def delete(task_id):
    
#     for task in tasks:
#         if task["id"] == task_id:
#            tasks.remove(task)
#            return jsonify(tasks)

#     return jsonify({
#         "message" : "task Not found"
#             }),404
    
    
        
  