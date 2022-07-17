# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a1_hello_milvus.py
@Time: 2022-05-18 16:50
@Last_update: 2022-05-18 16:50
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
# This program demos how to connect to Milvus vector database,
# create a vector collection,
# insert 10 vectors,
# and execute a vector similarity search.
# 测试连接milvus并插入10个向量，同事进行向量的相似性搜索
import random
from milvus import Milvus, IndexType, MetricType, Status

# Milvus server IP address and port.
# You may need to change _HOST and _PORT accordingly.
# 服务器的连接地址
_HOST = '127.0.0.1'
_PORT = '19530'  # default value
# _PORT = '19121'  # default http value

# Vector parameters
# 向量的长度
_DIM = 8  # dimension of vector
# TODO
_INDEX_FILE_SIZE = 32  # max file size of stored index


def main():
    # Specify server addr when create milvus client instance
    # milvus client instance maintain a connection pool, param
    # `pool_size` specify the max connection num.
    # 获取服务端的连接
    milvus = Milvus(_HOST, _PORT)

    # Create collection demo_collection if it dosen't exist.
    # 创建collection
    collection_name = 'example_collection_'
    # 看是否有这个collection
    status, ok = milvus.has_collection(collection_name)
    # 如果没有则创建
    if not ok:
        param = {
            'collection_name': collection_name,
            'dimension': _DIM,
            'index_file_size': _INDEX_FILE_SIZE,  # optional
            'metric_type': MetricType.L2  # optional
        }
        # 创建collection
        milvus.create_collection(param)

    # Show collections in Milvus server
    # 查看所有的collection
    _, collections = milvus.list_collections()
    print(collections)

    # Describe demo_collection
    # 得到当前的collection
    _, collection = milvus.get_collection_info(collection_name)
    print(collection)

    # 10000 vectors with 128 dimension
    # element per dimension is float32 type
    # vectors should be a 2-D array
    # 创建10个长度为8的向量
    vectors = [[random.random() for _ in range(_DIM)] for _ in range(10)]
    print(vectors)
    # You can also use numpy to generate random vectors:
    #   vectors = np.random.rand(10000, _DIM).astype(np.float32)

    # Insert vectors into demo_collection, return status and vectors id list
    # 把这10个向量都插入milvus
    status, ids = milvus.insert(collection_name=collection_name, records=vectors)
    if not status.OK():
        print("Insert failed: {}".format(status))
    print(ids)

    # Flush collection  inserted data to disk.
    # 数据落盘
    milvus.flush([collection_name])
    # Get demo_collection row count
    # 得到当前row的数量
    status, result = milvus.count_entities(collection_name)
    print(status)
    print(result)

    # present collection statistics info
    # 查看collection的统计数据
    _, info = milvus.get_collection_stats(collection_name)
    print(info)

    # Obtain raw vectors by providing vector ids
    # 得到前十个数据
    status, result_vectors = milvus.get_entity_by_id(collection_name, ids[:10])
    print(result_vectors)

    # create index of vectors, search more rapidly
    # 创建索引
    index_param = {
        'nlist': 2048
    }

    # Create ivflat index in demo_collection
    # You can search vectors without creating index. however, Creating index help to
    # search faster
    # 创建ivf_flat
    print("Creating index: {}".format(index_param))
    status = milvus.create_index(collection_name, IndexType.IVF_FLAT, index_param)

    # describe index, get information of index
    # 得到索引的信息
    status, index = milvus.get_index_info(collection_name)
    print(index)

    # Use the top 10 vectors for similarity search
    # 对前10个数据进行query
    query_vectors = vectors[0:10]

    # execute vector similarity search
    # 索引的搜索的中心点数量
    search_param = {
        "nprobe": 16
    }

    print("Searching ... ")

    param = {
        'collection_name': collection_name,
        'query_records': query_vectors,
        'top_k': 1,
        'params': search_param,
    }
    # 进行搜索
    status, results = milvus.search(**param)
    if status.OK():
        print(results)
        # indicate search result
        # also use by:
        #   `results.distance_array[0][0] == 0.0 or results.id_array[0][0] == ids[0]`
        if results[0][0].distance == 0.0 or results[0][0].id == ids[0]:
            print('Query result is correct')
        else:
            print('Query result isn\'t correct')

        # print results
        print(results)
    else:
        print("Search failed. ", status)

    # Delete demo_collection
    # 删除掉collection
    status = milvus.drop_collection(collection_name)


if __name__ == '__main__':
    main()