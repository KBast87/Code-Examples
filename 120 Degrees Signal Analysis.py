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

hundredtwenty_deg_wo_spec = B.get_spectrum('120 Degrees without Target.SPE', calibration = cal.line)
hundredtwenty_deg_wo_spec.set_window(0,1.5)
#twenty_deg_wo_spec.plot()

#B.pl.show()
#B.pl.xlabel("Energy [MeV]")

hundredtwenty_deg_w_spec = B.get_spectrum('120 Degrees with Target.SPE', calibration = cal.line)
hundredtwenty_deg_w_spec.set_window(0,1.5)
#twenty_deg_w_spec.plot()

#B.pl.show()
#B.pl.xlabel("Energy [MeV]")

#Signal Histogram:

hundredtwenty_deg_signal = hundredtwenty_deg_w_spec - hundredtwenty_deg_wo_spec
hundredtwenty_deg_signal.set_window(0,1.5)
hundredtwenty_deg_signal.plot()

B.pl.show()

#Analysis:

hundredtwenty_deg_signal_1 = hundredtwenty_deg_w_spec - hundredtwenty_deg_wo_spec
hundredtwenty_deg_signal_1.set_window(0.04,0.10)
hundredtwenty_deg_signal_1.plot()
hundredtwenty_deg_signal_1.fit()
hundredtwenty_deg_signal_1.plot_fit()
B.pl.show()

B.pl.xlabel("Energy [MeV]")
B.pl.ylabel("Counts [unitless]")
B.pl.title("Signal Histogram: Counts [Unitless] vs Energy [MeV]")

#Fitting Results:

avg_sig_120 = 0.0640157453718
uncer_sig_120 = 0.0106867697174 
 


