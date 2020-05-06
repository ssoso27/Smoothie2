def solution(dataSource, tags):
    result = set()

    # 태그 별로 분류하기
    tags_in_docs = {}
    for ds in dataSource:
        doc = ds.pop(0)
        for tag in ds:
            if tag not in tags_in_docs.keys():
                tags_in_docs[tag] = []
            tags_in_docs[tag].append(doc)

    # 검색
    have_tags_cnt = {}
    for tag in tags:
        # result = result.union(set(tags_in_docs[tag]))
        for doc in tags_in_docs[tag]:
            if doc not in have_tags_cnt.keys():
                have_tags_cnt[doc] = 10**5
            result.add(doc)
            have_tags_cnt[doc] -= 1

    answer = sorted(sorted(result), key=lambda x: have_tags_cnt[x])[:10]
    return answer


dataSource = [
    ["doc1", "t1", "t2", "t3"],
    ["doc2", "t0", "t2", "t3"],
    ["doc3", "t1", "t6", "t7"],
    ["doc4", "t1", "t2", "t4"],
    ["doc5", "t6", "t100", "t8"]
]
tags = ["t1", "t2", "t3"]
print(solution(dataSource, tags))