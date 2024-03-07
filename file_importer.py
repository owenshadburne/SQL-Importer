import sqlite3, csv, json
import xml.etree.ElementTree as ET 

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
        with open(filename + '.csv', mode='r', encoding='utf-8') as file:
            d = csv.DictReader(file)
            self.dictionary_to_sql(filename, d)
    def import_json(self, filename):
        j = json.load(open(filename + ".json", mode='r', encoding="utf-8"))
        self.dictionary_to_sql(filename, j)

    def dictionary_to_sql(self, filename, d):
        data.execute("DROP TABLE IF EXISTS " + filename)

        results = []
        creation = "id INTEGER PRIMARY KEY, "
        insertHeader = ""
        for row in d:
            for title in row:
                item = row[title]
                print("Title: " + str(title) + " Item: " + str(item))
                insertHeader += title + ", "
                if type(item) is int or len(item) < 6 and item.isdigit():
                    results.append((title, "INTEGER"))
                    creation += title + " INTEGER, "
                elif type(item) is float or "." in item and item.replace(".", "").isdigit():
                    results.append((title, "REAL"))
                    creation += title + " REAL, "
                else:
                    results.append((title, "TEXT"))
                    creation += title + " TEXT, "
            break

        data.execute("CREATE TABLE IF NOT EXISTS " + filename + "(" + creation[:-2] + ")")
        
        for row in d:
            values = ""
            for title in row:
                item = row[title]
                if type(item) is int or len(item) < 6 and item.isdigit():
                    results.append((title, "INTEGER"))
                    values += str(item) + ", "
                elif type(item) is float or "." in item and item.replace(".", "").isdigit():
                    results.append((title, "REAL"))
                    values += str(item) + ", "
                else:
                    results.append((title, "TEXT"))
                    values += "'" + item.replace("'", "''") + "', "

            data.execute("INSERT INTO " + filename + "(" + insertHeader[:-2] + ")" + " VALUES (" + values[:-2] + ")")

        data.commit()

    def import_xml(self, filename):
        root = ET.parse(filename + '.xml').getroot()

    
