# 知恵
- B問題レベルであれば，まず全探索を検討する

# 解法メモ
- 素因数分解（factorize.py）
- 回文問題（is_palindrome.py）
  - string == string[::-1]
- 約数（divisors_list.pys）

---
# 解いてて思ったこと

## ABC321
### B - Cutoff

回答パターンはせいぜい3パターン
- 既に合格点を上回っている場合：minより小さい方に挿入
- 既に上回っていない場合：maxよりも大きい方に挿入
- どちらでもない場合：目標点からmin，maxを引き，部分和を出せば良い
みたいに考えて頑張ったがテストケースで4件突破できなかった...

おそらく自分の解法に一番近いものはこれ↓
- https://atcoder.jp/contests/abc321/submissions/46695929
こんなシンプルに書けるんか？という感じ．

B問題レベルだから全探索すればええやん，ということに早く気づくべきだった...

## ABC320
#### B - Longest Palindrome

回文判定
カウントミスらないように...

## ABC319
#### B - Measure

問題文理解するのに手間取ってしまった．実装自体は簡単
