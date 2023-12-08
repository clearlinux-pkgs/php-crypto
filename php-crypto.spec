#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-crypto
Version  : 0.3.2
Release  : 49
URL      : https://pecl.php.net/get/crypto-0.3.2.tgz
Source0  : https://pecl.php.net/get/crypto-0.3.2.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : PHP-3.01
Requires: php-crypto-lib = %{version}-%{release}
Requires: php-crypto-license = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : openssl-dev

%description
# PHP OpenSSL Crypto wrapper
The php-crypto is an objective wrapper for OpenSSL Crypto library.

%package lib
Summary: lib components for the php-crypto package.
Group: Libraries
Requires: php-crypto-license = %{version}-%{release}

%description lib
lib components for the php-crypto package.


%package license
Summary: license components for the php-crypto package.
Group: Default

%description license
license components for the php-crypto package.


%prep
%setup -q -n crypto-0.3.2
cd %{_builddir}/crypto-0.3.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-crypto
cp %{_builddir}/crypto-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-crypto/1979963df4747a96d74e8044f0046cf58a2a21a3
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20220829/crypto.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-crypto/1979963df4747a96d74e8044f0046cf58a2a21a3
