
all_id = []

#Object for every unique teamspeak user ID
class User:

	def __init__(self, teamspeak_id):
		self.teamspeak_id = teamspeak_id
		self.names = []

	def add_name(self, str1):
		name_exists = False
		for name in self.names:
			if (name==str1):
				name_exists = True
				break
		if(name_exists == False):
			self.names.append(str1)


	def get_teamspeak_id(self):
		return self.teamspeak_id

	def get_all_names(self):
		return self.names

input_file = open("Server test.html", "r")

def ClientConnected(str):
	current_line = str
	print current_line + '\n'
	teamspeak_id_index_start = current_line.find('href="client://', 0)
	teamspeak_id_index_end = current_line.find('=~',teamspeak_id_index_start)

	#teamspeak ID is stored in variable below
	teamspeak_id = current_line[18+teamspeak_id_index_start:teamspeak_id_index_end]

	name_index_start = current_line.find('>&quot;', teamspeak_id_index_end)
	name_index_end = current_line.find('&quot;</a>', name_index_start)

	#teamspeak name is stored in variable below
	name = current_line[7+name_index_start: name_index_end]

	print "HER ER USER NAME:" + name
	print "HER ER USER ID:" + teamspeak_id

	id_exists = -1
	for i in range(0, len(all_id)):
		if(all_id[i].get_teamspeak_id() == teamspeak_id):
			id_exists = i

			break

	if(id_exists == -1):
		new_user = User(teamspeak_id)
		all_id.append(new_user)
		new_user.add_name(name)
	else:
		all_id[id_exists].add_name(name)
	

#main loop
for i in range(0, 100):
	current_line = input_file.readline()

	#ClientConnected
	index = current_line.find('<p class="TextMessage_ClientConnected">', 0)
	if (index != -1):
		ClientConnected(current_line)



print "TEST!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
print all_id[0].get_all_names()


print "end of file"

