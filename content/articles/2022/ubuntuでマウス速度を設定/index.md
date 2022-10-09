Title: ubuntuでマウス速度を自動設定
Category: 開発環境
Tags: ubuntu

ubuntuは設定画面から「マウスの速度」を設定できます。

しかし、High DPIディスプレイを使っていると設定画面からできる最大速度より速くしたくなります。

ここでは、ターミナルを起動したときにマウスの速度を設定画面で設定できる最大値以上にする方法を説明します。

# 方法

## デバイスの情報を調べる

まず、目的のデバイスのidと名称を調べます。

```bash
$ xinput list
⎡ Virtual core pointer                          id=2    [master pointer  (3)]
⎜   ↳ Virtual core XTEST pointer                id=4    [slave  pointer  (2)]
⎜   ↳ Logitech MX Ergo Multi-Device Trackball   id=12   [slave  pointer  (2)]
⎣ Virtual core keyboard                         id=3    [master keyboard (2)]
    ↳ Virtual core XTEST keyboard               id=5    [slave  keyboard (3)]
    ↳ Power Button                              id=6    [slave  keyboard (3)]
    ↳ Power Button                              id=7    [slave  keyboard (3)]
    ↳ PFU Limited HHKB-Classic                  id=8    [slave  keyboard (3)]
    ↳ PFU Limited HHKB-Classic Consumer Control id=9    [slave  keyboard (3)]
    ↳ PFU Limited HHKB-Classic Keyboard         id=10   [slave  keyboard (3)]
    ↳ HD Pro Webcam C920                        id=11   [slave  keyboard (3)]
```

私の場合、id=12で名前は`Logitech MX Ergo Multi-Device Trackball`でした。

次に、このマウスに設定できるパラメーターを調べます。

```bash
$ xinput list-props 12
Device 'Logitech MX Ergo Multi-Device Trackball ':
        Device Enabled (156):   1
        Coordinate Transformation Matrix (158): 5.000000, 0.000000, 0.000000, 0.000000, 5.000000, 0.000000, 0.000000, 0.000000, 1.000000
        libinput Natural Scrolling Enabled (508):       0
        libinput Natural Scrolling Enabled Default (509):       0
        libinput Scroll Methods Available (510):        0, 0, 1
        libinput Scroll Method Enabled (511):   0, 0, 0
        libinput Scroll Method Enabled Default (512):   0, 0, 0
        libinput Button Scrolling Button (513): 0
        libinput Button Scrolling Button Default (514): 2
        libinput Button Scrolling Button Lock Enabled (515):    0
        libinput Button Scrolling Button Lock Enabled Default (516):    0
        libinput Middle Emulation Enabled (517):        0
        libinput Middle Emulation Enabled Default (518):        0
        libinput Rotation Angle (519):  0.000000
        libinput Rotation Angle Default (520):  0.000000
        libinput Accel Speed (521):     1.000000
        libinput Accel Speed Default (522):     0.000000
        libinput Accel Profiles Available (523):        1, 1
        libinput Accel Profile Enabled (524):   1, 0
        libinput Accel Profile Enabled Default (525):   1, 0
        libinput Left Handed Enabled (526):     0
        libinput Left Handed Enabled Default (527):     0
        libinput Send Events Modes Available (276):     1, 0
        libinput Send Events Mode Enabled (277):        0, 0
        libinput Send Events Mode Enabled Default (278):        0, 0
        Device Node (279):      "/dev/input/event18"
        Device Product ID (280):        1133, 45085
        libinput Drag Lock Buttons (528):       <no items>
        libinput Horizontal Scroll Enabled (529):       1
        libinput Scrolling Pixel Distance (530):        15
        libinput Scrolling Pixel Distance Default (531):        15
        libinput High Resolution Wheel Scroll Enabled (532):    1
```

ここで、マウス速度のパラメーターは、 `Coordinate Transformation Matrix (158)` です。

## マウス速度を設定する

マウス速度を設定するには、下のようなコマンドを実行すればよいです。

```bash
xinput set-prop 12 158 5 0 0 0 5 0 0 0 1
```

ここで、12はデバイスのid、158はパラメーターのid、5はマウス速度です。

そのため、`~/.zshrc`や`~/.bashrc`などに上のコマンドを書き加えておけば、ターミナルを起動するごとにマウスの速度を設定することができます。

ちなみに、`~/.profile`に上のコマンドを書かない理由は、bluetoothマウスだとしばらく動かさないとPCとの接続が切れその結果マウス速度がリセットされてしまうことがあるためです。
言い換えると、bluetooth接続が切れるたびにログアウトしないとマウス速度を設定できなくなるからです。

## マウスのidが再起動ごとに変わる場合

その場合、マウスのidが12以外のこともあるため上のコードを少し変更する必要があります。

若干汚いコードですが、下のコードを使いました。

```bash
MX_ID=$(xinput list | grep MX | cut -f2 | cut -d'=' -f2)
xinput set-prop ${MX_ID} 158 5 0 0 0 5 0 0 0 1
```

まず、`xinput list`でデバイスidと名前の一覧を表示します。
その結果をパイプでつなぎ、`grep MX`でMXが含まれる行を検索します。
その後、idだけを取り出せるように`cut -f2 | cut -d'=' -f2`としています。

上のようにすれば、MX_IDには私の使っているマウスのIDが代入され、その`MX_ID`をxinputで使うことで、idが変わっても同じスクリプトでマウスの速度を設定できます。


# 謝辞

上の情報を教えてくださったvim-jpの方々に感謝します。

# 参考サイト


- [unity - Change mouse speed on Ubuntu 18.04 - Ask Ubuntu](https://askubuntu.com/questions/1067062/change-mouse-speed-on-ubuntu-18-04/1209053#1209053)

以下3つは試していないが参考サイト。

- [How to set device-specific mouse settings in Wayland under Libinput (Debian Gnome)? - Unix & Linux Stack Exchange](https://unix.stackexchange.com/questions/422470/how-to-set-device-specific-mouse-settings-in-wayland-under-libinput-debian-gnom)
- [Solaar | Linux Device Manager for Logitech Unifying Receivers and Devices.](https://pwr-solaar.github.io/Solaar/)
