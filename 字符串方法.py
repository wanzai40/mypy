my_str = 'when i was 13 i had my first love'
# 统计有多少个i
const = my_str.count('i')
print(f'统计有多少个i: {const}')

# 格空替换为 |
replacement = my_str.replace(' ','|')
print(f'格空替换为 | : {replacement}')

# 按照| 分割成列表
partition = replacement .split('|')
print(f'{partition}')