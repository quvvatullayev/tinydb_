from tinydb import TinyDB
from tinydb.table import Document

db = TinyDB('db.json', sort_keys = True, indent = 4)
doc_id = 1

for i in range(len(db.all()) + 1):
    if not db.contains(doc_id=doc_id):
        data = Document({
            'name':'ozod',
            'age':15
            }, doc_id=doc_id)
        db.insert(data)
        print(db.get(doc_id=doc_id))
    else:
        doc_id += 1
