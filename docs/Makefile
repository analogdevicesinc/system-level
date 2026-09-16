SHELL         = /bin/bash
SPHINXOPTS   ?= -j auto
SPHINXBUILD  ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

help:
	$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Watch all .svg files under this directory and `touch` any .rst that
# embeds them via `.. svg::` whenever an SVG changes. Run alongside
# `adoc serve` in a second terminal. Works around the fact that the
# adi_doctools .. svg:: directive does not register the SVG as a
# Sphinx dependency, so SVG-only edits otherwise need a manual `touch`
# (or `make clean`) to be picked up.
svg-watch:
	python3 svg-watch.py

.PHONY: help Makefile svg-watch

%: Makefile
	@if [ -t 0 ]; then \
		printf "Use \033[0;34madoc serve --sparse <path>\033[0m for faster build time.\n"; \
		read -p "Continue? (yes/no) " yn ; \
		case $$yn in \
			y ) ;; \
			yes ) ;; \
			* ) exit 1 ;; \
		esac ; \
	fi
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
