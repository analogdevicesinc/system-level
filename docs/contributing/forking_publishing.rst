.. _forking-publishing:

Forking and publishing
======================

The steps below are a walk-through to contribute to
:git-system-level:`this </>` repository,
It ensures that GitHub Actions and GitHub Pages are enabled, so you can run
continuous integration and see the pages live at *<your_user>.github.io/system-level*,
and `git-lfs <https://git-lfs.com/>`__ artifacts are properly synced.
To learn about git LFS and use it as a pro, read :ref:`git-lfs`.

.. note::

   Using the Python virtual environment (venv) is recommended, but if you wish
   to not use it, skip steps in :green:`green`.

Preparing your origin
---------------------

There are three options to contribute:

* :ref:`forking-publishing branch`: with write access to *analogdevicesinc* organization (recommended).
* :ref:`forking-publishing fork`: that want to use the GitHub flow.
* :ref:`forking-publishing copy`: that want to work privately first.

.. tip::

   If using Github Codespaces, just fork/create a branch/copy and follow
   :ref:`this section <forking-publishing github-codespaces>`.

.. _forking-publishing branch:

Branch
~~~~~~

If you have write permission to the repository, you shall add your work to a
branch at mainland, then just:

Ensure git-lfs is installed with:

.. code:: bash

   sudo apt install git-lfs -y

Initialize it with skip-smudge during clone, so we can fetch on demand later:

.. code:: shell

   git lfs install --skip-smudge

Clone the repository

.. shell::

   $ git clone https://github.com/analogdevicesinc/system-level \
         --origin public \
         --depth 10 \
         -- system-level
   $ cd system-level

Create and checkout a branch

.. shell::

   ~/system-level
   $ git checkout -b <your_branch>

.. _forking-publishing fork:

Fork
~~~~

Fork the *analogdevicesinc/system-level* repo on your account.

**Enable the workflows** on the forked repo at *github.com/<your_user>/system-level/actions*
by clicking the :green:`green button` "I understand my workflows, go ahead and enable them".

.. caution::

   If you forked all branches, the :green:`green button` **will** be hidden by
   the ``pages build and deployment`` run. You **need** to delete all runs from
   the Actions tab to get the :green:`green button` again.

Ensure git-lfs is installed with:

.. code:: bash

   sudo apt install git-lfs -y

Initialize it with skip-smudge during clone, so we can fetch on demand later:

.. code:: shell

   git lfs install --skip-smudge

Clone the repository:

.. shell::

   $ git clone https://github.com/<your_user>/system-level \
         --origin public \
         --depth 10 -- system-level
   $ cd system-level


Fetch the large files from *analogdevicesinc* that you are working on and push
to your copy the large files binaries (and vice versa):

.. shell::

   ~/system-level
   $ git lfs pull public -I file_basename
   $ git lfs push private --all

If you don't have write permission to *analogdevicesinc*, you won't be able
to push to it, but a reviewer can do in your behalf during review.

Pull requests against your own fork
+++++++++++++++++++++++++++++++++++

GitHub Pages deployments from pull request runs are not allowed by default in
forks. When opening a pull request against your fork, the deployment step will
fail with:

  .. error::

     The deployment was rejected or didn't satisfy other protection rules.

To allow these deployments, open your fork's
``https://github.com/<USER>/system-level/settings/environments`` page and
select the ``github-pages`` environment. Under **Deployment branches and
tags**, ensure the list includes:

