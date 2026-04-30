from __future__ import annotations

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


SLIDES = [
    {
        "title": "Apresentacao de Padroes",
        "bullets": [
            "Disciplina: Padroes de Projeto",
            "Grupo estudou Chain of Responsibility e Flyweight",
            "Todos os integrantes participam da explicacao e da demo",
            "Objetivo: mostrar conceito, estrutura e exemplo executavel em Java",
        ],
    },
    {
        "title": "Chain of Responsibility: Motivation e Applicability",
        "bullets": [
            "Evita concentrar toda decisao em um unico bloco de if/else",
            "Uma solicitacao pode ser tratada por diferentes niveis de atendimento",
            "Aplicavel a suporte, aprovacao, validacao e processamento em etapas",
            "O cliente envia a requisicao ao primeiro elo da cadeia",
        ],
    },
    {
        "title": "Chain of Responsibility: Structure, Participants e Collaborations",
        "bullets": [
            "Structure: Cliente -> Bot -> N1 -> N2 -> Gerente",
            "Handler define setNext() e handle()",
            "Handlers concretos resolvem ou encaminham o ticket",
            "Cada elo colabora decidindo se trata ou repassa a solicitacao",
        ],
    },
    {
        "title": "Chain of Responsibility: Consequences e codigo",
        "bullets": [
            "Baixo acoplamento entre o cliente e quem resolve o problema",
            "Fluxo extensivel com novos handlers",
            "Cadeias longas podem dificultar rastreamento",
            "Demo: ticket simples no Bot, intermediario em N1/N2 e critico no Gerente",
        ],
    },
    {
        "title": "Flyweight: Motivation e Applicability",
        "bullets": [
            "Evita repetir os mesmos dados em muitos objetos parecidos",
            "Varios tickets usam a mesma categoria, prioridade e SLA",
            "Aplicavel a cenarios com muitos objetos pequenos e estado compartilhavel",
            "Separa estado intrinseco do estado extrinseco",
        ],
    },
    {
        "title": "Flyweight: Structure, Participants e Collaborations",
        "bullets": [
            "Ticket usa TicketType e TicketTypeFactory reaproveita instancias",
            "TicketType guarda categoria, prioridade e SLA",
            "Ticket guarda id, cliente e descricao",
            "O factory consulta o cache antes de criar um novo tipo",
        ],
    },
    {
        "title": "Flyweight: Consequences e codigo",
        "bullets": [
            "Reduz duplicacao e uso de memoria",
            "Centraliza o estado compartilhado",
            "Exige separar bem o que e intrinseco e extrinseco",
            "Demo: count() do factory menor que o total de tickets",
        ],
    },
    {
        "title": "Roteiro da demonstracao",
        "bullets": [
            "Executar primeiro chain-of-responsibility",
            "Mostrar criacao da cadeia e encaminhamento dos tickets",
            "Executar depois flyweight",
            "Mostrar o cache do factory e o reuso de tipos",
        ],
    },
    {
        "title": "Comparacao rapida entre os padroes",
        "bullets": [
            "Chain define quem processa uma solicitacao",
            "Flyweight define como compartilhar dados repetidos",
            "O primeiro foca em fluxo e encaminhamento",
            "O segundo foca em economia de recursos e reuso",
        ],
    },
    {
        "title": "Encerramento e divisao da fala",
        "bullets": [
            "Integrante 1: abertura, motivacao e aplicabilidade do Chain",
            "Integrante 2: estrutura, participantes e consequencias do Chain",
            "Integrante 3: Flyweight",
            "Integrante 4: demo, comparacao final e perguntas",
        ],
    },
]

NS_A = "http://schemas.openxmlformats.org/drawingml/2006/main"
NS_R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NS_P = "http://schemas.openxmlformats.org/presentationml/2006/main"


