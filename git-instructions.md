# Setting up and using your team GitHub repository
Authors: Jobeth Muncy & Cynthia Chiang

### Part 1 - Create your repo

1. Pick one person in your team to be the repo maintainer.
2. This person will use their __public facing GitHub account__ (not Enterprise) to create a new repo.
3. In this repo:
   - public
   - primary branch name: _main_
   - add a .gitignore and select _python_
   - license: _creative commons_, _MIT_, etc.
4. Add team members
    Go to Settings->Manage Access->Invite Collaborators

### Part 2  - Clone the repo

1. Each team member must clone the repo (not a fork and clone, just a clone)
1. In the browser on the main page your new repo, go to __Code__ and copy the link
1. In Terminal or Git Bash, navigate the location that you want to have the repo on your local machine
1. `git clone [paste link]`
1. Check which remote repositories your local repo is pointing to with `git remote -v`

### Part 3 - Create branches

1. Each team member (including person hosting the repo) must create their own branch
2. `git switch -c yourname`
3. Use `git branch` to check which branch you are on. __Always work on your own branch.__

### Part 4 - Ready to work!

1. Each person will do a `git switch [name]` to move onto their own branch.
2. Have each person create their own notebook and name it _yourname.ipynb_
3. Now add these notebooks to the repo:
  ```
   git add .
   git commit -m 'very informative message'
   git push origin yourname
   ```
4. Go to the browser and create a pull request. __DO NOT approve your own pull requests.__
5. The repo host will be the maintainer of the repo and approve pull requests.

### Part 5 - Updating your branch

1. When you are ready to work, update your branch with changes from the main branch
     ```
     git switch main
     git pull origin main
     git switch yourname
     git merge main
    ```

2. Now any changes that have been made to the main branch online are merged on your local branch 😀

3. You are ready to work! Make sure you are on your own branch when you are working. When you are done:
    ```
    git add .
    git commit -m 'very informative message'
    git push origin yourname
    ```

4. Create a pull request.
  Tip: you can close open issues from your pull request like this: _closes #3_,  

 ## Part 6 - Suggestions

Set VS Code as your editor for resolving git merge conflicts, if you haven't already done so. Diffing and resolving conflicts in Jupyter Notebooks is a 
pain that VS Code makes much easier.  

Create issues in your GitHub repo to organize yourselves and collaborate. Close an issue when a task is completed. If the issue was resolved with code, 
reference th issue in your pull request to close it.

You can use GitHub's **Projects** tab to track your issue workflow. Select a Kanban board for that view.

