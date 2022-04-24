# Python script for pulling each submodule

try:
    import git
except Exception:
    print("You need git to use this script! Make sure you run:")
    print("  python3 -m pip install -r requirements.txt")
    exit(1)

try:
    from colorama import Fore, Style
    colorama_found = True
except Exception:
    colorama_found = False

################################
main_repo_path = "../.."       # The location of r4v10l1/codewars. Because we are in /scripts/python, "../.."
################################

# -----------------------------------------------------------------------
# Functions for printing with colorama (if found)

def cprint_pulling(repo_color, repo_name, remote_name):
    if colorama_found:
        print("%s%s[%s%s%s%s%s] Pulling commits from %s%s%s...%s" % 
                (Style.RESET_ALL, Fore.WHITE, repo_color, Style.BRIGHT, repo_name, Style.RESET_ALL, Fore.WHITE,
                    repo_color, remote_name, Fore.WHITE, Style.RESET_ALL))
    else:
        print("[%s] Pulling commits from %s..." % (repo_name, remote_name))

def cprint_pulled(repo_color, repo_name, commit_number):
    if colorama_found:
        print("%s%s[%s%s%s%s%s] Pulled %s%s%s commits from %sorigin/main%s...%s" % 
                (Style.RESET_ALL, Fore.WHITE, repo_color, Style.BRIGHT, repo_name, Style.RESET_ALL, Fore.WHITE,
                    repo_color, commit_number, Fore.WHITE, Style.BRIGHT, Style.NORMAL, Style.RESET_ALL))
    else:
        print("[%s] Pulled %s commits from origin/main..." % (repo_name, commit_number))

def cprint_error(error_text):
    if colorama_found:
        print("%s%s[%s%sError%s%s] %s%s" % 
                (Style.RESET_ALL, Fore.WHITE, Fore.RED, Style.BRIGHT, Style.RESET_ALL, Fore.WHITE,
                    error_text, Style.RESET_ALL))
    else:
        print("[Error] %s" % (error_text))

def cprint_error_suggestion():
    if colorama_found:
        print("%s%s[%s%sInfo%s%s] You might want to use %s--recurse-submodules%s when cloning, or run %sscripts/sync-submodules.sh%s to easily pull all of them.%s" % 
                (Style.RESET_ALL, Fore.WHITE, Fore.BLUE, Style.BRIGHT, Style.RESET_ALL, Fore.WHITE,
                    Style.BRIGHT, Style.NORMAL, Style.BRIGHT, Style.NORMAL, Style.RESET_ALL))
        print("%s%s[%s%sInfo%s%s] You can also use %sgit submodule update --init --recursive%s from the main repo folder to fix this.%s" % 
                (Style.RESET_ALL, Fore.WHITE, Fore.BLUE, Style.BRIGHT, Style.RESET_ALL, Fore.WHITE,
                    Style.BRIGHT, Style.NORMAL, Style.RESET_ALL))
    else:
        print("[Info] You might want to use --recurse-submodules when cloning, or run scripts/sync-submodules.sh to easily pull all of them.")

def cprint_detached(repo_color, repo_name):
    if colorama_found:
        print("%s%s[%s%s%s%s%s] Head is detached. Checking out to %smain%s...%s" % 
                (Style.RESET_ALL, Fore.WHITE, repo_color, Style.BRIGHT, repo_name, Style.RESET_ALL, Fore.WHITE,
                    Style.BRIGHT, Style.NORMAL, Style.RESET_ALL))
    else:
        print("[%s] Head is detached. Checking out to main..." % (repo_name))

# -----------------------------------------------------------------------
# Functions for each repo

def pull_repo_py():
    repo_path = "%s/codewars-python" % main_repo_path
    try:
        repo = git.Repo(repo_path)
    except Exception:
        cprint_error("I can't find a repo in %s" % (repo_path))
        cprint_error_suggestion()
        exit(1)
    if repo.head.is_detached:
        cprint_detached(Fore.BLUE, "Python")
        repo.git.checkout("main")
    repo_origin = repo.remotes.origin
    cprint_pulling(Fore.BLUE, "Python", "r4v10l1/codewars-python")
    repo_origin.fetch()
    commits_to_pull = repo.git.rev_list("--count", "HEAD..origin/main")
    repo_origin.pull()
    cprint_pulled(Fore.BLUE, "Python", commits_to_pull)

def pull_repo_c():
    repo_path = "%s/codewars-c" % main_repo_path
    try:
        repo = git.Repo(repo_path)
    except Exception:
        cprint_error("I can't find a repo in %s" % (repo_path))
        cprint_error_suggestion()
        exit(1)
    if repo.head.is_detached:
        cprint_detached(Fore.BLUE, "C")
        repo.git.checkout("main")
    repo_origin = repo.remotes.origin
    cprint_pulling(Fore.BLUE, "C", "r4v10l1/codewars-c")
    repo_origin.fetch()
    commits_to_pull = repo.git.rev_list("--count", "HEAD..origin/main")
    repo_origin.pull()
    cprint_pulled(Fore.BLUE, "C", commits_to_pull)

def pull_repo_sh():
    repo_path = "%s/codewars-shell" % main_repo_path
    try:
        repo = git.Repo(repo_path)
    except Exception:
        cprint_error("I can't find a repo in %s" % (repo_path))
        cprint_error_suggestion()
        exit(1)
    if repo.head.is_detached:
        cprint_detached(Fore.BLUE, "Shell")
        repo.git.checkout("main")
    repo_origin = repo.remotes.origin
    cprint_pulling(Fore.BLUE, "Shell", "r4v10l1/codewars-shell")
    repo_origin.fetch()
    commits_to_pull = repo.git.rev_list("--count", "HEAD..origin/main")
    repo_origin.pull()
    cprint_pulled(Fore.BLUE, "Shell", commits_to_pull)

def pull_repo_rust():
    repo_path = "%s/codewars-rust" % main_repo_path
    try:
        repo = git.Repo(repo_path)
    except Exception:
        cprint_error("I can't find a repo in %s" % (repo_path))
        cprint_error_suggestion()
        exit(1)
    if repo.head.is_detached:
        cprint_detached(Fore.BLUE, "Rust")
        repo.git.checkout("main")
    repo_origin = repo.remotes.origin
    cprint_pulling(Fore.BLUE, "Rust", "r4v10l1/codewars-rust")
    repo_origin.fetch()
    commits_to_pull = repo.git.rev_list("--count", "HEAD..origin/main")
    repo_origin.pull()
    cprint_pulled(Fore.BLUE, "Rust", commits_to_pull)

def pull_repo_bf():
    repo_path = "%s/codewars-brainfuck" % main_repo_path
    try:
        repo = git.Repo(repo_path)
    except Exception:
        cprint_error("I can't find a repo in %s" % (repo_path))
        cprint_error_suggestion()
        exit(1)
    if repo.head.is_detached:
        cprint_detached(Fore.BLUE, "Brainfuck")
        repo.git.checkout("main")
    repo_origin = repo.remotes.origin
    cprint_pulling(Fore.BLUE, "Brainfuck", "r4v10l1/codewars-brainfuck")
    repo_origin.fetch()
    commits_to_pull = repo.git.rev_list("--count", "HEAD..origin/main")
    repo_origin.pull()
    cprint_pulled(Fore.BLUE, "Brainfuck", commits_to_pull)

# -----------------------------------------------------------------------
# Pull each repo

def main():
    pull_repo_py()
    pull_repo_c()
    pull_repo_sh()
    pull_repo_rust()
    pull_repo_bf()

main()
