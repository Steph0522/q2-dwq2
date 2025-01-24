from skbio import DNA

from q2_dwq2 import SingleRecordDNAFASTAFormat

from .plugin_setup import plugin


# Define and register transformers
@plugin.register_transformer
def _1(ff: SingleRecordDNAFASTAFormat) -> DNA:
    # by default, DNA.read will read the first sequence in the file
    with ff.open() as fh:
        return DNA.read(fh)
@plugin.register_transformer
def _2(seq: DNA) -> SingleRecordDNAFASTAFormat:
    ff = SingleRecordDNAFASTAFormat()
    seq.write(str(ff.path))
    return ff
