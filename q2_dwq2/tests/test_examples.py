from qiime2.plugin.testing import TestPluginBase


class UsageExampleTests(TestPluginBase):
    package = 'q2_dwq2.tests'

    def test_examples(self):
        self.execute_examples()
