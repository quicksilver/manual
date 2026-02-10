# Github

We agreed on some best practices for handling things on Github and I thought they should be documented somewhere.

### Coding Styles

* The more modern literal syntax should be used for NSDictionaries and NSArrays (e.g. `@[obj1, obj2, obj3]`, `id firstObj = myArray[0]`)
* For method declarations/definitions, there should be a space between the class/instance indicator and the return type bracket. (e.g. `- (BOOL)isGood;`, `+ (id)sharedInstance`)
* For method definitions, the first curly brace should appear on the same line as the method declaration (not one below)
* Most things at [http://llvm.org/docs/CodingStandards.html#don-t-use-else-after-a-return](http://llvm.org/docs/CodingStandards.html#don-t-use-else-after-a-return)

### Pull Requests

If you have commits you feel should be included in the Quicksilver core repository, you can submit a 'Pull Request' from within your fork and branch on GitHub (see GitHub contributer workflow below for more details). Once this is done, your code changes will be checked over by another member of the team, tested and then merged with the main repository if no problems are found.

#### Pull Request Rules

These rules must be followed for any pull request to be accepted:

* **Always** use Pull Request. Do not push your own commits to the main repository (if you have access).
* After creating a Pull Request, do not merge it yourself. One other person must also 'OK' the pull request.
* After you merged a pull request, close or comment on related issues (if appropriate). They are often linked in the pull request itself.
* Any user visible string that you add or modify in a pull request **must** be wrapped in `NSLocalizedString()` (or similar)
* No pull requests should be made for localisation changes. All localisation must occur on the [Transifex Quicksilver project](https://www.transifex.com/projects/p/quicksilver/) page
* No pull request may increase the number of build warnings for the Quicksilver project
* Any pull request for a plugin **must** also include [adequate documentation](http://projects.skurfer.com/QuicksilverPlug-inReference.mdown#documentation\_and\_bltrversion) (if it doesn't already exist)
* The items listed in 'Coding Styles' (above) should be followed.

### Issues

* First come, first serve. If you want to work on an issue, just assign it to yourself.
* If you think you know someone who can help with an issue, just @mention the person in the comments (like "@pjrobertson don't you know something about this?"). They will be notified.
* If you have an idea on how to fix the issue but don't have the time to fix it, just leave a comment explaining your idea.

### Github Contributor Workflow

I had some problems with Git and Github and getting the correct commits into my pull requests. It took me a while to work out a workflow that worked well for me (lots of work ;-)), so thought I'd share it here:

* Fork on GitHub

&#x20;   `click the big "Fork" button on` [`1`](https://github.com/quicksilver/Quicksilver)

* Clone you own fork

&#x20;   `git clone git@github.com:`_\<your\_username>_`/Quicksilver.git`

* Add a remote (called upstream) linking to the Quicksilver main repository

&#x20;   `cd Quicksilver` `git remote add upstream git@github.com:quicksilver/Quicksilver.git`

* Get dependencies (submodules)

&#x20;   `git submodule init` `git submodule update`

* **Always keep the master branch clean. Never do any work/commits here.**
* Instead, only pull in changes from quicksilver/Quicksilver with --rebase

&#x20;   `git pull --rebase upstream master`

* Make a branch from master for every separate thing you're working on (checkout with the -b option creates a new branch)

&#x20;   `git checkout -b  master`

* Work...commit...work...commit...work...commit ;-)

&#x20;   `git add .` `git commit`

* When you finished something, push that branch to your repository, creating a new branch on GitHub

&#x20;   `git push origin`&#x20;

* Go to your repository on GitHub, select the newly created branch, then click the "Pull Request" button. Try to enter a description other developers will understand and try to mention/link any related issues. :-)
* There will be some testing and a code review. If during this code review something comes up that should be changed, you can add more commits to a pull request, simply by pushing to the branch on GitHub (just like you did before)
* Once the pull request is accepted and merged, you can delete the branch on GitHub (note the colon in the push command) and locally

&#x20;   `git push origin :` `git branch -D`&#x20;

* Pull the changes into the local master branch

&#x20;  `git pull --rebase upstream master`

* Rebase other **unpublished** branches to the new master

&#x20;   `git checkout` `git rebase master`

**=> Don't merge your own changes back into your own master branch**

Keeping all the changes in separate branches and never merging them back to your own master branch seems complicated, but it takes takes care of a couple of problems:

* When you do a pull request on Github, it puts all the commits in the pull request. There is no way to separate commits that don't belong together. But since you are having only commits belonging together in any one branch, that's not a problem anymore.
* If you did already commit things that you want separate later, you can just do a cherry-pick locally into a new branch, push that new branch to Github and do the pull request from there.
* If your commits are cherry-picked by a maintainer, it creates new commits. If you merge these commits back into the branch where they came from, Github gets confused and thinks your original commits should still be merged, even though they already in the main repository. But since you only merge stuff from the main repository into your master branch, this also isn't a problem.

I hope I did explain my problems (and solutions) sufficiently. :-)

### Github Collaborator/Maintainer Merge Worklow

If you, along with one other person, have decided a pull request is safe to merge to the main repository, here are the main steps that should be taken.

* Comment on the pull request as to why it should be merged (e.g. this is working, only a small fix, comments look good etc.)
* Click the 'Merge Help' button on the Pull Request Page
* **Before** you complete to the step 'git checkout master' rebuild the source and make sure everything works
* Also, run

&#x20;   `git log`

to see the list of commits on the pull requester's repository, and make sure they match those for the master branch closely

* If all is well, checkout the master branch (note that you may have your own GitHub repository called master, so this repository may be called qs-master)
* Follow the rest of the commands in the 'Merge Help' window.
* **Before** pushing the changes. Run git log once more and check the list of commits. Make sure there are no silly 'merge branch x from y' commits that may cause problems (typically when the user issuing the pull request hasn't updated his branch for a long time)
* Push the changes to upstream (or otherwise named, see below). Use

&#x20;   `git push upstream qs-master:master`

This means: push to remote upstream from my local branch qs-master to the remote branch master.

#### Adding the Quicksilver Remote Repository

If you haven't made a merge before, you'll need to add Quicksilver as a remote repository to you local git folder

* Go to the Quicksilver GitHub repository page. You should see a URL such as

&#x20;      `git@github.com:quicksilver/Quicksilver.git`

* Copy this, and then in Terminal, navigate to the folder you want to install the source (you can use Quicksilver's 'Go To Directory in Terminal' action.
* To initialise a git repository, type

&#x20;     `git init`

* then type

&#x20;     `git remote add upstream <git URL from 1st step>`

* Checkout a local branch using

&#x20;    `git checkout -b qs-master`

* Pull the changes from the Quicksilver remote to your new local branch using

&#x20;   `git pull upstream master`

* Update the git submodules using

&#x20;   `git submodule init` `git submodule update`

* Verify you've got the right commits (the list should be the same as what's on the [GitHub page](https://github.com/quicksilver/quicksilver/commits)) by typing

```
   git log
```

and comparing the list with what's on GitHub
