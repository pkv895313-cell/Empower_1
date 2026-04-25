#WAP- Create a dictionary out of the following list 
colours_list=["Yellow","Blue","Red","Black","Orange","White"]

colour_dictionary = dict();
position = 1

for item in colours_list:
    colour_dictionary[position] = item
    position +=1
    
    print(colour_dictionary)
