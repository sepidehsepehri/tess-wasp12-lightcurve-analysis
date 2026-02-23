# main.py
from preprocessing import download_and_clean_tpf
from bls_analysis import run_bls
from transit_modeling import transit_fit

TARGET = "WASP-12"
SECTORS = [20, 43, 44, 45, 71, 72]

clean_lcs = download_and_clean_tpf(TARGET, SECTORS)

for lc, sector in clean_lcs:
    best_period = run_bls(lc, sector)
    transit_fit(lc, best_period, sector)
