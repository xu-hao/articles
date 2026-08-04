from __future__ import annotations

import json
import unittest

from cases import CONDITIONS, LEXICAL_MAPPINGS, corpus_manifest, make_cases, render_prompt
from experiment import all_count_jobs, generation_jobs, score_response


class CorpusTests(unittest.TestCase):
    def test_expected_corpus_dimensions(self) -> None:
        self.assertEqual(40, len(LEXICAL_MAPPINGS))
        self.assertEqual(32, len(make_cases()))
        self.assertEqual(644, len(all_count_jobs()))
        self.assertEqual(256, len(generation_jobs(2)))

    def test_every_case_has_a_match_and_an_obvious_miss(self) -> None:
        for case in make_cases():
            self.assertIn("R01", case.answer)
            self.assertNotIn("R02", case.answer)

    def test_abbreviation_conditions_do_not_change_gold_data(self) -> None:
        for case in make_cases():
            full = render_prompt(case, "full")
            defined = render_prompt(case, "abbr_defined")
            undefined = render_prompt(case, "abbr_undefined")
            self.assertIn(case.domain.entity, full)
            self.assertIn(case.domain.entity, defined)  # definition legend
            self.assertNotIn(case.domain.entity, undefined)
            for record in case.records:
                for prompt in (full, defined, undefined, render_prompt(case, "concise")):
                    self.assertIn(record.record_id, prompt)

    def test_manifest_hash_is_stable_and_not_self_referential(self) -> None:
        first = corpus_manifest()
        second = corpus_manifest()
        self.assertEqual(first["sha256"], second["sha256"])
        self.assertEqual(64, len(first["sha256"]))
        json.dumps(first)

    def test_job_ids_are_unique(self) -> None:
        count_ids = [job.job_id for job in all_count_jobs()]
        generation_ids = [job.job_id for job in generation_jobs(20)]
        self.assertEqual(len(count_ids), len(set(count_ids)))
        self.assertEqual(len(generation_ids), len(set(generation_ids)))

    def test_scorer_is_order_insensitive_but_rejects_duplicates(self) -> None:
        expected = ("R01", "R03")
        self.assertTrue(score_response('{"answer":["R03","R01"]}', expected)[0])
        self.assertFalse(score_response('{"answer":["R01","R01","R03"]}', expected)[0])
        self.assertFalse(score_response('{"answer":["R01"]}', expected)[0])
        self.assertFalse(score_response('not json', expected)[0])


if __name__ == "__main__":
    unittest.main()
