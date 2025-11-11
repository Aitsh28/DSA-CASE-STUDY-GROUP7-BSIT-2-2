# src/ingest.py
import csv

def read_csv(file_path: str) -> list[dict]:
    """Reads student data from a CSV file and returns a list of cleaned student records."""
    records = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            record = {}
            record['student_id'] = row.get('student_id', '').strip()
            record['last_name'] = row.get('last_name', '').strip().title()
            record['first_name'] = row.get('first_name', '').strip().title()
            record['section'] = row.get('section', '').strip().upper()

            numeric_fields = ['quiz1', 'quiz2', 'quiz3', 'quiz4', 'quiz5', 'midterm', 'final', 'attendance_percent']
            for field in numeric_fields:
                value = row.get(field, '').strip()
                if value == '':
                    record[field] = None
                else:
                    try:
                        num = float(value)
                        record[field] = num if 0 <= num <= 100 else None
                    except ValueError:
                        record[field] = None

            records.append(record)
    return records


def validate_records(records: list[dict]) -> list[dict]:
    """Validates that required fields exist and student_id is unique."""
    valid_records = []
    seen_ids = set()
    for rec in records:
        sid = rec.get('student_id', '')
        if not sid or sid in seen_ids:
            continue
        seen_ids.add(sid)
        valid_records.append(rec)
    return valid_records


def ingest(file_path: str) -> list[dict]:
    """Full ingest pipeline: read CSV → clean → validate."""
    raw_records = read_csv(file_path)
    clean_records = validate_records(raw_records)
    return clean_records


if __name__ == "__main__":
    import pprint
    data = ingest("input.csv")
    pprint.pprint(data)
