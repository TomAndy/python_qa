import csv

transformer={'critical':'high',
             'high':'medium',
             'medium':'low'}

def func4():
    with open('Python for QA - bugs list - Sheet1.csv','r') as csvfile:
        with open('resulted_file.csv','w') as resultCsvFile:
            reader=csv.DictReader(csvfile)
            writer=csv.writer(resultCsvFile)
            for row in reader:
                row['Priority']=transformer.get(row.get('Priority'))
                if row['Priority'] is None:
                    continue
                else:
                    writer.writerow([row])
                # if row.get('Priority')=='critical':
                #     row['Priority']='high'
                #     writer.writerow([row])
                # elif row.get('Priority') == 'high':
                #     row ['Priority'] = 'medium'
                #     writer.writerow([row])
                # elif row.get('Priority') == 'medium':
                #     row ['Priority'] = 'low'
                #     writer.writerow([row])
        resultCsvFile.close()
    csvfile.close()

if __name__ == '__main__':
    func4()
