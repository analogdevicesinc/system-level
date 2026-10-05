.. _docs_guidelines:

Documentation guidelines
========================

This documentation is built with `Sphinx <https://www.sphinx-doc.org>`_ and
all source code is available at the path :git-system-level:`docs`.

To contribute to it, first read :ref:`forking-publishing`,
read the guidelines
(both the :external+doctools:ref:`general <docs_guidelines>` **and** the
additional guidelines below)
and also :ref:`creating-new-pages`.

When you are satisfied with your contribution, open a pull request with the
changes to :git-system-level:`this repository </>`.

Templates
---------

Any page can be used as a template.

In particular, for evaluation board user-guide, use the :ref:`adrv9009` pages
as a template.

For (future) template pages with ``:orphan:`` on the first line, remove it.
This marker is used to hide the templates from the
`TOC tree <https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-toctree>`_.

Also, instructions using the comment syntax may be present on the page and also
need to be removed.
Those comments have the format:

::

   ..
      I'm a comment

