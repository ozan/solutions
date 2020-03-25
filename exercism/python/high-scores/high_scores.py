def latest(scores):
    return scores[-1] if scores else None


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    return sorted(scores, reverse=True)[:3]
