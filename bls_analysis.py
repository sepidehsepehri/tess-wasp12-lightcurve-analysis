# bls_analysis.py
from astropy.timeseries import BoxLeastSquares
import matplotlib.pyplot as plt
import numpy as np

def run_bls(lc, sector):
    bls = BoxLeastSquares(lc.time, lc.flux, lc.flux_err)
    periodogram = bls.autopower(0.2)
    best_fit_period = periodogram.period[np.argmax(periodogram.power)]

    plt.figure(figsize=(12,4))
    plt.plot(periodogram.period, periodogram.power, 'k')
    plt.title(f'BLS Periodogram - WASP-12 - Sector {sector}')
    plt.xlabel('Period (days)')
    plt.ylabel('Power')
    plt.show()

    print(f'Best-fit period: {best_fit_period:.4f} days')
    return best_fit_period
