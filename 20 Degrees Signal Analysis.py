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

twenty_deg_wo_spec = B.get_spectrum('20 Degrees without Target.SPE', calibration = cal.line)
twenty_deg_wo_spec.set_window(0,1.5)
#twenty_deg_wo_spec.plot()

#B.pl.show()
#B.pl.xlabel("Energy [MeV]")

twenty_deg_w_spec = B.get_spectrum('20 Degrees with Target.SPE', calibration = cal.line)
twenty_deg_w_spec.set_window(0,1.5)
#twenty_deg_w_spec.plot()

#B.pl.show()
#B.pl.xlabel("Energy [MeV]")

#Signal Histogram:

twenty_deg_signal = twenty_deg_w_spec - twenty_deg_wo_spec
twenty_deg_signal.set_window(0,1.5)
twenty_deg_signal.plot()

B.pl.show()

B.pl.xlabel("Energy [MeV]")
B.pl.ylabel("Counts [unitless]")
B.pl.title("Signal Histogram: Counts [Unitless] vs Energy [MeV]")

#Analysis:

twenty_deg_signal_1 = twenty_deg_w_spec - twenty_deg_wo_spec
twenty_deg_signal_1.set_window(0.550,0.690)
twenty_deg_signal_1.plot()
twenty_deg_signal_1.fit()
twenty_deg_signal_1.plot_fit()
B.pl.show()

B.pl.xlabel("Energy [MeV]")
B.pl.ylabel("Counts [unitless]")
B.pl.title("Signal Histogram: Counts [Unitless] vs Energy [MeV]")

#Fitting Results:

avg_sig_20 = 0.634256370564
uncer_sig_20 = 0.0383317330836


