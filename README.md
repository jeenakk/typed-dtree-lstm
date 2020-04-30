# Typed Dependency Tree LSTM in Pytorch

This is a PyTorch implementation of Typed Dependency Tree-LSTM as published in the paper [An enhanced Tree-LSTM architecture for sentence semantic modeling using typed dependencies](https://arxiv.org/abs/2002.07775) by Jeena Kleenankandy and Dr. K. A. Abdul Nazeer.

## Requirements

    Python (tested on 3.6.5, should work on >=2.7)
    Java >= 8 (for Stanford CoreNLP utilities)
    Other dependencies are in requirements.txt 

## Contents :

- `fetch_and_preprocess.sh` :   
    - downloads the SICK dataset, Stanford Parser and POS Tagger, and Glove word vectors (Common Crawl 840)
    - generate the dependency parses using Stanford Neural Network Dependency Parser.
- `main.py` : does training and testing of the model. 
- `config.py`: list of all command-line arguments and their default values
- `TD_set.py` : list of universal dependencies used (update this list if you are using a different version)
        
## Usage

To run the code execute these steps :
```
- bash fetch_and_preprocess.sh
- pip install -r requirements.txt
- python main.py
```

## Acknowledgements

Shout-out to [Riddhiman Dasgupta](https://dasguptar.github.io/) for Pytorch implementation of the paper [Improved Semantic Representations From Tree-Structured Long Short-Term Memory Networks](https://arxiv.org/abs/1503.00075), which served as a starter code for this project.
