# trích chọn đặc trưng url

# F1: Trả về giá trị 1 nếu tồn tại &lt, ngược lại trả về giá trị 0
def hasLt(script):
    if "&lt" in script:
        return 1
    return 0


# F2: Trả về giá trị 1 nếu tồn tại từ khóa script, ngược lại trả về giá trị 0
def hasScript(script):
    if "script" in script:
        return 1
    return 0


# F3: Trả về giá trị 1 nếu tồn tại từ khóa Alert, ngược lại trả về giá trị 0
def hasAlert(script):
    if "Alert" in script:
        return 1
    return 0


# F4: Trả về giá trị 1 nếu tồn tại “><, ngược lại trả về giá trị 0
def hasBigSmallSign2(script):
    if '''"><''' in script:
        return 1
    return 0


# F5: Trả về giá trị 1 nếu tồn tại ‘><, ngược lại trả về giá trị 0
def hasBigSmallSign1(script):
    if ''''><''' in script:
        return 1
    return 0


# F6: Trả về giá trị 1 nếu tồn tại từ khóa and, ngược lại trả về giá trị 0
def hasAnd(script):
    if "and" in script:
        return 1
    return 0


# F7: Trả về giá trị 1 nếu tồn tại %, ngược lại trả về giá trị 0
def hasPercentage(script):
    if "%" in script:
        return 1
    return 0


# F8: Trả về giá trị 1 nếu tồn tại /, ngược lại trả về giá trị 0
def hasSlash(script):
    if "/" in script:
        return 1
    return 0


# F9: Trả về giá trị 1 nếu tồn tại \, ngược lại trả về giá trị 0
def hasBackSlash(script):
    if "\\" in script:
        return 1
    return 0


# F10: Trả về giá trị 1 nếu tồn tại +, ngược lại trả về giá trị 0
def hasPlus(script):
    if "+" in script:
        return 1
    return 0


# F11: Trả về giá trị 1 nếu tồn tại từ khóa Document, ngược lại trả về giá trị 0
def hasDocument(script):
    if "Document" in script:
        return 1
    return 0


# F12: Trả về giá trị 1 nếu tồn tại từ khóa Window, ngược lại trả về giá trị 0
def hasWindow(script):
    if "Window" in script:
        return 1
    return 0


# F13: Trả về giá trị 1 nếu tồn tại từ khóa Onload, ngược lại trả về giá trị 0
def hasOnload(script):
    if "Onload" in script:
        return 1
    return 0


# F14: Trả về giá trị 1 nếu tồn tại từ khóa Onerror, ngược lại trả về giá trị 0
def hasOnError(script):
    if "Onerror" in script:
        return 1
    return 0


# F15: Trả về giá trị 1 nếu tồn tại từ khóa DIV, ngược lại trả về giá trị 0
def hasDiv(script):
    if "DIV" in script:
        return 1
    return 0


# F16: Trả về giá trị 1 nếu tồn tại từ khóa iframe, ngược lại trả về giá trị 0
def hasIframe(script):
    if "iframe" in script:
        return 1
    return 0


# F17: Trả về giá trị 1 nếu tồn tại từ khóa img, ngược lại trả về giá trị 0
def hasImg(script):
    if "img" in script:
        return 1
    return 0


# F18: Trả về giá trị 1 nếu tồn tại từ khóa SRC, ngược lại trả về giá trị 0
def hasSRC(script):
    if "SRC" in script:
        return 1
    return 0


# F19: Trả về giá trị 1 nếu tồn tại từ khóa Var, ngược lại trả về giá trị 0
def hasVar(script):
    if "Var" in script:
        return 1
    return 0


# F20: Trả về giá trị 1 nếu tồn tại từ khóa Eval, ngược lại trả về giá trị 0
def hasEval(script):
    if "Eval" in script:
        return 1
    return 0


# F21: Trả về giá trị 1 nếu tồn tại từ khóa href, ngược lại trả về giá trị 0
def hasHref(script):
    if "href" in script:
        return 1
    return 0


# F22: Trả về giá trị 1 nếu tồn tại từ khóa Cookie, ngược lại trả về giá trị 0
def hasCookie(script):
    if "Cookie" in script:
        return 1
    return 0


# F23: Trả về giá trị 1 nếu tồn tại từ khóa StringfromCharCode, ngược lại trả về giá trị 0
def hasStringfromCharCode(script):
    if "StringfromCharCode" in script:
        return 1
    return 0


# F24: Trả về giá trị 1 nếu chứa ngoặc đơn ‘ , ngược lại trả về giá trị 0
def hasSingleQoute(script):
    if "'" in script:
        return 1
    return 0


# F25: Trả về giá trị 1 nếu chứa dấu chấm hỏi ? , ngược lại trả về giá trị 0
def hasQuestionMark(script):
    if "?" in script:
        return 1
    return 0


# F26: Trả về giá trị 1 nếu chứa dấu chấm than ! , ngược lại trả về giá trị 0
def hasExclamationMark(script):
    if "!" in script:
        return 1
    return 0


