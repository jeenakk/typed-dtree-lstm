from tqdm import tqdm
import numpy as np
import torch

from . import utils


class Trainer(object):
    def __init__(self, args, model, criterion, optimizer, device):
        super(Trainer, self).__init__()
        self.args = args
        self.model = model
        self.criterion = criterion
        self.optimizer = optimizer
        self.device = device
        self.epoch = 0

    # helper function for training
    def train(self, dataset):
        self.model.train()
        self.optimizer.zero_grad()
        total_loss = 0.0
        indices = torch.randperm(len(dataset), dtype=torch.long, device='cpu')
        for idx in tqdm(range(len(dataset)), desc='Training epoch ' + str(self.epoch + 1) + ''):
            ltree, linput, rtree, rinput, label, lroles, rroles = dataset[indices[idx]]
            # For scoring SICK dataset
            target = utils.map_label_to_target(label, dataset.dataset.num_classes)
            # For Quora classification
            #target = torch.zeros(1,dataset.num_classes, dtype=torch.float, device='cpu')
            #print(label,"label")
            #target[0,int(label)]=1
            linput, rinput, lroles, rroles = linput.to(self.device), rinput.to(self.device),lroles.to(self.device), rroles.to(self.device)
            target = target.to(self.device)
            output = self.model(ltree, linput, rtree, rinput, lroles, rroles)
            loss = self.criterion(output, target)
            total_loss += loss.item()
            loss.backward()
            if idx % self.args.batchsize == 0 and idx > 0:
                self.optimizer.step()
                self.optimizer.zero_grad()
        self.epoch += 1
        return total_loss / len(dataset)

    # helper function for testing
    def test(self, dataset):
        self.model.eval()
        with torch.no_grad():
            total_loss = 0.0
            predictions = torch.zeros(len(dataset), dtype=torch.float, device='cpu')
            indices = torch.arange(1, dataset.num_classes + 1, dtype=torch.float, device='cpu')
            for idx in tqdm(range(len(dataset)), desc='Testing epoch  ' + str(self.epoch) + ''):
                ltree, linput, rtree, rinput, label,lroles, rroles = dataset[idx]
                # For scoring SICK dataset
                target = utils.map_label_to_target(label, dataset.dataset.num_classes)
                # For Quora classification
                #target = torch.zeros(1,dataset.num_classes, dtype=torch.float, device='cpu')
                #target[0,int(label)]=1 
                linput, rinput, lroles, rroles = linput.to(self.device), rinput.to(self.device),lroles.to(self.device), rroles.to(self.device)
                target = target.to(self.device)
                output = self.model(ltree, linput, rtree, rinput, lroles, rroles)
                loss = self.criterion(output, target)
                total_loss += loss.item()
                output = output.squeeze().to('cpu')
                # Use argmax for classifier(as in Quora) and dot for scoring (SICK)
                #predictions[idx] = np.argmax(torch.exp(output))
                predictions[idx] = torch.dot(indices, torch.exp(output))
        return total_loss / len(dataset),predictions #--> for quora
