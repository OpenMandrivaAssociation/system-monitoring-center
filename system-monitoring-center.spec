Summary:	Multi-featured system monitor
Name:		system-monitoring-center
Version:	2.26.1
Release:	1
License:	GPLv3
Group:		Monitoring
Url:		https://github.com/mamolinux/system-monitoring-center
Source0:  https://github.com/mamolinux/system-monitoring-center/archive/%{version}/%{name}-%{version}.tar.gz
# archived
#Source0:	https://github.com/hakandundar34coding/system-monitoring-center/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:	gtk4
BuildRequires:	meson
BuildRequires:	ninja
BuildRequires:	python3dist(setuptools)
BuildRequires:	pkgconfig(python3)
Requires: dmidecode
Requires: hwdata
Requires:	python-gi
Requires:	python3dist(pycairo)
Requires:	python3dist(pygobject)
Requires:	typelib(Adw)
Requires: typelib(GLib)
Requires: typelib(GdkWayland)
Requires: typelib(Pango)
BuildArch:	noarch

%description
Provides information about CPU/RAM/Disk/Network/GPU performance, sensors,
processes, users, storage, startup programs, services, environment
variables and system.

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/appdata/io.github.hakandundar34coding.%{name}.appdata.xml
%{_datadir}/applications/io.github.hakandundar34coding.%{name}.desktop
%{_datadir}/%{name}/*
%{_iconsdir}/hicolor/scalable/apps/io.github.hakandundar34coding.%{name}.svg
%{_localedir}/*
%{_mandir}/man1/%{name}.1.*

#------------------------------------------------------------------

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
