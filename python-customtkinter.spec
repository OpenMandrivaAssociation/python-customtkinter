%global pypi_name customtkinter

Name:		python-%{pypi_name}
Version:	5.2.2
Release:	1
Summary:	A modern and customizable python UI-library based on Tkinter

Group:		Development/Python
License:	MIT
URL:		https://customtkinter.tomschimansky.com/
Source0:	https://files.pythonhosted.org/packages/source/c/customtkinter/customtkinter-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	git-core
BuildRequires:	python%{pyver}dist(setuptools)
#BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildSystem:	python

Requires: tkinter
Requires: python-darkdetect

Provides: customtkinter

%description
CustomTkinter is a python desktop UI-library based on Tkinter, which provides modern looking and fully customizable widgets. 
With CustomTkinter you'll get a consistent look across all desktop platforms (Windows, macOS, Linux).

%prep
%autosetup -n %{pypi_name}-%{version} -p1

%files
#doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info
%{python3_sitelib}/customtkinter/
