from clone_repo import clone_repositories
from keyword_search import find_performance_fixes
from write_csv import write_to_csv


def main():
    input_file = 'repositories/repositories.txt'
    output_file = 'output/performance_fixes.csv'

    # Clone repositories
    clone_repositories(input_file)

    # Find performance fixes and write to CSV
    all_performance_fixes = []
    with open(input_file, 'r') as file:
        repos = file.readlines()

    for repo in repos:
        repo_name = repo.strip().split('/')[-1].replace('.git', '')
        performance_fixes = find_performance_fixes(repo_name)
        all_performance_fixes.extend(performance_fixes)

    write_to_csv(all_performance_fixes, output_file)
    print(f"Performance fixes have been written to {output_file}")


# Execute the main function
if __name__ == "__main__":
    main()