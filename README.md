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

で場合の数を計算できる。

### 組み合わせ

順番は考慮せずに選び方だけを重視するもの

![\begin{align*} {}_n C_r \end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%7B%7D_n+C_r%0A%5Cend%7Balign%2A%7D%0A)

のように表す。C は、combination の頭文字。

![\begin{align*} {}_n C_r = \frac{{}_n P_r}{r!} \end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%7B%7D_n+C_r+%3D+%5Cfrac%7B%7B%7D_n+P_r%7D%7Br%21%7D%0A%5Cend%7Balign%2A%7D%0A)

で計算することができる。

## 確率

### 機械学習

大量の Data を使って反復的に学習することによって、何らかの特徴を見つけ出す技術。

- ECサイトのあなたにおすすめの商品
- 文字をカメラで撮影するだけで翻訳してくれる Application.

など。機会学習には「確率」や「乱数」が必須知識。

### 確率

ある施行を行ったとき、その結果として起こりうるすべての事象のうち、特定の事象になる割合のこと。

確率 p の範囲は必ず

![\begin{align*} 0 \leqq p \leqq 1 \end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A0+%5Cleqq+p+%5Cleqq+1%0A%5Cend%7Balign%2A%7D%0A)

になる。p = 0 の場合は、その事象が起こる可能性がないことを表し、p = 1 であればその事象が必ず起こることになる。

## 数学的確率と統計的確率

### 数学的確率

それぞれの事象がほぼ同じ程度で発生することが予想されることを「同様に確からしい」と表現し、ある事象A が起こる確率p のこと。

### 統計的確率

過去の Data をもとに計算した値で、Data 数が増えれば変化する可能性のある確率のこと。

# 統計と乱数

## 母集団と標本

### 母集団

本当に調べたい集団全体のこと。

### 標本

母集団の中から無作為に選んだ集団のこと。

### 推測統計学

標本から母集団を推測することを研究する領域。

## Data のばらつき具体を見る

### 度数分布図または Histogram

Data のばらつき具合がひと目でわかる図のこと。

### 分布

Data のばらつき状態のこと。

### 分布曲線

Data のばらつきの様子をなだらかな曲線で表したもの。  
集団の特徴を分析するときに、度数分布図の形が重要になる。分布曲線の山の形に偏りがあるときは注意が必要になり、平均値だけを見ていても、それが集団の 一般的な値とは限らなくなる。

### 正規分布

分布曲線の山の形が左右対称になっている分布。  
ex). 年齢別の身長や体重、桜の開花日や梅雨入りの日、工場で生産されているおにぎりや工業製品の長さや重さなどが正規分布になることが知られている。

### 一様分布

分布曲線が一定で、サイコロを何百回も振ったときの目の出方のようなときになる。

## 平均値、中央値、最頻値

### 代表値

平均値、中央値、最頻値など、集団の傾向を見るときに使う値。

### 平均値

全ての Data を合計して、その Data 数で割った値。

![\begin{align*} \bar{x} &= \frac{1}{n} \sum_{i=1}^{n}x_i \end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%5Cbar%7Bx%7D+%26%3D+%5Cfrac%7B1%7D%7Bn%7D+%5Csum_%7Bi%3D1%7D%5E%7Bn%7Dx_i%0A%5Cend%7Balign%2A%7D%0A)

集団の中の一般の値と解釈されがち。集団を形成する Data に偏りがないときが前提になる。  
極端な値に大きく作用される。

### 中央値（中間地、中位置）

Data を小さい順に並べたときに、順番的に真ん中にくる値。  
Data が奇数の場合は真ん中の自然数。Data が偶数の時は、真ん中の２つの数字の平均が中央値になる。  
集団の形が正規分布や一様分布のとき、平均値と中央値ははぼ同じ値になる。偏りがある場合は、代表値としてふさわしいこともある。

### 最頻値（ Mode ）

集団の中で、度数がもっとも大きな値。  
ex). 既製服を作る場合は、平均値よりも**最頻値**を利用した方が、より多くの人に Fit する製品を作ることができます。

## 度数分布図

Data がどのように分布されているか、ひと目で把握できる図。

### 度数分布図の作り方

