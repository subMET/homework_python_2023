names = ['Name1','Name2','Name3']
salary = [100,200,150]
premium = ['1.5%','2.0%','0.5%']

dict_gen = {item[0]:round(item[1]*(1+float(str(item[2]).replace('%',''))/100),2) for item in zip(names, salary, premium)}

for i in dict_gen.keys():
    print(f'{i} - {dict_gen.get(i):>8} у.е.')