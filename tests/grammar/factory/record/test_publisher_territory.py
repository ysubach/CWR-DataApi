# -*- coding: utf-8 -*-
import unittest

from data.accessor import CWRConfiguration
from cwr.grammar.factory.field import DefaultFieldFactory
from data.accessor import CWRTables
from cwr.grammar.factory.record import PrefixBuilder, RecordFactory


"""
CWR Publisher Territory of Control (SPT) grammar tests.

The following cases are tested:
"""

__author__ = 'Bernardo Martínez Garrido'
__license__ = 'MIT'
__version__ = '0.0.0'
__status__ = 'Development'


class TestNPNGrammar(unittest.TestCase):
    """
    Tests that the NPN grammar decodes correctly formatted strings
    """

    def setUp(self):
        _config = CWRConfiguration()

        _data = _config.load_field_config('table')
        _data.update(_config.load_field_config('common'))

        _factory_field = DefaultFieldFactory(_data, CWRTables())

        _prefixer = PrefixBuilder(_config.record_types())
        _factory_record = RecordFactory(_config.load_record_config('common'), _prefixer, _factory_field)

        self.grammar = _factory_record.get_transaction_record('publisher_territory')

    def test_valid_common(self):
        """
        Tests that Publisher Territory of Control grammar decodes correctly formatted record prefixes.

        This test contains all the optional fields.
        """
        record = 'SPT000001790000054770             013330133301333I0484Y001'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('SPT', result.record_type)
        self.assertEqual(179, result.transaction_sequence_n)
        self.assertEqual(547, result.record_sequence_n)
        self.assertEqual('70', result.ip_n)
        self.assertEqual(13.33, result.pr_collection_share)
        self.assertEqual(13.33, result.mr_collection_share)
        self.assertEqual(13.33, result.sr_collection_share)
        self.assertEqual('I', result.inclusion_exclusion_indicator)
        self.assertEqual(484, result.tis_numeric_code)
        self.assertEqual(True, result.shares_change)
        self.assertEqual(1, result.sequence_n)

    def test_valid_full(self):
        """
        Tests that Publisher Territory of Control grammar decodes correctly formatted record prefixes.

        This test contains all the optional fields.
        """
        record = 'SPT0000123400000023A12345678      010120500002520I0008Y012'

        result = self.grammar.parseString(record)[0]

        self.assertEqual('SPT', result.record_type)
        self.assertEqual(1234, result.transaction_sequence_n)
        self.assertEqual(23, result.record_sequence_n)
        self.assertEqual('A12345678', result.ip_n)
        self.assertEqual(10.12, result.pr_collection_share)
        self.assertEqual(50, result.mr_collection_share)
        self.assertEqual(25.2, result.sr_collection_share)
        self.assertEqual('I', result.inclusion_exclusion_indicator)
        self.assertEqual(8, result.tis_numeric_code)
        self.assertEqual(True, result.shares_change)
        self.assertEqual(12, result.sequence_n)