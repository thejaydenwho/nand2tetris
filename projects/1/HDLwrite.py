def sixteenbit_gen(function_name):
    with open("generated.txt", "w") as file:
        if function_name == "Not":
            for n in range(16):
                file.write(f"{function_name}(in=in[{n}], out=out[{n}]);\n")

        elif function_name == "And":
            for n in range(16):
                file.write(f"{function_name}(a=a[{n}], b=b[{n}], out=out[{n}]);\n")

        elif function_name == "Or":
            for n in range(16):
                file.write(f"{function_name}(a=a[{n}], b=b[{n}], out=out[{n}]);\n")

        elif function_name == "Mux":
            for n in range(16):
                file.write(f"{function_name}(a=a[{n}], b=b[{n}], sel=sel, out=out[{n}]);\n")

def mux4way16_gen():
    with open("generated.txt", "w") as file:
        for n in range(16):
            file.write(f"Mux4Way(a=a[{n}], b=b[{n}], c=c[{n}], d=d[{n}], sel=sel, out=out[{n}]);\n")

mux4way16_gen()