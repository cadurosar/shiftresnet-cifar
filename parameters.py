import argparse

binarized = False
display = False
temperature = 1.0
maxvalue = 0

 
parser = argparse.ArgumentParser(description='PyTorch CIFAR10 Training')
parser.add_argument('--lr', default=0.1, type=float, help='learning rate')
parser.add_argument('--resume', '-r', action='store_true', help='resume from checkpoint')
parser.add_argument('--batch_size', '-b', default=128, type=int, help='batch size')
parser.add_argument('--arch', '-a', default='shiftresnet110', help='neural network architecture')
parser.add_argument('--expansion', '-e', help='Expansion for shift resnet.', default=1, type=float)
parser.add_argument('--reduction', help='Amount to reduce raw resnet model by', default=1.0, type=float)
parser.add_argument('--reduction-mode', choices=('block', 'net', 'depthwise'), help='"block" reduces inner representation for BasicBlock, "net" reduces for all layers', default='net')
parser.add_argument('--dataset', choices=('cifar10', 'cifar100', 'imagenet'), help='Dataset to train and validate on.', default='cifar10')
parser.add_argument('--datadir', help='Folder containing data', default='./data/')
parser.add_argument('--feature_maps', default=16, type=int, help='Number of feature_maps for first blocks')
parser.add_argument('--kernel_size', default=3, type=int, help='Kernel size')
parser.add_argument('--dropout', default=0., type=float, help='dropout')

args = parser.parse_args()

