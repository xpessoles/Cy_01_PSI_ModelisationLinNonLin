set table "gnuplot/DS-trainPendulaire/2.table"; set format "%.5f"
set samples 100.0; plot [x=0:0.04]  10*(0.952e-1-0.954e-1*exp(-246.*x)*cos(250.*x)-0.938e-1*exp(-246.*x)*sin(250.*x)) 
