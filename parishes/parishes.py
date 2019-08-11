import csv
import sqlite3
import os

csv_file = open('parishes.csv', 'r')
csv_reader = csv.reader(csv_file, delimiter=',')

dist_files = os.listdir('districts_2')

conn = sqlite3.connect('parishes.sqlite')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS parishes (id, district, subcounty, parish)''')
conn.commit()

def filter_places():
    empty_lines = 0

    dist_no = 1
    
    for row in csv_reader:
        info = row[0] + row[1]
        line = row[0] + row[1] + row[2] + row[3]
        #print(info)
        
        if line.strip() == '':
            empty_lines += 1
        else:
            empty_lines = 0
            
        if empty_lines == 1:
            pass
            #print('\t\t\t\t\t\t\t ************ New Sub County')
            
        elif empty_lines > 1:
            #print('\t\t\t\t\t\t\t ############ New District')
            #dist_file = open('districts/'+str(dist_no)+'.txt', 'a')
            dist_no += 1

        dist_file = open('districts/'+str(dist_no)+'.txt', 'a')
        dist_file.write(info + '\n')
        dist_file.close()


def delete_empty_files():
    for file in dist_files:
        fhand = open('districts/'+file)
        cont = fhand.read().strip()
        if cont == '':
            file_to_rem = 'districts/'+file
        fhand.close()
        try:
            os.remove(file_to_rem)
        except:
            pass

def strip_districts():
    dist_no = 1
    for file in dist_files:
        fhand = open('districts/'+file)
        cont = fhand.read().strip()
        fhand.close()

        fhand1 = open('districts_2/'+str(dist_no)+'.txt', 'w')
        fhand1.write(cont)
        fhand.close()
        dist_no += 1


def store_districts():
    n = 1
    places = []
    for file in dist_files:
        fhand = open('districts_2/'+file)
        cont = fhand.read()
        chunks = cont.split('\n\n')

        i = 0
        for chunk in chunks:
            pars = []
            
            i += 1
            bits = chunk.split('\n')
            if i == 1:
                dist = bits[0].strip()
                sc = bits[1].strip()
                par = bits[2:]
                
            else:
                sc = bits[0].strip()
                par = bits[1:]

            for p in par:
                parish = p.strip()
                place = (n, dist,sc,parish)
                write(place)
                n+=1
                #write(place)
                pars.append(parish)
        print(file)



def write(row):
    sql = '''INSERT INTO parishes (id, district, subcounty, parish) VALUES (?,?,?,?)'''
    cur.execute(sql, row)
    conn.commit()

        

store_districts()            
        
            



#store_districts()














































        
