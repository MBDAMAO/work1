def replace_duplicate_chars(input_str, k):
    output_str = list(input_str)
    replaced = [False] * len(output_str)
    for i in range(len(output_str)):
        if not replaced[i]:
            for j in range(1, k + 1):
                if i - j >= 0 and output_str[i - j] == output_str[i]:
                    output_str[i] = '-'
                    replaced[i] = True
                    break
    return ''.join(output_str)

# 输入格式为 "字符串 k"
input_data = input("输入字符串和k值：")
input_list = input_data.split()
input_str = input_list[0]
k = int(input_list[1])

# 调用函数并输出结果
output_str = replace_duplicate_chars(input_str, k)
print(output_str)
