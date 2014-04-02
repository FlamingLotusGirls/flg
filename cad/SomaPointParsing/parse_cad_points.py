import csv
import sys
import os.path

def parse_cad_points_to_json(file):
    output_string = "[\n"

    with open(file, 'rb') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            new_row = str(row)
            for ch in [" ","'","[","]"]:
                new_row = new_row.replace(ch,"")
            row_array = new_row.split(",")
            new_array = []
            for x in row_array:
                 new_array.append(float(x)/1000)
            output_string += '{"point": ' + str(new_array) + '},\n'
    output_string = output_string[:-2]
    output_string += "\n]"

    json_file_name = file.replace(".txt", ".json")

    write_to_file = open(json_file_name, 'w')
    write_to_file.write(output_string)
    write_to_file.close()

    return json_file_name

input_file = sys.argv[1]
if os.path.isfile(input_file):
    json_file = parse_cad_points_to_json(input_file)
    print json_file + " created"
else:
    print "Booooo-urns"


