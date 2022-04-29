import os
arr = os.listdir()

for i in range (1):#(len(arr)):
    if(".xml" in arr[i]):
        #print(arr[i])
        input_file = open(arr[i],"r")
        file_name = arr[i].replace(".xml",".txt")
        #print(file_name)
        output_file = open(file_name,"w")
        Lines = input_file.readlines()
        final_string=""
        for line in Lines:
            string_holder=""
            if "<xmin>" in line:
                string_holder =line+""
                string_holder = string_holder.replace("<xmin>","")
                string_holder = string_holder.replace("</xmin>","")
                string_holder = string_holder.replace("  ","")
                string_holder = string_holder.replace("\n","")
                final_string += string_holder+ " "
                #print(string_holder+" ")
            elif "<ymin>" in line:
                string_holder =line+""
                string_holder = string_holder.replace("<ymin>","")
                string_holder = string_holder.replace("</ymin>","")
                string_holder = string_holder.replace("  ","")
                string_holder = string_holder.replace("\n","")
                string_holder=string_holder+" "
                final_string += string_holder+ " "
                #print(string_holder)
            elif "<xmax>" in line:
                string_holder =line+""
                string_holder = string_holder.replace("<xmax>","")
                string_holder = string_holder.replace("</xmax>","")
                string_holder = string_holder.replace("  ","")
                string_holder = string_holder.replace("\n","")
                string_holder=string_holder+" "
                final_string += string_holder+ " "
                #print(string_holder)
            elif "<ymax>" in line:
                string_holder =line+""
                string_holder = string_holder.replace("<ymax>","")
                string_holder = string_holder.replace("</ymax>","")
                string_holder = string_holder.replace("  ","")
                string_holder = string_holder.replace("\n","")
                string_holder=string_holder+" "
                final_string += string_holder+ " \n"
                #print(string_holder)
            
        output_file.write(final_string)
        print(final_string)
        
