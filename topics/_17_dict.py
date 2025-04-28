# Dictionary : a collection of {key:value} pairs
#              ordered and changeable. NO Duplicates

states_capital = {"TamilNadu": "Chennai",
                  "Karnataka": "Bangalore",
                  "Kerala": "Trivandrum"}

print(states_capital)
print(states_capital.get("TamilNadu"))

states_capital.update({"UP": "Lucknow"})
state = "MP"
print(states_capital.get(state))
if states_capital.get(state):
    print(states_capital.get(state))
else:
    print(f"{state} state not available in dict")

states_capital.pop("UP")
states_capital.popitem()
# states_capital.clear()

for states in states_capital:
    print(states)

keys = states_capital.keys()
print(keys)

for key in keys:
    print(key)

print(states_capital.values())

for val in states_capital.values():
    print(val)

items = states_capital.items()  # [(),(),()]
print(items)

for k, v in states_capital.items():
    print(f"{k} : {v}")
