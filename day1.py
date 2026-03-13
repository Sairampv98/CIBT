suspect_name = "Ravi"
id_no = 1045
is_active = True
threat_level = None

print(suspect_name)
print(id_no)
print(is_active)
print(threat_level)

print(type(suspect_name))
print(type(id_no))
print(type(is_active))
print(type(threat_level))

evidence_count = 5
new_evidence = 3
#f"Ravi-{evidence_count}"
total = evidence_count + new_evidence
print(f"Total evidence : {new_evidence}")

id_string = "1045"
id_number = int(id_string)

print(id_number + 10)
print(id_string + "10")

detective_name = "Sai Ram"
badge_number = 132
is_on_duty = True
print(f"Detective {detective_name} with badge {badge_number} is on duty: {is_on_duty}")

suspects = ["Alex Mercer", "Sarah Connor", 109.99 , "John Doe"]
print("All Suspects:", suspects)
print("Type:", type(suspects))
print("Count:", len(suspects))
first_suspect = suspects[0]
print("First:", first_suspect)
second_suspect = suspects[2]
print("Second:", second_suspect)
print(suspects[3])  # <-- Uncommenting
#append = adding the list
#remove = removing the list
#[1] = "" = updatig the list
suspects.append("Ellen Ripley")
print("After Append:", suspects)
suspects.remove("John Doe")
print("After Remove:", suspects)
suspects[1] = "Sarah Connor-Smith"
print("Updated:", suspects)
subset = suspects[0:2]
print("Subset:", subset)
reversed_suspects = suspects[::-1]
print("Reversed:", reversed_suspects)
evidence_items = ["bottle", "chips", "watch"]
evidence_items.append("clock")
print(evidence_items[2])
print(evidence_items[len(evidence_items)-1])
dictionary = {0:"bottle", 2:"chips", 10:"watch"}
print(dictionary)
your_name = int(input("Enter your name: "))
print(your_name+5)
