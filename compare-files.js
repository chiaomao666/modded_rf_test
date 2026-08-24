const fs = require('fs');
const orig = fs.readFileSync('assets/static/js/main.94fae2cd.js', 'utf8');
const out = fs.readFileSync('assets/static/js/main.94fae2cd.ifelse.js', 'utf8');
const origLen = orig.length;
const outLen = out.length;
const origQ = (orig.match(/\?/g) || []).length;
const outQ = (out.match(/\?/g) || []).length;
const origCond = (orig.match(/\?[^:\n]*:/g) || []).length;
const outCond = (out.match(/\?[^:\n]*:/g) || []).length;
console.log('origLen', origLen);
console.log('outLen', outLen);
console.log('orig ? count', origQ);
console.log('out ? count', outQ);
console.log('orig ternary-like count', origCond);
console.log('out ternary-like count', outCond);
console.log('output vs original prefix diff sample:');
for (let i = 0; i < 1000; i += 100) {
  if (orig[i] !== out[i]) { console.log('diff at', i); break; }
}
console.log('output first 20 chars:', JSON.stringify(out.slice(0, 20)));
console.log('original first 20 chars:', JSON.stringify(orig.slice(0,20)));
