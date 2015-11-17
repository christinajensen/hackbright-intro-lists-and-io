christina_file = open("christina_fav_foods.txt")
christina_fav = christina_file.readlines() 
christina_file.close()

kelsey_file = open("kelsey_fav_foods.txt")
kelsey_fav = kelsey_file.readlines()
kelsey_file.close()

#both_files = open("christina_fav_foods.txt"), open("kelsey_fav_foods.txt") 
#both_favs = both_files.readlines() 
#both_favs.close()
#print both_favs

def compare_favs(list1, list2):
	if (christina_fav[0] == kelsey_fav[0]):
		print "Our favorite foods are the same!"
	else:
		print "Our favorite foods are different"	

compare_favs(christina_fav, kelsey_fav)