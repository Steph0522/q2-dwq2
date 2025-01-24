from skbio import DNA

from qiime2.plugin.testing import TestPluginBase

from q2_dwq2 import SingleRecordDNAFASTAFormat


class SingleDNASequenceTransformerTests(TestPluginBase):
    package = 'q2_dwq2.tests'

    def test_DNA_to_single_record_fasta_simple1(self):
        in_ = DNA('ACCGGTGGAACCGGTAACACCCAC',
                  metadata={'id': 'example-sequence-1', 'description': ''})
        tx = self.get_transformer(DNA, SingleRecordDNAFASTAFormat)

        observed = tx(in_)
        # confirm "round-trip" of DNA -> SingleRecordDNAFASTAFormat -> DNA
        # results in an observed sequence that is the same as the starting
        # sequence
        self.assertEqual(observed.view(DNA), in_)

    def test_DNA_to_single_record_fasta_simple2(self):
        in_ = DNA('ACCGGTAACCGGTTAACACCCAC',
                  metadata={'id': 'example-sequence-2', 'description': ''})
        tx = self.get_transformer(DNA, SingleRecordDNAFASTAFormat)

        observed = tx(in_)
        self.assertEqual(observed.view(DNA), in_)
