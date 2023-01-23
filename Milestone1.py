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
        # self.
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
            print(fig.layer_content)
            self.objects.append(fig)
            fig.get_layer_content()



    

def readfile(loc):
    with open(r"Milestone_Input/Milestone 1/Format_Source.txt") as file:
        all_lines=file.readlines()
    for i in range(0,len(all_lines)):
        all_lines[i]=all_lines[i].strip()
    return all_lines

def write_to_output(content):
    with open(r"Results/Milestone1.txt","a+") as file:
        for each in content:
            file.write(f"{each}\n")

m=MyClass(r"Milestone_Input/Milestone 1/Format_Source.txt")
m.get_header()
write_to_output(m.header)
footer=["endlib","endstr"]
(m.get_objects())
# print(m.objects)

for i  in range(2):
    a=m.objects[i].get_layer_content()
    write_to_output(a)

write_to_output(footer)

