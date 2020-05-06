'''
Integer right triangles

If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''
#right angle triangle:
#a + b + sqrt(a**2 + b**2)  =  p

#tu sta še vedno dve spremenljivki glede na p, to sta a in b
#nevem kako bi se ene znebil, tako da bom se zapeljal po vseh moznostih

def stevilo_resitev(p): #p = 1000
	resitve = 0
	for a in range(1, p // 2): #najdaljsa mozna stranica = 499
		for b in range(a, p // 2): #vsi mozni a in b,   a <= b
			c = p - a - b
            #zdaj imamo a in b in c.
            #ali je zdaj c najdaljsa? lahko bi biu tudi b
			if a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2:
				resitve += 1
	return resitve

x = 1001
najvec = max(range(1, x), key=stevilo_resitev)
#840