from clone_repo import clone_repositories
from keyword_search import find_performance_fixes
from write_csv import write_to_csv
import os
from urllib.parse import urlparse


def main():
    input_file = 'repositories/repositories.txt'
    output_file = 'performance_fixes.csv'

    # Clone repositories
    #clone_repositories(input_file)

    # Find performance fixes and write to CSV
    all_performance_fixes = []
    with open(input_file, 'r') as file:
        repos = file.readlines()
        
    print(f"Repository Size: {len(repos)}")    
               
    for repo in repos:
        repo_url = repo.strip()
        if repo_url:  # Check if the line is not empty
            repo_name = os.path.basename(repo_url).replace('.git', '')
            print(f"Looking for repository folder: {repo_name}")
            performance_fixes = find_performance_fixes(repo_name)
            if performance_fixes:
            	all_performance_fixes.extend(performance_fixes)
            
            	
    print(len(all_performance_fixes))	
    write_to_csv(all_performance_fixes, output_file)
    print(f"Performance fixes have been written to {output_file}")


# Execute the main function
if __name__ == "__main__":
    main()
