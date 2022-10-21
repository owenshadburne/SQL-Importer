import sqlite3

table = sqlite3.connect('data.sqlite')

class Importer:

    def import_file(self, filename):
        print("BUTTS")
        if(filename[:-3] == "csv"):
            self.import_csv(filename)
        elif(filename[:-4] == "json"):
            self.import_json(filename)
        elif(filename[:-3] == "xml"):
            self.import_xml(filename)
        #table.execute("DROP TABLE IF EXISTS data")
        #table.execute("""CREATE TABLE IF NOT EXISTS data ()""")

    def import_csv(self, filename):
        print("THIS IS A CSV")

    def import_json(self, filename):
        print("THIS IS A JSON")

    def import_xml(self, filename):
        print("THIS IS AN XML")
