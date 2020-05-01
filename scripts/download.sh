#!/bin/bash
set -e

echo "Downloading SICK dataset"
mkdir -p data/sick/
cd data/sick/
wget -q -c http://alt.qcri.org/semeval2014/task1/data/uploads/sick_train.zip
unzip -q -o sick_train.zip
wget -c http://alt.qcri.org/semeval2014/task1/data/uploads/sick_trial.zip
unzip -q -o sick_trial.zip
wget -c http://alt.qcri.org/semeval2014/task1/data/uploads/sick_test_annotated.zip
unzip -q -o sick_test_annotated.zip
rm *.zip readme.txt
cd ../../

echo "Downloading Stanford parser and tagger"
cd lib/
wget -q -c https://nlp.stanford.edu/software/stanford-postagger-2018-10-16.zip
unzip -q stanford-postagger-2018-10-16.zip
mv stanford-postagger-2018-10-16.zip/ stanford-tagger
rm stanford-postagger-2018-10-16.zip

wget -q -c https://nlp.stanford.edu/software/stanford-parser-full-2018-10-17.zip
unzip -q stanford-parser-full-2018-10-17.zip
mv stanford-parser-full-2018-10-17.zip/ stanford-parser
rm stanford-parser-full-2018-10-17.zip
cd ../


echo "Downloading GLOVE"
mkdir -p data/glove/
cd data/glove/
wget -c http://www-nlp.stanford.edu/data/glove.840B.300d.zip
unzip glove.840B.300d.zip
rm glove.840B.300d.zip
