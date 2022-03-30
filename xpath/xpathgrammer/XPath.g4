grammar XPath;        // XPATH GRAMMAR

EXPR : '/' NODE_TEST PRED? EXPR?;
PRED : '[' ']';

NODE_TEST: (AXES '::') ? ;

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
