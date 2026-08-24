const fs = require('fs');
const parser = require('@babel/parser');
const traverse = require('@babel/traverse').default;
const code = fs.readFileSync('assets/static/js/main.94fae2cd.ifelse.js', 'utf8');
const ast = parser.parse(code, {
  sourceType: 'unambiguous',
  plugins: [
    'jsx',
    'classProperties',
    'optionalChaining',
    'nullishCoalescingOperator',
    'topLevelAwait',
    'logicalAssignment',
    'numericSeparator',
    'bigInt',
    'optionalCatchBinding',
    'privateMethods',
    'privateIn',
  ],
});
let count = 0;
traverse(ast, {
  ConditionalExpression(path) {
    count += 1;
  }
});
console.log('parse ok');
console.log('ConditionalExpression count:', count);
