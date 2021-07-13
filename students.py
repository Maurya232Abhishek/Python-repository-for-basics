students={1:{"name":"Pappu","address":"VNS","marks":{"phy":50,"chem":60}},2:{"name":"Dappu","address":"VNS","marks":{"phy":50,"chem":60}}}
student =students.get(1)
print(student)
address=student.get("address")
print(address)
marks=student.get("marks")
print(marks)
phy = marks.get("phy")
print(phy)