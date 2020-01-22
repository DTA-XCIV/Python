from sys import argv

script, een1, twee2, drie3, vier4, vijf5 = argv

def tellen_tot_vijf(*args):
    args1, args2, args3, args4, args5 = args
    print(f"Tellen tot tien:\n{args1},{args2},{args3},{args4},{args5}\n")
# 1 gewoon integers meegeven
tellen_tot_vijf(1,2,3,4,5)

# 2 cijfers onder een variabelen zetten en die vervolgens meegeven
een = 1
twee = 2
drie = 3
vier = 4
vijf = 5

tellen_tot_vijf(een, twee, drie, vier, vijf)

#3 strings meegeven
tellen_tot_vijf("een","twee","drie","vier","vijf")

#4 wiskunde
tellen_tot_vijf(0+1, 1+1, 1+2, 1+3, 1+4)

#5 met format
een = "{}"
twee = "{}"
drie = "{}"
vier = "{}"
vijf = "{}"

tellen_tot_vijf(een.format(1), twee.format(2), drie.format(3), vier.format(4), vijf.format(5))

#6 vanuit argv
tellen_tot_vijf(een1, twee2, drie3, vier4, vijf5)

#7 met user-input
print("We're counting to ten!: ")
i1 = input("First number >")
i2 = input("Second number >")
i3 = input("Third number >")
i4 = input("Fourth number >")
i5 = input("Fifth number >")
tellen_tot_vijf(i1, i2, i3, i4, i5)

#8 function voor een function
def vijf(een, twee, drie, vier, vijf):
    tellen_tot_vijf(een, twee, drie, vier, vijf)

vijf(1,2,3,4,5)

#9 Enkel een input als scriptpauze
print("Wil je tot tien tellen? Druk op RETURN.")
input()
tellen_tot_vijf(1,2,3,4,5)

#10 function loop? zolang mogelijk
def five(e1e, t2t, d3d, v4v, v5v):
    tellen_tot_vijf(e1e, t2t, d3d, v4v, v5v)

e1 = "{}"
t2 = "{}"
d3 = "{}"
v4 = "{}"
v5 = "{}"

print("Geef eens wat cijfers mee:")
e1 = 0 + int(e1.format(input("Een: ")))
t2 = 5 - int(t2.format(input("Twee: "))) - 1
d3 = 34 + int(d3.format(input("Drie: "))) - 34
v4 = -2 + int(v4.format(input("Vier: "))) + 2
v5 = 0 + int(v5.format(input("Vijf: ")))

five(e1, t2, d3, v4, v5)
