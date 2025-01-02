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

fourty_deg_wo_spec = B.get_spectrum('40 Degrees without Target.SPE', calibration = cal.line)
fourty_deg_wo_spec.set_window(0,1.5)
#twenty_deg_wo_spec.plot()

#B.pl.show()
#B.pl.xlabel("Energy [MeV]")

fourty_deg_w_spec = B.get_spectrum('40 Degrees with Target.SPE', calibration = cal.line)
fourty_deg_w_spec.set_window(0,1.5)
#twenty_deg_w_spec.plot()

#B.pl.show()
#B.pl.xlabel("Energy [MeV]")

#Signal Histogram:

fourty_deg_signal = fourty_deg_w_spec - fourty_deg_wo_spec
fourty_deg_signal.set_window(0,1.5)
fourty_deg_signal.plot()

B.pl.show()

B.pl.xlabel("Energy [MeV]")
B.pl.ylabel("Counts [unitless]")
B.pl.title("Signal Histogram: Counts [Unitless] vs Energy [MeV]")

#Analysis:

fourty_deg_signal_1 = fourty_deg_w_spec - fourty_deg_wo_spec
fourty_deg_signal_1.set_window(0.380,0.600)
fourty_deg_signal_1.plot()
fourty_deg_signal_1.fit()
fourty_deg_signal_1.plot_fit()
B.pl.show()

B.pl.xlabel("Energy [MeV]")
B.pl.ylabel("Counts [unitless]")
B.pl.title("Signal Histogram: Counts [Unitless] vs Energy [MeV]")

#Fitting Results:

avg_sig_40 = 0.500792494624
uncer_sig_40 = 0.0509249795527
