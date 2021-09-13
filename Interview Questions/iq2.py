"""
There can be 3 types of floors in a building: Residential(R), cafeteria(C), official(O).
Given the number of floors, return the total possible number of ways to create a building
according to the owner’s wishes.
Wishes: 1) There cannot be more than one cafeteria in the entire building
2) There can not be more than 2 consecutive official floors in the entire building.
 Since the answer can be long, modulo it 10^9+7.
Constraints: 1<=f<=10^5
I/P: 2
O/P: 8
Explanation: Possible ways are RR,RO,OR,RC,CR,OC,CO,OO
O/P: 19
I/P: 3
"""
