# 文系 Programmer のための Python で学び直す高校数学

# 第1章　Computer と「数」

# 1. 位取り記数法

位取り記数法とは「数」を表す方法のこと。

使用者 | 位取り記数法
--- | ---
人間 | 10進位取り記数法
Computer | 2進位取り記数法

２つの違いは 数を数える時に使える数字の種類。

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
  例). 2進数: 「11111111」ぱっとみて何桁か分からない。16進数「FF」=>2進数「1111 1111」に変換できる。
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

10進数を2進数に変換するときは、変換したい10進数の値を変換先の基数である「2」で割り算する。 商が0になるまで計算したあと、求めた余りを右から順に並べると、元の10進数を2進数で表せる。

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

# 便利な公式

## 点から直線までの距離を求める公式

![\begin{align*} \frac{|ax_1 + by_1 + c|}{\sqrt{a^2 + b^2}} \end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%5Cfrac%7B%7Cax_1+%2B+by_1+%2B+c%7C%7D%7B%5Csqrt%7Ba%5E2+%2B+b%5E2%7D%7D%0A%5Cend%7Balign%2A%7D%0A)

## 直線で囲まれた領域の面積

### ヘロンの公式

三角形の各辺の長さを a, b, c, この合計を2で割ったものをsとすると、三角形の面積Sは

![\begin{align*} S = \sqrt{s(s-a)(s-b)(s-c)} \end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AS+%3D+%5Csqrt%7Bs%28s-a%29%28s-b%29%28s-c%29%7D%0A%5Cend%7Balign%2A%7D%0A)

で求められる。

# 第4章 ベクトル

## ベクトルとは

**方向**と**大きさ**で１つの意味を持つ量のこと。

- 数学の世界では矢印の向きで方向、長さで大きさを表す。
- ベクトルを扱うときは方向と大きさが重要であり、位置はどこでもかまわない。
- 座標の原点を始点とするベクトルを**位置ベクトル**という。

## ベクトルの大きさ

三平方の定理を使って求めることができる。  
ex).  
![\begin{align*} \left|\vec{OA}\right|=\sprt{2^2+3^2} \end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%5Cleft%7C%5Cvec%7BOA%7D%5Cright%7C%3D%5Csprt%7B2%5E2%2B3%5E2%7D%0A%5Cend%7Balign%2A%7D%0A)

## 内積の性質

### 内積の結果を見ると２つのベクトルの位置関係がわかる

大きさが１の単位ベクトルで内積を計算すると必ずー１～１の値になる。

内積の結果 | ２つのベクトルが作る角度
--- | ---
正 | 90度未満(鋭角)
０ | 直角
負 | 90度以上(鈍角)

## ベクトルの外積

1. 外積は２つのベクトルに垂直なベクトルになる。
2. そのベクトルの大きさは、２つのベクトルが作る平行四辺形の面積と等しい。

# 行列

## 逆行列と連立方程式

逆行列を利用すると連立方程式が解ける

## 図形の一次変換

## ベクトルと行列の関係

### 一次変換

一次式で表すことができる変換。

### 変換行列

座標を変換するための行列

## 図形の拡大と縮小

元座標を x 方向に a 倍、y 方向に b 倍すると、図形を任意の大きさに拡大できる。  
※ a = b のときは、**相似変換**になる。

### 相似変換

元の図形の形を保ったま拡大・縮小すること。

# 一次変換の組み合わせ

複数の座標交換を組み合わせる場合は、先に処理する交換が掛け算の右側になる。  
※行列の掛け算では多くの場合交換法則は成立しない。

# 集合と確率

## 集合

はっきりと区別できて、同じ性質を持った Data の集まり。

### 集合の表し方

![\begin{align*} A = \{1, 2, 3, 4,5, 6, 7, 8, 9, 10\} \end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AA+%3D+%5C%7B1%2C+2%2C+3%2C+4%2C5%2C+6%2C+7%2C+8%2C+9%2C+10%5C%7D%0A%5Cend%7Balign%2A%7D%0A)

