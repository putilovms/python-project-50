from gendiff.normalizer import normalize_value
import gendiff.constants as const


def pre_stylish(tree):
    TAB = {const.EQUAL: '  ', const.DEL: '- ',
           const.ADD: '+ ', const.UNFORM: '  '}
    result = {}
    for k, v in tree.items():
        if isinstance(v, list) and \
                (isinstance(v[0], dict) or (isinstance(v[2], dict))):
            if v[1] == const.EDIT:
                result[TAB[const.DEL] + k] = pre_stylish(
                    tree[k][0]) if isinstance(v[0], dict) else tree[k][0]
                result[TAB[const.ADD] + k] = pre_stylish(
                    tree[k][2]) if isinstance(v[2], dict) else tree[k][2]
            else:
                result[TAB[v[1]] + k] = pre_stylish(tree[k][0])
        elif isinstance(v, list):
            if v[1] == const.EDIT:
                result[TAB[const.DEL] + k] = tree[k][0]
                result[TAB[const.ADD] + k] = tree[k][2]
            else:
                result[TAB[v[1]] + k] = tree[k][0]
        else:
            result[TAB[const.UNFORM] + k] = pre_stylish(
                tree[k]) if isinstance(v, dict) else tree[k]
    return result


def format_stylish(ast_tree):
    def walk(tree, acc, depth=0):
        R = '    '
        for k, v in tree.items():
            r = (R * (depth + 1))
            if isinstance(v, dict):
                acc.append(r[:-2] + k + ': {')
                walk(v, acc, depth + 1)
                acc.append(r + '}')
            else:
                acc.append(r[:-2] + k + ': ' + normalize_value(v))
    result = []
    result.append("{")
    walk(pre_stylish(ast_tree), result)
    result.append("}")
    return result
