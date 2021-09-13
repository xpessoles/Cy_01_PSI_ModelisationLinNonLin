set table "gnuplot/DS-trainPendulaire/3.table"; set format "%.5f"
set samples 100.0; plot [x=0:0.04]  10*(0.952e-1-0.952e-1*exp(-123.*x)*cos(328.*x)-0.356e-1*exp(-123.*x)*sin(328.*x)) 
