from copy import deepcopy

import torch


class Metrics():
    def __init__(self, num_classes):
        self.num_classes = num_classes

    def pearson(self, predictions, labels):
        x = deepcopy(predictions)
        y = deepcopy(labels)
        x = (x - x.mean()) / x.std()
        y = (y - y.mean()) / y.std()
        return torch.mean(torch.mul(x, y))

    def mse(self, predictions, labels):
        x = deepcopy(predictions)
        y = deepcopy(labels)
        return torch.mean((x - y) ** 2)
        
    def accuracy(self, predictions, labels):
        x = deepcopy(predictions)
        y = deepcopy(labels)
        print (x.dtype,y.dtype)
        #print(torch.sum(x==y))
        print(torch.sum(x==y))
        return torch.sum(x==y).float()/float(y.size()[0])

    def spearmanr(self, predictions, labels):
        x = deepcopy(predictions)
        y = deepcopy(labels)
        corr, p_value = spearmanr(x.numpy(), y.numpy())
        return corr

    def prf1_score(self, predictions, labels):
        assert labels.ndim == 1
        assert predictions.ndim == 1 
        tp = (labels * predictions).sum()
        tn = ((1 - labels) * (1 - predictions)).sum()
        fp = ((1 - labels) * predictions).sum()
        fn = (labels * (1 - predictions)).sum()
        if((tp + fp) == 0) or ((tp + fn) == 0) : 
            return torch.tensor([-1,-1,-1])
        precision = tp / (tp + fp)
        recall = tp / (tp + fn)
        f1 = 2* (precision*recall).float() / (precision + recall).float()
        return precision, recall, f1
