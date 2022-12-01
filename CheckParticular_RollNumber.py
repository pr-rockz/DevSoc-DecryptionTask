# Checks if a particular roll number exists in the list of DevSoc members

import hashlib

a_string = "21" + "PH10031"

total_members = ["46b42d", "e11e5f", "0b684k", "36f5f5", "a76y31", "jd7kt8", "94ec5c", "95597e", "a921d9", "4db990", "beaf85", "bfa0d5", "c85261", "776f63", "a085f4", "1aee3e", "849182", "174fea", "b9d5bd", "919876", "9eaa9b", "d7bbce", "39fu04", "991243", "039869", "d9b386", "389f4e", "e1f420", "6eb8af", "872c4a", "ac85dd", "d1ddfc", "c760b2", "c5ac28", "024899", "830d6b", "4d8bc4", "e8490c", "17239e", "8c2f88", "3c4ab9", "54f581", "8bd49d", "128edb"]

hashed_string = hashlib.sha256(a_string.encode('utf-8')).hexdigest()
hashed_string = hashed_string[-6:]

for j in total_members:
    if hashed_string == j:
        print(a_string)