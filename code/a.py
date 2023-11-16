import torch

print(f'is_tensor : {torch.is_tensor(torch.tensor([1, 2, 3]))}')
print(f'is_storage : {torch.is_storage(torch.tensor([1, 2, 3]))}')
