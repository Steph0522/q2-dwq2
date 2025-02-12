import tempfile

import skbio

import qiime2

from q2_dwq2 import SingleRecordDNAFASTAFormat


def seq1_factory():
    seq = skbio.DNA("AACCGGTTGGCCAA", metadata={"id": "seq1"})
    return qiime2.Artifact.import_data(
        "SingleDNASequence", seq, view_type=skbio.DNA)


def seq2_factory():
    seq = skbio.DNA("AACCGCTGGCGAA", metadata={"id": "seq2"})
    return qiime2.Artifact.import_data(
        "SingleDNASequence", seq, view_type=skbio.DNA)

def nw_align_example_1(use):
    seq1 = use.init_artifact('seq1', seq1_factory)
    seq2 = use.init_artifact('seq2', seq2_factory)

    msa, = use.action(
        use.UsageAction(plugin_id='dwq2',
                        action_id='nw_align'),
        use.UsageInputs(seq1=seq1, seq2=seq2),
        use.UsageOutputNames(aligned_sequences='msa'),
    )
def align_and_summarize_example_1(use):
    seq1 = use.init_artifact('seq1', seq1_factory)
    seq2 = use.init_artifact('seq2', seq2_factory)

    msa, msa_summary, = use.action(
        use.UsageAction(plugin_id='dwq2',
                        action_id='align_and_summarize'),
        use.UsageInputs(seq1=seq1, seq2=seq2),
        use.UsageOutputNames(aligned_sequences='msa',
                             msa_summary='msa_summary'),
    )


