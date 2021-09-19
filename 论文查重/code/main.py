import gensim
import jieba
import re
import sys


def get_file(path):
    with open(path) as fd:
        content = fd.read()
    return content


def filter_string(string):
    my_re = re.compile(u"[^a-zA-Z0-9\u4e00-\u9fa5]")
    string = my_re.sub("", string)
    result = jieba.lcut(string)
    return result


def calc_similarity(text1, text2):
    texts = [text1, text2]
    dictionary = gensim.corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    similarity = gensim.similarities.Similarity('-Similarity-index', corpus, num_features=len(dictionary))
    test_corpus_1 = dictionary.doc2bow(text1)
    cosine_sim = similarity[test_corpus_1][1]
    return cosine_sim


def main():
    try:
        #        path1 = "../test_txt/orig.txt"
        #        path2 = "../test_txt/orig_0.8_add.txt"
        #        save_path = "../result.txt"
        path1 = sys.argv[1]  # 论文原文的文件的绝对路径
        path2 = sys.argv[2]  # 抄袭版论文的文件的绝对路径
        save_path = sys.argv[3]  # 输出结果绝对路径
        text1 = filter_string(get_file(path1))
        text2 = filter_string(get_file(path2))
        similarity = calc_similarity(text1, text2)
        print("文章相似度： %.4f" % similarity)
        fd = open(save_path, 'w')
        fd.write("文章相似度： %.4f" % similarity)
        fd.close()
        result = round(similarity.item(), 2)  # 取小数点后两位
    except Exception as e:
        print(e)
    finally:
        return result


if __name__ == '__main__':
    main()
