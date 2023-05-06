import csv

with open("title.basics.tsv.gz", encoding="latin1", newline='') as csvfile:
    tsv_file = csv.reader(csvfile, delimiter="\t")
    #fixed_lines = (line.replace(b'\x00', b'') for line in tsv_file)
    for line in tsv_file:
        print(line)