import itertools as it
import json
import math


#何発で乱数何%かを返す。
def damagerate(rnd, hp=0):
	if hp == 0:
		return None
	else:
		if max(rnd) >= hp:
			ro = sum(i >= hp for i in rnd)
			return 1, ro/16 * 100
			
		for i in range(2, 6):
			da = list(it.product(rnd,repeat=i))
			for n, co in enumerate(da):
				da[n] = sum(co)
			if max(da) >= hp:
				rn = sum(i >= hp for i in da)
				return i, rn* 100 /len(da)
		return 6
		

#タイプ
ls = []
with open('./data/type.txt', 'r', encoding='utf-8') as f:
	for i in f.readlines():
		ls.append(i.rstrip('\n'))

typetuple = tuple(ls)


#タイプ相性を返す関数
def type_effectiveness(atk, dff, dfs=None):
	
	atk_type_num = int(typetuple.index(atk))
	dff_type_num = int(typetuple.index(dff))
	
	with open('./data/type_effectiveness.txt', 'r', encoding='utf-8') as g:
		sorce = g.readlines()[atk_type_num]
		effectdata = sorce.rstrip('\n').split('/')
	
	effect_dff = effectdata[dff_type_num]
	effect_dfs = 2
	
	if bool(dfs) == True:
	    dfs_type_num = int(typetuple.index(dfs))
	    effect_dfs = effectdata[dfs_type_num]
	
	effectf = int(effect_dff) * int(effect_dfs)
	effect = effectf / 4
	return effect
	

#技名からタイプと分類と威力を返す
def movefind(move):
	with open('./data/moves_data.json', 'r') as f:
		data = json.load(f)
	type = data[move]['type']
	power = data[move]['power']
	cat = data[move]['cat']
	return type, power, cat
	

def myround(val):
	return (val*2+1)//2
	
#相手の実数値、自分のレベル、タイプ、実数値、技のタイプ、威力、補正からダメージのリストを返す
def damage(atklv, atkstts, defstts, movepwr, rev):
	base = math.floor(math.floor(math.floor(atklv*2/5+2)*movepwr*atkstts/defstts)/50+2)
	
	for i in range(4):
		base = myround(base*rev[i]-0.1)
	
	randamage = []
	for i in range(85, 101):
		randamage.append(math.floor(base*i/100))
	
	result = []
	for i in randamage:
		i = math.floor(myround(myround(myround(math.floor(myround(i * rev[4] -0.1) * rev[5]) * rev[6] -0.1) * rev[7] -0.1) * rev[8] -0.1))
		result.append(i)
		
	return result
	