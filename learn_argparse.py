import argparse

parser = argparse.ArgumentParser(description='演示 subparsers 的使用')
subparsers = parser.add_subparsers(dest='command', help='子命令')

# 子命令 add
parser_add = subparsers.add_parser('add', help='添加一个项目')
parser_add.add_argument('--name', required=True, help='项目名称')

# 子命令 delete
parser_delete = subparsers.add_parser('delete', help='删除一个项目')
parser_delete.add_argument('--id', type=int, required=True, help='项目ID')

args = parser.parse_args()

if args.command == 'add':
    print(f"添加项目: {args.name}")
elif args.command == 'delete':
    print(f"删除项目ID: {args.id}")
else:
    parser.print_help()

''' 使用示例：
python myprog.py add --name "测试项目"
输出: 添加项目: 测试项目

python myprog.py delete --id 123
输出: 删除项目ID: 123
'''


''' 有 subparsers 的优势:
| 方面       | `subparsers` 的优势                            |
| -------- | ------------------------------------------- |
| **参数隔离** | 各命令有自己独立的参数，互不影响                            |
| **帮助文档** | `python script.py add --help` 自动显示该命令的参数和说明 |
| **代码组织** | 子命令可以分模块管理，每个命令逻辑清晰                         |
| **自动验证** | argparse 会自动帮你检查缺失或非法参数                     |
| **交互体验** | 可以配合 `argcomplete` 实现 bash/zsh tab 补全       |

'''