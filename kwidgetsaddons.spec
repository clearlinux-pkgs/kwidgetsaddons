#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: fbbd4e3
#
# Source0 file verified with key 0x2C8DF587A6D4AAC1 (nicolas.fella@kde.org)
#
Name     : kwidgetsaddons
Version  : 6.12.0
Release  : 98
URL      : https://download.kde.org/stable/frameworks/6.12/kwidgetsaddons-6.12.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.12/kwidgetsaddons-6.12.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.12/kwidgetsaddons-6.12.0.tar.xz.sig
Source2  : 2C8DF587A6D4AAC1.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause CC0-1.0 GPL-2.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kwidgetsaddons-data = %{version}-%{release}
Requires: kwidgetsaddons-lib = %{version}-%{release}
Requires: kwidgetsaddons-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : python3-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KWidgetsAddons
Large set of desktop widgets
## Introduction
This repository contains add-on widgets and classes for applications
that use the Qt Widgets module. If you are porting applications from
KDE Platform 4 "kdeui" library, you will find many of its classes here.

%package data
Summary: data components for the kwidgetsaddons package.
Group: Data

%description data
data components for the kwidgetsaddons package.


%package dev
Summary: dev components for the kwidgetsaddons package.
Group: Development
Requires: kwidgetsaddons-lib = %{version}-%{release}
Requires: kwidgetsaddons-data = %{version}-%{release}
Provides: kwidgetsaddons-devel = %{version}-%{release}
Requires: kwidgetsaddons = %{version}-%{release}

%description dev
dev components for the kwidgetsaddons package.


%package lib
Summary: lib components for the kwidgetsaddons package.
Group: Libraries
Requires: kwidgetsaddons-data = %{version}-%{release}
Requires: kwidgetsaddons-license = %{version}-%{release}

%description lib
lib components for the kwidgetsaddons package.


%package license
Summary: license components for the kwidgetsaddons package.
Group: Default

