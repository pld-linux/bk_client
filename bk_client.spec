Summary:	BitKeeper client
Summary(pl):	Klient BitKeeper
Name:		bk_client
Version:	1.1
Release:	1
License:	No Whining License
Group:		Development/Version Control
Source0:	http://www.bitmover.com/bk-client.shar
# Source0-md5:	fd22644204abc0c9d1a35b5d78b654f5
URL:		http://www.bitkeeper.com/
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Free BitKeeper client.

%description -l pl
Darmowy klient BitKeeper.

%prep
%setup -q -T -c
/bin/sh %{SOURCE0}

%build
cd bk_client-%{version}
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install bk_client-%{version}/sfioball $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
