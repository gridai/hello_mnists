import os
import torch
import torch.nn.functional as F
from torchvision.datasets import CIFAR10
from torchvision import transforms
from torch.utils.data import DataLoader
import pytorch_lightning as pl
from torch.utils.data import random_split
from pytorch_lightning.metrics.functional import accuracy

class LitModel(pl.LightningModule):

    def __init__(self, lr:float = 0.0001, batch_size:int = 32):
        super().__init__()
        self.save_hyperparameters()
        self.layer_1 = torch.nn.Linear(3 * 32 * 32, 128)
        self.layer_2 = torch.nn.Linear(128, 10)

    def forward(self, x):
        x = x.view(x.size(0), -1)
        x = self.layer_1(x)
        x = F.relu(x)
        x = self.layer_2(x)
        x = F.log_softmax(x)
        return x

    def configure_optimizers(self):
        optimizer = torch.optim.Adam(self.parameters(), lr=self.hparams.lr)
        return optimizer

    def training_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = F.nll_loss(y_hat, y)
        self.log('train_loss', loss)
        self.log('train_acc', accuracy(y_hat.exp(), y), prog_bar=True)
        return loss

if __name__ == '__main__':
    from configargparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('--gpus', type=int, default=0)
    parser.add_argument('--lr', type=float, default=1e-3, env_var="CIFAR_LR")
    parser.add_argument('--batch_size', type=int, default=32, env_var="CIFAR_BATCH_SIZE")
    parser.add_argument('--max_epochs', type=int, default=10, env_var="CIFAR_MAX_EPOCHS")
    parser.add_argument('--data_dir', type=str, default=os.getcwd())
    parser.add_argument('--num_workers', type=int, default=8)
 
    args = parser.parse_args()

    dataset = CIFAR10(args.data_dir, download=True, transform=transforms.ToTensor())
    train_loader = DataLoader(dataset, batch_size=args.batch_size, num_workers=args.num_workers)

    # init model
    model = LitModel(lr=args.lr)

    # most basic trainer, uses good defaults (auto-tensorboard, checkpoints, logs, and more)
    trainer = pl.Trainer(gpus=args.gpus, max_epochs=args.max_epochs)
    trainer.fit(model, train_loader)
