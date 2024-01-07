# import os
# print(os.getcwd())

# import json
# username = "admin"
# password = "1234"
# with open("users.json", "r") as f:
#     users = json.load(f)
# if username in users and users[username]["password"] == password:
#     print(users[username].keys())
operation = 'SELECT 1; INSERT INTO t1 VALUES (); SELECT 2'
for result in cursor.execute(operation, multi=True):
  if result.with_rows:
    print("Rows produced by statement '{}':".format(
      result.statement))
    print(result.fetchall())
  else:
    print("Number of rows affected by statement '{}': {}".format(
      result.statement, result.rowcount))
