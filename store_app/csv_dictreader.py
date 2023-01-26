import csv
class CSV_Interface:

    def __init__(self, file_name):

         with open(file_name, 'r') as file:
            reader = csv.DictReader(file)
            self.columns = reader.fieldnames

         self.file_name = file_name
         self.update_data_from_file()
  
    def update_data_from_file(self):
        data=[]
        with open(self.file_name, 'r') as file:
            reader = csv.DictReader(file)
            for i in reader:
                data.append(i)
        self.all_data = data
        return self.all_data

    def append_one_row_to_file(self, new_data_dict):

        with open(self.file_name, "a", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.columns)
            writer.writerow(new_data_dict)
    
    def unique_counter(self, file_sets):
        second_holder=[]
        count = ''
        new_cost= ''
        for i in file_sets:
     
            i['count'] = sum([1 for j in file_sets if j['product'] == i['product']])
        second_holder.append({k['product']:k for k in file_sets}.values()) 
        last_holder=[]
        for i in second_holder:
            print(i)
            for j in i:
                count= int(j['count'])
                new_cost = float(j['cost']) * count
                j['cost'] = round(new_cost,2)
                last_holder.append({'product': j['product'],'cost': j['cost'],'count': j['count']})
         
        return last_holder


    def no_copies(self):
        data=[]
        with open(self.file_name, 'r') as file:
            reader = csv.DictReader(file)
            for i in reader:
                data.append(i)
        result = list( {
        dictionary['category']: dictionary
        for dictionary in data
        }.values())
        self.all_data = data

        return result
    