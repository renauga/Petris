import pickle

def store_score(name, score):
    scores = read_scores()
    scores.append((name,score))
    scores = sorted(scores, key= lambda x:-x[1])
    if len(scores)>15:
        scores.pop()
    with open('scores.dat', 'wb') as file:
        pickle.dump(scores, file)

def read_scores():
    try:
        with open('scores.dat', 'rb') as file:
            scores = pickle.load(file)
    except:
        scores = []
    return scores