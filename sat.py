import torch
import torch.nn
import parameters

class ShiftAttention(torch.nn.Conv2d):

    def __init__(self, in_features, out_features, stride=1, bias=False, padding = 0, kernel_size=3):
        super(ShiftAttention, self).__init__(in_features, out_features, stride = stride, bias = bias, padding = padding, kernel_size = kernel_size)
        self.in_features = in_features
        self.out_features = out_features
        self.kernel_width = kernel_size
        # self.temperature = temperature
        # self.bias = bias
        # self.stride = stride
        # self.padding = padding
        # self.conv = torch.nn.Conv2d()
        self.attentionWeights = torch.nn.parameter.Parameter(torch.FloatTensor(out_features, in_features, kernel_size* kernel_size))
        torch.nn.init.normal_(self.attentionWeights)

    def forward(self,input):
        # attention = torch.nn.functional.normalize(self.attentionWeights, dim=2, p=2)
        attention = self.attentionWeights / self.attentionWeights.std(dim=2).view(self.out_features, self.in_features, -1)
        attention = torch.nn.functional.softmax(parameters.temperature * attention, dim = 2)
        parameters.maxvalue = torch.max(attention[0,0,:]).item()
        attention = attention.view(self.out_features, self.in_features, self.kernel_width, self.kernel_width)
        #final_attention = attention.clone()
        #while final_attention.shape[0] < self.weight.shape[0]:
        #    final_attention = torch.cat([final_attention,attention],dim=0)
        #attention = final_attention
        if parameters.binarized:
            attention = torch.round(attention)
        if parameters.display:
            print(torch.max(attention[0,0,:]))
        attention = attention * self.weight
        return torch.nn.functional.conv2d(input, attention, bias = self.bias, stride = self.stride, padding = self.padding)


