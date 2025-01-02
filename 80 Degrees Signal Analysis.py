import LT.box as B
import numpy as np
import scipy as sp

#Calibration Data:

file_name = 'Calibration Linear Analysis.data'
f = B.get_file(file_name)

E = B.get_data(f,'E')
C = B.get_data(f,'C')
dC = B.get_data(f,'dC')

cal = B.linefit(C,E)

#Spectrum for 20 Degrees with and without target:

eighty_deg_wo_spec = B.get_spectrum('80 Degrees without Target.SPE', calibration = cal.line)
eighty_deg_wo_spec.set_window(0,1.5)
#twenty_deg_wo_spec.plot()

#B.pl.show()
#B.pl.xlabel("Energy [MeV]")

eighty_deg_w_spec = B.get_spectrum('80 Degrees with Target.SPE', calibration = cal.line)
eighty_deg_w_spec.set_window(0,1.5)
#twenty_deg_w_spec.plot()

#B.pl.show()
#B.pl.xlabel("Energy [MeV]")

#Signal Histogram:

eighty_deg_signal = eighty_deg_w_spec - eighty_deg_wo_spec
eighty_deg_signal.set_window(0,1.5)
eighty_deg_signal.plot()

B.pl.show()

B.pl.xlabel("Energy [MeV]")
B.pl.ylabel("Counts [unitless]")
B.pl.title("Signal Histogram: Counts [Unitless] vs Energy [MeV]")

#Analysis:

eighty_deg_signal_1 = eighty_deg_w_spec - eighty_deg_wo_spec
eighty_deg_signal_1.set_window(0.220,0.380)
eighty_deg_signal_1.plot()
eighty_deg_signal_1.fit()
eighty_deg_signal_1.plot_fit()
B.pl.show()

B.pl.xlabel("Energy [MeV]")
B.pl.ylabel("Counts [unitless]")
B.pl.title("Signal Histogram: Counts [Unitless] vs Energy [MeV]")

#Fitting Results:

avg_sig_80 = 0.300422304972 
uncer_sig_60 = 0.0349983433044
