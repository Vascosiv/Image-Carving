import os
import re

JPEG_SOF = b'\xFF\xD8\xFF\xE0' #magic number for DOF
JPEG_EOF = b'\xFF\xD9'         #magic number for EOF

file_obj = open('2006.raw',"rb") #open raw file of dfrws-2006-challenge
data = file_obj.read() #read binary of the raw file
file_obj.close()
SOF_list = [match.start() for match in re.finditer(re.escape(JPEG_SOF),data)] #find SOF
EOF_list=[match.start() for match in re.finditer(re.escape(JPEG_EOF),data)] #find EOF
i=0
for SOF in SOF_list:
    for EOF in EOF_list:
        if SOF<EOF:                                                         #for loop for find SOF which less than  EOF
            subdata=data[SOF:EOF]
            filename = "Carve" +str(i+1)+ "_" +str(SOF)+"_"+str(EOF)+".jpg" #create filename of the JPEG 
            path = 'C:\\Users\\User\\Desktop\\CODE\\Python\\carverel'       #make path for extracted images
            carve_filename = os.path.join(path,filename)                    #os.path.join() module used for python in operating system path
            newfile = open('location.txt',"a")                              #for python to auto create a txt file
            newfile.write(filename + '\n')                                  #write the filename
            newfile.close()
            carve_obj = open(carve_filename,"wb")                           #open file created to write binary of the magic number
            carve_obj.write(subdata)
            carve_obj.close()

            i=i+1
            print (filename)
            



            
