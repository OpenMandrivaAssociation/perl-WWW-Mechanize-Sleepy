%define upstream_name    WWW-Mechanize-Sleepy
%define upstream_version 0.7
Name:		perl-%{upstream_name}
Version:	0.7
Release:	3

Summary:	WWW::Mechanize::Sleepy - A Sleepy Mechanize Agent
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/WWW-Mechanize-Sleepy
Source0:	https://cpan.metacpan.org/authors/id/K/KN/KNTONAS/WWW-Mechanize-Sleepy-0.7.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Sometimes when testing the behavior of a webserver it is important
to be able to space out your requests in order to simulate a
person reading, thinking (or sleeping) at the keyboard.

WWW::Mechanize::Sleepy subclasses WWW::Mechanize to provide pauses
between your server requests. Use it just like you would use
WWW::Mechanize.

%prep
%setup -q -n WWW-Mechanize-Sleepy-0.7

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

# make test || : don't work...
#make test || :

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/WWW/Mechanize/Sleepy.pm
%{_mandir}/*/*


