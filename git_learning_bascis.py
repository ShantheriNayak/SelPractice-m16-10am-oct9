'''
1. adding files to git:
        git add file.py
        ex: git add learning_GIT.py
2. Checking status:
        git status

        you will get the following on comd prompt:

        On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   learning_GIT.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .idea/
        DataDrivenTesting/
        Modular_Framework_POM/
        RamyaMaam_notes/
        Sel-Oct9_M16-Shantheri_Training/
        Self_tried_AutomationTCs/
        hello_world.py


3.after adding files to staging area, now we need to commit the code file.

git commit -m "DESCRIPTION message"

git commit -m "check if num is odd or even"   060cc52---short commit id

>git commit -m "Checking num if the num is even or not"
[master (root-commit) 060cc52] Checking num if the num is even or not
 1 file changed, 6 insertions(+)
 create mode 100644 learning_GIT.py


 4. git log
commit 060cc5281d7f33c5845841bf127b9819a1afdb81 (HEAD -> master)---->complete commit ID
Author: ShantheriNayak <shantherinayak@gmail.com>
Date:   Mon Dec 8 11:33:30 2025 +0530

    Checking num if the num is even or not

5. git log --oneline   ### short commit id and details
060cc52 (HEAD -> master) Checking num if the num is even or not



6, made changes to the master code now.
a. add file to git:
b.check status
c. commit
d check commit id is reflected

C:\Users\Prashanth Nayak\PycharmProjects\Selenuim_ProjectTraining>git add learning_GIT.py ##a

C:\Users\Prashanth Nayak\PycharmProjects\Selenuim_ProjectTraining>git status ##b
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   learning_GIT.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .idea/
        DataDrivenTesting/
        Modular_Framework_POM/
        RamyaMaam_notes/
        Sel-Oct9_M16-Shantheri_Training/
        Self_tried_AutomationTCs/
        git_learning_bascis.py
        hello_world.py


C:\Users\Prashanth Nayak\PycharmProjects\Selenuim_ProjectTraining>git commit -m "defined func"  ##c
[master 25dcf98] defined func
 1 file changed, 9 insertions(+), 6 deletions(-)

C:\Users\Prashanth Nayak\PycharmProjects\Selenuim_ProjectTraining>git log --oneline ##d
25dcf98 (HEAD -> master) defined func      ## both the commit id s are present (head-->master ) pointer is the changed code
060cc52 Checking num if the num is even or not # first code




'''