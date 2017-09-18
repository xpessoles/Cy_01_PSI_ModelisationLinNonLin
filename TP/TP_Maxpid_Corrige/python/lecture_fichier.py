import numpy as np
import matplotlib.pyplot as plt

def read_max(file):
    fid = open(file)
    data = fid.readlines()
    fid.close()
    les_t,les_cons,les_pos,les_vol,les_cour,les_w_bras,les_w_mot=[],[],[],[],[],[],[]
    
    for line in data :
        line=line.strip().split("     ")
        try :
            les_t.append(float(line[0])/1000)
            les_cons.append(float(line[1]))
            les_pos.append(float(line[2]))
            les_vol.append(float(line[3]))
            les_cour.append(float(line[4]))
            les_w_bras.append(float(line[5]))
            les_w_mot.append(float(line[6]))
            
        except ValueError :
            e=0
        except IndexError :
            e=0
    return les_t,les_cons,les_pos,les_vol,les_cour,les_w_bras,les_w_mot
        
def read_matlab(file):
    fid = open(file)
    data = fid.readlines()
    fid.close()
    les_t=[]
    les_pos=[]
    for line in data[1:]:
        line = line.split(",")
        les_t.append(float(line[0]))
        les_pos.append(float(line[1]))
    return les_t,les_pos
    
#les_t,les_cons,les_pos,les_vol,les_cour,les_w_bras,les_w_mot=read_max("Ech_10_20_KP_50.Txt")
#les_t,les_cons,les_pos,les_vol,les_cour,les_w_bras,les_w_mot=read_max("Ech_20_90_KP_50.Txt")
#les_t,les_cons,les_pos,les_vol,les_cour,les_w_bras,les_w_mot=read_max("Ech_60_70_KP_50.Txt")

#les_t,les_cons,les_pos,les_vol,les_cour,les_w_bras,les_w_mot=read_max("kp_100_ech_10_20.Txt")
les_t,les_cons,les_pos,les_vol,les_cour,les_w_bras,les_w_mot=read_max("kp_100_ech_60_65.Txt")
#les_t,les_cons,les_pos,les_vol,les_cour,les_w_bras,les_w_mot=read_max("kp_100_ech_10_90.Txt")

f=len(les_t)
if len(les_t)!=len(les_cons):
 
    f=f-(f-len(les_cons))
#les_tm,les_posm = read_matlab("kp_100_ech_10_20_M.txt")
les_tm,les_posm = read_matlab("kp_100_ech_60_65_M.txt")
#les_tm,les_posm = read_matlab("kp_100_ech_10_80_M.txt")
#les_tm,les_posm = read_matlab("kp_100_ech_10_80_M_Sat.txt")
#les_tm,les_posm = read_matlab("kp_100_ech_60_65_M_Sat.txt")
##les_tm,les_posm = read_matlab("K100_60_65_fr.txt")
plt.plot(les_t[0:f],les_cons,'b',label="Position consigne")
plt.plot(les_t[0:f],les_pos,'r.',label="Position mesurée")

ind=0
for val in les_tm:
    if val<1:
        ind=ind+1

les_tm = [k-1 for k in les_tm]
les_posm = [k for k in les_posm]

plt.plot(les_tm[ind:],les_posm[ind:],'k',label="Position simulée")

plt.grid()
plt.legend()
plt.show()