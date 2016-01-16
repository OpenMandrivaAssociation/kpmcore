Summary:	Library for managing partitions
Name:		kpmcore
Version:	2.0.0
Release:	1
License:	GPLv3
Group:		System/Libraries
Url:		http://www.kde.org
Source0:	http://download.kde.org/stable/kpmcore/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(blkid)
BuildRequires:	pkgconfig(libatasmart)
BuildRequires:	pkgconfig(libparted)
BuildRequires:	pkgconfig(Qt5Core) >= 5.3.0
BuildRequires:	pkgconfig(Qt5Gui) >= 5.3.0
BuildRequires:	pkgconfig(Qt5Widgets) >= 5.3.0
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5Service)

%description
Library for managing partitions.
Common code for KDE Partition Manager and other projects.

%prep
%setup -q
%apply_patches

%build
%cmake_qt5
%ninja

%install
%ninja_install -C build


%files
