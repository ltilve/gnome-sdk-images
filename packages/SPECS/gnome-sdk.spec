Name:           gnome-sdk
Version:        0.1
Release:        1%{?dist}
Summary:        Gnome sdk

License: Various
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch

BuildRequires: gnome-sdk-base
BuildRequires: gtk2
BuildRequires: gtk3 gtk3-immodules
BuildRequires: hicolor-icon-theme
BuildRequires: adwaita-icon-theme
BuildRequires: gnome-themes-standard
BuildRequires: dejavu-fonts
BuildRequires: abattis-cantarell-fonts
BuildRequires: dbus-libs
BuildRequires: librsvg2
BuildRequires: dbus-glib
BuildRequires: gobject-introspection
BuildRequires: libsoup
BuildRequires: gvfs
BuildRequires: desktop-file-utils
BuildRequires: json-glib

Requires: gtk2-devel gtk2-immodules
Requires: gtk3-devel gtk3-immodules
Requires: desktop-file-utils
Requires: json-glib-devel
Requires: gvfs-devel
Requires: librsvg2-devel
Requires: hicolor-icon-theme
Requires: adwaita-icon-theme-devel
Requires: gnome-themes-standard
Requires: gtk-doc-stub
Requires: atk-devel
Requires: at-spi2-atk-devel
Requires: at-spi2-core-devel
Requires: cairo-devel
Requires: cairo-gobject-devel
Requires: dbus-devel
Requires: dbus-glib-devel
Requires: fontconfig-devel
Requires: freetype-devel
Requires: gdk-pixbuf2-devel
Requires: glib2-devel
Requires: gobject-introspection-devel
Requires: graphite2-devel
Requires: gtk3-devel
Requires: harfbuzz-devel
Requires: libcroco-devel
Requires: librsvg2-devel
Requires: libthai-devel
Requires: libX11-devel
Requires: libXau-devel
Requires: libxcb-devel
Requires: libXcomposite-devel
Requires: libXcursor-devel
Requires: libXdamage-devel
Requires: libXdmcp-devel
Requires: libXext-devel
Requires: libXfixes-devel
Requires: libXft-devel
Requires: libXi-devel
Requires: libXinerama-devel
Requires: libXrandr-devel
Requires: libXrender-devel
Requires: libXtst-devel
Requires: pango-devel
Requires: pixman-devel
Requires: vala-devel
Requires: dejavu-fonts
Requires: abattis-cantarell-fonts
Requires: dconf-devel
Requires: libsoup-devel
Requires: libproxy-devel
Requires: gsettings-desktop-schemas

%description
Meta package for Gnome SDK dependencies

%prep


%build


%install

%files
%doc

%changelog
* Fri Nov  7 2014 Alexander Larsson <alexl@redhat.com>
- Initial version
