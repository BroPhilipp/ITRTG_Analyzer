file = "ExampleData.txt"

def open_file(file):
    content = []
    with open (file,"r") as f:
        for line in f:
            content.append(line.strip())
    return content
        
def c_pets_list(file):
    content = open_file(file)
    pets_list =[]
    pos_empty_str = []
    summary_text = []
    for i,x in enumerate(content):
        if x == "":
            pos_empty_str.append(i)
    summary_text.append(content[int(pos_empty_str[1]+1):int(pos_empty_str[2])])
    for i in summary_text:
        print(i)
c_pets_list(file)