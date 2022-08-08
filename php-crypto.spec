#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-crypto
Version  : 0.3.2
Release  : 18
URL      : https://pecl.php.net/get/crypto-0.3.2.tgz
Source0  : https://pecl.php.net/get/crypto-0.3.2.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : PHP-3.01
Requires: php-crypto-lib = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : openssl-dev

%description
# PHP OpenSSL Crypto wrapper
The php-crypto is an objective wrapper for OpenSSL Crypto library.

%package lib
Summary: lib components for the php-crypto package.
Group: Libraries

%description lib
lib components for the php-crypto package.


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
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20210902/crypto.so
