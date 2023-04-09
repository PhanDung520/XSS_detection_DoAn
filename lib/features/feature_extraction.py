import lib.features.features as Features
# 2 8 18 24 25 31 32 36 41 50 53 59 60 61 - vị trí ban đầu
# Trích xuất đặc trưng
def ftrExtract2(script):
    features =[]
    features.append(Features.hasScript(script))  # F1
    features.append(Features.hasSlash(script))  # F2
    features.append(Features.hasSRC(script))  # F13
    features.append(Features.hasSingleQoute(script))  # F4
    features.append(Features.hasQuestionMark(script))  # F5
    features.append(Features.hasEqual(script))  # F6
    features.append(Features.hasOpenBracket(script))  # F7
    features.append(Features.hasOpenParenthesis(script))  # F8
    features.append(Features.hasLessThan(script))  # F9
    features.append(Features.hasOpenBrace(script))  # F10
    features.append(Features.hasSpace(script))  # F11
    features.append(Features.lettersRatio(script))  # F12
    features.append(Features.numbersRatio(script))  # F13
    features.append(Features.symbolsRatio(script))  # F14

    return features


# Trích xuất đặc trưng
def ftrExtract(script, label):
    features = []
    features.append(Features.hasScript(script))  # F1
    features.append(Features.hasSlash(script))  # F2
    features.append(Features.hasSRC(script))  # F13
    features.append(Features.hasSingleQoute(script))  # F4
    features.append(Features.hasQuestionMark(script))  # F5
    features.append(Features.hasEqual(script))  # F6
    features.append(Features.hasOpenBracket(script))  # F7
    features.append(Features.hasOpenParenthesis(script))  # F8
    features.append(Features.hasLessThan(script))  # F9
    features.append(Features.hasOpenBrace(script))  # F10
    features.append(Features.hasSpace(script))  # F11
    features.append(Features.lettersRatio(script))  # F12
    features.append(Features.numbersRatio(script))  # F13
    features.append(Features.symbolsRatio(script))  # F14
    features.append(label)  # label

    return features
