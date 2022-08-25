import os
import orjson


def merge_json(path_results, path_merges):
    d = {}
    with open(path_merges, "w+", encoding="utf-8") as f0:
        for file in os.listdir(path_results):
            if file == 'av_train.json':
                with open(os.path.join(path_results, file), "r", encoding="utf-8") as f1:
                    json_dict = orjson.loads(f1.read())
                    d = json_dict.copy()
            elif file == 'av_val.json':
                with open(os.path.join(path_results, file), "r", encoding="utf-8") as f2:
                    json_dict = orjson.loads(f2.read())
                    vs = json_dict['videos']
                    for v in vs:
                        d['videos'].append(v)
        f0.write(orjson.dumps(d).decode("utf-8"))