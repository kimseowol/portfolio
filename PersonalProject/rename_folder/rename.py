import os

def convert_file_foo(path):
    list = os.listdir(path)
    for i in list:
        my_path = path+i+os.sep+"shot"+os.sep
        #print(my_path)
        list2 = os.listdir(my_path)
        for j in list2:
            if j == "foo":
                my_path2 = my_path+j+os.sep
                list3 = os.listdir(my_path2)
                print(list3)
                for k in list3:
                    #print(k)
                    my_path3 = my_path2+k+os.sep+"plate"+os.sep+"v001"
                    list4 = os.listdir(my_path3)
                    for l in list4:
                        # print(l)
                        src = os.path.join(my_path3,l)
                        #print(src)
                        dst_name = l.replace("foo","far")
                        #print(dst_name)
                        dst = os.path.join(my_path3, dst_name)
                        #print(dst)
                        os.rename(src,dst)

##########
def convert_foo(path):
    list = os.listdir(path)
    for i in list:
        my_path = path + i + os.sep + "shot" + os.sep
        print(my_path)
        if os.path.isdir(my_path):
            list = os.listdir(my_path)
            for i in list:
                if i == "foo":
                    os.rename(my_path+"foo",my_path+"far")
        


if __name__=="__main__":
    convert_file_foo(input("input a Project path"))