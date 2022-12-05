import pandas as pd
import scikit_allel_wrapper as allel_wrapper

def create_statistics_data_frame(vcf_dict, windowSize):
    """creates the dataframe of statistics

    Args:
        vcf_dict (_type_): _description_
        windowSize (_type_): _description_

    Returns:
        _type_: pandas DataFrame
    """

    pi, windows, n_bases, counts = allel_wrapper.calculate_windowed_pi(vcf_dict, windowSize)
    h1, h12, h123, h2_h1, windows, counts = allel_wrapper.calculate_windowed_garud_h(vcf_dict, windowSize, windows)
    d, windows, counts = allel_wrapper.calculate_windowed_tajima_d(vcf_dict, windowSize, windows)
    theta_hat_w, windows, n_bases, counts = allel_wrapper.calculate_windowed_watterson_theta(vcf_dict, windowSize, windows)

    d = { 'Pi': pi, 'h1': h1, 'h12': h12, 'h123': h123, 'h2_h1': h2_h1, 'tajima_d': d, 'watterson_theta': theta_hat_w }

    df = pd.DataFrame(data=d)

    return df

def create_statistics_csv(vcf_file, windowSize, output):
    """creates the statistics csv

    Args:
        vcf_dict (_type_): _description_
        windowSize (_type_): _description_
        output (_type_): _description_
    """
    vcf_dict = allel_wrapper.read_vcf(vcf_file)
    df = create_statistics_data_frame(vcf_dict, windowSize)
    df.to_csv(output)