1. Data の取り得る範囲を等間隔に分ける(**階級**)
2. 各階級に含まれる Data 数を数える(**度数**)
3. 横軸に階級、縦軸に度数をとって棒グラフを作成する

## 分散と標準偏差

### 分散

「Data - 平均」を使って求めた値。

### 標準偏差

**分散**を元の値に戻すためにい平方根をとった値。

## 偏差値

単純に値でけでは比べられない時の判断基準として使う。

### 標準化

正規分布にもいりいろな形がある。例えば、

- 平均値が同じでも標準偏差が異なる場合は山の高さが変わる。
- 標準偏差が同じでも平均値が異なる場合は、山の出現する場所が変わる。

単純に比較できないないときに、**標準化**という作業を行う。

標準化した Data で度数分布図を描くと、正規分布の形が統一される。山の中心からどれだけ離れているかを見れば、それがどいう値か判断できるようになる。  
しかし、

1. 平均が0というのは現実味がない値
2. 標準化した後の Data は小さな値になる。

### 標準化の式

平均値が０、分散が１となるように Data を変換する。

![\begin{align*} Z = \frac{x_i - \bar{x}}{s} \end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AZ+%3D+%5Cfrac%7Bx_i+-+%5Cbar%7Bx%7D%7D%7Bs%7D%0A%5Cend%7Balign%2A%7D%0A)

### 偏差値

![\begin{align*} T = \frac{x_i - \bar{x}}{s} 10 + 50 \end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AT+%3D+%5Cfrac%7Bx_i++-++%5Cbar%7Bx%7D%7D%7Bs%7D+10+%2B+50%0A%5Cend%7Balign%2A%7D%0A)

平均の値を50として、そこから Data がどれだけ離れているかを見るようにした値。

- 利用する時は、基となる集団の形が正規分布になっていることが大前提。Data に偏りがあるときに偏差値を見ても意味がない。
- 特定の集団の中での位置を示しているだけにすぎない。

## 関係を調べる

### 散布図

２つの Data の関係性を表す図。

### 相関

**「相関」**とは、**「関係がある」**という意味。

### 正の相関

散布図で点群が右上がりになっているとき。x の値が増えるにつれて y の値も増えるという関係にある。

### 負の相関

散布図で点群が右下がりになるとき。x の値が増加すると y の値が減少する関係。

### 無相関

散布図で点群がバラバラな場合。Data に関係性は見られないと判断する。

## 共分散と相関係数

### 共分散

![\begin{align*} s_{xy} = \frac{1}{n}\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})
\end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0As_%7Bxy%7D+%3D+%5Cfrac%7B1%7D%7Bn%7D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28x_i+-+%5Cbar%7Bx%7D%29%28y_i+-+%5Cbar%7By%7D%29%0A%5Cend%7Balign%2A%7D%0A)

関係性を調べる２つの Data のそれぞれの値からそれぞれの値の平均値を引いた値を掛け算した時に

- 答えが正の値になるのは x と y の両方が平均値よりも大きい、もしくは小さいとき。
- 答えが負の値になるのは、一方が平均値より大きくて、もう一方が平均値よりも小さいとき。

すべての値についてこの値を調べて符号を見ることで２つの関係性を理解すること。  
※代表値として平均値を使う。

### 相関係数

**共分散**の単位が定まらず評価が難しいところを**標準化**したもの。  
必ずー１～１の値になり、一般的に

相関係数 | 意味
--- | ---
0 ~ 0.2 | ほとんど相関がない
0.2 ~ 0.4 | やや相関がある
0.4 ~ 0.7 | かなり相関がある
0.7 ~ 1.0 | 強い相関がある

という言葉に置き換えて使用される。（※負の値でも相関の強さを示す意味は同じ）

相関係数は、書きの式で求められる。

