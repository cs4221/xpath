java org.antlr.v4.Tool -Dlanguage=Python3 -o ./xpath/xpathgrammer/.antlr4py3 %*

del /S /Q .\xpath\compilerv1\X*
move /y .\xpath\xpathgrammer\.antlr4py3\xpath\xpathgrammer\* .\xpath\compilerv1\
