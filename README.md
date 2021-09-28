# 文系 Programmer のための Python で学び直す高校数学

# 第1章　Computer と「数」
# 1. 位取り記数法
位取り記数法とは「数」を表す方法のこと。

使用者 | 位取り記数法
--- | ---
人間 | 10進位取り記数法
Computer | 2進位取り記数法

２つの違いは
数を数える時に使える数字の種類。

## 1.1 10進位取り記数法
10種類の数字を使うから**10進位取り記数法**（または**10進法**）、この Rule で表される数を**10進数**と言う。

### 重み
各桁に意味を持たせるための重要な値。
- 10進数の場合、すべての桁の重みが「10の〇乗」になる。
- 10進法では桁が1つ繰り上がるごとに、重みは10倍になる。

### 基数（または、基底）
重みの基本になる値。
- 10進法だと「10｣
- 2進法だと「2」
- 16進法だと「16」

## 1.2 〇〇の0乗
基数がどんな数字でも「〇〇の0乗」は必ず「1」になる。  
10^n（10の n 乗）は「10を n 回かけ合わせる：という意味。  
10^0 は「10 * 0」ではない。「10 * 0」は10に0を掛けたのであって、10を0回かけ合わせることとは意味が違うので注意する。

## 1.3 2進位取り記数法
Computer の世界で使う。  
理由は、Computer が電気で動く機械の為。IC と呼ばれる電子部品の中を流れる電気信号で On と Off を表す。数字で表せば「1」と「0」の2つだけになる。

## 1.4 16進位取り記数法
- 2進数の4桁までを表現できる。  
    例). 2進数:　「11111111」ぱっとみて何桁か分からない。16進数「FF」=>2進数「1111 1111」に変換できる。
- 2進数を扱う Computer と10進法に慣れ親しんだ人間の間を取り持つ便利な表記法。

### 2進数を16進数に変換する方法
- 位取り記数法では、右側の桁から意味を持つ
- 2進数の4桁は16進数の1桁に相当する。
1. 2進数の右側から4桁ずつに区切る。
2. 区切った4桁ごとに16進数に置き換える。  
    ※ 4桁に満たない場合は左側に0を挿入して「11010」でえあれば「0001 1010」のように考えて上位4桁と下位4桁をそれぞれ16進数に置き換える。

# 2. 基数変換
10進数から2進数へ、2進数から10進数へ。表記されている数を別の位取り記数法で表すこと。

値の桁数は、「値を基数で繰り返し割ったときの余り」で決まっている。
**例).10進数**
1. 元の値を10で割り算する。その時の余りが1の位の値。
2. 上記の商を10で割って割り算する。2回目の割り算の余りが10の位の値。
3. 商が0になるまで繰り返す。
4. 最後まで計算したら、求めた余りを右から順番に並べると元の値に戻る。

## 10進数から2進数へ
10進数を2進数に変換するときは、変換したい10進数の値を変換先の基数である「2」で割り算する。
商が0になるまで計算したあと、求めた余りを右から順に並べると、元の10進数を2進数で表せる。

## 10進数を16進数に
1. 変換したい元の10進数の値を商が0になるまで16で割り算する。
2. 余りが0～15になるので、このうち10～15は、A～Fに置き換える。
3. 余りを右から順番に並べる。

## 2進数や16進数を10進数に
ほかの位取り記数法から10進数への変換は、どれも同じ法則で変換できる。
- m進法の「m」が基数になる。
- 桁の重みは「m の n 乗」で表し、n の値は右から順に0、1、2、3････「桁数 - 1」になる。

**例). 2進数: 11010**  
(2^4 * 1) + (2^3 * 1) + (2^2 * 0) + (2^1 * 1)  (2^0 * 0)  
= 16 + 8 + 0 + 2 + 0  
= 26  

**例). 16進数: 1A**  
(16^1 * 1) + (10^0 + 10)  
= 16 + 10  
= 26

# 3. Computer の世界の数字のお話
Computer の世界で Data がどう扱われているか。
### Bit 
1bitは Computer が扱う最小単位で、2進数の1桁を表す。

### Byte
Bit が8個集まると1byte。
- 1byte で2進数の8桁
- 2byte では16桁

を扱うことができる。

Computer が効率よく計算を行うために、決まった大きさの入れ物に Data を入れて読み書きする。  
その入れ物の大きさを表す単位。

### 桁あふれ or Overflow
Computer の入れ物(Byte)に右から桁を埋めていっておさまりきらないこと。  
どんなに Computer の計算が正しくても、Overflow が発生すると正しい答えは得られない。

Overflow は扱う Data に対して入れ物が小さいと発生する。Byte(入れ物) を増やすことで回避する。

## Computer の「演算」
### 算術演算
Computer の世界で
- 足し算
- 引き算
- 掛け算
- 割り算

を行うこと。
### Shift 演算と算術演算
- 2進数の Bit を動かす Shift 演算は、算術演算よりも高速に掛け算・割り算できる。
- 10進数になれている人間には分かりずらい。
- Compiler の性能が向上している現在、処理速度は気にするほどのものではない。
- 数値 Data を扱う場合は Program のわかりやすさを優先して算術演算を利用するべき。

