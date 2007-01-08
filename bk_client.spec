Summary:	BitKeeper client
Summary(pl):	Klient BitKeepera
Name:		bk_client
Version:	2.0
Release:	1
License:	No Whining License
Group:		Development/Version Control
Source0:	http://www.bitmover.com/bk-client%{version}.shar
# Source0-md5:	14680e84d0b0b359995643d2a1fd57ff
URL:		http://www.bitkeeper.com/
BuildRequires:	zlib-devel
Requires:	gzip
Requires:	patch
Requires:	tar
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Free BitKeeper client.

%description -l pl
Darmowy klient BitKeepera.

%prep
%setup -q -c -T
/bin/sh %{SOURCE0}

%build
%{__make} -C bk-client%{version} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install bk-client%{version}/bkf $RPM_BUILD_ROOT%{_bindir}/bkf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
