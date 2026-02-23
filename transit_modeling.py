# transit_modeling.py
import matplotlib.pyplot as plt
from batman import TransitModel, TransitParams

def transit_fit(lc, best_fit_period, sector):
    params = TransitParams()
    params.t0 = lc.time.jd.min()
    params.per = best_fit_period
    params.rp = 0.1
    params.a = 15
    params.inc = 87
    params.ecc = 0.
    params.w = 90
    params.u = [0.1]
    params.limb_dark = "linear"

    model = TransitModel(params, lc.time.jd)
    transit_model = model.light_curve(params)

    plt.figure(figsize=(12,4))
    plt.scatter(lc.time.jd % best_fit_period, lc.flux, c='k', s=0.5)
    plt.plot(lc.time.jd % best_fit_period, transit_model, 'r', label='Transit Model')
    plt.title(f'Transit Fit - WASP-12 - Sector {sector}')
    plt.xlabel('Phase (days)')
    plt.ylabel('Flux')
    plt.legend()
    plt.show()