%description license
license components for the kwidgetsaddons package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 2C8DF587A6D4AAC1' gpg.status
%setup -q -n kwidgetsaddons-6.12.0
cd %{_builddir}/kwidgetsaddons-6.12.0
pushd ..
cp -a kwidgetsaddons-6.12.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1742406653
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1742406653
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kwidgetsaddons
cp %{_builddir}/kwidgetsaddons-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/kwidgetsaddons/07c1ab270255cf247438e2358ff0c18835b6a6ce || :
cp %{_builddir}/kwidgetsaddons-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kwidgetsaddons/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kwidgetsaddons-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kwidgetsaddons/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/kwidgetsaddons-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kwidgetsaddons/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kwidgetsaddons-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kwidgetsaddons/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kwidgetsaddons-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kwidgetsaddons/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/kwidgetsaddons-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kwidgetsaddons/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/kwidgetsaddons-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kwidgetsaddons/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/kwidgetsaddons-%{version}/LICENSES/LGPL-3.0-or-later.txt %{buildroot}/usr/share/package-licenses/kwidgetsaddons/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/kwidgetsaddons-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kwidgetsaddons/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kwidgetsaddons-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kwidgetsaddons/e458941548e0864907e654fa2e192844ae90fc32 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/locale/af/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/ar/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/as/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/ast/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/az/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/be/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/be@latin/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/bg/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/bn/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/bn_IN/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/br/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/bs/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/ca/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/crh/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/cs/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/csb/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/cy/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/da/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/de/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/el/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/en/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/eo/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/es/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/et/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/eu/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/fa/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/fi/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/fr/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/fy/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/ga/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/gl/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/gu/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/ha/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/he/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/hi/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/hne/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/hr/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/hsb/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/hu/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/hy/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/ia/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/id/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/is/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/it/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/ja/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/ka/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/kk/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/km/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/kn/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/ko/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/ku/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/lb/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/lt/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/lv/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/mai/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/mk/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/ml/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/mr/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/ms/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/nb/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/nds/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/ne/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/nl/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/nn/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/oc/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/or/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/pa/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/pl/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/ps/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/pt/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/ro/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/ru/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/sa/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/se/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/si/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/sk/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/sl/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/sq/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/sr/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/sr@ijekavian/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/sr@latin/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/sv/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/ta/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/te/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/tg/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/th/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/tr/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/tt/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/ug/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/uk/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/uz/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/uz@cyrillic/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/vi/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/wa/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/xh/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/zh_HK/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/kwidgetsaddons6_qt.qm
/usr/share/qlogging-categories6/kwidgetsaddons.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/KWidgetsAddons/KAcceleratorManager
/usr/include/KF6/KWidgetsAddons/KActionMenu
/usr/include/KF6/KWidgetsAddons/KActionSelector
/usr/include/KF6/KWidgetsAddons/KAdjustingScrollArea
/usr/include/KF6/KWidgetsAddons/KAnimatedButton
/usr/include/KF6/KWidgetsAddons/KAssistantDialog
/usr/include/KF6/KWidgetsAddons/KBusyIndicatorWidget
/usr/include/KF6/KWidgetsAddons/KCapacityBar
/usr/include/KF6/KWidgetsAddons/KCharSelect
/usr/include/KF6/KWidgetsAddons/KCollapsibleGroupBox
/usr/include/KF6/KWidgetsAddons/KColorButton
/usr/include/KF6/KWidgetsAddons/KColorCombo
/usr/include/KF6/KWidgetsAddons/KColumnResizer
/usr/include/KF6/KWidgetsAddons/KContextualHelpButton
/usr/include/KF6/KWidgetsAddons/KCursor
/usr/include/KF6/KWidgetsAddons/KDateComboBox
/usr/include/KF6/KWidgetsAddons/KDatePicker
/usr/include/KF6/KWidgetsAddons/KDatePickerPopup
/usr/include/KF6/KWidgetsAddons/KDateTimeEdit
/usr/include/KF6/KWidgetsAddons/KDragWidgetDecorator
/usr/include/KF6/KWidgetsAddons/KDualAction
/usr/include/KF6/KWidgetsAddons/KEditListWidget
/usr/include/KF6/KWidgetsAddons/KFontAction
/usr/include/KF6/KWidgetsAddons/KFontChooser
/usr/include/KF6/KWidgetsAddons/KFontChooserDialog
/usr/include/KF6/KWidgetsAddons/KFontRequester
/usr/include/KF6/KWidgetsAddons/KFontSizeAction
/usr/include/KF6/KWidgetsAddons/KGradientSelector
/usr/include/KF6/KWidgetsAddons/KGuiItem
/usr/include/KF6/KWidgetsAddons/KJobWidgets
/usr/include/KF6/KWidgetsAddons/KLed
/usr/include/KF6/KWidgetsAddons/KLineEditEventHandler
/usr/include/KF6/KWidgetsAddons/KLineEditUrlDropEventFilter
/usr/include/KF6/KWidgetsAddons/KMessageBox
/usr/include/KF6/KWidgetsAddons/KMessageBoxDontAskAgainInterface
/usr/include/KF6/KWidgetsAddons/KMessageBoxNotifyInterface
/usr/include/KF6/KWidgetsAddons/KMessageDialog
/usr/include/KF6/KWidgetsAddons/KMessageWidget
/usr/include/KF6/KWidgetsAddons/KMimeTypeChooser
/usr/include/KF6/KWidgetsAddons/KMimeTypeChooserDialog
/usr/include/KF6/KWidgetsAddons/KMimeTypeEditor
/usr/include/KF6/KWidgetsAddons/KMultiTabBar
/usr/include/KF6/KWidgetsAddons/KMultiTabBarButton
/usr/include/KF6/KWidgetsAddons/KMultiTabBarTab
/usr/include/KF6/KWidgetsAddons/KNewPasswordDialog
/usr/include/KF6/KWidgetsAddons/KNewPasswordWidget
/usr/include/KF6/KWidgetsAddons/KPageDialog
/usr/include/KF6/KWidgetsAddons/KPageModel
/usr/include/KF6/KWidgetsAddons/KPageView
/usr/include/KF6/KWidgetsAddons/KPageWidget
/usr/include/KF6/KWidgetsAddons/KPageWidgetItem
/usr/include/KF6/KWidgetsAddons/KPageWidgetModel
/usr/include/KF6/KWidgetsAddons/KPassword
/usr/include/KF6/KWidgetsAddons/KPasswordDialog
/usr/include/KF6/KWidgetsAddons/KPasswordLineEdit
/usr/include/KF6/KWidgetsAddons/KPixmapRegionSelectorDialog
/usr/include/KF6/KWidgetsAddons/KPixmapRegionSelectorWidget
/usr/include/KF6/KWidgetsAddons/KPixmapSequence
/usr/include/KF6/KWidgetsAddons/KPixmapSequenceOverlayPainter
/usr/include/KF6/KWidgetsAddons/KPixmapSequenceWidget
/usr/include/KF6/KWidgetsAddons/KPopupFrame
/usr/include/KF6/KWidgetsAddons/KRatingPainter
/usr/include/KF6/KWidgetsAddons/KRatingWidget
/usr/include/KF6/KWidgetsAddons/KRecentFilesMenu
/usr/include/KF6/KWidgetsAddons/KRuler
/usr/include/KF6/KWidgetsAddons/KSelectAction
/usr/include/KF6/KWidgetsAddons/KSelector
/usr/include/KF6/KWidgetsAddons/KSeparator
/usr/include/KF6/KWidgetsAddons/KSplitterCollapserButton
/usr/include/KF6/KWidgetsAddons/KSqueezedTextLabel
/usr/include/KF6/KWidgetsAddons/KStandardGuiItem
/usr/include/KF6/KWidgetsAddons/KStyleExtensions
/usr/include/KF6/KWidgetsAddons/KTimeComboBox
/usr/include/KF6/KWidgetsAddons/KTitleWidget
/usr/include/KF6/KWidgetsAddons/KToggleAction
/usr/include/KF6/KWidgetsAddons/KToggleFullScreenAction
/usr/include/KF6/KWidgetsAddons/KToolBarLabelAction
/usr/include/KF6/KWidgetsAddons/KToolBarPopupAction
/usr/include/KF6/KWidgetsAddons/KToolBarSpacerAction
/usr/include/KF6/KWidgetsAddons/KToolTipWidget
/usr/include/KF6/KWidgetsAddons/KTwoFingerSwipe
/usr/include/KF6/KWidgetsAddons/KTwoFingerTap
/usr/include/KF6/KWidgetsAddons/KUrlLabel
/usr/include/KF6/KWidgetsAddons/KViewStateMaintainerBase
/usr/include/KF6/KWidgetsAddons/KViewStateSerializer
/usr/include/KF6/KWidgetsAddons/KXYSelector
/usr/include/KF6/KWidgetsAddons/kacceleratormanager.h
/usr/include/KF6/KWidgetsAddons/kactionmenu.h
/usr/include/KF6/KWidgetsAddons/kactionselector.h
/usr/include/KF6/KWidgetsAddons/kadjustingscrollarea.h
/usr/include/KF6/KWidgetsAddons/kanimatedbutton.h
/usr/include/KF6/KWidgetsAddons/kassistantdialog.h
/usr/include/KF6/KWidgetsAddons/kbusyindicatorwidget.h
/usr/include/KF6/KWidgetsAddons/kcapacitybar.h
/usr/include/KF6/KWidgetsAddons/kcharselect.h
/usr/include/KF6/KWidgetsAddons/kcollapsiblegroupbox.h
/usr/include/KF6/KWidgetsAddons/kcolorbutton.h
/usr/include/KF6/KWidgetsAddons/kcolorcombo.h
/usr/include/KF6/KWidgetsAddons/kcolumnresizer.h
/usr/include/KF6/KWidgetsAddons/kcontextualhelpbutton.h
/usr/include/KF6/KWidgetsAddons/kcursor.h
/usr/include/KF6/KWidgetsAddons/kdatecombobox.h
/usr/include/KF6/KWidgetsAddons/kdatepicker.h
/usr/include/KF6/KWidgetsAddons/kdatepickerpopup.h
/usr/include/KF6/KWidgetsAddons/kdatetimeedit.h
/usr/include/KF6/KWidgetsAddons/kdragwidgetdecorator.h
/usr/include/KF6/KWidgetsAddons/kdualaction.h
/usr/include/KF6/KWidgetsAddons/keditlistwidget.h
/usr/include/KF6/KWidgetsAddons/kfontaction.h
/usr/include/KF6/KWidgetsAddons/kfontchooser.h
/usr/include/KF6/KWidgetsAddons/kfontchooserdialog.h
/usr/include/KF6/KWidgetsAddons/kfontrequester.h
/usr/include/KF6/KWidgetsAddons/kfontsizeaction.h
/usr/include/KF6/KWidgetsAddons/kguiitem.h
/usr/include/KF6/KWidgetsAddons/kjobwidgets.h
/usr/include/KF6/KWidgetsAddons/kled.h
/usr/include/KF6/KWidgetsAddons/klineediteventhandler.h
/usr/include/KF6/KWidgetsAddons/klineediturldropeventfilter.h
/usr/include/KF6/KWidgetsAddons/kmessagebox.h
/usr/include/KF6/KWidgetsAddons/kmessageboxdontaskagaininterface.h
/usr/include/KF6/KWidgetsAddons/kmessageboxnotifyinterface.h
/usr/include/KF6/KWidgetsAddons/kmessagedialog.h
/usr/include/KF6/KWidgetsAddons/kmessagewidget.h
/usr/include/KF6/KWidgetsAddons/kmimetypechooser.h
/usr/include/KF6/KWidgetsAddons/kmimetypeeditor.h
/usr/include/KF6/KWidgetsAddons/kmultitabbar.h
/usr/include/KF6/KWidgetsAddons/knewpassworddialog.h
/usr/include/KF6/KWidgetsAddons/knewpasswordwidget.h
/usr/include/KF6/KWidgetsAddons/kpagedialog.h
/usr/include/KF6/KWidgetsAddons/kpagemodel.h
/usr/include/KF6/KWidgetsAddons/kpageview.h
/usr/include/KF6/KWidgetsAddons/kpagewidget.h
/usr/include/KF6/KWidgetsAddons/kpagewidgetmodel.h
/usr/include/KF6/KWidgetsAddons/kpassword.h
/usr/include/KF6/KWidgetsAddons/kpassworddialog.h
/usr/include/KF6/KWidgetsAddons/kpasswordlineedit.h
/usr/include/KF6/KWidgetsAddons/kpixmapregionselectordialog.h
/usr/include/KF6/KWidgetsAddons/kpixmapregionselectorwidget.h
/usr/include/KF6/KWidgetsAddons/kpixmapsequence.h
/usr/include/KF6/KWidgetsAddons/kpixmapsequenceoverlaypainter.h
/usr/include/KF6/KWidgetsAddons/kpixmapsequencewidget.h
/usr/include/KF6/KWidgetsAddons/kpopupframe.h
/usr/include/KF6/KWidgetsAddons/kratingpainter.h
/usr/include/KF6/KWidgetsAddons/kratingwidget.h
/usr/include/KF6/KWidgetsAddons/krecentfilesmenu.h
/usr/include/KF6/KWidgetsAddons/kruler.h
/usr/include/KF6/KWidgetsAddons/kselectaction.h
/usr/include/KF6/KWidgetsAddons/kselector.h
/usr/include/KF6/KWidgetsAddons/kseparator.h
/usr/include/KF6/KWidgetsAddons/ksplittercollapserbutton.h
/usr/include/KF6/KWidgetsAddons/ksqueezedtextlabel.h
/usr/include/KF6/KWidgetsAddons/kstandardguiitem.h
/usr/include/KF6/KWidgetsAddons/kstyleextensions.h
/usr/include/KF6/KWidgetsAddons/ktimecombobox.h
/usr/include/KF6/KWidgetsAddons/ktitlewidget.h
/usr/include/KF6/KWidgetsAddons/ktoggleaction.h
/usr/include/KF6/KWidgetsAddons/ktogglefullscreenaction.h
/usr/include/KF6/KWidgetsAddons/ktoolbarlabelaction.h
/usr/include/KF6/KWidgetsAddons/ktoolbarpopupaction.h
/usr/include/KF6/KWidgetsAddons/ktoolbarspaceraction.h
/usr/include/KF6/KWidgetsAddons/ktooltipwidget.h
/usr/include/KF6/KWidgetsAddons/ktwofingerswipe.h
/usr/include/KF6/KWidgetsAddons/ktwofingertap.h
/usr/include/KF6/KWidgetsAddons/kurllabel.h
/usr/include/KF6/KWidgetsAddons/kviewstatemaintainerbase.h
/usr/include/KF6/KWidgetsAddons/kviewstateserializer.h
/usr/include/KF6/KWidgetsAddons/kwidgetsaddons_export.h
/usr/include/KF6/KWidgetsAddons/kwidgetsaddons_version.h
/usr/include/KF6/KWidgetsAddons/kxyselector.h
/usr/lib64/cmake/KF6WidgetsAddons/KF6WidgetsAddonsConfig.cmake
/usr/lib64/cmake/KF6WidgetsAddons/KF6WidgetsAddonsConfigVersion.cmake
/usr/lib64/cmake/KF6WidgetsAddons/KF6WidgetsAddonsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6WidgetsAddons/KF6WidgetsAddonsTargets.cmake
/usr/lib64/libKF6WidgetsAddons.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF6WidgetsAddons.so.6.12.0
/V3/usr/lib64/qt6/plugins/designer/kwidgetsaddons6widgets.so
/usr/lib64/libKF6WidgetsAddons.so.6
/usr/lib64/libKF6WidgetsAddons.so.6.12.0
/usr/lib64/qt6/plugins/designer/kwidgetsaddons6widgets.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kwidgetsaddons/07c1ab270255cf247438e2358ff0c18835b6a6ce
/usr/share/package-licenses/kwidgetsaddons/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kwidgetsaddons/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kwidgetsaddons/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/kwidgetsaddons/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kwidgetsaddons/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kwidgetsaddons/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/kwidgetsaddons/e712eadfab0d2357c0f50f599ef35ee0d87534cb