# F27: Trả về giá trị 1 nếu chứa dấu chấm phẩy ; , ngược lại trả về giá trị 0
def hasSemicolon(script):
    if ";" in script:
        return 1
    return 0


# F28: Trả về giá trị 1 nếu tồn tại từ khóa HTTP, ngược lại trả về giá trị 0
def hasHTTP(script):
    if "HTTP" in script:
        return 1
    return 0


# F29: Trả về giá trị 1 nếu tồn tại từ khóa JS, ngược lại trả về giá trị 0
def hasJS(script):
    if "JS" in script:
        return 1
    return 0


# F30: Trả về giá trị 1 nếu chứa dấu thăng # , ngược lại trả về giá trị 0
def hasHash(script):
    if "#" in script:
        return 1
    return 0


# F31: Trả về giá trị 1 nếu chứa dấu bằng = , ngược lại trả về giá trị 0
def hasEqual(script):
    if "=" in script:
        return 1
    return 0


# F32: Trả về giá trị 1 nếu chứa dấu mở ngoặc nhọn { , ngược lại trả về giá trị 0
def hasOpenBracket(script):
    if "{" in script:
        return 1
    return 0


# F33: Trả về giá trị 1 nếu chứa dấu đóng ngoặc nhọn } , ngược lại trả về giá trị 0
def hasCloseBracket(script):
    if "}" in script:
        return 1
    return 0


# F34: Trả về giá trị 1 nếu chứa ký tự {}, ngược lại trả về giá trị 0
def hasDoubleBracket(script):
    if "{}" in script:
        return 1
    return 0


# F35: Trả về giá trị 1 nếu chứa dấu đô la $ , ngược lại trả về giá trị 0
def hasDollar(script):
    if "$" in script:
        return 1
    return 0


# F36: Trả về giá trị 1 nếu chứa dấu mở ngoặc đơn ( , ngược lại trả về giá trị 0
def hasOpenParenthesis(script):
    if "(" in script:
        return 1
    return 0


# F37: Trả về giá trị 1 nếu chứa dấu đóng ngoặc đơn ) , ngược lại trả về giá trị 0
def hasCloseParenthesis(script):
    if ")" in script:
        return 1
    return 0


# F38: Trả về giá trị 1 nếu chứa dấu đóng sao * , ngược lại trả về giá trị 0
def hasAsterisk(script):
    if "*" in script:
        return 1
    return 0


# F39: Trả về giá trị 1 nếu chứa dấu đóng phẩy , , ngược lại trả về giá trị 0
def hasComma(script):
    if "," in script:
        return 1
    return 0


# F40: Trả về giá trị 1 nếu chứa dấu gạch ngang - , ngược lại trả về giá trị 0
def hasHyphen(script):
    if "-" in script:
        return 1
    return 0


# F41: Trả về giá trị 1 nếu chứa dấu nhỏ < , ngược lại trả về giá trị 0
def hasLessThan(script):
    if "<" in script:
        return 1
    return 0


# F42: Trả về giá trị 1 nếu chứa dấu lớn > , ngược lại trả về giá trị 0
def hasGreaterThan(script):
    if ">" in script:
        return 1
    return 0


# F43: Trả về giá trị 1 nếu tồn tại từ khóa At, ngược lại trả về giá trị 0
def hasAt(script):
    if "At" in script:
        return 1
    return 0


# F44: Trả về giá trị 1 nếu chứa dấu gạch dưới _ , ngược lại trả về giá trị 0
def hasUnderscore(script):
    if "_" in script:
        return 1
    return 0


# F45: Trả về giá trị 1 nếu tồn tại từ khóa location, ngược lại trả về giá trị 0
def hasLocation(script):
    if "location" in script:
        return 1
    return 0


# F46: Trả về giá trị 1 nếu tồn tại từ khóa Search, ngược lại trả về giá trị 0
def hasSearch(script):
    if "Search" in script:
        return 1
    return 0


# F47: Trả về giá trị 1 nếu tồn tại &# , ngược lại trả về giá trị 0
def hasAndHash(script):
    if "&#" in script:
        return 1
    return 0


# F48: Trả về giá trị 1 nếu chứa dấu hai chấm : , ngược lại trả về giá trị 0
def hasColon(script):
    if ":" in script:
        return 1
    return 0


# F49: Trả về giá trị 1 nếu chứa nhiều dấu chấm . , ngược lại trả về giá trị 0
def hasDots(script):
    if "." in script:
        return 1
    return 0


# F50: Trả về giá trị 1 nếu chứa dấu mở ngoặc vuông [ , ngược lại trả về giá trị 0
def hasOpenBrace(script):
    if "[" in script:
        return 1
    return 0


# F51: Trả về giá trị 1 nếu chứa dấu đóng ngoặc vuông ] , ngược lại trả về giá trị 0
def hasCloseBrace(script):
    if "]" in script:
        return 1
    return 0


# F52: Trả về giá trị 1 nếu chứa dấu đóng ngã ~ , ngược lại trả về giá trị 0
def hasTilde(script):
    if "~" in script:
        return 1
    return 0


