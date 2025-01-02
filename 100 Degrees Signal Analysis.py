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

hundred_deg_wo_spec = B.get_spectrum('100 Degrees without Target.SPE', calibration = cal.line)
hundred_deg_wo_spec.set_window(0,1.5)
#twenty_deg_wo_spec.plot()

#B.pl.show()
#B.pl.xlabel("Energy [MeV]")

hundred_deg_w_spec = B.get_spectrum('100 Degrees with Target.SPE', calibration = cal.line)
hundred_deg_w_spec.set_window(0,1.5)
#twenty_deg_w_spec.plot()

#B.pl.show()
#B.pl.xlabel("Energy [MeV]")

#Signal Histogram:

hundred_deg_signal = hundred_deg_w_spec - hundred_deg_wo_spec
hundred_deg_signal.set_window(0,1.5)
hundred_deg_signal.plot()

B.pl.show()

B.pl.xlabel("Energy [MeV]")
B.pl.ylabel("Counts [unitless]")
B.pl.title("Signal Histogram: Counts [Unitless] vs Energy [MeV]")

#Analysis:

hundred_deg_signal_1 = hundred_deg_w_spec - hundred_deg_wo_spec
hundred_deg_signal_1.set_window(0.165,0.300)
hundred_deg_signal_1.plot()
hundred_deg_signal_1.fit()
hundred_deg_signal_1.plot_fit()
B.pl.show()

B.pl.xlabel("Energy [MeV]")
B.pl.ylabel("Counts [unitless]")
B.pl.title("Signal Histogram: Counts [Unitless] vs Energy [MeV]")

#Fitting Results:

avg_sig_100 = 0.235189291938
uncer_sig_100 = 0.0280944894092

