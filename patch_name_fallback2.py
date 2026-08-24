import re
from pathlib import Path

path = Path(r'c:/Users/wuser/Desktop/2.28/assets/static/js/main.29e3c7d8.js')
text = path.read_text(encoding='utf-8')
pattern = re.compile(r'onClick: \(\) => \{.*?3 !== x && 4 !== x \|\| y\(\{', re.S)
replacement = '''onClick: () => {
                                if (2 === x) {
                                    const cityName = _ && _.name ? _.name : "";
                                    return console.log("[UW] state(2) 造成 → 進入 ".concat(cityName, " 城內介面")), void n("/attacks/uwcity", {
                                        state: {
                                            cityName: cityName
                                        }
                                    });
                                }
                                if (1 === x) {
                                    const e = OY(d, c),
                                        r = _ && _.name ? _.name : "",
                                        t = (zY[d] && zY[d].name) || r,
                                        n = r;
                                    return void y({
                                        title: "uw_move_confirm",
                                        body: "確定要消耗 ".concat(e.energy, " 能量前往 ").concat(n, "？預計將於 ").concat(e.minutes.toFixed(1), " 分鐘後抵達。 (自 ").concat(t, " 出發，rail × ").concat(e.rail, "、highway × ").concat(e.highway, ")"),
                                        energyHeader: {
                                            current: h,
                                            need: e.energy
                                        },
                                        onConfirm: () => {
                                            h < e.energy ? y({
                                                title: "replenish_energy_confirm",
                                                body: "".concat(t, " → ").concat(n, " 需要 ").concat(e.energy, " 能量，目前 ").concat(h, "。是否進入能量補充？"),
                                                onConfirm: () => {
                                                    console.log("[UW] replenish_energy_confirm → (mock) 進入能量補充視窗"), y(null)
                                                }
                                            }) : (z(t => t - e.energy), m({
                                                destCityId: c,
                                                moveToAt: Date.now() + 60 * Math.max(1, e.minutes) * 1e3
                                            }), console.log("[UW] uw_move_confirm 確認 → 轉 ".concat(e.energy, " 能量；ETA ").concat(e.minutes, " 分鐘")), y(null))
                                        }
                                    })
                                }
                                3 !== x && 4 !== x || y({'''
new_text, count = pattern.subn(replacement, text, count=1)
if count != 1:
    raise SystemExit(f'pattern replacement count={count}')
path.write_text(new_text, encoding='utf-8')
print('patched')
