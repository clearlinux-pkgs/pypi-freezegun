#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-freezegun
Version  : 1.2.1
Release  : 37
URL      : https://files.pythonhosted.org/packages/89/a9/ebf3d233893752ca282d91c88103facf6d7d05ce22978829e4e0cbc4113d/freezegun-1.2.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/89/a9/ebf3d233893752ca282d91c88103facf6d7d05ce22978829e4e0cbc4113d/freezegun-1.2.1.tar.gz
Summary  : Let your Python tests travel through time
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-freezegun-license = %{version}-%{release}
Requires: pypi-freezegun-python = %{version}-%{release}
Requires: pypi-freezegun-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(python_dateutil)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)

%description
FreezeGun: Let your Python tests travel through time
====================================================

%package license
Summary: license components for the pypi-freezegun package.
Group: Default

%description license
license components for the pypi-freezegun package.


%package python
Summary: python components for the pypi-freezegun package.
Group: Default
Requires: pypi-freezegun-python3 = %{version}-%{release}

%description python
python components for the pypi-freezegun package.


%package python3
Summary: python3 components for the pypi-freezegun package.
Group: Default
Requires: python3-core
Provides: pypi(freezegun)
Requires: pypi(python_dateutil)

%description python3
python3 components for the pypi-freezegun package.


%prep
%setup -q -n freezegun-1.2.1
cd %{_builddir}/freezegun-1.2.1
pushd ..
cp -a freezegun-1.2.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656404432
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-freezegun
cp %{_builddir}/freezegun-1.2.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-freezegun/83ff4be984d95e17546d5eaa6e14beba8ef4b5e9
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-freezegun/83ff4be984d95e17546d5eaa6e14beba8ef4b5e9

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
