import gensim.models as gsm
import phrase2vec as p2v
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

w2v = gsm.KeyedVectors.load_word2vec_format('./w2v/google_w2v_without_emoji.bin', binary=True) #(cfg.DATA.W2V_PATH, binary=True)
e2v = gsm.KeyedVectors.load_word2vec_format('./e2v/emoji2vec.bin', binary=True) #(cfg.DATA.E2V_PATH, binary=True)
model = p2v.Phrase2Vec(300, w2v=w2v, e2v=e2v)

def tsne_plot(model):
    labels= []
    tokens = []
    
    for emoji in e2v.wv.vocab:
        tokens.append(model[emoji])
        labels.append(emoji)
        
    tsne_model = TSNE(perplexity=40, n_components=2, init='pca', n_iter=2500, random_state=23)
    new_values = tsne_model.fit_transform(tokens)
    
    x = []
    y = []
    
    for value in new_values:
        x.append(value[0])
        y.append(value[1])
        
    plt.figure(figsize=(50,50))
    for i in range(len(x)):
        plt.scatter(x[i],y[i]) 
        plt.annotate(labels[i],
                    xy = (x[i],y[i]),
                    xytext = (5,2),
                    textcoords = 'offset points',
                    ha = 'right',
                    va = 'bottom',
                    fontname='Segoe UI Emoji',
                    fontsize=40)
    plt.savefig('t-sne.png')

tsne_plot(model)
