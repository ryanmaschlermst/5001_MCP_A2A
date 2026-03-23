class Gatekeeper:

    def run(self, message):

        draft = message["content"]["draft"]

        checks = [
            ("Has Evidence", "Evidence" in draft),
            ("Has Test Plan or Criteria", "Test" in draft or "Acceptance" in draft),
        ]

        print("\n[Gatekeeper] Reflection Results:")

        passed = True
        for name, ok in checks:
            status = "PASS" if ok else "FAIL"
            print(f"{name}: {status}")
            if not ok:
                passed = False

        if not passed:
            print("Revision required.")
            return

        decision = input("\nApprove? (yes/no): ").strip().lower()

        if decision == "yes":
            print("[Gatekeeper] Approved. (Simulated GitHub creation)")
        else:
            print("[Gatekeeper] Rejected. No changes made.")
