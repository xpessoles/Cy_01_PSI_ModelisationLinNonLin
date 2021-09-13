set table "gnuplot/DS-trainPendulaire/5.table"; set format "%.5f"
set samples 100.0; plot [x=0:2]  0.1*(1.-0.400e-1*exp(-532.*x)+0.588e-1*exp(-439.*x)-1.02*exp(-4.48*x)) 
