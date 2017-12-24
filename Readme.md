# CON-SAI
CON-SAIは[RoboCup SSL](http://wiki.robocup.org/Small_Size_League)に
初めて参加する人でも開発できるサッカーAIです。

**CON**tribution to **S**occer **AI**

![running CON-SAI](https://github.com/SSL-Roots/CON-SAI/blob/Images/Images/CON-SAI-about.png "running CON-SAI")

## CON-SAIの開発コンセプト
CON-SAIを使う前に[コンセプト](doc/Concept.md)を読んでください。

## Requirements
CON-SAIはUbuntu 14.04で作成・テストしてます。

また、使用しているROS IndigoはUbuntu 14.04以下で動作するため、
Ubuntu 14.04のインストールを推奨します。

*Ubuntu 16.04, ROS Kineticに向けても開発中です。*

下記のPCスペックで問題なく動作します。
* Intel(R) Core(TM) i5-6600K CPU @ 3.50GHz
* 8 GB of RAM
* 有線LANポート（試合会場では有線LANでロボット・ボール位置座標データを受信します)

## Installation

### ROSのインストール
[ROS (Robot Operating System)](http://wiki.ros.org/ja)
は、ロボットソフトウェア開発をサポートする
ライブラリ・ツールが豊富に含まれたオープンソースソフトウェアです。

ROSにはいくつかのDistributionがありますが、**Indigo**をインストールしてください。

フルインストール推奨です。

[**ROS Indigo の Ubuntu へのインストール**](
http://wiki.ros.org/ja/indigo/Installation/Ubuntu
)


ROSインストール後はチュートリアルをひと通り実施してください。

(気が早い方は以下を実行)

```zsh
# catkinワークスペースを作成
$ mkdir -p ~/catkin_ws/src
$ cd ~/catkin_ws/src
$ catkin_init_workspace

# ワークスペースのビルド
$ catkin_make

# ワークスペースのオーバレイ
# ***shには使用しているshellを入力 (etc: bash, zsh)
$ source devel/setup.***sh 

# ROSのパッケージを追加するたびに入力する必要があるので
# bashrcやzshrcなどに加えておくと楽です

$ echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
```


### Google Protobufをインストール

[**ダウンロード protobuf-2.5.0.zip**](
https://github.com/google/protobuf/releases/download/v2.5.0/protobuf-2.5.0.zip
)

```zsh
$ cd {Download Directory}
$ unzip protobuf-2.5.0.zip
$ cd protobuf-2.5.0

# Install protobuf for C++
$ ./configure
$ make
$ make check 
# checkでエラー吐いたらREADME.txtを見て対処してください
$ sudo make install
    
# Install protobuf for python
$ cd python
$ python setup.py build
$ python setup.py test
# testでエラーはいたらREADME.txtを見て対処して
$ sudo python setup.py install
```

### その他インストール
```zsh
# ROS Navigationパッケージをインストール
$ sudo apt-get install ros-indigo-navigation
    
# グラフ描画ライブラリ(pygraphviz) をインストール
$ sudo apt-get install graphviz libgraphviz-dev pkg-config
$ sudo pip install pygraphviz --install-option="--include-path=/usr/include/graphviz" --install-option="--library-path=/usr/lib/graphviz/"
```

### CON-SAIをインストール
```zsh
# CON-SAIをクローン
$ git clone https://github.com/SSL-Roots/CON-SAI ~/catkin_ws/src/CON-SAI

# サブモジュール化したライブラリをダウンロード
$ cd ~/catkin_ws/src/CON-SAI
$ git submodule init
$ git submodule update

# ワークスペースに移動しCON-SAIをコンパイル
$ cd ~/catkin_ws
$ catkin_make

# エラーがでなければOK
```

CON-SAIの使い方は[チュートリアル](Tutorial.md)に書いてます。

チュートリアルを始める前に下記のgrSimとReferee Boxをインストールしてください。

## RoboCup SSLのAI開発に必要なツールをインストール

RoboCup SSLのAI開発にはシミュレータ(grSim)と審判ソフト(Referee Box)があると便利です。

インストール方法は各ページをご参照ください。

[grSim](https://github.com/RoboCup-SSL/grSim)

![grSim Image](https://github.com/SSL-Roots/CON-SAI/blob/Images/Images/grSim.png "grSim")

[Referee Box](https://robocup-ssl.github.io/ssl-refbox/)

![Referee Box Image](https://github.com/SSL-Roots/CON-SAI/blob/Images/Images/refereeBox.png "Referee Box")

## Tutorial

grSimを使ったシミュレータ上でのロボット操作方法、
実機ロボットの操作方法はこちらに書いてます。

[チュートリアル](doc/Tutorial.md)


## Author

CON-SAIはRoboCup SSLに参加している日本人チーム**Roots**が作成しています。

RoboCup SSLへの参加方法、ロボットに必要な機能、開発環境などは
Rootsのホームページに記載してます。


[Roots - Home](https://github.com/SSL-Roots/Roots_home/wiki)
