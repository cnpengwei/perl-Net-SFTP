#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	SFTP
Summary:	Net::SFTP - Secure File Transfer Protocol client
#Summary(pl):	
Name:		perl-Net-SFTP
Version:	0.08
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	cba9af8f26eee958733fa3b6ad4e2d8a
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Net-SSH-Perl >= 1.24
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
I<Net::SFTP> is a pure-Perl implementation of the Secure File
Transfer Protocol (SFTP)--file transfer built on top of the SSH
protocol. I<Net::SFTP> uses I<Net::SSH::Perl> to build a secure,
encrypted tunnel through which files can be transferred and
managed. It provides a subset of the commands listed in the
SSH File Transfer Protocol IETF draft, which can be found at
I<http://www.openssh.com/txt/draft-ietf-secsh-filexfer-00.txt>.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a eg/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README ToDo
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
