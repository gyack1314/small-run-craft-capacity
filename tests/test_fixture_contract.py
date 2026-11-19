import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]

class FixtureContractTests(unittest.TestCase):
    def test_scenario_is_synthetic_and_well_formed(self):
        data = json.loads((ROOT / 'fixtures/scenario.json').read_text(encoding='utf-8'))
        self.assertTrue(data['synthetic'])
        self.assertEqual(data['schema_version'], 1)
        self.assertEqual(len(data['entities']), len(set(data['entities'])))
        self.assertGreaterEqual(len(data['event_types']), 6)
        self.assertGreaterEqual(len(data['records']), 5)
        self.assertEqual(len({record['event_id'] for record in data['records']}), len(data['records']))
        self.assertTrue(all(record['type'] in data['event_types'] for record in data['records']))
        self.assertIsInstance(data['facts'], dict)

if __name__ == '__main__':
    unittest.main()
