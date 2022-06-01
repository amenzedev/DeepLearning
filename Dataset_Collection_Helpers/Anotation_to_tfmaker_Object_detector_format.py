import os
import json

validation_set = [1,23,31,35,39,40,56,60,61,80] #10% validation from 100 image dataset
testing_set = [29,36,42,52,54,70,82,85,90,92] #10% testing from 100 image dataset

output_file_name = "bounding_boxes.txt"
out_file = open(output_file_name, "w")
arr = os.listdir()
file_counter = 0
for file in arr:    
    if ".json" not in file or ".jpeg" in file or ".jpg" in file or ".png" in file or ".gif" in file:
        #print(file)
        arr.remove(file)
print(len(arr))
for file in arr:    
    if (".json" in file or True):
        #print(file)
        f = open(file)
        data = json.load(f)
        # #print(data['asset'])
        #print(data['asset']['name'])
        image_file = data['asset']['name']
        # info_name = data['asset']['name'].replace(".jpg",".txt")
        # info_name = info_name.replace(".jpeg",".txt")
        # info_name = info_name.replace(".png",".txt")
        # info_name = info_name.replace(".gif",".txt")

        # print(info_name)
        for i in range (len(data['regions'])):
            left = data['regions'][i]['boundingBox']['left']
            top = data['regions'][i]['boundingBox']['top']
            right =  data['regions'][i]['boundingBox']['width']+left
            bottom = data['regions'][i]['boundingBox']['height']+top
            #print((left,top),(right,bottom))
            
            if(file_counter in validation_set):                
                string_out = "VALIDATE,door_dataset/"+image_file+",door,"+str(left)+","+str(top)+","+str(right)+","+str(bottom)+"\n"
            elif(file_counter in testing_set):      
                #print(file_counter)          
                string_out = "TEST,door_dataset/"+image_file+",door,"+str(left)+","+str(top)+","+str(right)+","+str(bottom)+"\n"
            else:                
                string_out = "TRAIN,door_dataset/"+image_file+",door,"+str(left)+","+str(top)+","+str(right)+","+str(bottom)+"\n"
        
            out_file.write(string_out)
            #print((left,top),(right,bottom))
        f.close()
        file_counter+=1
#print(len(arr))
#print(arr)
print(file_counter)
out_file.close()
        