# F53: Trả về giá trị 1 nếu chứa space, ngược lại trả về giá trị 0
def hasSpace(script):
    if " " in script:
        return 1
    return 0


# F54: Trả về giá trị 1 nếu chứa dấu huyền ` , ngược lại trả về giá trị 0
def hasGrave(script):
    if "`" in script:
        return 1
    return 0


# F55: Trả về giá trị 1 nếu chứa == , ngược lại trả về giá trị 0
def hasDoubleEquals(script):
    if "==" in script:
        return 1
    return 0


# F56: Trả về giá trị 1 nếu chứa // , ngược lại trả về giá trị 0
def hasDoubleSlash(script):
    if "//" in script:
        return 1
    return 0


# F57: Trả về giá trị 1 nếu chứa | , ngược lại trả về giá trị 0
def hasVerticalBar(script):
    if "|" in script:
        return 1
    return 0


# F58: Trả về giá trị 1 nếu chứa ^ , ngược lại trả về giá trị 0
def hasPower(script):
    if "^" in script:
        return 1
    return 0


# F59: Tỉ lệ các kí tự chữ so với input
def lettersRatio(script):
    count = 0
    for element in range(len(script)):
        if 'a' <= script[element] <= 'z':
            count += 1
        if 'A' <= script[element] <= 'Z':
            count += 1
    return count / len(script)


# F60: Tỉ lệ các kí tự số so với input
def numbersRatio(script):
    count = 0
    for element in range(len(script)):
        if '0' <= script[element] <= '9':
            count += 1
    return count / len(script)


# F61: Tỉ lệ các kí tự đặc biệt, các dấu … so với input
def symbolsRatio(script):
    char_str = ['@', '&', '(', ')', '{', '}', '[', ']', '''"''', "'", '|', '/', ':', '.', '`', '~', '-', '_', '+', '=', '%', '#', '*', '^', '!', '&', ';', ',', '$', '?', chr(92)]
    countChar = 0
    for element in range(len(script)):
        try:
            char_str.index(script[element])
            countChar += 1
        except ValueError:
            countChar += 0
    return countChar / len(script)


# Trích xuất đặc trưng
def ftrExtract(script):
    features = []
    features.append(hasLt(script))  # F1
    features.append(hasScript(script))  # F2
    features.append(hasAlert(script))  # F3
    features.append(hasBigSmallSign2(script))  # F4
    features.append(hasBigSmallSign1(script))   # F5
    features.append(hasAnd(script))  # F6
    features.append(hasPercentage(script))  # F7
    features.append(hasSlash(script))  # F8
    features.append(hasBackSlash(script))  # F9
    features.append(hasPlus(script))  # F10
    features.append(hasDocument(script))  # F11
    features.append(hasWindow(script))  # F12
    features.append(hasOnload(script))  # F13
    features.append(hasOnError(script))  # F14
    features.append(hasDiv(script))  # F15
    features.append(hasIframe(script))  # F16
    features.append(hasImg(script))  # F17
    features.append(hasSRC(script))  # F18
    features.append(hasVar(script))  # F19
    features.append(hasEval(script))  # F20
    features.append(hasHref(script))  # F21
    features.append(hasCookie(script))  # F22
    features.append(hasStringfromCharCode(script))  # F23
    features.append(hasSingleQoute(script))  # F24
    features.append(hasQuestionMark(script))  # F25
    features.append(hasExclamationMark(script))  # F26
    features.append(hasSemicolon(script))  # F27
    features.append(hasHTTP(script))  # F28
    features.append(hasJS(script))  # F29
    features.append(hasHash(script))  # F30
    features.append(hasEqual(script))  # F31
    features.append(hasOpenBracket(script))  # F32
    features.append(hasCloseBracket(script))  # F33
    features.append(hasDoubleBracket(script))  # F34
    features.append(hasDollar(script))  # F35
    features.append(hasOpenParenthesis(script))  # F36
    features.append(hasCloseParenthesis(script))  # F37
    features.append(hasAsterisk(script))  # F38
    features.append(hasComma(script))  # F39
    features.append(hasHyphen(script))  # F40
    features.append(hasLessThan(script))  # F41
    features.append(hasGreaterThan(script))  # F42
    features.append(hasAt(script))  # F43
    features.append(hasUnderscore(script))  # F44
    features.append(hasLocation(script))  # F45
    features.append(hasSearch(script))  # F46
    features.append(hasAndHash(script))  # F47
    features.append(hasColon(script))  # F48
    features.append(hasDots(script))  # F49
    features.append(hasOpenBrace(script))  # F50
    features.append(hasCloseBrace(script))  # F51
    features.append(hasTilde(script))  # F52
    features.append(hasSpace(script))  # F53
    features.append(hasGrave(script))  # F54
    features.append(hasDoubleEquals(script))  # F55
    features.append(hasDoubleSlash(script))  # F56
    features.append(hasVerticalBar(script))  # F57
    features.append(hasPower(script))  # F58
    features.append(lettersRatio(script))  # F59
    features.append(numbersRatio(script))  # F60
    features.append(symbolsRatio(script))  # F61

    return features
