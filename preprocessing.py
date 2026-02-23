# preprocessing.py
import lightkurve as lk

def download_and_clean_tpf(target="WASP-12", sectors=None):
    """
    Download TESS Target Pixel Files for target and specified sectors,
    extract light curves, remove NaNs, outliers and flatten.
    """
    if sectors is None:
        sectors = []

    tpf_list = []
    for sector in sectors:
        tpf_search_result = lk.search_targetpixelfile(target, mission="TESS", sector=sector)
        tpf_list.append(tpf_search_result.download())

    tpf_collection = lk.TargetPixelFileCollection(tpf_list)
    clean_lcs = []

    for tpf in tpf_collection:
        lc = tpf.to_lightcurve(aperture_mask='pipeline')
        lc_clean = lc.remove_nans().remove_outliers().flatten(window_length=401)
        clean_lcs.append((lc_clean, tpf.sector))

    return clean_lcs
