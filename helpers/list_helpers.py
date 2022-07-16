from typing import List, Dict, Union, Any


def get_hierarchy_list(data: List[dict], hierarchy_name_field: str, name_field_name: str = 'name') \
        -> List[Dict[str, Union[Union[dict, None, list], Any]]]:
    """
    Построение иерархичного списка для TreeView

    :param data: Список данных
    :param hierarchy_name_field: Поля, по которому строиться иерархия
    :param name_field_name: Имя поля для отображения
    :return: Иерархичный список для TreeView
    """
    result = {}

    if not data:
        raise RuntimeError('Не переданы данные для построения списка')

    if not hierarchy_name_field:
        raise RuntimeError('Не передано поле для построения иерархии')

    for item in data:
        if item.get(hierarchy_name_field, False) is None:
            result[item.get('id')] = {
                'item': item,
                'label': item.get(name_field_name),
                'children': []
            }
        else:
            result[item.get(hierarchy_name_field)].get('children').append({
                'item': item,
                'label': item.get(name_field_name)
            })

    return list(result.values())
