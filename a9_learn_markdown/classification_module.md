文件名称
-------

#### clasification_module.py
###### version: 0.0.1
###### 当前维护人: 于洋

## 接口说明
> 进行分类的模块

## 整体流程
>1.判断有没有classify的json文件，没有则报错
>
>2.读取classify的json文件，得到clasify_list
>
>3.判断器官是否在classify_list中，若不在则报错

## 输入参数

| 参数               | 必选 | 类型       | 默认值  | 说明                                     |
|:------:           |:----:|:------:   |:------:|:---------------------------------------:|
| info_dict         | ture | InfoDict  |        | 信息字典用于获取路径等信息                  |

## 返回结果
| 返回字段           | 字段类型        | 说明                                             |
|:--------:        |:--------:      |:--------------------------------:                |
| info_dict        | InfoDict       | 返回更新过的信息字典，分类结果会在其中                 |

## 相关错误返回码
| 错误码            |说明                                             |
|:--------:        |:--------------------------------:              |
| xxxxx            |没有classify的json                               |
| xxxxx            |器官不在分类结果中                                 |

## 调用示例
```python
info_dict = classification(info_dict)
```

## 维护历史
| 代码版本           | 维护时间        | 维护人 | 修改历史                                  |
|:--------:        |:--------:      |:---:  |:---:                                          |
| 0.0.1            | 2018.12.06     | 于洋   | 创建文件                                  |