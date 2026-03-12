%global module customtkinter

Name:		python-customtkinter
Version:	5.3.0
Release:	1
Summary:	A modern and customizable python UI-library based on Tkinter
Group:		Development/Python
License:	MIT
URL:		https://github.com/TomSchimansky/CustomTkinter
Source0:	%{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	git-core
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(pillow)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

Requires:	tkinter
Requires:	python%{pyver}dist(typing-extensions)
Requires:	python%{pyver}dist(pillow)
Provides:	customtkinter

%description
CustomTkinter is a python desktop UI-library based on Tkinter, which provides modern looking and fully customizable widgets. 
With CustomTkinter you'll get a consistent look across all desktop platforms (Windows, macOS, Linux).


%files
%doc Readme.md
%license LICENSE
%{python3_sitelib}/%{module}
%{python3_sitelib}/%{module}-%{version}.dist-info
