

class Figure:
    def __init__(self):
        self.layer_num=0
        self.layer_content=[]
    def get_layer_content(self):
        a=[]
        a.append("boundary")
        a.append(f"layer {self.layer_num}")
        a.append("datatype 0")
        b=""
        for each in self.layer_content:
            for every in each:
                # print(every)
                b+=f"{every} "
                # print(b)
        c=f"xy {len(self.layer_content)} {b.strip()}"
        # print(c)
        a.append(c)
        a.append("endel")
        return a




class MyClass:
    def __init__(self,x):
        self.content=readfile(x)
        self.objects=[]
        self.header_end=0
    def get_header(self):
        ctr=0
        header=[]
        while(self.content[ctr]!="boundary"):
            header.append(self.content[ctr])
            ctr+=1
        self.header=header
        self.header_end=ctr
        self.data_end=len(self.content)-2
    def get_objects(self):
        # print(self.content[self.header_end])
        ctr=self.header_end
        for j in range(ctr,self.data_end,5):
            obj=self.content[j:j+5]
            fig=Figure()
            fig.layer_num=(obj[1].split()[-1])
            a=(obj[-2].split())
            a=a[2:]
            # print(a)
            c=[]
            for i in range(0,len(a),2):
                b=[int(a[i]),int(a[i+1])]
                # print(b)
                c.append(b)
            fig.layer_content=c
            # print(fig.layer_content)
            self.objects.append(fig)
            fig.get_layer_content()



    

def readfile(loc):
    with open(loc) as file:
        all_lines=file.readlines()
    for i in range(0,len(all_lines)):
        all_lines[i]=all_lines[i].strip()
    return all_lines

def write_to_output(content):
    with open(r"Results/Milestone5.txt","a+") as file:
        for each in content:
            file.write(f"{each}\n")

def getDiff(a):
    c=[[0,0]]
    d=[[0,0]]
    for i in range(1,len(a)):
        x,y=a[i][0],a[i][1]
        # print(x,y)
        c.append([abs(x-a[i-1][0]),abs(y-a[i-1][1])])
        d.append([abs(y-a[i-1][1]),abs(x-a[i-1][0])])
        # print(c)
    return c,d

footer=["endlib","endstr"]
src=MyClass(r"Milestone_Input/Milestone 5/Source.txt")
src.get_header()
src.get_objects()

poi=MyClass(r"Milestone_Input/Milestone 5/POI.txt")
poi.get_header()
print(poi.header)
poi.get_objects()

shape_tofind=poi.objects[0].layer_content
all_shapes=[]
for each in src.objects:
    all_shapes.append(each.layer_content)
print(shape_tofind)

shape,shape2=getDiff(shape_tofind)
found_idx=[]
for i  in range(len(all_shapes)):
    test_shape1,test_shape2=getDiff(all_shapes[i])
    # print(test_shape1)
    if(sorted(test_shape1)==sorted(shape) or sorted(test_shape2)==sorted(shape)):
        print("Match")
        print(i)
        found_idx.append(i)
# print(len(found_idx))

write_to_output(poi.header)
for each in found_idx:
    write_to_output(src.objects[each].get_layer_content())

write_to_output(footer)