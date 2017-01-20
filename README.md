# Description
POS tagger implementation project using Conditional Random Fields with an aim of getting better understanding of it.

## Data

    mkdir data
    cd data
    http http://www.cnts.ua.ac.be/conll2000/chunking/train.txt.gz | gunzip | cut -f1,2 -d" " > pos.train.txt
    http http://www.cnts.ua.ac.be/conll2000/chunking/test.txt.gz | gunzip | cut -f1,2 -d " " > pos.test.txt

## Useful links

 * [Intro to CRF](http://homepages.inf.ed.ac.uk/csutton/publications/crftut-fnt.pdf)
 * [Lafferty, 2001](http://repository.upenn.edu/cgi/viewcontent.cgi?article=1162&context=cis_papers)
 * [Huang, 2015](https://arxiv.org/pdf/1508.01991v1.pdf)
