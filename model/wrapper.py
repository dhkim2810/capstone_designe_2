from .mlp import MLP
from .lenet import LeNet
from .alexnet import AlexNet
from .convnet import ConvNet
from .vgg import VGG
from .resnet import ResNet18, ResNet18BN, ResNet18BN_AP

class ModelWrapper():
    def __init__(self, model, **kwargs):
        self.channel = kwargs.get('channel', 3)
        self.num_classes = kwargs.get('num_classes', 10)
        self.img_size = kwargs.get("image_size", (32,32))
        self.set_model(model)
    
    def set_model(self, model):
        if model == 'MLP':
            self.net = MLP(self.channel, self.num_classes)
        elif model == 'LeNet':
            self.net = LeNet(self.channel, self.num_classes)
        elif model == 'Alexself.net':
            self.net = AlexNet(self.channel, self.num_classes)
        elif 'Convself.net' in model:
            net_width, net_depth, net_act, net_norm, net_pooling = self.get_ConvNet_config(model)
            self.net = ConvNet(self.channel, self.num_classes, net_width, net_depth, net_act, net_norm, net_pooling, self.img_size)
        elif 'VGG' in model:
            self.net = VGG(model, self.channel, self.num_classes, norm='batchnorm' if 'BN' in model else 'instancenorm')
        elif model == 'ResNet18':
            self.net = ResNet18(self.channel, self.num_classes)
        elif model == 'ResNet18BN':
            self.net = ResNet18BN(self.channel, self.num_classes)
        elif model == 'ResNet18BN_AP':
            self.net = ResNet18BN_AP(self.channel, self.num_classes)
    
    def get_ConvNet_config(self, model):
        net_width = 128
        net_depth = 3
        net_act = 'relu'
        net_norm = 'instancenorm'
        net_pooling = 'avgpooling'
        
        if model ==  'ConvNetD1':
            net_depth = 1
        elif model == 'ConvNetD2':
            net_depth = 2
        elif model == 'ConvNetD3':
            net_depth = 3
        elif model == 'ConvNetD4':
            net_depth = 4
            
        elif model == 'ConvNetW32':
            net_width = 32
        elif model == 'ConvNetW64':
            net_width = 64
        elif model == 'ConvNetW128':
            net_width = 128
        elif model == 'ConvNetW256':
            net_width = 256

        elif model == 'ConvNetAS':
            net_act = 'sigmoid'
        elif model == 'ConvNetAR':
            net_act = 'relu'
        elif model == 'ConvNetAL':
            net_act = 'leakyrelu'

        elif model == 'ConvNetNN':
            net_norm = 'none'
        elif model == 'ConvNetBN':
            net_norm='batchnorm'
        elif model == 'ConvNetLN':
            net_norm='layernorm'
        elif model == 'ConvNetIN':
            net_norm='instancenorm'
        elif model == 'ConvNetGN':
            net_norm='groupnorm'

        elif model == 'ConvNetNP':
            net_pooling='none'
        elif model == 'ConvNetMP':
            net_pooling='maxpooling'
        elif model == 'ConvNetAP':
            net_pooling='avgpooling'
        
        return net_width, net_depth, net_act, net_norm, net_pooling