%global tl_name xymtex
%global tl_revision 32182

Name:		texlive-%{tl_name}
Epoch:		1
Version:	5.06
Release:	%{tl_revision}.1
Summary:	Typesetting chemical structures
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xymtex
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xymtex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xymtex.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xymtex.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
XyMTeX is a set of packages for drawing a wide variety of chemical
structural formulas in a way that reflects their structure. The package
provides three output modes: 'LaTeX', 'PostScript' and 'PDF'. XyMTeX's
commands have a systematic set of arguments for specifying substituents
and their positions, endocyclic double bonds, and bond patterns. In some
cases there are additional arguments for specifying hetero-atoms on the
vertices of heterocycles. It is believed that this systematic design
allows XyMTeX to operate as a practical (device-independent) tool for
use with LaTeX.