![\begin{align*} r_{xy} = \frac{s_{xy}}{s_x s_y} = \frac{\sum_{i = 1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i = 1}^n (x_i - \bar{x})^2}\sqrt{\sum_{i = 1}^n (y_i - \bar{y})^2}} = \frac{1}{n} \sum_{i = 1}^n \frac{x_i - \bar{x}}{s_x} \cdot \frac{y_i - \bar{y}}{s_y} \end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Ar_%7Bxy%7D%0A%3D+%5Cfrac%7Bs_%7Bxy%7D%7D%7Bs_x+s_y%7D%0A%3D+%5Cfrac%7B%5Csum_%7Bi+%3D+1%7D%5En+%28x_i+-+%5Cbar%7Bx%7D%29%28y_i+-+%5Cbar%7By%7D%29%7D%7B%5Csqrt%7B%5Csum_%7Bi+%3D+1%7D%5En+%28x_i+-+%5Cbar%7Bx%7D%29%5E2%7D%5Csqrt%7B%5Csum_%7Bi+%3D+1%7D%5En+%28y_i+-+%5Cbar%7By%7D%29%5E2%7D%7D%0A%3D+%5Cfrac%7B1%7D%7Bn%7D+%5Csum_%7Bi+%3D+1%7D%5En+%5Cfrac%7Bx_i+-+%5Cbar%7Bx%7D%7D%7Bs_x%7D+%5Ccdot+%5Cfrac%7By_i+-+%5Cbar%7By%7D%7D%7Bs_y%7D%0A%5Cend%7Balign%2A%7D%0A)

## Data から推測する

集まった Data を分析して、そこから何かしらの傾向や性質を見つけ出すこと。

## 移動平均法

注目 Data を中心に前後いくつかの平均値をとり、その値で注目 Data の値を置き換える方法。

## 回帰直線

散布図の点群の間をそれぞれの点とのずれの合計値が最小になるようにした直線。  
その傾きと切片は、次の式で求めることができる。

**傾き**

![\begin{align*} slope = \frac{\frac{1}{n}\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\frac{1}{n}\sum_{i=1}^n(x_i - \bar{x})^2} \end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Aslope+%3D+%5Cfrac%7B%5Cfrac%7B1%7D%7Bn%7D%5Csum_%7Bi%3D1%7D%5E%7Bn%7D%28x_i+-+%5Cbar%7Bx%7D%29%28y_i+-+%5Cbar%7By%7D%29%7D%7B%5Cfrac%7B1%7D%7Bn%7D%5Csum_%7Bi%3D1%7D%5En%28x_i+-+%5Cbar%7Bx%7D%29%5E2%7D%0A%5Cend%7Balign%2A%7D%0A)

**切片**

![\begin{align*} Intercept = \frac{1}{n}\sum_{i=1}^{n}y_i - (slope \cdot \frac{1}{n}\sum_{i=1}^{n}x_i)
\end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0AIntercept+%3D+%5Cfrac%7B1%7D%7Bn%7D%5Csum_%7Bi%3D1%7D%5E%7Bn%7Dy_i+-+%28slope+%5Ccdot+%5Cfrac%7B1%7D%7Bn%7D%5Csum_%7Bi%3D1%7D%5E%7Bn%7Dx_i%29%0A%5Cend%7Balign%2A%7D%0A)

## 回帰分析

回帰直線を利用して値を検証したり、未来を予測すること。

## Random に値を選ぶ

### 乱数

並びに規則性がなく、それぞれの数の出現回数がほぼ同じであるもの。  
<small>※ **擬似乱数**: Computer が生成した乱数。何らかの計算式で求められている。</small>

### 乱数を使うときに注意すること

計算式が発生する乱数には必ず何かの周期性がある。乱数を求める要素のことを**乱数の種(シード: seed)**という。  
ほとんどのPrograming 言語には乱数の種を初期化する命令があり、Computer の System 時刻と組み合わせるて実行するのが一般的。

# 微分・積分

### 微分

変化の様子を分析するための道具

## 変化を知る手がかり

曲線の山の頂上を正確に見つける作業

1. 隣り合う２つの年度の差分をとる
2. その差分を使って Graph を描く

## 微分とは

連続して変化する値の、ごく微かな部分に注目して変化の様子を調べること。

### 変化率

変化の様子、

![\begin{align*} \frac{\Delta y}{\Delta x} \end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%5Cfrac%7B%5CDelta+y%7D%7B%5CDelta+x%7D%0A%5Cend%7Balign%2A%7D%0A)

という比で表せる値。

### 微分係数

![\begin{align*} \lim_{h \to 0} \frac{f(a + h)-f(a)}{h} \end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%5Clim_%7Bh+%5Cto+0%7D+%5Cfrac%7Bf%28a+%2B+h%29-f%28a%29%7D%7Bh%7D%0A%5Cend%7Balign%2A%7D%0A)

