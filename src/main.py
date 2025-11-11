import json
from ingest import read_csv
from transform import compute_final_grade, assign_letter_grade
from analyze import analyze 
from reports import Reports

def main():
    with open("config.json") as f:
        config = json.load(f)
    
    #1. INGEST PART
    students = read_csv("input.csv")

    #2. TRANSFORM PART
    for s in students:
        compute_final_grade(s, config["weights"])
        assign_letter_grade(s)
    
    #3. ANALYZE PART
    analyze(students)

    #4. REPORTS PART
    rep = Reports()
    rep.print_summary(students)
    rep.export_per_section_csvs(students, output_dir="reports")
    rep.generate_at_risk_lists(students, config["at_risk_threshold"], output_dir="reports")

if __name__ == "__main__":
    main()