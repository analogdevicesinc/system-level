# System Level Documentation

The System Level Documentation is the top documentation for Hardware, Projects, and some Linux documentation;
it also has the ability to aggregate every other documentation into a single monolithic output/website.

See the deployed docs output at the [System Level Documentation](https://analogdevicesinc.github.io/system-level/) index.

> [!WARNING]
> This repository contains a massive amount of data!
> Don't clone or build before reading the instructions below, or will make your local builds painfully slow and trigger unnecessary bandwidth costs.
> Always use ``--skip-smudge`` and ``adoc serve --sparse``

## Getting started

The repository uses Git LFS to host large files.
To not download all large files at the HEAD commit, use `--skip-smudge` and let [adoc serve](https://analogdevicesinc.github.io/doctools/cli.html#serve) fetch them as you navigate the live server and touches files:

```
sudo apt install git-lfs -y
GIT_LFS_SKIP_SMUDGE=1 git clone https://github.com/analogdevicesinc/system-level \
    --origin public \
    --depth 10 \
    -- system-level
cd system-level
git lfs install --local --force --skip-smudge
```

Install the documentation tools.
```
python3 -m venv ./venv
source ./venv/scripts/activate
python3 -m ensurepip
pip install pip --upgrade
(cd docs ; pip install -r requirements.txt --upgrade)
```
Launch the live server, building only `docs/contributing`.
```
adoc serve --sparse docs/contributing
```
You can pass multiple paths as ``--sparse`` arguments, or remove it to build the whole documentation.
The generated documentation will be available at `docs/_build/html`.

### VSCode/VSCodium support

### Esbonio extension

[Esbonio](https://docs.esbon.io/en/latest/index.html)
([VSCode](https://marketplace.visualstudio.com/items?itemName=swyddfa.esbonio)
/[VSCodium](https://open-vsx.org/extension/swyddfa/esbonio))

is an extensively developed Language Server Protocol and Visual Studio Code extension for sphinx.
Setup the virtual environment first before opening the text editor, to avoid triggering fallback behaviours.

The live server cli is able to generate Estobio pyproject.toml entry with (including [Sparse builds](https://analogdevicesinc.github.io/doctools/cli.html#serve-sparse)):
```
adoc serve --esbonio --sparse docs/learning | tee pyproject.toml
```

### Doctools extension

An experimental doctools extension is available for
[VSCode](https://marketplace.visualstudio.com/items?itemName=gastmaier.adi-doctools)
/[VSCodium](https://open-vsx.org/extension/gastmaier/adi-doctools).

Quick start instructions are provided in the links above.

### Git LFS On-Demand extension

Assuming you followed the `--skip-smudge` instructions, you can use Git LFS On-Demand to auto fetch the artifacts included in open files or open.
Get from
[Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=gastmaier.git-lfs-on-demand) or
[Open VSX Registry](https://open-vsx.org/extension/gastmaier/git-lfs-on-demand)

For word wrapping at the column 80, you can use Rewrap.
Get from
[Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=stkb.Rewrap-18980) or
[Open VSX Registry](https://open-vsx.org/extension/stkb/rewrap)
