import csv


def write_to_csv(performance_fixes, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['Project Repo Name', 'Performance Fix Commit Message', 'Commit id']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for fix in performance_fixes:
            writer.writerow({
                'Project Repo Name': fix['repo_name'],
                'Performance Fix Commit Message': fix['message'],
                'Commit id': fix['commit_id']
            })
