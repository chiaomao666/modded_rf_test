const fs = require('fs');
const parser = require('@babel/parser');
const traverse = require('@babel/traverse').default;
const t = require('@babel/types');
const generator = require('@babel/generator').default;
const inputPath = 'assets/static/js/main.94fae2cd.js';
const outputPath = 'assets/static/js/main.94fae2cd.ifelse.js';
const code = fs.readFileSync(inputPath, 'utf8');
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
    const { test, consequent, alternate } = path.node;
    const ifStmt = t.ifStatement(
      test,
      t.blockStatement([t.returnStatement(consequent)]),
      t.blockStatement([t.returnStatement(alternate)])
    );
    const arrow = t.arrowFunctionExpression([], t.blockStatement([ifStmt]));
    const callExpr = t.callExpression(arrow, []);
    path.replaceWith(callExpr);
    count += 1;
  }
});
const output = generator(ast, { compact: false, retainLines: true, comments: true }).code;
fs.writeFileSync(outputPath, output, 'utf8');
console.log(`Converted ${count} conditional expressions into if/else wrapper expressions.`);
