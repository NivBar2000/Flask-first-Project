# from db import db

# tasks= [
# {
#     "id" : str(uuid.uuid4()),
#     "title":"learn flask",
#     "completed": False
# },

# {
#     "id" : str(uuid.uuid4()),
#     "title":"build API",
#     "completed": False
# },

# {
#     "id" : str(uuid.uuid4()),
#     "title":"Test with postman",
#     "completed": True
# }
# ]

# def get_all_tasks():
    # return tasks

# def get_task_by_id(task_id):
#      for task in tasks:
#          if task["id"] == task_id:
#              return task
#      return None
        
# def create_task(task_data):
#     new_task = {
#         "id": str(uuid.uuid4()),
#         "completed" : False,
#         "title" : task_data["title"].strip()
#     }
#     db.tasks.insert_one(new_task)
#     return new_task

# def update_task(body,task_id):
    
# for task in tasks:
#     if task["id"] == task_id:
#         if "title" in body:
#             task["title"] = body["title"]
#         if "completed" in body:
#             task["completed"] = body["completed"]
#         return task
# return None

# def delete_task(task_id):
#     for task in tasks:
#         if task["id"] == task_id:
#            tasks.remove(task)
#            return tasks
#     return None