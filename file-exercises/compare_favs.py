def convert_files_to_list(file): 
	open_files = open(file)
	favorites = open_files.readlines() 
	open_files.close()
	return favorites 

christina_fav = convert_files_to_list("christina_fav_foods.txt")
kelsey_fav = convert_files_to_list("kelsey_fav_foods.txt")

def compare_favs(list1, list2):
	if (list1[0] == list2[0]):
		print "Our favorite foods are the same!"
	else:
		print "Our favorite foods are different"	

compare_favs(christina_fav, kelsey_fav)

#def compare_favs2()
