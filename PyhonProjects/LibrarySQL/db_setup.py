import sqlite3
from pathlib import Path
import json

details_list = {
                "book": ["title", "author", "genre", "language", "publication year", "class"],
                "customer": ["family", "first", "address"],
                "employee": [],
                "library": ["title", "address"]
                }

sql_folder = Path(__file__).parent / "sql"
db_file_path = Path(__file__).with_name("data.db")
sql_setup = (sql_folder / "setup_db.sql").read_text()

db = sqlite3.connect(db_file_path)
cursor = db.cursor()
cursor.executescript(sql_setup)
db.commit()

with open("ItemData.json", "r") as f:
    item_data = json.load(f)

with open("sql/items_insert.sql", "r") as f:
                sql_i = f.read()
                
with open("sql/details_insert.sql", "r") as f:
                sql_d = f.read()
                
for serial in item_data:
    item0 = item_data[serial]["type"]
    item1 = item_data[serial]["value"]
    try:
        item1 = float(item1)
    except:
        item1 = 0.0
    item2 = "NIS"
    cursor.execute(sql_i, [item0, item1, item2])
    index = len(item_data[serial]["details"].values())
    detail_insert_list = []
    spacer = []
    for i in range(10 - index):
        spacer.append("")
    for d in range(index):
        detail_key = details_list[item0][d]
        detail_insert_list.append(item_data[serial]["details"][detail_key])
    detail_insert_list.extend(spacer)
    cursor.execute(sql_d, detail_insert_list)

db.commit()
            
            
            