- 「A」は集合に付けた名前
- { }に含まれる個々の値を**要素**という。  
  ※ １つの集合に同じ要素が含まれることはない。  
  ※ 集合の要素に順番という概念はない。

## いろいろな演算

### 集合演算

ある明確な条件に基づいて Group 分けをすること。

### 部分集合

A という集合の要素が別の U という集合に全て含まれている時に、集合A は、集合Uの**部分集合**と言う。

![\begin{align*} U \supset A \end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AU+%5Csupset+A%0A%5Cend%7Balign%2A%7D%0A)

と表記する。

### 補集合

A という集合が、別の U という集合に全て含まれている時に、A に含まれない要素のこと。

![\begin{align*} \overline{A} = \{ 1, 3, 5, 7, 9 \} \end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%5Coverline%7BA%7D+%3D+%5C%7B+1%2C+3%2C+5%2C+7%2C+9+%5C%7D%0A%5Cend%7Balign%2A%7D%0A)

と表記する。

### 全体集合

部分集合が属する集合のこと。

### 積集合

２つの集合に共通する集合のこと。  
![\begin{align*} A \cap B \end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AA+%5Ccap+B%0A%5Cend%7Balign%2A%7D%0A)

と表記する。

### 和集合

２つの集合の全要素を合わせた集合のこと。  
![\begin{align*} A \cup B \end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AA+%5Ccup+B%0A%5Cend%7Balign%2A%7D%0A)

と表記する。

### 差集合

一方の集合から、もう一方の集合を引いたもの。  
※どちらの集合から引くかによって結果がかわる。

### 対象差

２つの集合のすべての要素から、共通する要素を取り除いたもの。

### 空集合

集合演算の結果、要素が１つもない集合のこと。  
∅

という記号で表す。

### 集合と Database

Bigdata のように大量にある情報の中から必要な情報を抜き出して Database を構築・分析・活用するには集合の知識が役立つ。

## 順列と組み合わせ

### 場合の数

そこで起こりうる事象の数のこと。  
確率を求めるときに必要な値。

- 図や一覧を書く。
- 積の法則や和の法則を使う。
- 集合の要素数を利用する。

などを行い全体でどれだけの数があるか正しく把握することが大事。

### 「施行」と「事象」の関係

用語 | 意味 | 例
--- | --- | ---
施行 | 同じ条件のもとで繰り返し行うことができて、その結果が偶然い左右される実験や観察のこと。 | サイコロを投げる。
事象 | 施行の結果として起こる出来事。 | １がでた。

### 場合の数の求め方

用語 | 意味 | 算出式
--- | --- | ---
積の法則 | ２つの事象、A と B があり、A が a通り、B が b通りあるときの「場合の数」を求める法則| a * b 通り
和の法則 | ２つの事象、 A と B があり、どちらしか起こらないとして A が a通り、B が b通りあるときに、どちらかが起こる「場合の数」を求める法則 | a + b通り

### 順列

用語 | 意味 | 例・式
--- | --- | ---
樹形図 | 木の枝が伸びていくような形の図
順列 | 順番を考えて並べること | ![\begin{align*}{}_n P_r\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%7B%7D_n+P_r%0A%5Cend%7Balign%2A%7D%0A)

### 階乗

用語 | 意味 | 式・例
--- | --- | ---
階乗 | 1から n までの自然数を掛け合わせたもの | ![\begin{align*}n!\end{align*}](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0An%21%0A%5Cend%7Balign%2A%7D%0A)

### 重複順列

同じものを使ってもよいという条件のもとで順番に並べること。

![\begin{align*} {}_n \Pi_r = n^r \end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%7B%7D_n+%5CPi_r+%3D+n%5Er%0A%5Cend%7Balign%2A%7D%0A)

で場合の数を計算できる