# SPDX-License-Identifier: GPL-3.0-or-later
"""The labelled BAC column must never be confused with the national rank."""

import importlib.util
import json
from pathlib import Path
import unittest


SOURCE = Path(__file__).resolve().parents[1] / "date_istorice" / "generare_bac_din_bacplus.py"
spec = importlib.util.spec_from_file_location("bac_generator", SOURCE)
bac = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bac)

TABLE = """<h1>Colegiul Demo</h1><table><thead><tr>
<th></th><th>Medie Admitere</th><th>Medie Bac</th>
<th>Poziție Națională Bac</th><th>Elevi Bac</th><th>Rată de promovare</th>
</tr></thead><tbody>
<tr><td>2026</td><td>9,57</td><td>9,51</td><td>2</td><td>269</td><td><div>99,6%</div></td></tr>
<tr><td>2019</td><td></td><td>9,29</td><td>7</td><td>273</td><td>100%</td></tr>
</tbody></table>"""


class BacTableTests(unittest.TestCase):
    def test_published_dataset_coverage_ranges_and_sources(self):
        directory = SOURCE.parent
        records = json.loads((directory / "bac_istoric_licee.json").read_text())
        source = json.loads((directory / "bac_provenienta.json").read_text())
        self.assertEqual(len(records), 82)
        self.assertEqual(set(records), set(source["schools"]))
        self.assertEqual(sum(map(len, records.values())), 738)
        for school, years in records.items():
            self.assertEqual(set(years), {str(year) for year in bac.YEARS})
            self.assertTrue(source["schools"][school].startswith("https://www.plusedu.ro/i/"))
            for result in years.values():
                self.assertEqual(set(result), {"medie_bac", "promovare_%"})
                self.assertTrue(0 <= float(result["medie_bac"]) <= 10)
                self.assertTrue(0 <= float(result["promovare_%"]) <= 100)

    def test_average_is_selected_by_heading_even_when_rank_is_small(self):
        data = bac.extract(TABLE, "COLEGIUL DEMO")
        self.assertEqual(data["2026"], {"medie_bac": "9.51", "promovare_%": "99.6"})
        self.assertEqual(data["2019"], {"medie_bac": "9.29", "promovare_%": "100"})

    def test_rejects_wrong_school_and_changed_table_schema(self):
        with self.assertRaisesRegex(ValueError, "title"):
            bac.extract(TABLE, "ALT LICEU")
        with self.assertRaisesRegex(ValueError, "headings"):
            bac.extract(TABLE.replace("Medie Bac", "Scor"), "Colegiul Demo")

    def test_rejects_invalid_values_and_duplicates(self):
        with self.assertRaisesRegex(ValueError, "range"):
            bac.extract(TABLE.replace("9,51", "71"), "Colegiul Demo")
        with self.assertRaisesRegex(ValueError, "duplicate"):
            bac.extract(TABLE.replace("</tbody>", "<tr><td>2026</td><td>9</td><td>8</td><td>2</td><td>10</td><td>90%</td></tr></tbody>"), "Colegiul Demo")


if __name__ == "__main__":
    unittest.main()
