Install miniconda

`./Miniconda3-latest-Linux-x86_64.sh`

It will create an environment in bash, so when using different shell, type `bash` afterwards

Most libraries can be installed by `conda install libraryname` and they will be automatically picked up
by tools using the libraries (e.g. DataSpell)

To export jupyter notebooks to PDF via Latex:

```bash
sudo apt-get install texlive-xetex texlive-fonts-recommended texlive-plain-generic
```

run `xelatex` from the command line to check if the installation worked


Create a Jupyter notebook (.ipynb file), then

Run `jupyter notebook` from the same directory as the file you created

Export to PDF via Latex, or print preview and then advanced to pick the right page size


Examples and csv file from  https://www.jetbrains.com/help/dataspell/quick-start-guide.html#work-with-notebooks

## Exporting jupyter notebooks

1. From the directory where `jn3.ipynb` is located
```bash
jupyter notebook
```

2. Open the jpynb file
3. file -> print preview
4. firefox print, select the appropriate size, save as pdf
5. result for A3 size:  `jn3_via_print_preview.pdf`

