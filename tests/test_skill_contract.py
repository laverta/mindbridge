from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"


class SkillContractTests(unittest.TestCase):
    def test_skill_has_valid_minimal_frontmatter(self):
        text = SKILL.read_text(encoding="utf-8")
        self.assertTrue(text.startswith("---\n"))
        header, body = text.split("---\n", 2)[1:]
        self.assertIn("name: mindharp", header)
        self.assertIn("description:", header)
        self.assertIn("# Mindharp", body)

    def test_skill_has_non_clinical_guardrails(self):
        text = SKILL.read_text(encoding="utf-8")
        self.assertIn("Do not use it to diagnose", text)
        self.assertIn("professional care", text)
        self.assertIn("references/safety.md", text)
        self.assertIn("references/audhd-lens.md", text)
        self.assertIn("references/three-layer-lens.md", text)

    def test_audhd_lens_marks_metaphor_boundary(self):
        text = (ROOT / "references" / "audhd-lens.md").read_text(encoding="utf-8")
        self.assertIn("non-clinical vocabulary", text)
        self.assertIn("literal one-to-one mapping", text)
        self.assertIn("Do Not Claim", text)

    def test_peer_voice_has_boundaries(self):
        text = (ROOT / "references" / "audhd-lens.md").read_text(encoding="utf-8")
        self.assertIn("Peer Voice", text)
        self.assertIn("with consent", text)
        self.assertIn("never the boundaries", text)
        self.assertIn("safety.md", text)

    def test_foreword_exists_and_stays_non_clinical(self):
        text = (ROOT / "FOREWORD.md").read_text(encoding="utf-8")
        self.assertIn("never replacing care", text.lower())
        self.assertIn("not a triumph story", text.lower())

    def test_three_layer_lens_marks_boundaries(self):
        text = (ROOT / "references" / "three-layer-lens.md").read_text(encoding="utf-8")
        self.assertIn("non-clinical", text)
        self.assertIn("personal/system metaphor", text)
        self.assertIn("Do Not Claim", text)
        self.assertIn("hypothesis", text)

    def test_active_support_playbook_boundaries(self):
        text = (ROOT / "references" / "active-support.md").read_text(encoding="utf-8")
        self.assertIn("Completion:", text)
        self.assertIn("safety.md", text)
        self.assertIn("Never more than three suggestions", text)
        self.assertIn("no-decision", text.lower())
        lowered = text.lower()
        for banned in ("magnesium", "镁", "b-vitamin", "b族"):
            self.assertNotIn(banned, lowered)

    def test_safety_protocol_has_crisis_switch(self):
        text = (ROOT / "references" / "safety.md").read_text(encoding="utf-8")
        self.assertIn("Crisis switch", text)
        self.assertIn("STOP all metaphor", text)
        self.assertIn("does not handle crisis response", text)

    def test_safety_protocol_defers_crisis_lines_to_model(self):
        text = (ROOT / "references" / "safety.md").read_text(encoding="utf-8")
        # hotlines are the model's job, not the skill's
        self.assertIn("model's own responsibility", text)
        self.assertNotIn("12356", text)
        self.assertNotIn("988", text)

    def test_referenced_files_exist(self):
        text = SKILL.read_text(encoding="utf-8")
        for relative in re.findall(r"references/[A-Za-z0-9._-]+\.md", text):
            self.assertTrue((ROOT / relative).is_file(), relative)

    def test_state_schema_has_freshness_and_consent(self):
        text = (ROOT / "references" / "state-schema.md").read_text(encoding="utf-8")
        self.assertIn('"updated_at"', text)
        self.assertIn('"consent_scope"', text)
        self.assertIn("user_approved_shared", text)


    def test_brain_ops_has_fault_table_and_boundaries(self):
        text = (ROOT / "references" / "brain-ops.md").read_text(encoding="utf-8")
        self.assertIn("Fault table", text)
        self.assertIn("hot fix", text.lower())
        self.assertIn("not medical advice", text.lower())
        self.assertIn("island mode", text.lower())
        self.assertIn("no dosages", text.lower())
        self.assertNotIn("3-5g", text)

    def test_brain_ops_technical_error_not_self_attack(self):
        text = (ROOT / "references" / "brain-ops.md").read_text(encoding="utf-8")
        self.assertIn("Technical error reporting", text)
        self.assertIn("RAM overflow detected", text)
        self.assertIn("self-attack", text.lower())

    def test_minimum_completion_principle(self):
        text = SKILL.read_text(encoding="utf-8")
        self.assertIn("Minimum completion", text)
        self.assertIn("give the step first", text)
        self.assertIn("at most one optional follow-up", text)
        self.assertIn("never re-confirmed", text)
        self.assertIn("Metaphor on demand", text)

    def test_skill_is_lean(self):
        # the whole point of the redesign: SKILL.md stays small enough to hold
        text = SKILL.read_text(encoding="utf-8")
        self.assertLess(len(text), 6000, "SKILL.md grew too large again")
        self.assertNotIn("Response Contract", text)
        self.assertNotIn("Signing the Framework", text)

if __name__ == "__main__":
    import unittest

    unittest.main()
