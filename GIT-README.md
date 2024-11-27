# Python Coding Standards & Best Practices
## OneOrigin Team Brown Bag Session

### 1. Git Basics

![](https://www.cs.sfu.ca/~ashriram/Courses/CS295//assets/img/git/git_singleuserflow.png)
```python

# Basics
git status           # Check status of files
git add [file]       # Stage file(s) for commitwhy do we need this `gevent WSGI server`
git add .            # Stage all files
git commit -m "message"  # Commit staged files with a message


# Branch Commands 
git branch           # List branches
git branch [name]    # Create new branch
git checkout [branch]  # Switch to branch
git merge [branch]   # Merge branch into current branch


# Log Commands
git log             # View commit history
git diff            # Show changes in working directory

```

### 2. How to avoid merge conflict?

There's no secret sauce, but you can follow these steps to reduce/avoid merge conflict
```python
- Commit frequently and commit small changes
- Maintain the same formatting/linting style for code to avoid unneccessary conflicts
- Always take a pull request/rebase your master branch before making a commit 
```


### 3. How to write good commit message?
![](/commit-message.png)
Some more Examples
```python

- Bug Fix 
    fix: commits, trim long messages to 72

- New Feature/Improvments
    feat: issues, add option to filter by reviewer

- Boring changes like package upgrade, commenting, function/variable/class renames
    chore: foolib, upgrade to 1.2.3

- Major Performance Improvements
    perf: comments, index on author makes search 2x faster

- Link JIRA Ticket
    JIRA-101 - Add feature x
```


### 4. How to name branch?
```python
# Creating a new feature branch
git checkout -b feature/add-user-auth

# Switching to a bugfix branch
git checkout -b bugfix/logout-issue

# Creating new release branch
git checkout -b release/v2.4.0

# Preparing a hotfix
git checkout -b hotfix/logout-fix

# Jira Ticket
git checkout -b {feature/bugfix/release/hotfix}/JIRA-123-user-login
```

# add ticket branch name



### 5. CI/CD Pipeline

```python

```