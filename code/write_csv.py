import csv


def write_to_csv(performance_fixes, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['hash', 'author', 'date', 'message']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for fix in performance_fixes:
            writer.writerow(fix)