* ``main``
* ``refs/pull/*/merge``

By clicking ``Add deployment branch or tag rule`` and adding each,
allowing GitHub Pages deployments from pull request runs in your fork.

.. _forking-publishing copy:

Copy
~~~~

Ensure git-lfs is installed with:

.. code:: bash

   sudo apt install git-lfs -y

Initialize it with skip-smudge during clone, so we can fetch on demand later:

.. code:: shell

   git lfs install --skip-smudge

Clone mainland:

.. shell::

   $ git clone https://github.com/analogdevicesinc/system-level \
        --origin public \
        --depth 10 -- system-level
   $ cd system-level

Setup both origins, for example, call *analogdevicesinc* ``public`` and your
copy ``private`` at the *.git/config*, similar to:

::

   [core]
   	repositoryformatversion = 0
   	filemode = true
   	bare = false
   	logallrefupdates = true
   [remote "public"]
   	url = https://github.com/analogdevicesinc/system-level.git
   	fetch = +refs/heads/*:refs/remotes/public/*
   [remote "private"]
   	url = https://github.com/<your_user>/system-level.git
   	fetch = +refs/heads/*:refs/remotes/private/*
   [branch "main"]
        # Set your private copy as upstream
   	remote = private
   	merge = refs/heads/main


Push the working branch to your copy.

.. shell::

   ~/system-level
   $git push private main:main

Fetch the large files from *analogdevicesinc* that you are working on and push
to your copy the large files binaries (and vice-versa):

.. shell::

   ~/system-level
   $ git lfs pull public -I file_basename
   $ git lfs push private --all

If you don't have write permission to *analogdevicesinc*, you won't be able
to push to it, but a reviewer can do in your behalf during review.

Preparing your environment
--------------------------

It is possible to contribute:

* :ref:`forking-publishing local` (most freedom); or with
* A :ref:`forking-publishing github-codespaces`.

Follow either tutorial to bring up the environment.

.. _forking-publishing local:

Using your local host
~~~~~~~~~~~~~~~~~~~~~

To prepare your environment to work **locally**,
clone and build the doc for the first time (working directory: repo root):

:green:`Setup the virtual env at the repo root path:`

.. shell::

   ~/system-level
   $ python -m venv ./venv

:green:`Activate the virtual env`:

.. shell::

   ~/system-level
   $ source ./venv/scripts/activate

Ensure pip is up-to-date:

.. code:: bash

   python3 -m ensurepip
   pip install pip --upgrade


Install the requirements:

.. shell::

   ~/system-level
   $ (cd docs ; pip install -r requirements.txt --upgrade)

Launch the doc editing server using :external+doctools:ref:`serve`:

.. shell::

   ~/system-level
   $ (cd docs ; adoc serve)

The server will fetch on demand the git LFS resource (smudge step) from the
pages you visit on the local server, and watched files you touch.

Alternatively, you can build it once calling Sphinx directly, but if the git LFS
smudge step was skipped, the images and other binary files will be missing.

.. shell::

   ~/system-level
   $ (cd docs ; make html)

.. _forking-publishing github-codespaces:

GitHub Codespace
~~~~~~~~~~~~~~~~

Instead of working locally, you can use a cloud virtual machine with
GitHub Codespaces.

GitHub Codespaces uses the :git-system-level:`.devcontainer.json` file to
initialize a container in the cloud.
This container is pre-configured with all the tools required to build the
documentation, including the live preview daemon :external+doctools:ref:`serve`,
which is automatically started.
This setup provides a user experience comparable to platforms like Google Docs
or Overleaf.

.. caution::

   | GitHub Codespaces usage is billed to the user (you)!
   | Be sure to understand GitHub's billing policies and your account free quota.

To use GitHub Codespaces, navigate to the
:git-system-level:`GitHub GUI for this repository <+>` and click
*Code > Codespaces > Create codespace on main*.

This will open a new tab and set up the virtual environment.
The setup is complete  when the live preview panel appears on the right.

To manage all your GitHub Codespaces and shut them down, visit
`github.com/codespaces <https://github.com/codespaces>`__.

Adding content
--------------

Add a new topic and pages (working directory: docs).

On *index.rst*, add a new topic:

::

   .. toctree::
      :caption: My new topic
      :maxdepth: 2

       my_topic/index

Or add to an existing, for example, in *eval/index.rst*.

.. tip::

   Don't overthink the location at this point, it can be easily moved later.

Create a new folder and file matching the entry from last step:

.. shell::

   ~/system-level/docs
   $ mkdir my_topic; touch my_topic/index.rst

Edit *my_topic/index.rst*, adding a title and some content.

Build the doc and see the changes.

Commit the changes.

For a extensive guide on adding content see :ref:`creating-new-pages`.

Pushing and triggering the CI
-----------------------------

The CI (.github/workflows/top-level.yml) builds the doc and pushes to the
``gihub-pages`` branch and is triggered on push to main and on pull request
(every time):

* On pull request, the build doc target is run, which builds the doc and stores it as an artifact.
* On push to main, the build doc and deploy targets are run, the latter commits the doc artifact to the gh-pages branch.

.. tip::

   You can see the runs at github.com/<your_user>/system-level/actions.

Enable GitHub Pages to have the public website
configure GitHub Pages at *github.com/<your_user>/system-level/settings/pages*:

* Set Source as "deploy from branch"
* Set the branch as "gh-pages"

Resuming work at a later time
-----------------------------

:green:`Reactivate the virtual environment with:`

.. shell::

   ~/system-level
   $ source ./venv/scripts/activate

Ensure the tools are up to data from time to time with:

.. shell::

   ~/system-level
   $ (cd docs ; pip install -r requirements.txt --upgrade)

Edit, build, commit, push as usual.

.. _git-lfs:

Conquer git LFS
---------------

Since git LFS is not that common in the wild, it may be tricky to get the hang
of it.

First of all, the basics:
Git LFS replaces binaries files with pointers, and stores the binaries outside the
git repository, in an external server.

When you do ``git clone/pull``, by default LFS will also download the binaries
at the "smudge" step.
But we **highly** recommend changing this behavior fetch the artifacts on
demand by setting globally ``git lfs install --skip-smudge``.
It is recommended because it saves a lot of bandwidth and (your precious) time.

.. caution::

   ``GIT_LFS_SKIP_SMUDGE=1`` and ``--skip-smudge`` are not the identical!

   .. shell::
      :no-path:

      # Still fetches with either set.
      $ git lfs pull -I pointer_file
      # Only still fetches with --skip-smudge, skipped with GIT_LFS_SKIP_SMUDGE=1
      $ git lfs smudge < pointer_file > /tmp/file.png``

Instead of applying ``--skip-smudge`` globally, you can set locally (only at
the repository) with:

.. shell::

   $ GIT_LFS_SKIP_SMUDGE=1 git clone https://github.com/analogdevicesinc/system-level \
        --origin public \
        --depth 10 \
        -- system-level
   $ cd system-level
   $ git lfs install --local --force --skip-smudge

With ``--skip-smudge`` active, you can fetch the artifact with:

.. shell::

   ~/system-level
   $git lfs pull -I path/to/my_file.png
   # Checking size
   $ls -l path/to/my_file.png
    -rw-r--r-- 1 me me 34162787 Mar 25 11:09 path/to/my_file.png


And revert to its pointer state:

.. shell::

   ~/system-level
   $rm path/to/my_file.png ; git restore -- $_
   # Checking pointer
   $cat path/to/my_file.png
    version https://git-lfs.github.com/spec/v1
    oid sha256:837ad06a63c0b1c10a02615601f73b7b7596746a62064fe35bb8a4d1543f04a2
    size 34162787

For documentation, you don't need to do it manually, :external+doctools:ref:`serve`
will automatically fetch lfs artifacts of watched touched files and visited pages
on the live server.

In the following subsections are common issues and on what to do in each situation.

.. _files-pointers:

Files that should have been pointers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Git lfs simply follows the rules on the :git-system-level:`.gitattributes` file.
And some times you may encounter during clone and pull:

.. shell::
   :no-path:

   $git pull
    Encountered <n> file(s) that should have been pointers

That simply means that someone pushed files to remote that should have been
pointers (defined in the *.gitattributes* file).
And to fix is simple:

.. shell::

   $git add --renormalize .
   $git commit -m "lfs: convert binary files to pointers" --signoff
   $git push

Then, advise the committer to ensure he has git LFS enabled with
``git lfs install`` and to read this page.

.. _git-lfs-ssl-issues:

Failed to verify certificate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you encounter SSL errors like:

.. shell::

   $ git push
     LFS: Put "<url>" : tls failed to verify certificate: x509: certificate signed by unknown authority

You are likely in a managed network that injects SSL certificates (e.g, Netskope),
if it is the case, seek support from your network admin, this is not a git lfs issue.

Permission denied
~~~~~~~~~~~~~~~~~

If you encounter SSL errors like:

.. shell::

   $ git pull -I path/to/file
     batch request: me@github.com: Permission denied (publickey).: exit status 255

Git lfs is not picking-up the correct credentials automatically, which is
common for multi-remotes setups, you can set explicitely to resolve.

If you use SSH, set the lfs url to:

.. shell::

   $ git config lfs.url "ssh://git@github.com/analogdevicesinc/system-level.git"

If you use HTTPS, set:

.. shell::

   $ git config lfs.url "https://github.com/analogdevicesinc/system-level.git/info/lfs"

If using a fork, change `analogdevicesinc` to your username.

Checking out branches and commits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Git LFS simply follows the rules on the :git-system-level:`.gitattributes` file.
And sometimes you may encounter during checkout:

.. shell::
   :no-path:

   $ git checkout other_branch
    error: Your local changes to the following files would be overwritten by checkout:
            path/to/file/that_should_be_a_pointer.pptx
    Please commit your changes or stash them before you switch branches.
    Aborting

It is the same cause as :ref:`previously <files-pointers>`.
If you don't care about this file at the moment, just ``--force`` your way out.

.. shell::
   :no-path:

   $ git checkout other_branch -f

Pull request permission
~~~~~~~~~~~~~~~~~~~~~~~

When a user creates a pull request, they temporarily grant write permission for
the removal of branches containing commits. However, this does not extend to
LFS:

.. shell::
   :no-path:

   $ git push contributor
    error: Authentication error: Authentication required: You must have push access to verify locks
    error: failed to push some refs to 'https://github.com/<contributor>/system-level.git'

If you **didn't** touch any LFS files, you can just skip the verification:

.. shell::

   $ git push contributor --no-verify
    Writing objects: 100% (8/8), 1.08 KiB | 1.08 MiB/s, done.
    Total 8 (delta 6), reused 0 (delta 0), pack-reused 0 (from 0)
    To https://github.com/contributor/system-level.git
       21s72b2..1b31311  branch-name -> branch-name

But if you did add **new** or **modified** LFS artifacts, the push will fail:

.. shell::

   $ git push contributor --no-verify
    Writing objects: 100% (8/8), 1.08 KiB | 1.08 MiB/s, done.
    Total 8 (delta 6), reused 0 (delta 0), pack-reused 0 (from 0)
    remote: Resolving deltas: 100% (6/6), completed with 6 local objects.
    remote: error: GH008: Your push referenced at least 1 unknown Git LFS object:
    remote:     9b439f0ad3b1e8e965955487b72e84045e85fb844392890c7d34ba45b3430c1e
    remote: Try to push them with 'git lfs push --all'.
    To https://github.com/<contributor>/system-level.git


As a reviewer, this gets on the way and there is no straightforward
solution beyond not pushing commits with new LFS artifacts, or awkwardly requesting
contributor permissions to their repository.

If you wish to add new LFS artifacts, as a reviewer, simply merge the PR and commit to the
further changes.
If the pull request is complex, you can push to a new branch, work on it, and
once both parties are satisfied, close the original PR without merging, merging
the branch onto the main remote instead.

For rebasing, if you **won't** touch any LFS file, you can temporarily
disable lfs, work, push, and enable again:

.. shell::

   $ git lfs uninstall
    Hooks for this repository have been removed.
    Global Git LFS configuration has been removed.
   # Restore any smudged file to its pointer state, to make sure no miss touches
   $ git restore .
   # Work, work, work...
   $ git rebase -i @~20
   # Push even to a contributor's fork with an open PR
   # Re-install lfs
   $ git lfs install --skip-smudge
   $ git push contributor --no-verify --force
    Writing objects: 100% (4/4), 768 bytes | 768.00 KiB/s, done.
    Total 16 (delta 10), reused 0 (delta 0), pack-reused 0 (from 0)
    To https://github.com/contributor/system-level.git
       21s72b2..1b31311  branch-name -> branch-name
