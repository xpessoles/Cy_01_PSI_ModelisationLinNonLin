set table "gnuplot/4.table"; set format "%.5f"
set samples 50.0; set parametric; plot [t=-2:2] [] [] log10(10**t),-180/3.1415957*atan(0.3*10**t)
