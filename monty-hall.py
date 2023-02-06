import random

# creating doors

doors=[0,0,1]

# creating list for result

result = []

# monty choosing doors without avoiding

def monty_door_random(doors, alice_door, prize_door):
    monty_door = random.choice(doors)
    return monty_door

# monty choosing doors avoiding the prize and alice's door

def monty_door_avoid_both(doors, alice_door, prize_door):
    candidates = list(set(doors) - {prize_door, alice_door})
    monty_door = random.choice(candidates)
    return monty_door

# monty-hall simulation
for i in range(100000):
    # shuffling the door
    random.shuffle(doors)
    # alice choosing random door
    alice_door = random.choice(doors)
    # choosing monty door to open (avoid alice's door,prize door)
    monty_door = monty_door_avoid_both(doors, alice_door, prize_door)
    # changing door selection by alice
    changed_doors = set(doors) - {alice_door} - {monty_door}
    # opening the result
    result.append(random.choice(list(changed_doors)) == 1)
    #if i % 1000 == 0:
    #    print(i * 1000)

# print(result)

print("Probability of getting prize when Monty chooses the door avoiding both Alice and Prize?\n %f" % (float(sum(result))/len(result)))
print("you should change your choice in monty-hall problem!!")


