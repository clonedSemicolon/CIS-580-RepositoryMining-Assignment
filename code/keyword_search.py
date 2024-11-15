from pydriller import Repository


def find_performance_fixes(repo_path):
    keywords = ["performance", "speed up", "accelerate", "fast", "slow", "latency", "contention", "optimize",
                "efficient"]
    performance_fixes = []

    for commit in Repository(repo_path).traverse_commits():
        if any(keyword in commit.msg.lower() for keyword in keywords):
            performance_fixes.append({
                'hash': commit.hash,
                'author': commit.author.name,
                'date': commit.author_date,
                'message': commit.msg
            })

    return performance_fixes