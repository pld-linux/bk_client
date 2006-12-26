Summary:	BitKeeper client
Summary(pl):	Klient BitKeepera
Name:		bk_client
Version:	1.1
Release:	1
License:	No Whining License
Group:		Development/Version Control
Source0:	http://www.bitmover.com/bk-client.shar
# Source0-md5:	fd22644204abc0c9d1a35b5d78b654f5
Patch0:		%{name}-names.patch
URL:		http://www.bitkeeper.com/
BuildRequires:	zlib-devel
Requires:	gzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Free BitKeeper client.

%description -l pl
Darmowy klient BitKeepera.

%prep
%setup -q -c -T
/bin/sh %{SOURCE0}
cd bk_client-%{version}
%patch0 -p1

%build
%{__make} -C bk_client-%{version} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install bk_client-%{version}/sfio $RPM_BUILD_ROOT%{_bindir}/bk_sfio
install bk_client-%{version}/sfioball $RPM_BUILD_ROOT%{_bindir}/bk_sfioball
install bk_client-%{version}/update $RPM_BUILD_ROOT%{_bindir}/bk_update

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
