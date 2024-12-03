### Part 1 (Manager) - Create your repo
1. Pick one person in your team to be the repo maintainer.
2. This person will use their __public facing GitHub account__ (not Enterprise) to create a new repo.
3. In this repo:
   - public
   - primary branch name: _main_
   - add a .gitignore and select _python_
   - license: _creative commons_
   - initialize with a readme file
4. Add team members
    Go to Settings->Manage Access->Invite Collaborators
5. Add some text to the readme file on GitHub (click the pencil icon to edit the file, commit changes when done)

### Part 2 (Everybody) - Clone the repository
1. Each team member must clone the repo (**not a fork and clone**, just a clone)
2. In the browser on the main page your new repo, go to __Code__ and copy the link
3. Clone the repository to your desired location. **Do not do clone the repo within an existing repo**
4. Check which remote repositories your local repo is pointing to with `git remote -v`

### Part 3 (Everybody) - Create Branches
1. Each team member (including person hosting the repo) must create their own branch
2. `git switch -c <yourname>`; this command creates (`-c`) and switches to (`switch`) a new branch with indicated name
3. Use `git branch` to check which branch you are on. __Always work on your own branch.__

### Part 4 (Member A) - No conflict
1. From your terminal run `echo 'sometexthere' > file.txt`. This will create a new file with whatever text you've provided.
2. Add **only** that file to the staging area (aka **do not** just use `git add .`)
3. Commit your changes
4. Push your changes with `git push origin <yourbranchname>`
    - The last line should indicate that your local branch was pushed to a new branch on the remote with the same name

### Part 5 (Member A) - Create a pull request
1. Go to your repository on GitHub and you should see a yellow box saying `<yourbranchname> had recent pushes...`; click the green button saying "Compare & 
pull request"
    - Alternatively, you might see "This branch is <number> commits ahead of main"; in this case, click `Contribute` -> `Open pull request`
2. Write a descriptive comment for your pull request
3. Click `Create pull request`
    - GitHub will then automatically check for any merge conflicts and will then say that there are no conflict
4. DO NOT DO ANYTHING ELSE. Merging is the manager's job.

### Part 5 (Manager) - Merge pull request
1. On your repository page you should now see a number `1` next to the `Pull requests` tab toward the top of the page, indicating that a pull request has 
been submitted
2. Click on the name of the request to navigate to it
3. Click `Merge request`
4. Click `Confirm merge`

### Part 6 (Everybody) - Let the work begin!
***Every day before you start working, you should do this (assuming all of your work has been committed, pushed, and merged into the main via a PR)***
1. `git switch main` to make sure you're on the `main` branch
2. `git pull origin main` to pull any changes on the `main` branch of the remote
3. `git switch <yourbranchname>`
4. `git merge main` to merge in changes from the `main` branch
5. Now you're ready to start working!

### Part 7a (Member B) - What's a little conflict?
Let's say two members of your team started working on the same lines of a file at the same time and both submitted pull requests to integrate their work. 
How do we deal with that? Let's simulate it.
1. Make sure you are on your branch.
2. Run `echo 'somemorenewtext' >> file.txt` to add some more new text to the existing text file
3. Add, commit, and push **only** `file.txt`
4. Open a pull request.
### Part 7b (Manager or Member C)
1. Make sure you are on your branch
2. Run `echo 'overruled!' > file.txt` to overwrite the text that's in `file.txt`
3. Add, commit, and push **only** `file.txt`
4. Open a pull request.

### Part 8 (Manager) - Conflict resolution
1. Complete and merge one pull request
2. Complete the second pull request; GitHub will notify you that there are conflicts which must be resolved.
3. Click 'Resolve conflicts`
4. A text editor will open with all merge conflicts denoted with conflict markers
5. Resolve all conflicts and then click "Mark as resolved"
6. Once all conflicts have been resolved, click "Complete merge"

### Part 9 (Everybody except one person) - Get to work!
1. Complete the beginning of day protocol

### Part 10 (The odd person out) - Castaway season
Oh no, it looks like you've been working away all this time oblivious to what's been going on. You even made several commits from a different starting 
point on the main and now everybody else is ahead of you!
1. Run `echo 'newtext' > new.txt` to create a new file
2. Add, commit, push that file to your branch
3. Run `echo 'morenewtext' > new2.txt` to create another new file
4. Add, commit, push that file to your branch
5. Run `git pull origin main --rebase` to get your commits to point to the HEAD of the remote main.
    - You should see "rewinding head to replay your work on top of it" 
