set table "gnuplot/DS-trainPendulaire/1.table"; set format "%.5f"
set samples 100.0; plot [x=0:0.04]  10*(0.975e-1-0.974e-1*exp(-492.*x)*cosh(40.3*x)-1.19*exp(-492.*x)*sinh(40.3*x)) 
