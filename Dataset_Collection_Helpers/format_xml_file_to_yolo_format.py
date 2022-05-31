import os
arr = os.listdir()

for i in range (len(arr)): #(1):#
    if(".xml" in arr[i]):
        #print(arr[i])
        input_file = open(arr[i],"r")
        file_name = arr[i].replace(".xml",".txt")
        #print(file_name)
        output_file = open(file_name,"w")
        Lines = input_file.readlines()
        final_string=""
        width = 1
        height = 1
        xmin = 0
        ymin = 0
        xmax = 0 
        ymax = 0

        for line in Lines:
            string_holder=""
            if "<xmin>" in line:
                string_holder =line+""
                string_holder = string_holder.replace("<xmin>","")
                string_holder = string_holder.replace("</xmin>","")
                string_holder = string_holder.replace("  ","")
                string_holder = string_holder.replace("\n","")
                #final_string += string_holder+ " "
                xmin = int (string_holder)
                #print(xmin)
            elif "<ymin>" in line:
                string_holder =line+""
                string_holder = string_holder.replace("<ymin>","")
                string_holder = string_holder.replace("</ymin>","")
                string_holder = string_holder.replace("  ","")
                string_holder = string_holder.replace("\n","")
                string_holder=string_holder+" "
                #final_string += string_holder+ " "
                ymin = int (string_holder)
                #print(ymin)
                #print(string_holder)
            elif "<xmax>" in line:
                string_holder =line+""
                string_holder = string_holder.replace("<xmax>","")
                string_holder = string_holder.replace("</xmax>","")
                string_holder = string_holder.replace("  ","")
                string_holder = string_holder.replace("\n","")
                string_holder=string_holder+" "
                #final_string += string_holder+ " "
                xmax = int (string_holder)
                #print(xmax)
            elif "<ymax>" in line:
                string_holder =line+""
                string_holder = string_holder.replace("<ymax>","")
                string_holder = string_holder.replace("</ymax>","")
                string_holder = string_holder.replace("  ","")
                string_holder = string_holder.replace("\n","")
                string_holder=string_holder+" "
                #final_string += string_holder+ " "
                ymax = int (string_holder)
                #print(ymax)
                #print(string_holder)
            elif "<width>" in line:
                string_holder =line+""
                string_holder = string_holder.replace("<width>","")
                string_holder = string_holder.replace("</width>","")
                string_holder = string_holder.replace("  ","")
                string_holder = string_holder.replace("\n","")
                string_holder=string_holder+" "
                #final_string += string_holder+ " "
                width = int (string_holder)
                #print(width)
                #print(string_holder)
            elif "<height>" in line:
                string_holder =line+""
                string_holder = string_holder.replace("<height>","")
                string_holder = string_holder.replace("</height>","")
                string_holder = string_holder.replace("  ","")
                string_holder = string_holder.replace("\n","")
                string_holder=string_holder+" "
                #final_string += string_holder+ " "
                height = int (string_holder)
                #print(height)
                #print(string_holder)
            
        center_x = (xmax - xmin) /(2*width)
        center_y = (ymax - ymin) /(2*height)
        width_object = (xmax - xmin)/width
        height_object = (ymax - ymin)/ height
        final_string += "2 " + str(center_x) + " " +str(center_y) + " "+str(width_object) + " "+str(height_object) + " "
            
        output_file.write(final_string)
        print(final_string)
        
