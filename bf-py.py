import sys, re

if len(sys.argv) < 2:
    print("Please input filename.")
    exit(1)
elif len(sys.argv) > 2:
    print("Too many argument.")
    exit(1)

try:
    file = open(sys.argv[1], "r")
except FileNotFoundError:
    print("File not found.")
    exit(1)

program = ""

for line in file.readlines():
    program += line

program = re.sub(r"[^+\-><.,[\]]", "", program)

MEMSIZE = 30000

loops = []
stack = []

for i in range(len(program)):
    el = program[i]

    if el == "[":
        stack.append(i)
    elif el == "]":
        if len(stack) == 0:
            print("Error!\nLoop brackets didn't match.")
            sys.exit(1)
        else:
            loops.append([stack[-1], i])
            stack.pop()
    
if len(stack) != 0:
    print("Error!\nLoop brackets didn't match.")
    sys.exit(1)

memory = [0] * MEMSIZE
pointer = 0
i = 0

while True:
    code = program[i]

    if code == "+":
        memory[pointer] += 1

        if memory[pointer] == 256:
            memory[pointer] = 0
    elif code == "-":
        memory[pointer] -= 1

        if memory[pointer] == -1:
            memory[pointer] = 255
    elif code == ">":
        pointer += 1
        
        if pointer == MEMSIZE:
            print("Error!\nOut of the memory!")
            sys.exit(1)
    elif code == "<":
        pointer -= 1

        if pointer == -1:
            print("Error!\nOut of the memory!")
            sys.exit(1)
    elif code == ".":
        print(chr(memory[pointer]), end="")
    elif code == ",":
        memory[pointer] = ord(sys.stdin.readline(1))
    elif code == "[":
        if memory[pointer] == 0:
            for loop in loops:
                if loop[0] == i:
                    i = loop[1] - 1
                    break
    elif code == "]":
        if memory[pointer] != 0:
            for loop in loops:
                if loop[1] == i:
                    i = loop[0] - 1
                    break
    
    i += 1
    
    if i == len(program):
        sys.exit(0)
