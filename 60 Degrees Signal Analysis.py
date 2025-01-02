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

sixty_deg_wo_spec = B.get_spectrum('60 Degrees without Target.SPE', calibration = cal.line)
sixty_deg_wo_spec.set_window(0,1.5)
#twenty_deg_wo_spec.plot()

#B.pl.show()
#B.pl.xlabel("Energy [MeV]")

sixty_deg_w_spec = B.get_spectrum('60 Degrees with Target.SPE', calibration = cal.line)
sixty_deg_w_spec.set_window(0,1.5)
#twenty_deg_w_spec.plot()

#B.pl.show()
#B.pl.xlabel("Energy [MeV]")

#Signal Histogram:

sixty_deg_signal = sixty_deg_w_spec - sixty_deg_wo_spec
sixty_deg_signal.set_window(0,1.5)
sixty_deg_signal.plot()

B.pl.show()

B.pl.xlabel("Energy [MeV]")
B.pl.ylabel("Counts [unitless]")
B.pl.title("Signal Histogram: Counts [Unitless] vs Energy [MeV]")

#Analysis:

sixty_deg_signal_1 = sixty_deg_w_spec - sixty_deg_wo_spec
sixty_deg_signal_1.set_window(0.300,0.500)
sixty_deg_signal_1.plot()
sixty_deg_signal_1.fit()
sixty_deg_signal_1.plot_fit()
B.pl.show()

B.pl.xlabel("Energy [MeV]")
B.pl.ylabel("Counts [unitless]")
B.pl.title("Signal Histogram: Counts [Unitless] vs Energy [MeV]")

#Fitting Results:

avg_sig_60 = 0.392795975053
uncer_sig_60 = 0.0476882682715

