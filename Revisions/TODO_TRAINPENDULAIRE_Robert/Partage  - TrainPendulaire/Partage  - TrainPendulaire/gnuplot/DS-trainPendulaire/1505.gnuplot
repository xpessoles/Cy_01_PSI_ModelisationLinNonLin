set table "gnuplot/DS-trainPendulaire/1505.table"; set format "%.5f"
set samples 100.0; plot [x=0:0.04]  10*(0.975e-1-0.975e-1*exp(-983.*x)*cosh(852.*x)-.112*exp(-983.*x)*sinh(852.*x)) 
