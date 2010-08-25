# JavaScript 1.7 keywords
keywords = [
    "break",
    "case", "catch", "const", "continue",
    "debugger", "default", "delete", "do",
    "else",
    "false", "finally", "for", "function",
    "if", "in", "instanceof",
    "let",
    "new", "null",
    "return",
    "switch",
    "this", "throw", "true", "try", "typeof",
    "var", "void",
    "yield",
    "while", "with"
]

# By Mozilla MDC
# https://developer.mozilla.org/en/Core_JavaScript_1.5_Guide/Statements#Exception_Types
ecmaExceptions = ["Error", "EvalError", "RangeError", "ReferenceError", "SyntaxError", "TypeError", "URIError"]
domExceptions = ["DOMException", "EventException", "RangeException"]

#
# Small list of globally allowed values
globalObjects = ["Math","Error","String","Array","Object","Function","RegExp"]
globalFunctions = ["window","document","parseInt","parseFloat"]