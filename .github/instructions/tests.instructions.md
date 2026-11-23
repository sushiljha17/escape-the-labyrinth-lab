---
applyTo: "tests/**/*.py"
---
# Rules for test files

- Use `unittest` from the standard library: test methods in `unittest.TestCase` classes, checked with `self.assertEqual`, `self.assertIn` and the like. No pytest and no other third-party packages. The tests run with `python -m unittest -v`.
- One test per acceptance criterion, named `test_ac_<id>_<short_name>`, for example `test_ac_04_blocked_direction`. Map checks are named `test_data_<short_name>`.
- Each test checks the exact reply text from the feature's spec.md and can fail. Flag `self.assertTrue(True)`, tests without an assertion and tests that only check that no error was raised.
- Test the engine through `Game.handle()` and the play loop through `cli.run()` with `io.StringIO`: no real keyboard input, no sleeps, no network.
- Test data is invented.
