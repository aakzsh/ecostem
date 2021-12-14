


def calc(area, animals, tractors, tractor_type, fert_type, years, rotation):
    
    emissions = 0
    emissions+= animals*773.391273
    if tractor_type=='a':
        emissions+=tractors* (20000/6) * 9 * 3.78 * 0.001
    elif tractor_type=='b':
        emissions+=tractors* (20000/6) * 11 * 3.78 * 0.001
    else:
        pass
    emissions2=0
    if fert_type=='b':
        emissions2+=area*(0.28/25)*2
    emissions2+=float(years)*0.5*float(area)
    if rotation=='a':
        emissions+=0.65*emissions2
    elif rotation=='b':
        emissions+=0.75*emissions2
    elif rotation=='c':
        emissions+=0.90*emissions2

    return emissions

# print("enter area of land in metres")
# area = int(input())

# emissions = 0

# print("How many dairy animals do you own?")
# animals = int(input())

# emissions+= animals*773.391273

# print("how many tractors do you have?")
# tractors = int(input())

# print("1. petrol\n2. diesel\n3. none?")
# type = int(input())

# if type==1:
#     emissions+=tractors* (20000/6) * 9 * 3.78 * 0.001
# elif type==2:
#     emissions+=tractors* (20000/6) * 11 * 3.78 * 0.001
# else:
#     pass

# emissions2 = 0

# print("do you use fertilizers? y/n")

# s = input()
# if s=='y':
#     print("what kinda? \n1: organic\n2: inorganic")
#     type_fert = int(input())
#     if type_fert!=1:
#         emissions2+=area*(0.28/25)*2
    
# print("whats the age of your soil? in yrs")

# years = int(input())
# emissions2+=years*0.5*area

# print("what kinda crop rotation do you follow?\n1: extensive\n2: medium\n3: rare\n4: none")
# rotation = int(input())

# if rotation==1:
#     emissions+=0.65*emissions2
# elif rotation==2:
#     emissions+=0.75*emissions2
# elif rotation==3:
#     emissions+=0.90*emissions2
    
# print(f'Your carbon footprint is around {round(emissions,2)} tonnes per year')
    
    
    
    