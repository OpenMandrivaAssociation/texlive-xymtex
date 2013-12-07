# revision 32182
# category Package
# catalog-ctan /macros/latex/contrib/xymtex
# catalog-date 2013-10-31 09:17:33 +0100
# catalog-license lppl1.3
# catalog-version 5.06
Name:		texlive-xymtex
Version:	5.06
Release:	5
Summary:	Typesetting chemical structures
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xymtex
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xymtex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xymtex.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xymtex.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
XyMTeX is a set of packages for drawing a wide variety of
chemical structural formulas in a way that reflects their
structure. The package provides three output modes: 'LaTeX',
'PostScript' and 'PDF'. XyMTeX's commands have a systematic set
of arguments for specifying substituents and their positions,
endocyclic double bonds, and bond patterns. In some cases there
are additional arguments for specifying hetero-atoms on the
vertices of heterocycles. It is believed that this systematic
design allows XyMTeX to operate as a practical (device-
independent) tool for use with LaTeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/xymtex/base/aliphat.sty
%{_texmfdistdir}/tex/latex/xymtex/base/assurelatexmode.sty
%{_texmfdistdir}/tex/latex/xymtex/base/bondcolor.sty
%{_texmfdistdir}/tex/latex/xymtex/base/carom.sty
%{_texmfdistdir}/tex/latex/xymtex/base/ccycle.sty
%{_texmfdistdir}/tex/latex/xymtex/base/chemstr.sty
%{_texmfdistdir}/tex/latex/xymtex/base/fusering.sty
%{_texmfdistdir}/tex/latex/xymtex/base/hcycle.sty
%{_texmfdistdir}/tex/latex/xymtex/base/hetarom.sty
%{_texmfdistdir}/tex/latex/xymtex/base/hetaromh.sty
%{_texmfdistdir}/tex/latex/xymtex/base/lewisstruc.sty
%{_texmfdistdir}/tex/latex/xymtex/base/locant.sty
%{_texmfdistdir}/tex/latex/xymtex/base/lowcycle.sty
%{_texmfdistdir}/tex/latex/xymtex/base/methylen.sty
%{_texmfdistdir}/tex/latex/xymtex/base/polymers.sty
%{_texmfdistdir}/tex/latex/xymtex/base/sizeredc.sty
%{_texmfdistdir}/tex/latex/xymtex/base/steroid.sty
%{_texmfdistdir}/tex/latex/xymtex/base/xymtex.sty
%{_texmfdistdir}/tex/latex/xymtex/base/xymtexpdf.sty
%{_texmfdistdir}/tex/latex/xymtex/base/xymtexps.sty
%{_texmfdistdir}/tex/latex/xymtex/chemist/assurechemist.sty
%{_texmfdistdir}/tex/latex/xymtex/chemist/chemist.sty
%{_texmfdistdir}/tex/latex/xymtex/chemist/chemtimes.sty
%{_texmfdistdir}/tex/latex/xymtex/xymtxpdf/chmst-pdf.sty
%{_texmfdistdir}/tex/latex/xymtex/xymtxpdf/xymtx-pdf.sty
%{_texmfdistdir}/tex/latex/xymtex/xymtxps/chmst-ps.sty
%{_texmfdistdir}/tex/latex/xymtex/xymtxps/xymtx-ps.sty
%doc %{_texmfdistdir}/doc/latex/xymtex/doc/README.TEXLIVE
%doc %{_texmfdistdir}/doc/latex/xymtex/readme/oldreadme/readme402.doc
%doc %{_texmfdistdir}/doc/latex/xymtex/readme/oldreadme/readme402.jpn
%doc %{_texmfdistdir}/doc/latex/xymtex/readme/oldreadme/readme403.doc
%doc %{_texmfdistdir}/doc/latex/xymtex/readme/oldreadme/readme403.jpn
%doc %{_texmfdistdir}/doc/latex/xymtex/readme/oldreadme/readme404.doc
%doc %{_texmfdistdir}/doc/latex/xymtex/readme/oldreadme/readme404.jpn
%doc %{_texmfdistdir}/doc/latex/xymtex/readme/oldreadme/readme405.doc
%doc %{_texmfdistdir}/doc/latex/xymtex/readme/oldreadme/readme405.jpn
%doc %{_texmfdistdir}/doc/latex/xymtex/readme/oldreadme/readme406.doc
%doc %{_texmfdistdir}/doc/latex/xymtex/readme/oldreadme/readme406.jpn
%doc %{_texmfdistdir}/doc/latex/xymtex/readme/oldreadme/readme500.doc
%doc %{_texmfdistdir}/doc/latex/xymtex/readme/oldreadme/readme500.jpn
%doc %{_texmfdistdir}/doc/latex/xymtex/readme/oldreadme/readme500a.doc
%doc %{_texmfdistdir}/doc/latex/xymtex/readme/oldreadme/readme500a.jpn
%doc %{_texmfdistdir}/doc/latex/xymtex/readme/oldreadme/xymtx402.doc
%doc %{_texmfdistdir}/doc/latex/xymtex/readme/oldreadme/xymtx402.jpn
%doc %{_texmfdistdir}/doc/latex/xymtex/readme/oldreadme/xymtx403.doc
%doc %{_texmfdistdir}/doc/latex/xymtex/readme/oldreadme/xymtx403.jpn
%doc %{_texmfdistdir}/doc/latex/xymtex/readme/oldreadme/xymtx404.doc
%doc %{_texmfdistdir}/doc/latex/xymtex/readme/oldreadme/xymtx404.jpn
%doc %{_texmfdistdir}/doc/latex/xymtex/readme/oldreadme/xymtx405.doc
%doc %{_texmfdistdir}/doc/latex/xymtex/readme/oldreadme/xymtx405.jpn
%doc %{_texmfdistdir}/doc/latex/xymtex/readme/oldreadme/xymtx406.doc
%doc %{_texmfdistdir}/doc/latex/xymtex/readme/oldreadme/xymtx406.jpn
%doc %{_texmfdistdir}/doc/latex/xymtex/readme/oldreadme/xymtx500.doc
%doc %{_texmfdistdir}/doc/latex/xymtex/readme/oldreadme/xymtx500.jpn
%doc %{_texmfdistdir}/doc/latex/xymtex/readme/oldreadme/xymtx500a.doc
%doc %{_texmfdistdir}/doc/latex/xymtex/readme/oldreadme/xymtx500a.jpn
%doc %{_texmfdistdir}/doc/latex/xymtex/readme/readme501.doc
%doc %{_texmfdistdir}/doc/latex/xymtex/readme/readme501.jpn
%doc %{_texmfdistdir}/doc/latex/xymtex/readme/xymtx501.doc
%doc %{_texmfdistdir}/doc/latex/xymtex/readme/xymtx501.jpn
#- source
%doc %{_texmfdistdir}/source/latex/xymtex/base/aliphat.dtx
%doc %{_texmfdistdir}/source/latex/xymtex/base/aliphat.ins
%doc %{_texmfdistdir}/source/latex/xymtex/base/assurelatexmode.dtx
%doc %{_texmfdistdir}/source/latex/xymtex/base/assurelatexmode.ins
%doc %{_texmfdistdir}/source/latex/xymtex/base/bondcolor.dtx
%doc %{_texmfdistdir}/source/latex/xymtex/base/bondcolor.ins
%doc %{_texmfdistdir}/source/latex/xymtex/base/carom.dtx
%doc %{_texmfdistdir}/source/latex/xymtex/base/carom.ins
%doc %{_texmfdistdir}/source/latex/xymtex/base/ccycle.dtx
%doc %{_texmfdistdir}/source/latex/xymtex/base/ccycle.ins
%doc %{_texmfdistdir}/source/latex/xymtex/base/chemstr.dtx
%doc %{_texmfdistdir}/source/latex/xymtex/base/chemstr.ins
%doc %{_texmfdistdir}/source/latex/xymtex/base/doins.bat
%doc %{_texmfdistdir}/source/latex/xymtex/base/fusering.dtx
%doc %{_texmfdistdir}/source/latex/xymtex/base/fusering.ins
%doc %{_texmfdistdir}/source/latex/xymtex/base/hcycle.dtx
%doc %{_texmfdistdir}/source/latex/xymtex/base/hcycle.ins
%doc %{_texmfdistdir}/source/latex/xymtex/base/hetarom.dtx
%doc %{_texmfdistdir}/source/latex/xymtex/base/hetarom.ins
%doc %{_texmfdistdir}/source/latex/xymtex/base/hetaromh.dtx
%doc %{_texmfdistdir}/source/latex/xymtex/base/hetaromh.ins
%doc %{_texmfdistdir}/source/latex/xymtex/base/lewisstruc.dtx
%doc %{_texmfdistdir}/source/latex/xymtex/base/lewisstruc.ins
%doc %{_texmfdistdir}/source/latex/xymtex/base/locant.dtx
%doc %{_texmfdistdir}/source/latex/xymtex/base/locant.ins
%doc %{_texmfdistdir}/source/latex/xymtex/base/lowcycle.dtx
%doc %{_texmfdistdir}/source/latex/xymtex/base/lowcycle.ins
%doc %{_texmfdistdir}/source/latex/xymtex/base/methylen.dtx
%doc %{_texmfdistdir}/source/latex/xymtex/base/methylen.ins
%doc %{_texmfdistdir}/source/latex/xymtex/base/polymers.dtx
%doc %{_texmfdistdir}/source/latex/xymtex/base/polymers.ins
%doc %{_texmfdistdir}/source/latex/xymtex/base/putline.sed
%doc %{_texmfdistdir}/source/latex/xymtex/base/putput.bat
%doc %{_texmfdistdir}/source/latex/xymtex/base/sizeredc.dtx
%doc %{_texmfdistdir}/source/latex/xymtex/base/sizeredc.ins
%doc %{_texmfdistdir}/source/latex/xymtex/base/steroid.dtx
%doc %{_texmfdistdir}/source/latex/xymtex/base/steroid.ins
%doc %{_texmfdistdir}/source/latex/xymtex/base/xymtex.dtx
%doc %{_texmfdistdir}/source/latex/xymtex/base/xymtex.ins
%doc %{_texmfdistdir}/source/latex/xymtex/chemist/assurechemist.dtx
%doc %{_texmfdistdir}/source/latex/xymtex/chemist/assurechemist.ins
%doc %{_texmfdistdir}/source/latex/xymtex/chemist/chemist.dtx
%doc %{_texmfdistdir}/source/latex/xymtex/chemist/chemist.ins
%doc %{_texmfdistdir}/source/latex/xymtex/chemist/chemtimes.dtx
%doc %{_texmfdistdir}/source/latex/xymtex/chemist/chemtimes.ins
%doc %{_texmfdistdir}/source/latex/xymtex/xymtxpdf/chmst-pdf.dtx
%doc %{_texmfdistdir}/source/latex/xymtex/xymtxpdf/chmst-pdf.ins
%doc %{_texmfdistdir}/source/latex/xymtex/xymtxpdf/xymtx-pdf.dtx
%doc %{_texmfdistdir}/source/latex/xymtex/xymtxpdf/xymtx-pdf.ins
%doc %{_texmfdistdir}/source/latex/xymtex/xymtxps/chmst-ps.dtx
%doc %{_texmfdistdir}/source/latex/xymtex/xymtxps/chmst-ps.ins
%doc %{_texmfdistdir}/source/latex/xymtex/xymtxps/xymtx-ps.drv
%doc %{_texmfdistdir}/source/latex/xymtex/xymtxps/xymtx-ps.dtx
%doc %{_texmfdistdir}/source/latex/xymtex/xymtxps/xymtx-ps.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
