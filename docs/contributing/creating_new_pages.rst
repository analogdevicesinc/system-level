.. _creating-new-pages:

Creating new pages
==================

The first step on adding new content is to understand the
:ref:`creating-new-pages documentation-structure`.
Then, proceed with :ref:`creating-new-pages adding-content`.

.. _creating-new-pages documentation-structure:

Documentation structure
-----------------------

:git-system-level:`This </>` repository hosts any type of content that is not
version controlled with a particular source code, or in other words,
"don't deserve their own repository".

Due to this, there are multiple topics,
for example, there is information from
:ref:`linux drivers`
to
:ref:`Evaluation boards user guides <reference-designs>`.

As an analogy, if this documentation were a encyclopedia, each topic would be
a volume.

To create each "volume", two
`toctrees <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-toctree>`__
replicate the structure of the context top level.

For example, while in :git-system-level:`docs/index.rst#L24`
we have:

.. code:: rst


   .. toctree::
      :caption: Linux Kernel & Software
      :maxdepth: 2
      :glob:

      linux/*/index

At the specific context toctree (:git-system-level:`docs/linux/index.rst#L9`)
we have:

.. code:: rst

   .. toctree::
      :glob:

      */index

*Glob* is used to match any document that matches the pattern and avoids simple
but annoying merge conflicts of contributors adding pages to the same toctree
at the same time.

Use case for the structure
~~~~~~~~~~~~~~~~~~~~~~~~~~

This structure enables to concatenate other documentations ("volumes") to this
one, allowing to generate an aggregated monolithic output, for example.

Suppose we have a repository called ``my-repo`` with the following toctree:

.. code:: rst

   .. toctree::
      :glob:

      */index

.. tip::

   Notice the usage of the ``:glob:`` options.
   It is particular useful to avoid merge conflict scenarios.


To add to this doc, we only need to append to *docs/index.rst* as:

.. code:: rst

   .. toctree::
      :glob:

      my-repo/*/index

And copy ``my-repo/docs`` as ``system-level/docs/my-repo`` (mostly).

.. _creating-new-pages template:

Content templates and guidelines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Templates and guidelines for specific types of content are available:

.. toctree::
   :glob:
   :titlesonly:

   template/*

.. _creating-new-pages adding-content:

Adding content
--------------

The documentation is highly hierarchical and contextual, that means a page
about "Peeling Blue Bananas" should be located at
``fruits/banana/blue/peeling.rst``
and **not** ``eval/tutorial-peeling_blue_bananas.rst``.

The title should also be kept short, since it directly inherits the context from
the hierarchical structure, so it's preferred:

.. code:: rst

   Peeling blue bananas
   =====================

Over:

.. code:: rst

   Fruits tutorials: peeling blue bananas
   ======================================

At the ``toctree``, the title shall be overwritten to reduce the title length
on the sidebar further:

.. code:: rst

   Blue bananas
   ============

   .. toctree::

      Peeling <peeling>
      Recipes <recipes>

.. tip::

   Don't overthink the location of the content, it can be easily moved later.
   Just try to keep it *contextual* and *hierarchical*.


Having that in mind, proceed with creating the directories, toc-entries, and
files for your content:

.. shell::
   :no-path:

   $cd ~/system-level/docs ; pwd
    ~/system-level/docs
   $mkdir my_topic
   # Add "My Topic" to the main index
   $vi index.rst
   # Create topic/volume index
   $vi my_topic/index.rst
   # Create more content
   $vi my_topic/page0.rst my_topic/page1.rst
   # Add/create images
   $cp ~/some-image.svg my_topic/
    ...

Edit *my_topic/index.rst*, adding a title and some content.

Build the doc and see the changes:

.. shell::

   ~/system-level
   $ adoc serve --once

Sphinx only rebuilds modified files, so subsequent builds are faster.
If you encounter issues with the current build, try cleaning the cache with
``cd docs ; make clean``.

.. tip::

   Use :external+doctools:ref:`serve sparse` to build only the pages you are
   interested.

   .. shell::

      ~/system-level/docs
      # Include only learning/**/* and solutions/**/*
      $ adoc serve --once --sparse learning solutions

:external+doctools:ref:`serve` also supports live-updating the doc (drop the
``--once`` flag), you just need to save the file and the build will be
triggered automatically.

Adding images and other binary files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As described in :ref:`forking-publishing`, this repository leverages
`git-lfs <https://git-lfs.com/>`__ to keep clone time low and storage space
in check.
It also recommends setting ``--skip-smudge`` globally and let :external+doctools:ref:`serve`
manage them for you.

When adding images and other binary files, if the extension matches the :git-system-level:`.gitattributes`
file, git lfs will automatically create a symbolic link and upload to the remote with
``git lfs push public --all``.

Please remember that repository write permission is required for pushing git lfs artifacts,
so if you are working on a fork, push them to your fork, and a reviewer can fetch and push to public/origin
accordingly.

Finally, if you are adding a binary type not in the :git-system-level:`.gitattributes` file, please add it
to it also, this way we can keep the repository lean and efficient long-term.

.. _importing-dokuwiki:

Importing from DokuWiki
~~~~~~~~~~~~~~~~~~~~~~~

To import content from dokuwiki, a script is available to help on this task:
`DokuWiki to Sphinx (bash.sh) <https://gist.github.com/gastmaier/9d9c8281dc3c8551991a857cdb2692cc>`__.

It requires you have ``pandoc`` and ``sed`` installed:

.. code:: bash

   sudo apt install pandoc sed

It will try its best to reduce the amount of manual work necessary, still,
please review the content carefully.

For images, ensure to click on the image on *wiki.analog.com* to ensure you
download the original and not the compressed image.

Always prioritize vector images (*.svg*).

Finally, content yet not imported, keep/use the :external+doctools:ref:`role dokuwiki`.
And for deprecated content, add the qualifier ``+deprecated``, for example:

::

    :dokuwiki+deprecated:`Old content <resources/old/content>`

The reason for this is that with this differentiation we can easily track yet
to import pages and deprecated content with:

.. shell::

   ~/system-level/docs
   $grep --exclude-dir=_build -rnw :dokuwiki:
    software/libiio/internals.rst:58:like :dokuwiki:`GNU Radio ...
    software/libiio/index.rst:270::dokuwiki:`here <resources/t ...
    ...
   $grep --exclude-dir=_build -rnw :dokuwiki+deprecated:
    software/libiio/index.rst:54:* :dokuwiki+deprecated:`Beac ...
    ...

