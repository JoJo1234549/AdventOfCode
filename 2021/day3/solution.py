with open("input.txt") as f:
    _input = f.read().split("\n")

def den(binary):
    return int(str(binary), base = 2)

## Part 1 ##

gamma = ""
epsilon = ""

for index, bit in enumerate(_input[0]):
    zero, one = 0, 0
    for item in _input:
        if item[index] == "0":
            zero += 1
        elif item[index] == "1":
            one += 1
    if zero >= one:
        gamma += "0"
        epsilon += "1"
    elif zero <= one:
        gamma += "1"
        epsilon += "0"

print(f"Gamma: {gamma} = {den(gamma)}\nEpsilon: {epsilon} = {den(epsilon)}")

print(f"Power consumption is {den(gamma) * den(epsilon)}")

### Part 2 ###

def find_oxy(oxy, pos = 0):
    oxy_filtered = []
    zero, one = 0, 0
    if len(oxy) == 1:
        return oxy[0]
    for item in oxy:
        if item[pos] == "0":
            zero += 1
        elif item[pos] == "1":
            one += 1
    if one >= zero:
        for i in oxy:
            if str(i)[pos] == "1":
                oxy_filtered.append(i)
        return find_oxy(oxy_filtered, pos + 1)
    elif one <= zero:
        for i in oxy:
            if str(i)[pos] == "0":
                oxy_filtered.append(i)
        return find_oxy(oxy_filtered, pos + 1)
    elif one == zero:
        for i in oxy:
            if str(i)[pos] == "1":
                return i

def find_co2(co2, pos = 0):
    co2_filtered = []
    zero, one = 0, 0
    if len(co2) == 1:
        return co2[0]
    for item in co2:
        if item[pos] == "0":
            zero += 1
        elif item[pos] == "1":
            one += 1
    if one >= zero:
        for i in co2:
            if str(i)[pos] == "0":
                co2_filtered.append(i)
        return find_co2(co2_filtered, pos + 1)
    elif one <= zero:
        for i in co2:
            if str(i)[pos] == "1":
                co2_filtered.append(i)
        return find_co2(co2_filtered, pos + 1)
    elif one == zero:
        for i in co2:
            if str(i)[pos] == "0":
                return i

print(f"Oxygen generator rating: {find_oxy(_input)} = {den(find_oxy(_input))}\nCO2 scrubber rating: {find_co2(_input)} = {den(find_co2(_input))}")

print(f"Lift support rating is {den(find_oxy(_input)) * den(find_co2(_input))}")

input()