import hashlib,json,pathlib,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]

class SourceIntegrityTests(unittest.TestCase):
    def test_source_bytes_and_observation_keys(self):
        manifest=json.loads((ROOT/'fixtures/manifest.json').read_text(encoding='utf-8'))
        for source in manifest['tables']:
            with self.subTest(file=source['file']):
                raw=(ROOT/source['file']).read_bytes()
                self.assertEqual(hashlib.sha256(raw).hexdigest(),source['sha256'])
                rows=[json.loads(line) for line in raw.decode().splitlines()]
                self.assertEqual(len(rows),source['rows'])
                self.assertEqual(len(rows),len({row['row_id'] for row in rows}))
                self.assertTrue(all(set(row).issubset(source['columns']) for row in rows))
    def test_policies_and_case_materials_are_present(self):
        p=json.loads((ROOT/'fixtures/policies.json').read_text(encoding='utf-8'))
        self.assertTrue(p)
        m=json.loads((ROOT/'fixtures/manifest.json').read_text(encoding='utf-8'))
        self.assertTrue(m['synthetic'])
        self.assertTrue(m['tables'])
        self.assertTrue(all(t['rows']>0 for t in m['tables']))

if __name__=='__main__':unittest.main()
