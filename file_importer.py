import sqlite3, csv, json, xml

data = sqlite3.connect('data.sqlite')

class Importer:

    def import_file(self, filename):
        if(filename[-3:] == "csv"):
            self.import_csv(filename[:-4])
        elif(filename[-4:] == "json"):
            self.import_json(filename[:-5])
        elif(filename[-3:] == "xml"):
            self.import_xml(filename[:-4])

    def import_csv(self, filename):
        data.execute("DROP TABLE IF EXISTS " + filename)

        results = []
        creation = "id INTEGER PRIMARY KEY, "
        insertHeader = ""
        with open((filename + '.csv'), mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                for title in row:
                    item = row[title]
                    insertHeader += title + ", "
                    if len(item) < 6 and item.isdigit():
                        results.append((title, "INTEGER"))
                        creation += title + " INTEGER, "
                    elif "." in item and item.replace(".", "").isdigit():
                        results.append((title, "REAL"))
                        creation += title + " REAL, "
                    else:
                        results.append((title, "TEXT"))
                        creation += title + " TEXT, "
                break

        insertHeader = insertHeader[-2]
        print(results)
        data.execute("CREATE TABLE IF NOT EXISTS " + filename + "(" + creation[:-2] + ")")

        with open((filename + '.csv'), mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                values = ""
                for title in row:
                    item = row[title]
                    if len(item) < 6 and item.isdigit():
                        results.append((title, "INTEGER"))

                    elif "." in item and item.replace(".", "").isdigit():
                        results.append((title, "REAL"))
                    else:
                        results.append((title, "TEXT"))
            data.execute("INSERT INTO " + filename + "(" + insertHeader[] + ")" + "VALUES (" + values + ")")

    def import_json(self, filename):
        print("THIS IS A JSON")

    def import_xml(self, filename):
        print("THIS IS AN XML")
