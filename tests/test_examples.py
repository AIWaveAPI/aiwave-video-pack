"""Prevent the published video curl examples from drifting into invalid JSON."""

import json
import os
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class CopyableVideoExamples(unittest.TestCase):
    def test_all_prompt_payloads_are_json_and_use_the_published_prompt(self):
        for path in sorted((ROOT / "prompts").glob("*.md")):
            with self.subTest(path=path.name):
                text = path.read_text(encoding="utf-8")
                prompt = re.search(r"## English prompt\s+```\s*([^`]+?)\s*```", text)
                payload = re.search(r"(?m)^\s+--data-binary @- <<'JSON'\s*\n([^\n]+)\nJSON$", text)
                self.assertIsNotNone(prompt, "missing English prompt")
                self.assertIsNotNone(payload, "missing literal JSON curl payload")
                body = json.loads(payload.group(1))
                self.assertEqual(body["model"], "kling-video-o1")
                self.assertEqual(body["prompt"], prompt.group(1).strip())
                self.assertEqual(set(body), {"model", "prompt"})

    @unittest.skipIf(os.name == "nt" or not shutil.which("bash"), "requires bash")
    def test_copy_pasted_bash_sends_one_valid_payload_without_network(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            fake_curl = root / "curl"
            fake_curl.write_text(
                "#!/usr/bin/env python3\n"
                "import os,sys\n"
                "from pathlib import Path\n"
                "assert '--data-binary' in sys.argv and '@-' in sys.argv\n"
                "Path(os.environ['CAPTURE']).write_text(sys.stdin.read())\n"
                "print('{\"task_id\":\"synthetic\"}')\n",
                encoding="utf-8",
            )
            fake_curl.chmod(0o755)
            for path in sorted((ROOT / "prompts").glob("*.md")):
                with self.subTest(path=path.name):
                    text = path.read_text(encoding="utf-8")
                    match = re.search(r"## Reproduce\s+```bash\s*\n(.*?)\n```", text, re.S)
                    self.assertIsNotNone(match)
                    capture = root / "captured.json"
                    env = {**os.environ, "PATH": str(root) + os.pathsep + os.environ["PATH"],
                           "CAPTURE": str(capture)}
                    result = subprocess.run(["bash", "-c", match.group(1)], env=env,
                                            capture_output=True, text=True, timeout=10)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertIn("task_id", result.stdout)
                    payload = json.loads(capture.read_text(encoding="utf-8"))
                    self.assertEqual(payload["model"], "kling-video-o1")
                    capture.unlink()


if __name__ == "__main__":
    unittest.main()
