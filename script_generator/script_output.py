from uuid import uuid4


def finish_simulation(filepath: str, population: str):
    """
    Finish simulation

    Args:
        filepath (str): filepath to output to, default: ./{uuid4}
    """
    sample_size = 20  # sample size for sampleIndividuals
    return "10000 late() {" \
        f"g = {population}.sampleIndividuals({sample_size}).genomes" \
        f"g.outputVCF(filePath=\"runs/{filepath or uuid4()}\", simplifyNucleotides=T);" \
        "sim.simulationFinished();}"