def esc(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def bullet_paragraph(text: str) -> str:
    return f"""
      <a:p>
        <a:pPr marL="342900" indent="-285750">
          <a:buChar char="•"/>
        </a:pPr>
        <a:r>
          <a:rPr lang="pt-BR" sz="2200"/>
          <a:t>{esc(text)}</a:t>
        </a:r>
      </a:p>""".rstrip()


def slide_xml(title: str, bullets: list[str]) -> str:
    body = "\n".join(bullet_paragraph(item) for item in bullets)
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:a="{NS_A}" xmlns:r="{NS_R}" xmlns:p="{NS_P}">
  <p:cSld>
    <p:spTree>
      <p:nvGrpSpPr>
        <p:cNvPr id="1" name=""/>
        <p:cNvGrpSpPr/>
        <p:nvPr/>
      </p:nvGrpSpPr>
      <p:grpSpPr>
        <a:xfrm>
          <a:off x="0" y="0"/>
          <a:ext cx="0" cy="0"/>
          <a:chOff x="0" y="0"/>
          <a:chExt cx="0" cy="0"/>
        </a:xfrm>
      </p:grpSpPr>
      <p:sp>
        <p:nvSpPr>
          <p:cNvPr id="2" name="Title"/>
          <p:cNvSpPr/>
          <p:nvPr>
            <p:ph type="title"/>
          </p:nvPr>
        </p:nvSpPr>
        <p:spPr>
          <a:xfrm>
            <a:off x="457200" y="274638"/>
            <a:ext cx="8229600" cy="914400"/>
          </a:xfrm>
        </p:spPr>
        <p:txBody>
          <a:bodyPr/>
          <a:lstStyle/>
          <a:p>
            <a:r>
              <a:rPr lang="pt-BR" sz="2800" b="1"/>
              <a:t>{esc(title)}</a:t>
            </a:r>
            <a:endParaRPr lang="pt-BR" sz="2800"/>
          </a:p>
        </p:txBody>
      </p:sp>
      <p:sp>
        <p:nvSpPr>
          <p:cNvPr id="3" name="Content"/>
          <p:cNvSpPr txBox="1"/>
          <p:nvPr>
            <p:ph type="body" idx="1"/>
          </p:nvPr>
        </p:nvSpPr>
        <p:spPr>
          <a:xfrm>
            <a:off x="685800" y="1417320"/>
            <a:ext cx="8458200" cy="4267200"/>
          </a:xfrm>
        </p:spPr>
        <p:txBody>
          <a:bodyPr wrap="square"/>
          <a:lstStyle/>
{body}
          <a:endParaRPr lang="pt-BR" sz="2200"/>
        </p:txBody>
      </p:sp>
    </p:spTree>
  </p:cSld>
  <p:clrMapOvr>
    <a:masterClrMapping/>
  </p:clrMapOvr>
</p:sld>
"""


def slide_rels_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/>
</Relationships>
"""


def content_types_xml(slide_count: int) -> str:
    slide_overrides = "\n".join(
        f'  <Override PartName="/ppt/slides/slide{i}.xml" '
        'ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>'
        for i in range(1, slide_count + 1)
    )
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
  <Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/>
  <Override PartName="/ppt/presProps.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presProps+xml"/>
  <Override PartName="/ppt/viewProps.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.viewProps+xml"/>
  <Override PartName="/ppt/tableStyles.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.tableStyles+xml"/>
  <Override PartName="/ppt/theme/theme1.xml" ContentType="application/vnd.openxmlformats-officedocument.theme+xml"/>
  <Override PartName="/ppt/slideMasters/slideMaster1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml"/>
  <Override PartName="/ppt/slideLayouts/slideLayout1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml"/>
{slide_overrides}
</Types>
"""


ROOT_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="ppt/presentation.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>
"""

APP_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"
            xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
  <Application>Microsoft Office PowerPoint</Application>
  <PresentationFormat>Tela</PresentationFormat>
  <Slides>10</Slides>
  <Notes>0</Notes>
  <HiddenSlides>0</HiddenSlides>
  <MMClips>0</MMClips>
  <ScaleCrop>false</ScaleCrop>
  <HeadingPairs>
    <vt:vector size="2" baseType="variant">
      <vt:variant><vt:lpstr>Slides</vt:lpstr></vt:variant>
      <vt:variant><vt:i4>10</vt:i4></vt:variant>
    </vt:vector>
  </HeadingPairs>
  <TitlesOfParts>
    <vt:vector size="10" baseType="lpstr">
      <vt:lpstr>Apresentacao de Padroes</vt:lpstr>
      <vt:lpstr>Chain of Responsibility: Motivation e Applicability</vt:lpstr>
      <vt:lpstr>Chain of Responsibility: Structure, Participants e Collaborations</vt:lpstr>
      <vt:lpstr>Chain of Responsibility: Consequences e codigo</vt:lpstr>
      <vt:lpstr>Flyweight: Motivation e Applicability</vt:lpstr>
      <vt:lpstr>Flyweight: Structure, Participants e Collaborations</vt:lpstr>
      <vt:lpstr>Flyweight: Consequences e codigo</vt:lpstr>
      <vt:lpstr>Roteiro da demonstracao</vt:lpstr>
      <vt:lpstr>Comparacao rapida entre os padroes</vt:lpstr>
      <vt:lpstr>Encerramento e divisao da fala</vt:lpstr>
    </vt:vector>
  </TitlesOfParts>
  <Company>UFRN</Company>
  <LinksUpToDate>false</LinksUpToDate>
  <SharedDoc>false</SharedDoc>
  <HyperlinksChanged>false</HyperlinksChanged>
  <AppVersion>16.0000</AppVersion>
</Properties>
"""

CORE_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
                   xmlns:dc="http://purl.org/dc/elements/1.1/"
                   xmlns:dcterms="http://purl.org/dc/terms/"
                   xmlns:dcmitype="http://purl.org/dc/dcmitype/"
                   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dc:title>Apresentacao de Padroes</dc:title>
  <dc:subject>Chain of Responsibility e Flyweight</dc:subject>
  <dc:creator>Codex</dc:creator>
  <cp:keywords>padroes, chain of responsibility, flyweight</cp:keywords>
  <dc:description>Apresentacao sobre padroes de projeto com exemplos em Java.</dc:description>
  <cp:lastModifiedBy>Codex</cp:lastModifiedBy>
  <dcterms:created xsi:type="dcterms:W3CDTF">2026-04-30T00:00:00Z</dcterms:created>
  <dcterms:modified xsi:type="dcterms:W3CDTF">2026-04-30T00:00:00Z</dcterms:modified>
</cp:coreProperties>
"""


def presentation_xml(slide_count: int) -> str:
    slide_ids = "\n".join(
        f'    <p:sldId id="{255 + i}" r:id="rId{i + 1}"/>'
        for i in range(1, slide_count + 1)
    )
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:presentation xmlns:a="{NS_A}" xmlns:r="{NS_R}" xmlns:p="{NS_P}"
                saveSubsetFonts="1" autoCompressPictures="0">
  <p:sldMasterIdLst>
    <p:sldMasterId id="2147483648" r:id="rId{slide_count + 1}"/>
  </p:sldMasterIdLst>
  <p:sldIdLst>
{slide_ids}
  </p:sldIdLst>
  <p:sldSz cx="9144000" cy="6858000" type="screen4x3"/>
  <p:notesSz cx="6858000" cy="9144000"/>
  <p:defaultTextStyle>
    <a:defPPr>
      <a:defRPr lang="pt-BR"/>
    </a:defPPr>
  </p:defaultTextStyle>
</p:presentation>
"""


def presentation_rels_xml(slide_count: int) -> str:
    slide_rels = "\n".join(
        f'  <Relationship Id="rId{i}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide{i}.xml"/>'
        for i in range(1, slide_count + 1)
    )
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
{slide_rels}
  <Relationship Id="rId{slide_count + 1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="slideMasters/slideMaster1.xml"/>
  <Relationship Id="rId{slide_count + 2}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/presProps" Target="presProps.xml"/>
  <Relationship Id="rId{slide_count + 3}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/viewProps" Target="viewProps.xml"/>
  <Relationship Id="rId{slide_count + 4}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/tableStyles" Target="tableStyles.xml"/>
</Relationships>
"""


SLIDE_MASTER_XML = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldMaster xmlns:a="{NS_A}" xmlns:r="{NS_R}" xmlns:p="{NS_P}">
  <p:cSld name="Master">
    <p:bg>
      <p:bgPr>
        <a:solidFill>
          <a:srgbClr val="F8FAFC"/>
        </a:solidFill>
      </p:bgPr>
    </p:bg>
    <p:spTree>
      <p:nvGrpSpPr>
        <p:cNvPr id="1" name=""/>
        <p:cNvGrpSpPr/>
        <p:nvPr/>
      </p:nvGrpSpPr>
      <p:grpSpPr>
        <a:xfrm>
          <a:off x="0" y="0"/>
          <a:ext cx="0" cy="0"/>
          <a:chOff x="0" y="0"/>
          <a:chExt cx="0" cy="0"/>
        </a:xfrm>
      </p:grpSpPr>
    </p:spTree>
  </p:cSld>
  <p:clrMap accent1="accent1" accent2="accent2" accent3="accent3" accent4="accent4" accent5="accent5" accent6="accent6"
            bg1="lt1" bg2="lt2" folHlink="folHlink" hlink="hlink" tx1="dk1" tx2="dk2"/>
  <p:sldLayoutIdLst>
    <p:sldLayoutId id="1" r:id="rId1"/>
  </p:sldLayoutIdLst>
  <p:txStyles>
    <p:titleStyle>
      <a:lvl1pPr algn="l">
        <a:defRPr sz="2800" b="1"/>
      </a:lvl1pPr>
    </p:titleStyle>
    <p:bodyStyle>
      <a:lvl1pPr marL="342900" indent="-285750">
        <a:buChar char="•"/>
        <a:defRPr sz="2200"/>
      </a:lvl1pPr>
    </p:bodyStyle>
    <p:otherStyle/>
  </p:txStyles>
</p:sldMaster>
"""

SLIDE_MASTER_RELS_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideLayout" Target="../slideLayouts/slideLayout1.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme" Target="../theme/theme1.xml"/>
</Relationships>
"""

SLIDE_LAYOUT_XML = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sldLayout xmlns:a="{NS_A}" xmlns:r="{NS_R}" xmlns:p="{NS_P}" type="titleAndContent" preserve="1">
  <p:cSld name="Title and Content">
    <p:spTree>
      <p:nvGrpSpPr>
        <p:cNvPr id="1" name=""/>
        <p:cNvGrpSpPr/>
        <p:nvPr/>
      </p:nvGrpSpPr>
      <p:grpSpPr>
        <a:xfrm>
          <a:off x="0" y="0"/>
          <a:ext cx="0" cy="0"/>
          <a:chOff x="0" y="0"/>
          <a:chExt cx="0" cy="0"/>
        </a:xfrm>
      </p:grpSpPr>
    </p:spTree>
  </p:cSld>
  <p:clrMapOvr>
    <a:masterClrMapping/>
  </p:clrMapOvr>
</p:sldLayout>
"""

SLIDE_LAYOUT_RELS_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slideMaster" Target="../slideMasters/slideMaster1.xml"/>
</Relationships>
"""

THEME_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" name="Tema Simples">
  <a:themeElements>
    <a:clrScheme name="Codex">
      <a:dk1><a:srgbClr val="111827"/></a:dk1>
      <a:lt1><a:srgbClr val="FFFFFF"/></a:lt1>
      <a:dk2><a:srgbClr val="1F2937"/></a:dk2>
      <a:lt2><a:srgbClr val="F8FAFC"/></a:lt2>
      <a:accent1><a:srgbClr val="0F172A"/></a:accent1>
      <a:accent2><a:srgbClr val="1D4ED8"/></a:accent2>
      <a:accent3><a:srgbClr val="0F766E"/></a:accent3>
      <a:accent4><a:srgbClr val="B45309"/></a:accent4>
      <a:accent5><a:srgbClr val="7C3AED"/></a:accent5>
      <a:accent6><a:srgbClr val="BE185D"/></a:accent6>
      <a:hlink><a:srgbClr val="2563EB"/></a:hlink>
      <a:folHlink><a:srgbClr val="7C3AED"/></a:folHlink>
    </a:clrScheme>
    <a:fontScheme name="CodexFonts">
      <a:majorFont>
        <a:latin typeface="Aptos Display"/>
        <a:ea typeface=""/>
        <a:cs typeface=""/>
      </a:majorFont>
      <a:minorFont>
        <a:latin typeface="Aptos"/>
        <a:ea typeface=""/>
        <a:cs typeface=""/>
      </a:minorFont>
    </a:fontScheme>
    <a:fmtScheme name="CodexFormats">
      <a:fillStyleLst>
        <a:solidFill><a:schemeClr val="lt1"/></a:solidFill>
        <a:solidFill><a:schemeClr val="accent1"/></a:solidFill>
        <a:solidFill><a:schemeClr val="accent2"/></a:solidFill>
      </a:fillStyleLst>
      <a:lnStyleLst>
        <a:ln w="9525"><a:solidFill><a:schemeClr val="accent1"/></a:solidFill></a:ln>
        <a:ln w="25400"><a:solidFill><a:schemeClr val="accent2"/></a:solidFill></a:ln>
        <a:ln w="38100"><a:solidFill><a:schemeClr val="accent3"/></a:solidFill></a:ln>
      </a:lnStyleLst>
      <a:effectStyleLst>
        <a:effectStyle><a:effectLst/></a:effectStyle>
        <a:effectStyle><a:effectLst/></a:effectStyle>
        <a:effectStyle><a:effectLst/></a:effectStyle>
      </a:effectStyleLst>
      <a:bgFillStyleLst>
        <a:solidFill><a:schemeClr val="lt1"/></a:solidFill>
        <a:solidFill><a:schemeClr val="lt2"/></a:solidFill>
        <a:solidFill><a:schemeClr val="accent1"/></a:solidFill>
      </a:bgFillStyleLst>
    </a:fmtScheme>
  </a:themeElements>
  <a:objectDefaults/>
  <a:extraClrSchemeLst/>
</a:theme>
"""

PRES_PROPS_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:presentationPr xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"
                  xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
                  xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"/>
"""

VIEW_PROPS_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:viewPr xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"
          xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
          xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:normalViewPr>
    <p:restoredLeft sz="15620"/>
    <p:restoredTop sz="94660"/>
  </p:normalViewPr>
  <p:slideViewPr/>
  <p:outlineViewPr/>
  <p:notesTextViewPr/>
  <p:sorterViewPr/>
  <p:extLst/>
</p:viewPr>
"""

TABLE_STYLES_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<a:tblStyleLst xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" def="{5C22544A-7EE6-4342-B048-85BDC9FD1C3A}"/>
"""


def build_pptx(output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output_path, "w", ZIP_DEFLATED) as archive:
        archive.writestr("[Content_Types].xml", content_types_xml(len(SLIDES)))
        archive.writestr("_rels/.rels", ROOT_RELS)
        archive.writestr("docProps/app.xml", APP_XML)
        archive.writestr("docProps/core.xml", CORE_XML)
        archive.writestr("ppt/presentation.xml", presentation_xml(len(SLIDES)))
        archive.writestr("ppt/_rels/presentation.xml.rels", presentation_rels_xml(len(SLIDES)))
        archive.writestr("ppt/presProps.xml", PRES_PROPS_XML)
        archive.writestr("ppt/viewProps.xml", VIEW_PROPS_XML)
        archive.writestr("ppt/tableStyles.xml", TABLE_STYLES_XML)
        archive.writestr("ppt/slideMasters/slideMaster1.xml", SLIDE_MASTER_XML)
        archive.writestr("ppt/slideMasters/_rels/slideMaster1.xml.rels", SLIDE_MASTER_RELS_XML)
        archive.writestr("ppt/slideLayouts/slideLayout1.xml", SLIDE_LAYOUT_XML)
        archive.writestr("ppt/slideLayouts/_rels/slideLayout1.xml.rels", SLIDE_LAYOUT_RELS_XML)
        archive.writestr("ppt/theme/theme1.xml", THEME_XML)
        for index, slide in enumerate(SLIDES, start=1):
            archive.writestr(f"ppt/slides/slide{index}.xml", slide_xml(slide["title"], slide["bullets"]))
            archive.writestr(f"ppt/slides/_rels/slide{index}.xml.rels", slide_rels_xml())


if __name__ == "__main__":
    build_pptx(Path(__file__).with_name("apresentacao-padroes.pptx"))
