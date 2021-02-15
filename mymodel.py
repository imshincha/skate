import timm
from pprint import pprint
model_names = timm.list_models(pretrained = True)
model = timm.create_model('efficientnet_b3a', pretrained = True)
model.eval()
