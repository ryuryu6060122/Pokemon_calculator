
#種族値、個体値、努力値、レベル、性格からステータスを計算する
#結果はとりあえずHABCDSのリストで返す。
#Bs,Iv,Ntは[h,a,b,c,d,s]

import math
import json

def stats_calculate(Bs, Iv, Ev, Lv, Nt):
	if not bool(Nt):
		return []
	stats = []
	H = math.floor((Bs[0]*2 +Iv[0] +Ev[0]/4)*Lv/100 +Lv +10)
	stats.append(H)
	for i in range(1,6):
		abcds = math.floor(((Bs[i]*2 +Iv[i] +Ev[i]/4)*Lv/100 +5)*Nt[i-1])
		stats.append(abcds)
	if Bs[0]==1:
		stats[0]=1
	return  stats

#ポケモン名から種族値を返す
def Bsfind(name):
	with open('./data/pokemon_data.json', 'r') as f:
		data = json.load(f)
	try:
		bs = data[name]['stats']
	except KeyError:
		return [0,0,0,0,0,0]
	else:
		return bs

#性格から補正のリストを返す
def Ntfind(nature):
	with open ('./data/nature_data.json', 'r') as f:
		data = json.load(f)
	try:
		nt = data[nature]
	except KeyError:
		return []
	else:
		return nt
