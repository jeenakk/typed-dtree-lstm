PAD = 0
UNK = 1
BOS = 2
EOS = 3

PAD_WORD = '<blank>'
UNK_WORD = '<unk>'
BOS_WORD = '<s>'
EOS_WORD = '</s>'

# Complete list of typed dependency relation from stanford dependency parser
TD_SET = './treelstm/TD_set.txt'
TD_List = open(TD_SET).read().splitlines()

# Number of TDs in the TD_SET
DR_SIZE = 56
