indian_states = ["Kerala", "MP", "UP"]
print(indian_states)

# access list element
print(indian_states[0])
print(indian_states[-1])

indian_states[1] = "Madhya Pradesh"
print(indian_states[1])

indian_states.append("Rajasthan")
print(indian_states)

other_states = ["Delhi", "Punjab", "Gujarat"]
indian_states.extend(["Delhi", "Punjab", "Gujarat"])

print(indian_states)
