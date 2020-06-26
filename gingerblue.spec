Summary:	Free Music Software for GNOME
Summary(pl.UTF-8):	Wolnodostępne oprogramowanie muzyczne dla GNOME
Name:		gingerblue
Version:	0.1.1
Release:	1
License:	GPL v3
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gingerblue/0.1/%{name}-%{version}.tar.xz
# Source0-md5:	0dbd1205c82a4c60cbcf84b5f4ad539a
Patch0:		%{name}-pc.patch
URL:		https://wiki.gnome.org/Apps/Gingerblue
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.11
BuildRequires:	geocode-glib-devel >= 3.20
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.38.0
BuildRequires:	gstreamer-devel >= 1.0
BuildRequires:	gstreamer-plugins-bad-devel >= 1.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0
BuildRequires:	gtk+3-devel >= 3.22.30
BuildRequires:	intltool >= 0.50.1
BuildRequires:	libchamplain-devel >= 0.12.10
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pango-devel >= 1:0.28
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.596
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	geocode-glib >= 3.20
Requires:	glib2 >= 1:2.38.0
Requires:	gstreamer-plugins-bad >= 1.0
Requires:	gstreamer-plugins-base >= 1.0
Requires:	gstreamer-plugins-good >= 1.0
Requires:	gtk+3 >= 3.22.30
Requires:	libchamplain >= 0.12.10
Requires:	pango >= 1:0.28
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gingerblue is Free Software in development for musicians who want to
compose, record and share original music to the Internet from the
GNOME Desktop.

%description -l pl.UTF-8
Gingerblue to wolnodostępne oprogramowanie na wczesnym etapie rozwoju,
przeznaczone dla muzyków chcących komponować, nagrywać i udostępniać
oryginalną muzykę w Internecie z poziomu środowiska GNOME.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# useless now
%{__rm} -r $RPM_BUILD_ROOT%{_includedir}/gingerblue

# nothing yet
#find_lang %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files
# -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gingerblue
