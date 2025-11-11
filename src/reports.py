# src/reports.py
import os
import csv

class Reports:
    def print_summary(self, students):
        print("\n=== STUDENT GRADE SUMMARY ===")
        for s in students:
            name = f"{s['last_name']}, {s['first_name']}"
            print(f"{s['student_id']} | {name:<20} | Sec {s['section']} | {s['final_grade']} ({s['letter_grade']})")

    def export_per_section_csvs(self, students, output_dir='reports'):
        os.makedirs(output_dir, exist_ok=True)
        sections = {}

        for s in students:
            sec = s["section"]
            sections.setdefault(sec, []).append(s)

        headers = list(students[0].keys())

        for sec, group in sections.items():
            file_path = os.path.join(output_dir, f"section_{sec}.csv")
            with open(file_path, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=headers)
                writer.writeheader()
                writer.writerows(group)

    def generate_at_risk_lists(self, students, threshold, output_dir='reports'):
        os.makedirs(output_dir, exist_ok=True)

        risk = [s for s in students if s["final_grade"] < threshold]

        if not risk:
            print("\nNo students at risk. ✅")
            return

        file_path = os.path.join(output_dir, "at_risk_students.csv")
        headers = list(risk[0].keys())

        with open(file_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(risk)

        print(f"\nGenerated at-risk report → {file_path}")
