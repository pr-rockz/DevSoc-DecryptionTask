# prints all the roll numbers and their hashes in a readable format

import hashlib
import json


# storing the department code in a list
list_departments = ["AE", "AG", "AR", "BT", "CH", "CE", "CS", "CY", "EC", "EE", "EX", "GG", "HS", "IE", "IM", "MA", "MF", "ME", "MI", "MT", "NA", "PH"]

# storing the different program(4 year or dual degree) code in a list
list_years = ["1", "2", "3"]

# storing the total number of students(real or fake) in a list
total_members = ["46b42d", "e11e5f", "0b684k", "36f5f5", "a76y31", "jd7kt8", "94ec5c", "95597e", "a921d9", "4db990", "beaf85", "bfa0d5", "c85261", "776f63", "a085f4", "1aee3e", "849182", "174fea", "b9d5bd", "919876", "9eaa9b", "d7bbce", "39fu04", "991243", "039869", "d9b386", "389f4e", "e1f420", "6eb8af", "872c4a", "ac85dd", "d1ddfc", "c760b2", "c5ac28", "024899", "830d6b", "4d8bc4", "e8490c", "17239e", "8c2f88", "3c4ab9", "54f581", "8bd49d", "128edb"]

# this dictionary is for storing the real roll numbers and their corresponding secret ids
dictionary = {}

roll_number = "21"

# the following nested for loops are used to generate all the possible roll numbers and then check if they are present in the list of total members
for list1 in list_departments:
    for list2 in list_years:
        for i in range(1, 100):
            
            roll_number = "21"
            if i < 10:
                roll_number = roll_number + list1 + list2 + "000" + str(i)
            else:
                roll_number = roll_number + list1 + list2 + "00" + str(i)
            
            hashed_string = hashlib.sha256(roll_number.encode('utf-8')).hexdigest()
            hashed_string = hashed_string[-6:]
            
            for j in total_members:
                if hashed_string == j:
                    dictionary[roll_number] = hashed_string
                    
                    
# print("\n".join("{}\t{}".format(k, v) for k, v in dictionary.items())) --> This is for printing the dictionary in a tabular format

# prints the dictionary
print(json.dumps(dictionary, indent=4, sort_keys=True))