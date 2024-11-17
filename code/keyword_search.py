from pydriller import Repository


def find_performance_fixes(repo_path):
    keywords = ["performance", "speed up", "accelerate", "fast", "slow", "latency", "contention", "optimize", "efficient"]
    performance_fixes = []
    
    print(f"Repository: {repo_path}")

    try:
        for commit in Repository(repo_path).traverse_commits():
            print(commit.msg)	
            commit_message = commit.msg.lower()
            for keyword in keywords:
                if keyword in commit_message:
                    print(f"commitMessage: {commit.msg} Keyword: {keyword}")
                    performance_fixes.append({
                        'hash': commit.hash,
                        'author': commit.author.name,
                        'date': commit.author_date,
                        'message': commit.msg
                    })
                    break
    except Exception as e:
        print(f"Repository path error for {repo_path}: {e}")
    except Exception as e:
        print(f"An error occurred while processing {repo_path}: {e}")
        
    return performance_fixes	        
