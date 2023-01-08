file = "ExampleData.txt"

def open_file(file):
    content = []
    with open (file,"r") as f:
        for line in f:
            content.append(line.strip())
    return content
        
