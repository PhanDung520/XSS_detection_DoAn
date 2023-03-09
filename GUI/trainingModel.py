import pandas as pd

# lấy ra các đặc trưng
Script = pd.read_csv(r'')

# Biểu diễn dữ liệu dưới dạng 1 dataFrame
df = pd.DataFrame(Script, columns=['hasLt', 'hasScript', 'hasAlert', 'hasBigSmallSign2', 'hasBigSmallSign1', 'hasAnd',
                                   'hasPercentage', 'hasSlash', 'hasBackSlash', 'hasPlus', 'hasDocument', 'hasWindow',
                                   'hasOnload', 'hasOnError', 'hasDiv', 'hasIframe', 'hasImg', 'hasSRC', 'hasVar',
                                   'hasEval', 'hasHref', 'hasCookie', 'hasStringfromCharCode', 'hasSingleQoute',
                                   'hasQuestionMark', 'hasExclamationMark', 'hasSemicolon', 'hasHTTP', 'hasJS',
                                   'hasHash', 'hasEqual', 'hasOpenBracket', 'hasCloseBracket', 'hasDoubleBracket',
                                   'hasDollar', 'hasOpenParenthesis', 'hasCloseParenthesis', 'hasAsterisk', 'hasComma',
                                   'hasHyphen', 'hasLessThan', 'hasGreaterThan', 'hasAt', 'hasUnderscore',
                                   'hasLocation', 'hasSearch', 'hasAndHash', 'hasColon', 'hasDots', 'hasOpenBrace',
                                   'hasCloseBrace', 'hasTilde', 'hasSpace', 'hasGrave', 'hasDoubleEquals',
                                   'hasDoubleSlash', 'hasVerticalBar', 'hasPower', 'LettersRatio', 'NumbuersRatio',
                                   'SymbolsRatio'])

X = df['hasLt', 'hasScript', 'hasAlert', 'hasBigSmallSign2', 'hasBigSmallSign1', 'hasAnd',
        'hasPercentage', 'hasSlash', 'hasBackSlash', 'hasPlus', 'hasDocument', 'hasWindow',
        'hasOnload', 'hasOnError', 'hasDiv', 'hasIframe', 'hasImg', 'hasSRC', 'hasVar',
        'hasEval', 'hasHref', 'hasCookie', 'hasStringfromCharCode', 'hasSingleQoute',
        'hasQuestionMark', 'hasExclamationMark', 'hasSemicolon', 'hasHTTP', 'hasJS',
        'hasHash', 'hasEqual', 'hasOpenBracket', 'hasCloseBracket', 'hasDoubleBracket',
        'hasDollar', 'hasOpenParenthesis', 'hasCloseParenthesis', 'hasAsterisk', 'hasComma',
        'hasHyphen', 'hasLessThan', 'hasGreaterThan', 'hasAt', 'hasUnderscore',
        'hasLocation', 'hasSearch', 'hasAndHash', 'hasColon', 'hasDots', 'hasOpenBrace',
        'hasCloseBrace', 'hasTilde', 'hasSpace', 'hasGrave', 'hasDoubleEquals',
        'hasDoubleSlash', 'hasVerticalBar', 'hasPower', 'LettersRatio', 'NumbuersRatio',
        'SymbolsRatio']


y = df['Class']
