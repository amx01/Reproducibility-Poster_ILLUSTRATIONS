Reproducibility Illustrations
====================================

This is the repository for reproducibility part for the poster presentation at the launch of the Berkeley Institute for Data Science at Sutardja Dai Hall. The Data Science Faire will be held from 1 to 3pm on 12th Dec, 2013.


Summary Report
---------------
In this part, we will mainly discuss the current research on data science regarding reproducibility as well as experiences in the course Reproducible and Collaborative Data Science offered by the Statistics Department in Fall 2013 from the students' point of view. The summary paragraph that will be appear on the poster is at [paragraph.md](https://github.com/amx01/Reproducibility-Poster_ILLUSTRATIONS/blob/master/paragraph.md).


Data Visualization
------------------
In this repo, you will find the data visualization from students in response to the survey conducted regarding reproducibility. I have parsed the survey response and tokenize each word to generate a frequency distribution. The frequency distribution of each word is presented as bubble cloud so that user can clearly see the words that appear most frequently regarding the topic of reproducibility. User can select options to view the visualization. They can see all the word frequencies in the first view; words that appear more than two times in the second view and words appear more than 3 times in the third view. In addition, it is implemented with d3.js and user can drag to re-dimension to view and interact by dragging the words in different positions. The simulation is hosted at the [amx01.github.io](http://amx01.github.io/) and you can try it out. This simulation can be both shown during the data science faire and in a session of the poster to generalize the summary of the survey response. The snapshots are shown as follow:

**All Word Frequencies**
![fq1](https://github.com/amx01/Reproducibility-Poster_ILLUSTRATIONS/blob/master/survey/word-fq1.jpg?raw=true)



**2 or above Word Frequencies**
![fq2](https://github.com/amx01/Reproducibility-Poster_ILLUSTRATIONS/blob/master/survey/word-fq2.jpg?raw=true)



** 3 or above Word Frequencies**
![fq3](https://github.com/amx01/Reproducibility-Poster_ILLUSTRATIONS/blob/master/survey/word-fq3.jpg?raw=true)

The bubble cloud framework is built on top of [vallandingham](http://vallandingham.me/building_a_bubble_cloud.html)
