# SQLite Import

It's time to put everything together and import data into a SQLite database file.

Your task is to implement the `Import` class so that it will import data from `xml`, `json` or `csv` files. For each data set there is an XML, JSON, and CSV file to test with. The database structure should be the same after importing each, although the actual data differs. 

For all of these imports you should use the filename `data.sqlite` for the database. The table names will be based on the filename of the import. `data.sqlite` will have multiple tables after running multiple import files. 

Tables should start empty before importing so that if you import the same file multiple times only the data from the last run is in the table. If the table doesn't exist, it must be created prior to import. 

Field names will have to be determined by the data. In addition, there should be an auto incrementing primary key field named `id` in each table created. The creation query should add this field, but it does not need to be included in your `INSERT` queries. SQLite will take care of automatically incrementing the field. 

### Field Types
All fields will either be text, integer, real / decimal, or date time. To receive full credit your code must use the data to determine field types. You can assume that all records have the same field type. For example, in `cars.xml` there is a field named `date_time` that will be a date time field in all records.

Date time fields will all be formatted like `2020-06-15 03:20:58` with `YYYY-MM-DD HH:MM:SS`. Integer fields are always whole number, but never longer than 6 digits. Treat any whole number longer than 6 digits as text. Decimal / real fields are numeric, but will have decimals. Use text for anything else. 

## Command Line Arguments
Your script, in `runner.py`, should pull the filename to import from the command line. 

For example, let's say you run the following command from the terminal.

```
python runner.py cars.json
```

Inside of `runner` you will have access to the list `sys.argv`. Element `sys.argv[0]` is the name of the file executed, in this case `runner.py`. `sys.argv[1]` will be the name of the file to import, in this case `cars.json`. You will need that filename to pass in to your `Import::import` method.

## Methods in Import

### import
The `import` method is a wrapper around the other methods. It should hand off to the other `import_X` methods in this class to actually do the import based on the extension of `filename`. You may assume that any file ending with `.xml` is an XML file, `.csv` is a CSV file, and `.json` is a JSON file. You do not need to determine file type based on the actual contents. 

This must be the only method actually called from the runner. 

### import_csv
`import_csv` reads `filename` and imports into `data.sqlite` in a table named the same as the file, minus the extension. For example, `books.csv` should import into a table called `books`.

The first line in the CSV file will be field names. Each subsequent line is a data line.

### import_json
`import_json` reads `filename` and imports into `data.sqlite` in a table named the same as the file, minus the extension. For example, `cars.json` should import into a table called `cars`. 

You may assume that all records have the same fields as the first record. 

### import_xml
`import_xml` reads `filename` and imports it into `data.sqlite` in a table named the same as the file, minus the extension. For example, `cars.xml` should import into a table called `cars`. 

You can assume that XML are all wrapped in the root `dataset` and each record is `record`. 

Field names should be the element name. For example, `<model>Buick</model>` should put `Buick` in a field named `model`.

You may assume that all records have the same field names as the first record. 

## Testing and Grading
You have multiple matching sets of data in each format. For example; there is a `cars.xml`, `cars.csv` and a `cars.json` file in the starter code. Each of these files will create a database table with the same structure, although the actual data may differ. They also might be different number of rows to import. 

To grade, I'm going to use a different set of files to check your import so it's critical that you do not write  your code specifically to the files you're given. 