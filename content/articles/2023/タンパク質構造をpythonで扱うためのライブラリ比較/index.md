Title: タンパク質構造をpythonで扱うためのライブラリを調べてみた
Category: 研究
Tags: protein, pdb, mmcif, python
Summary: タンパク質構造ファイルとpythonで扱うためのライブラリを調べてみた

# 前書き

今までタンパク質の構造データといえばpdbファイルしか知らなかったのですが、mmCIFという形式があることをボスに教えていただいたのでどんなファイル形式が存在するのか、そしてそのファイルをpythonでいじれるライブラリはどんなものがあるのかを調べてみた。

# タンパク質構造のファイル形式

## PDB

拡張子は`.pdb`。
タンパク質の構造を記録するファイルで最も有名なのがpdbファイルだと思います。
1行80文字(パンチカードの幅の成約)以内に収まるように設計されています。
ただし、最近になり構造データが大きくなることでpdb形式の限界に到達したため新しい形式の方が良いです。
具体的には、1行80文字なので99,999原子以下かつ36 chainまで、座標は最大4桁という制限があります。

## mmCIFファイル

拡張子は`.cif`。
上のPDBファイルの問題点を解消したファイル形式。
結晶構造で使われているCIF形式を、高分子用に拡張しています。


## PDBML

mmCIFファイルをxmlで記述した形式(なので拡張子は`.xml`)。
xmlなので多くの分野で使われるツールを使うことができ、XMLスキーマを使った検証も行えます。
PDBデータの正式なXML形式のフォーマットだそうです。

## その他

他にも、NMRで解析した場合に必要なファイルやX線結晶解析の場合に必要なファイルなどがありますが説明は省きます。

# pythonライブラリ

## [rcsb/py-mmcif: mmCIF Core Access Library](https://github.com/rcsb/py-mmcif)

> This module includes a native Python mmCIF API for data files and dictionaries along with pybind11 wrappers for the PDB C++ Core mmCIF Library.

とある通り、低レイヤーなAPIを提供しているみたいです。



## [GEMMI - library for structural biology — Gemmi 0.5.8 documentation](https://gemmi.readthedocs.io/en/latest/)

> Gemmi is a library, accompanied by a set of programs, developed primarily for use in **macromolecular crystallography** (MX). For working with:
>
> - macromolecular models (content of PDB, PDBx/mmCIF and mmJSON files),
> - refinement restraints (CIF files),
> - reflection data (MTZ and mmCIF formats),
> - data on a 3D grid (electron density maps, masks, MRC/CCP4 format)
> - crystallographic symmetry.

もともと高分子結晶学用に開発されていたライブラリーですが、他にもいろいろ使えるみたいです。

ドキュメントをチラ見したところ例えば、下のようなものを見つけました。

* ファイルからモデルを読み込む
* [空間群](https://www.jeol.co.jp/words/emterms/20121023.022259.html)(対称性を扱う議論らしい)をモデルの中から探す
  * `find_spacegroup_by_name`みたいなメソッドがあった
* unit cell(結晶学の用語？)や座標を便利に扱える
* ある原子から一定距離にある原子をリストアップする



## [samirelanduk/atomium: Python macromolecular parsing (with .pdb/.cif/.mmtf parsing and production)](https://github.com/samirelanduk/atomium)

> atomium is a molecular modeller and file parser, capable of reading from and writing to .pdb, .cif and .mmtf files.
>

```python
>>> import atomium
>>> pdb = atomium.fetch("5HVD")
>>> pdb.model
<Model (1 chain, 6 ligands)>
>>> pdb.model.chain("A")
<Chain A (255 residues)>
```

ReadMeに書いてあるexampleを読んだほうが話が早いですが、構造モデルのchain, atomを検索/取得/追加できます。さらに、近くのatomやchainを調べられます。

## [iotbx - file readers and writers — CCTBX Developer documentation](https://cctbx.github.io/iotbx/index.html)

> The iotbx module contains most tools for reading and writing the standard formats used by both macromolecular and small-molecule crystallographers, including PDB, CIF, MTZ, and various other file types. For some formats the resulting data will be encapsulated in objects defined in [`cctbx`](https://cctbx.github.io/cctbx/cctbx.html#module-cctbx) and/or `scitbx`; others have custom classes, in particular PDB/mmCIF files which have their own complex internal representation independent of the X-ray scattering properties.

高分子結晶学でも低分子結晶学でも使えるライブラリーです。ドキュメントをちゃんと読む時間はなかったのですが、上のatomiumと同等の機能はありそうに思えました。

## [soedinglab/pdbx: pdbx is a parser module in python for structures of the protein data bank in the mmcif format](https://github.com/soedinglab/pdbx)

> Proper recognition to the [Protein Data Bank](http://mmcif.wwpdb.org/docs/sw-examples/python/html/index.html) where this library for protein structures in the mmCIF format initially came from. We modified the original library to support python3. This fork is used by scripts in the HHsuite [on GitHub](https://github.com/soedinglab/hh-suite).

チュートリアルが[こちら](https://mmcif.wwpdb.org/docs/sw-examples/python/html/)。flaskみたいに機能は少なめな気がする。

## [Biopython · Biopython](https://biopython.org/)

タンパク質の構造データ以外にも塩基配列など様々な機能が実装されている巨大なライブラリ。

Entity→Structure→Model→Chain→Residue→Atomのように分けられているらしい。

それぞれの値を参照/代入することはもちろん、原子間距離、二面角を求めたりもできる。

# 参考記事

- [PDB データの読み解き方](https://pdbj.org/cms-data/workshop/20130823/kinjo.pdf)
- [蛋白質構造データバンク - Wikipedia](https://ja.wikipedia.org/wiki/蛋白質構造データバンク)
- [PDBデータの書式 - 日本蛋白質構造データバンク](https://pdbj.org/help/data-format?lang=ja)
- [PDB | タンパク質の立体構造データベース](https://bi.biopapyrus.jp/db/pdb.html)
- [Protein Data Bankで利用するPDBx/mmCIF形式について](https://www.jstage.jst.go.jp/article/jcrsj/61/3/61_159/_pdf)
- [Space Group for Crystal Structure Analysis](http://nc-imr.imr.tohoku.ac.jp/HERMES/Analysis/SPGroup.html)
