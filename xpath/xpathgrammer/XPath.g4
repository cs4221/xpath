grammar XPath;

// Parser Rules
expr: '/' nodetest pred? expr?;
pred: '['']';
nodetest: pathid? NODE ;
pathid: AXES '::';


// Lexer Rules
    AXES:  'self'
        |  'child'
        |  'descendant'
        |  'parent'
        |  'ancestor'
        |  'preceding-sibling'
        |  'following-sibling'
        |  'preceding'
        |  'following'
        |  'ancestor-or-self'
        |  'descendant-or-self'
        |  'attribute'
        ;

OPERATOR:  '+'
        |  '-'
        |  '|'
        |  '*'
        |  'div'
        |  '='
        |  '!='
        |  '<'
        |  '<='
        |  '>'
        |  '>='
        |  'or'
        |  'and'
        |  'mod'
        ;
        
    NODE:  [a-zA-Z]+;

      WS: [ \t\n\r\f\s] -> skip;
