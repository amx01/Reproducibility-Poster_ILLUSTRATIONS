# The Tools of Reproducible Science in Stat 157

## IPython Notebook

We use the IPython Notebook to take our work from data curation to analysis to visualization -- all in one place.  Instead of using one script to fetch and clean the data, another script to analyze it, and yet another to visualize it -- sometimes in different languages -- before pasting it all into a presentation, the IPython Notebook keeps the process in one place.  It is an exceptional tool because it can be run in real-time while presenting.  It makes the code part of the presentation, which allows anyone to see not only the final, polished results, but also the steps taken to produce them. See an example [here](http://nbviewer.ipython.org/github/stat157/analyzers/blob/master/notebooks/aftershock_arrival_plots.ipynb)!

## GitHub

By publicly posting our code to GitHub and keeping it in a neatly-curated repository, our process remains transparent and reproducible.  Anyone can download and run our code, and if they have trouble they can simply post an issue.  Git also keeps track of the lifecycle of the code, in case someone wants to see a previous version.  See an example [here](https://github.com/stat157/analyzers/)!

## VirtualBox/Vagrant

We use virtual machines to run our code in a controlled environment: we decide which operating system and programs to use.  We use Vagrant to package this environment and make it easy to download and start running.  It guarantees that our code is able to run and that our results can be replicated on anyone's computer, no matter the operating system on their laptop.  It has the added benefit of already having the necessary programs and dependencies installed, to save time and headache for the person trying to reproduce our work.  See an example [here](https://github.com/stat157/analyzers/blob/master/notes/vagrant_setup.md)!