のように表す。「h が限りなく０にちかづくとき」という意味で、０になることはない。  
微分係数とは、**ある点における変化率**

## 微分する

変化の様子を見る、という意味。x の値をほんの少しずつ動かしながら、y の値がどう変化するかを調べている。

一般式で表すと
![\begin{align*} \lim_{n \to 0} \frac{f(x + h) - f(x)}{h} \end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%5Clim_%7Bn+%5Cto+0%7D+%5Cfrac%7Bf%28x+%2B+h%29+-+f%28x%29%7D%7Bh%7D%0A%5Cend%7Balign%2A%7D%0A)

となり、この式を**関数 f(x) の指導関数**という。

- 微分係数
- 導関数

どちらも簡単に言えば「変化の様子を見る」、それでけのこと。

## 微分の公式

f(x) | f'(x)
--- | ---
k(定数) | 0
x | 1
x^n | nx^{n-1}

## 導関数が教えてくれること

### 極値

なめらかに連続する山の中にある

- 谷の底を**極小**
- 山の頂上を**極大**

という。

## 変曲点

関数f(x) の変化がもっとも大きな地点。「変化率が高い」「変化が大きい」地点。

<small>
※極大と極小は、Graph によっては何回も登場することがあり、場合によっては極大値が極小値を下回る（逆もしかり）ことのある。
極大と極小を最大値と最小値と近藤しないように気をつける
</small>

# 積分とは

1. 積分は面積を扱う
2. 積分は微分の逆演算

## 変化を積み重ねる

「ある部分を積み重ねる」から**積分**。積み重ねとは、足し算そのもの

## 積分する

連続して変化する値を足して、合計を求める

式で表すと

![\begin{align*} \int f(x)dx \end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%5Cint+f%28x%29dx%0A%5Cend%7Balign%2A%7D%0A)

上記の式の意味は、「関数 f(x)に、ごく小さな値 dx を与えたときの合計を求める」と思えばよい。

曲線で囲まれた領域の面積を求める公式はないため、極細の棒を敷き詰め、それを加算して面積を求めるという方法を利用する。 そのため、棒の幅が広いと誤差が生じてしまう。「ごく小さな値」というのが大事になる。

## 定積分・不定積分

### 定積分

範囲を決めて積分をすること。

![\begin{align*} \int_a^b f(x)dx \end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%5Cint_a%5Eb+f%28x%29dx%0A%5Cend%7Balign%2A%7D%0A)

「f(x) に a から b までの範囲で、ごく小さな値 dx を入れて積分する」という意味になる。

### 不定積分

積分する範囲を指定していない式のこと。

![\begin{align*} \int f(x)dx \end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%5Cint+f%28x%29dx%0A%5Cend%7Balign%2A%7D%0A)

### 原始関数

微分して

![\begin{align*} f(x)
\end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Af%28x%29%0A%5Cend%7Balign%2A%7D%0A)

になる関数のこと。  
原始関数を求めることを「f((x) を不定積分する」と言う。

## 積分の公式

## 不定積分を求める公式

![\begin{align*} \int x^ndx = \frac{1}{n+1} x^{n+1} + C \end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%5Cint+x%5Endx+%3D+%5Cfrac%7B1%7D%7Bn%2B1%7D+x%5E%7Bn%2B1%7D+%2B+C%0A%5Cend%7Balign%2A%7D%0A)

（ただし、C は積分定数）

## 定積分を求める公式

![\begin{align*} \int_a^b f(x)dx = [F(x)]_a^b = F(b) - F(a)
\end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0A%5Cint_a%5Eb+f%28x%29dx+%3D+%5BF%28x%29%5D_a%5Eb+%3D+F%28b%29+-+F%28a%29%0A%5Cend%7Balign%2A%7D%0A)

# 道具としての微分・積分

微分 | 変化の様子を知る為の道具。
--- | ---
積分 | ごく小さな部部の合計を知るための道具

## 曲線の接線
微分係数とは、

![\begin{align*}
y = f(x)
\end{align*}
](https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Balign%2A%7D%0Ay+%3D+f%28x%29%0A%5Cend%7Balign%2A%7D%0A)

の x = a におけいる接線の傾きである。