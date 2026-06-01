# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/140?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/140
- Title: Wildfire Prevention Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 140
- Origin chamber: Senate
- Introduced date: 2025-01-16
- Update date: 2026-04-08T14:17:26Z
- Update date including text: 2026-04-08T14:17:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in Senate
- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S228-231)
- 2025-12-02 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- Latest action: 2025-01-16: Introduced in Senate

## Actions

- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S228-231)
- 2025-12-02 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/140",
    "number": "140",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "B001261",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Barrasso, John [R-WY]",
        "lastName": "Barrasso",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "Wildfire Prevention Act of 2025",
    "type": "S",
    "updateDate": "2026-04-08T14:17:26Z",
    "updateDateIncludingText": "2026-04-08T14:17:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-02",
      "committees": {
        "item": {
          "name": "Public Lands, Forests, and Mining Subcommittee",
          "systemCode": "sseg03"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S228-231)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-01-16T22:12:19Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-02T20:00:04Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Public Lands, Forests, and Mining Subcommittee",
          "systemCode": "sseg03"
        }
      },
      "systemCode": "sseg00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "MT"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "WY"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "MT"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "ID"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "ID"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s140is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 140\nIN THE SENATE OF THE UNITED STATES\nJanuary 16, 2025 Mr. Barrasso (for himself, Mr. Daines , Ms. Lummis , Mr. Sheehy , and Mr. Risch ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo address the forest health crisis on the National Forest System and public lands, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Wildfire Prevention Act of 2025 .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Definitions.\nTITLE I\u2014Accomplishments over rhetoric\nSec. 101. Accelerating treatments on Federal land.\nSec. 102. Annual reports.\nSec. 103. Transparency in hazardous fuels reduction activity reporting.\nSec. 104. Regional forest carbon accounting.\nSec. 105. Wildland fire performance metrics.\nTITLE II\u2014Forest management\nSec. 201. Vegetation management, facility inspection, and operation and maintenance relating to electric transmission and distribution facility rights-of-way.\nSec. 202. Timber sales on National Forest System land.\nSec. 203. Categorical exclusion for high-priority hazard trees.\nSec. 204. Intervenor status.\nSec. 205. Utilizing grazing for wildfire risk reduction.\nTITLE III\u2014Cultural change in agencies\nSec. 301. Mandatory use of existing authorities.\nSec. 302. Public-private wildfire technology deployment and testbed partnership.\nSec. 303. Repeal of FLAME reports.\n#### 2. Definitions\nIn this Act:\n**(1) Federal land**\nThe term Federal land means\u2014\n**(A)**\nland of the National Forest System; and\n**(B)**\npublic lands (as defined in section 103 of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1702 )), the surface of which is administered by the Secretary of the Interior, acting through the Director of the Bureau of Land Management.\n**(2) Hazardous fuels reduction activity**\n**(A) In general**\nThe term hazardous fuels reduction activity means any vegetation management activity to reduce the risk of wildfire, including mechanical treatments and prescribed burning.\n**(B) Exclusion**\nThe term hazardous fuels reduction activity does not include the awarding of a contract to conduct any activity described in subparagraph (A).\n**(3) National Forest System**\n**(A) In general**\nThe term National Forest System has the meaning given the term in section 11(a) of the Forest and Rangeland Renewable Resources Planning Act of 1974 ( 16 U.S.C. 1609(a) ).\n**(B) Exclusion**\nThe term National Forest System does not include any forest reserve not created from the public domain.\n**(4) Secretary concerned**\nThe term Secretary concerned means\u2014\n**(A)**\nthe Secretary of Agriculture, acting through the Chief of the Forest Service, with respect to Federal land described in paragraph (1)(A); and\n**(B)**\nthe Secretary of the Interior, acting through the Director of the Bureau of Land Management, with respect to Federal land described in paragraph (1)(B).\n**(5) Wildland-urban interface**\nThe term wildland-urban interface has the meaning given the term in section 101 of the Healthy Forests Restoration Act of 2003 ( 16 U.S.C. 6511 ).\nI\nAccomplishments over rhetoric\n#### 101. Accelerating treatments on Federal land\n##### (a) Baseline treatments for fuels reduction and forest health\nFor Federal land, the Secretary concerned shall determine\u2014\n**(1)**\nfor each of fiscal years 2019 through 2023\u2014\n**(A)**\nthe number of acres mechanically thinned, for acres commercially thinned and for acres pre-commercially thinned; and\n**(B)**\nthe number of acres treated by prescribed fire; and\n**(2)**\nthe average of the numbers described in subparagraphs (A) and (B) of paragraph (1) over the period of fiscal years 2019 through 2023.\n##### (b) Annual goals\n**(1) In general**\nFor Federal land for fiscal year 2025 and each fiscal year thereafter, the Secretary concerned shall establish annual\u2014\n**(A)**\nmechanical thinning goals for acres commercially thinned and for acres pre-commercially thinned; and\n**(B)**\nprescribed fire goals.\n**(2) Requirements**\n**(A) Fiscal years 2025 and 2026**\nFor each of fiscal years 2025 and 2026, the goals established under subparagraphs (A) and (B) of paragraph (1) shall be not less than the number of acres described in subsection (a)(2).\n**(B) Fiscal years 2027 and 2028**\nFor each of fiscal years 2027 and 2028, the goals established under subparagraphs (A) and (B) of paragraph (1) shall be not less than 20 percent more than the number of acres described in subsection (a)(2).\n**(C) Fiscal year 2029 and subsequent fiscal years**\nFor fiscal year 2029 and each fiscal year thereafter, the goals established under subparagraphs (A) and (B) of paragraph (1) shall be not less than 40 percent more than the number of acres described in subsection (a)(2).\n##### (c) Regional allotments\nNot later than 90 days after the date of enactment of this Act, and annually thereafter, the Secretary concerned shall assign annual acreage allotments for mechanical thinning and prescribed fire on Federal land, categorized by National Forest System region or by State, as appropriate.\n##### (d) Publication\nThe Secretary concerned shall make publicly available the data described in subsections (a), (b), and (c), including by publishing that data on the website of the Forest Service and the website of the Bureau of Land Management.\n##### (e) Savings provision\nNothing in this section shall be construed to supersede or conflict with any other provision of law, including\u2014\n**(1)**\nsection 40803(b) of the Infrastructure Investment and Jobs Act ( 16 U.S.C. 6592(b) ); and\n**(2)**\nthe Wilderness Act ( 16 U.S.C. 1131 et seq. ).\n##### (f) Applicability of NEPA\nThe establishment of annual goals under subsection (b)(1) and the assignment of regional allotments under subsection (c) shall not be subject to the requirements of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ).\n#### 102. Annual reports\nNot later than September 30, 2025, and annually thereafter, the Secretary concerned shall publish on a public website of the Forest Service and a public website of the Bureau of Land Management the following information with respect to the Federal land during the preceding fiscal year:\n**(1)**\nThe number of acres treated pursuant to section 40803(b) of the Infrastructure Investment and Jobs Act ( 16 U.S.C. 6592(b) ).\n**(2)**\n**(A)**\nThe number of acres mechanically thinned;\n**(B)**\nthe number of acres treated by prescribed fire; and\n**(C)**\nwhether the number of acres described in subparagraphs (A) and (B) met or exceeded the acres described in section 101(b)(2).\n**(3)**\nAny limitations or challenges, including litigation or delays in the preparation of environmental documentation, that hindered the Secretary concerned from meeting or exceeding the annual goals established under section 101(b)(1), if applicable.\n**(4)**\nThe number of acres that have undergone a regeneration harvest.\n**(5)**\nThe number of acres described in subparagraphs (A) and (B) of paragraph (2) and paragraph (4) that are in an area identified as having\u2014\n**(A)**\nthe expectation that, without remediation, at least 25 percent of standing live basal area greater than 1 inch in diameter may die over a 15-year time frame due to insects and diseases, as depicted on the National Insect and Disease Composite Risk Map; or\n**(B)**\na very high or high wildfire hazard potential.\n**(6)**\nThe number of acres described in subparagraphs (A) and (B) of paragraph (2) and paragraph (4) that use either of the following streamlined authorities for environmental review:\n**(A)**\nA categorical exclusion.\n**(B)**\nAn emergency action authority of the Secretary concerned.\n**(7)**\nThe number of acres described in subparagraphs (A) and (B) of paragraph (2) and paragraph (4) with respect to which partners are used to carry out the work through\u2014\n**(A)**\na good neighbor agreement under section 8206 of the Agricultural Act of 2014 ( 16 U.S.C. 2113a );\n**(B)**\na master stewardship agreement;\n**(C)**\na contract or agreement entered into under the Tribal Forest Protection Act of 2004 ( 25 U.S.C. 3115a ); or\n**(D)**\na stewardship end-result contract.\n#### 103. Transparency in hazardous fuels reduction activity reporting\n##### (a) Inclusion of hazardous fuels reduction report in materials submitted in support of the President\u2019s budget\n**(1) In general**\nThe Secretary concerned shall include in the materials submitted in support of the President\u2019s budget pursuant to section 1105 of title 31, United States Code, a report describing\u2014\n**(A)**\nfor each of fiscal years 2025 through 2030, the number of acres of Federal land on which the Secretary concerned carried out hazardous fuels reduction activities during each of the preceding 6 fiscal years, as assessed by the Secretary concerned using\u2014\n**(i)**\nthe methodology of the Secretary concerned in effect on the day before the date of enactment of this Act; and\n**(ii)**\nthe methodology described in paragraph (2); and\n**(B)**\nfor fiscal year 2031 and each fiscal year thereafter, the number of acres of Federal land on which the Secretary concerned carried out hazardous fuels reduction activities during each of the preceding 6 fiscal years, as assessed by the Secretary concerned using the methodology described in paragraph (2).\n**(2) Requirements**\nFor purposes of the reports required under paragraph (1), the Secretary concerned shall\u2014\n**(A)**\nin determining the number of acres of Federal land on which the Secretary concerned carried out hazardous fuels reduction activities during each fiscal year covered by the report\u2014\n**(i)**\nrecord acres of Federal land on which hazardous fuels reduction activities were completed during each such fiscal year; and\n**(ii)**\nrecord each acre described in clause (i) once in the report with respect to a fiscal year, regardless of whether multiple hazardous fuels reduction activities were carried out on such acre during such fiscal year; and\n**(B)**\nwith respect to the acres of Federal land recorded in the report, include information on\u2014\n**(i)**\nwhich such acres are located in the wildland-urban interface;\n**(ii)**\nthe level of wildfire risk (high, moderate, or low) on the first and last day of each fiscal year covered by the report;\n**(iii)**\nthe types of hazardous fuels reduction activities completed for such acres, delineating between whether such activities were conducted\u2014\n**(I)**\nin a wildfire managed for resource benefits; or\n**(II)**\nthrough a planned project;\n**(iv)**\nthe cost per acre of hazardous fuels reduction activities carried out during each fiscal year covered by the report;\n**(v)**\nthe region or System unit in which the acres are located; and\n**(vi)**\nthe effectiveness of the hazardous fuels reduction activities on reducing the risk of wildfire.\n**(3) Transparency**\nThe Secretary concerned shall make each report submitted under paragraph (1) publicly available on the website of the Department of Agriculture and the Department of the Interior, as applicable.\n##### (b) Accurate data collection\n**(1) In general**\nNot later than 90 days after the date of enactment of this Act, the Secretary concerned shall implement standardized procedures for tracking data relating to hazardous fuels reduction activities carried out by the Secretary concerned.\n**(2) Elements**\nThe standardized procedures required under paragraph (1) shall include\u2014\n**(A)**\nregular, standardized data reviews of the accuracy and timely input of data used to track hazardous fuels reduction activities;\n**(B)**\nverification methods that validate whether such data accurately correlates to the hazardous fuels reduction activities carried out by the Secretary concerned;\n**(C)**\nan analysis of the short- and long-term effectiveness of the hazardous fuels reduction activities on reducing the risk of wildfire; and\n**(D)**\nfor hazardous fuels reduction activities that occur partially within the wildland-urban interface, methods to distinguish which acres are located within the wildland-urban interface and which acres are located outside the wildland-urban interface.\n**(3) Report**\nNot later than 14 days after implementing the standardized procedures required under paragraph (1), the Secretary concerned shall submit to Congress a report that describes\u2014\n**(A)**\nsuch standardized procedures; and\n**(B)**\nprogram and policy recommendations to Congress to address any limitations in tracking data relating to hazardous fuels reduction activities under this subsection.\n#### 104. Regional forest carbon accounting\nNot later than September 30, 2025, and every 3 years thereafter, the Secretary of Agriculture, acting through the Chief of the Forest Service, shall\u2014\n**(1)**\nusing data from the forest inventory and analysis program, determine the net forest carbon balance on the land in the National Forest System of each Forest Service region, including whether the National Forest System land is\u2014\n**(A)**\na carbon source; or\n**(B)**\na carbon sink; and\n**(2)**\npublish the information described in paragraph (1) on the website of the Forest Service.\n#### 105. Wildland fire performance metrics\n##### (a) In general\nNot later than 18 months after the date of enactment of this Act, the Secretary concerned shall submit to the committees of Congress described in subsection (c) a report on existing key performance indicators and potential outcome-based performance measures to reduce wildfire risk on Federal land.\n##### (b) Inclusions\nThe report submitted under subsection (a) shall identify solutions to track the implementation and effectiveness of hazardous fuels reduction activities and forest restoration treatments, including strategies\u2014\n**(1)**\nto track whether land management activities are reducing wildfire hazards and ways to quantify and track acres in maintenance status;\n**(2)**\nto track place-based and locally led outcomes;\n**(3)**\nto standardize national-level monitoring measures;\n**(4)**\nto quantify catastrophic wildfire risk reduction;\n**(5)**\nto identify modeling and data challenges that are preventing the transition to annual wildfire risk mapping updates; and\n**(6)**\nto integrate advanced technologies or a combination of technologies and analyses that will benefit the quality of information reported.\n##### (c) Committees of Congress described\nThe committees of Congress referred to in subsection (a) are\u2014\n**(1)**\nthe Committee on Energy and Natural Resources of the Senate;\n**(2)**\nthe Committee on Agriculture, Nutrition, and Forestry of the Senate;\n**(3)**\nthe Committee on Natural Resources of the House of Representatives; and\n**(4)**\nthe Committee on Agriculture of the House of Representatives.\nII\nForest management\n#### 201. Vegetation management, facility inspection, and operation and maintenance relating to electric transmission and distribution facility rights-of-way\n##### (a) Hazard trees within 50 feet of electric power line\nSection 512(a)(1)(B)(ii) of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1772(a)(1)(B)(ii) ) is amended by striking 10 and inserting 50 .\n##### (b) Permits and agreements with owners and operators of electric transmission or distribution facilities\nSection 512 of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1772 ) is amended\u2014\n**(1)**\nin the section heading, by striking managment and inserting management ;\n**(2)**\nby redesignating subsections (j) and (k) as subsections (k) and (l), respectively; and\n**(3)**\nby inserting after subsection (i) the following:\n(j) Permits and agreements with owners and operators of electric transmission or distribution facilities (1) In general In any special use permit or easement on National Forest System or Bureau of Land Management land provided to the owner or operator of an electric transmission or distribution facility, the Secretary concerned may provide permission to cut and remove trees or other vegetation from within the vicinity of the electric transmission or distribution facility without requiring a separate timber sale, if that cutting and removal is consistent with\u2014 (A) the applicable plan; (B) the applicable land and resource management plan or land use plan; and (C) other applicable environmental laws (including regulations). (2) Use of proceeds A special use permit or easement that includes permission for cutting and removal described in paragraph (1) shall include a requirement that, if the owner or operator of the electric transmission or distribution facility sells any portion of the material removed under the permit or easement, the owner or operator shall provide to the Secretary concerned any proceeds received from the sale, less any transportation costs incurred in the sale. (3) Effect Nothing in paragraph (2) shall require the sale of any material removed under a permit or easement that includes permission for cutting and removal described in paragraph (1). .\n#### 202. Timber sales on National Forest System land\nSection 14(d) of the National Forest Management Act of 1976 ( 16 U.S.C. 472a(d) ) is amended, in the first sentence, by striking $10,000 and inserting $55,000 .\n#### 203. Categorical exclusion for high-priority hazard trees\n##### (a) Definitions\nIn this section:\n**(1) High-priority hazard tree**\nThe term high-priority hazard tree means a standing tree that\u2014\n**(A)**\npresents a visible hazard to people or Federal property due to conditions such as deterioration of or damage to the root system, trunk, stem, or limbs of the tree, or the direction or lean of the tree, as determined by the Secretary;\n**(B)**\nis determined by the Secretary to be highly likely to fail and, if it failed, would be highly likely to cause injury to people or damage to Federal property; and\n**(C)**\nis\u2014\n**(i)**\nwithin 300 feet of a National Forest System road with a maintenance level of 3, 4, or 5;\n**(ii)**\nalong a National Forest System trail; or\n**(iii)**\nin a developed recreation site on National Forest System land that is operated and maintained by the Secretary.\n**(2) High-priority hazard tree activity**\n**(A) In general**\nThe term high-priority hazard tree activity means a forest management activity that mitigates the risks associated with high-priority hazard trees, which may include pruning, felling, and disposal of those high-priority hazard trees.\n**(B) Exclusions**\nThe term high-priority hazard tree activity does not include\u2014\n**(i)**\nany activity conducted in a wilderness area or wilderness study area;\n**(ii)**\nany activity for the construction of a permanent road or permanent trail;\n**(iii)**\nany activity conducted on Federal land on which, by Act of Congress or Presidential proclamation, the removal of vegetation is restricted or prohibited;\n**(iv)**\nany activity conducted in an area in which activities described in subparagraph (A) would be inconsistent with the applicable land and resource management plan; or\n**(v)**\nany activity conducted in an inventoried roadless area.\n**(3) Secretary**\nThe term Secretary means the Secretary of Agriculture.\n##### (b) Categorical exclusion\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, the Secretary shall develop a categorical exclusion (as defined in 111 of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4336e )) for high-priority hazard tree activities.\n**(2) Administration**\nIn developing and administering the categorical exclusion under paragraph (1), the Secretary shall\u2014\n**(A)**\ncomply with the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ); and\n**(B)**\napply the extraordinary circumstances procedures under section 220.6 of title 36, Code of Federal Regulations (or successor regulations), in determining whether to use the categorical exclusion.\n**(3) Project size limitation**\nA project carried out using the categorical exclusion developed under paragraph (1) may not exceed 3,000 acres.\n#### 204. Intervenor status\n##### (a) In general\nFor purposes of a civil action relating to a qualified project described in subsection (b), a unit of local government or an Indian Tribe shall be\u2014\n**(1)**\nentitled to intervene, as of right, in any subsequent civil action; and\n**(2)**\nconsidered to be a full participant in any settlement negotiation relating to the qualified project if the unit of local government or Indian Tribe, as applicable, intervenes.\n##### (b) Description of qualified project\nA qualified project referred to in subsection (a) is a project that\u2014\n**(1)**\nis located on Federal land adjacent, or with sufficient minimum contacts, as determined by the Secretary concerned, to the land under the jurisdiction of the unit of local government or Indian Tribe, as applicable;\n**(2)**\nhas been approved by the Secretary concerned; and\n**(3)**\n**(A)**\nreduces the risk posed by wildfire, insect, or disease; or\n**(B)**\ngenerates revenue from the harvesting of timber.\n#### 205. Utilizing grazing for wildfire risk reduction\n##### (a) In general\nNot later than 18 months after the date of enactment of this Act, the Secretary concerned shall develop and submit to the Committee on Energy and Natural Resources of the Senate and the Committee on Natural Resources of the House of Representatives a strategy to analyze and identify opportunities to use livestock grazing as a wildfire risk reduction tool on Federal land, consistent with the laws applicable to the Secretary concerned.\n##### (b) Inclusions\nThe strategy developed under subsection (a) shall include an analysis of\u2014\n**(1)**\nopportunities\u2014\n**(A)**\nto increase the use of any authorities applicable to livestock grazing, including modifications to grazing permits or leases to allow variances;\n**(B)**\nto use targeted grazing to reduce hazardous fuels;\n**(C)**\nto integrate advanced technologies to dynamically adjust livestock placement;\n**(D)**\nto increase the use of livestock grazing to eradicate invasive annual grasses and as a post-fire restoration and recovery strategy, as appropriate; and\n**(E)**\nto facilitate and expedite the temporary use of vacant allotments during extreme weather events or natural disasters; and\n**(2)**\nany other opportunities determined to be appropriate by the Secretary concerned.\n##### (c) Effect on existing grazing programs\nNothing in this section affects\u2014\n**(1)**\nany livestock grazing program carried out by the Secretary concerned as of the date of enactment of this Act; or\n**(2)**\nany statutory authority for any program described in paragraph (1).\nIII\nCultural change in agencies\n#### 301. Mandatory use of existing authorities\nNot later than 3 years after the date of enactment of this Act, with respect to each unit of Federal land that contains land described in section 102(5), the Secretary concerned shall use not fewer than 1 of the following streamlined authorities for environmental review:\n**(1)**\nSection 603(a) of the Healthy Forests Restoration Act of 2003 ( 16 U.S.C. 6591b(a) ).\n**(2)**\nSection 605(a) of the Healthy Forests Restoration Act of 2003 ( 16 U.S.C. 6591d(a) ).\n**(3)**\nSection 606(b) of the Healthy Forests Restoration Act of 2003 ( 16 U.S.C. 6591e(b) ).\n**(4)**\nSection 40806(b) of the Infrastructure Investment and Jobs Act ( 16 U.S.C. 6592b(b) ).\n**(5)**\nSection 40807 of the Infrastructure Investment and Jobs Act ( 16 U.S.C. 6592c ).\n**(6)**\nSection 207 of the Wildfire Suppression Funding and Forest Management Activities Act ( 16 U.S.C. 6591c note; Public Law 115\u2013141 ).\n#### 302. Public-private wildfire technology deployment and testbed partnership\n##### (a) Definitions\nIn this section:\n**(1) Appropriate committees**\nThe term appropriate committees means\u2014\n**(A)**\nthe Committees on Agriculture, Nutrition, and Forestry, Energy and Natural Resources, and Commerce, Science, and Transportation of the Senate; and\n**(B)**\nthe Committees on Agriculture, Natural Resources, and Science, Space, and Technology of the House of Representatives.\n**(2) Covered agency**\nThe term covered agency means\u2014\n**(A)**\neach Federal land management agency (as defined in section 802 of the Federal Lands Recreation Enhancement Act ( 16 U.S.C. 6801 ));\n**(B)**\nthe Department of Defense;\n**(C)**\nthe National Oceanic and Atmospheric Administration;\n**(D)**\nthe United States Fire Administration;\n**(E)**\nthe Federal Emergency Management Agency;\n**(F)**\nthe National Aeronautics and Space Administration;\n**(G)**\nthe Bureau of Indian Affairs; and\n**(H)**\nany other Federal agency involved in wildfire response.\n**(3) Covered entity**\nThe term covered entity means\u2014\n**(A)**\na private entity;\n**(B)**\na nonprofit organization; and\n**(C)**\nan institution of higher education (as defined in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 )).\n**(4) Pilot Program**\nThe term Pilot Program means the deployment and testbed pilot program established under subsection (b).\n**(5) Secretaries**\nThe term Secretaries means the Secretary of Agriculture and the Secretary of the Interior, acting jointly.\n##### (b) Establishment\nNot later than 60 days after the date of enactment of this Act, the Secretaries, in coordination with the heads of the covered agencies, shall establish a deployment and testbed pilot program for new and innovative wildfire prevention, detection, communication, and mitigation technologies.\n##### (c) Functions\nIn carrying out the Pilot Program, the Secretaries shall\u2014\n**(1)**\nincorporate the Pilot Program into an existing interagency coordinating group on wildfires;\n**(2)**\nin consultation with the heads of covered agencies, identify key technology priority areas with respect to the deployment of wildfire prevention, detection, communication, and mitigation technologies, including\u2014\n**(A)**\nhazardous fuels reduction activities or treatments;\n**(B)**\ndispatch communications;\n**(C)**\nremote sensing and tracking;\n**(D)**\nsafety equipment; and\n**(E)**\ncommon operating pictures or operational dashboards; and\n**(3)**\nconnect each covered entity selected to participate in the Pilot Program with the appropriate covered agency to coordinate real-time and on-the-ground testing of technology during wildland fire mitigation activities and training.\n##### (d) Applications\nTo participate in the Pilot Program, a covered entity shall submit to the Secretaries an application at such time, in such manner, and containing such information as the Secretaries may require, which shall include a proposal to test technologies specific to key technology priority areas identified under subsection (c)(2).\n##### (e) Prioritization of emerging technologies\nIn selecting covered entities to participate in the Pilot Program, the Secretaries shall give priority to covered entities developing and applying emerging technologies that address issues identified by the Secretaries, including artificial intelligence, quantum sensing, computing and quantum-hybrid applications, augmented reality, and 5G private networks and device-to-device communications supporting nomadic mesh networks, for wildfire mitigation.\n##### (f) Outreach\nThe Secretaries, in coordination with the heads of the covered agencies, shall make publicly available the key technology priority areas identified under subsection (c)(2) and invite covered entities to apply to test and demonstrate their technologies to address those priority areas.\n##### (g) Reports and recommendations\nNot later than 1 year after the date of enactment of this Act, and each year thereafter for the duration of the Pilot Program, the Secretaries shall submit to the appropriate committees a report that includes the following with respect to the Pilot Program:\n**(1)**\nA list of participating covered entities.\n**(2)**\nA brief description of the technologies tested by such covered entities.\n**(3)**\nAn estimate of the cost of acquiring the technology tested in the Pilot Program and applying it at scale.\n**(4)**\nOutreach efforts by Federal agencies to covered entities developing wildfire technologies.\n**(5)**\nAssessments of, and recommendations relating to, new technologies with potential adoption and application at-scale in the wildfire prevention, detection, communication, and mitigation efforts of Federal land management agencies (as defined in section 802 of the Federal Lands Recreation Enhancement Act ( 16 U.S.C. 6801 )).\n##### (h) Termination\nThe Pilot Program shall expire on the date that is 7 years after the date of enactment of this Act.\n#### 303. Repeal of FLAME reports\nSection 502 of the FLAME Act of 2009 ( 43 U.S.C. 1748a ) is amended\u2014\n**(1)**\nby striking subsection (h); and\n**(2)**\nby redesignating subsection (i) as subsection (h).",
      "versionDate": "2025-01-16",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Climate change and greenhouse gases",
            "updateDate": "2025-03-12T13:37:15Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-03-12T13:37:41Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-08T14:17:26Z"
          },
          {
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2025-03-12T13:37:01Z"
          },
          {
            "name": "Fires",
            "updateDate": "2025-03-12T13:36:55Z"
          },
          {
            "name": "Forests, forestry, trees",
            "updateDate": "2025-03-12T13:36:48Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-03-12T13:37:09Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2025-03-12T13:37:21Z"
          },
          {
            "name": "Livestock",
            "updateDate": "2025-03-12T13:37:33Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2025-03-12T13:37:53Z"
          },
          {
            "name": "Public-private cooperation",
            "updateDate": "2025-03-12T13:37:48Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-03-12T13:37:28Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-02-27T19:22:06Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s140",
          "measure-number": "140",
          "measure-type": "s",
          "orig-publish-date": "2025-01-16",
          "originChamber": "SENATE",
          "update-date": "2025-07-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s140v00",
            "update-date": "2025-07-25"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This bill establishes forest management requirements for federal lands, particularly with respect to reducing wildfires.\u00a0</p><p>For example, the bill establishes annual goals to increase (1) the number of acres of Forest Service and Bureau of Land Management (BLM) land that are mechanically thinned (i.e., a management process related to the removal of trees and vegetation); and (2) the number of acres of Forest Service and BLM land treated by prescribed fire. By FY2029, the goals must be to increase the number of acres of each by at least 40% compared to the average number of acres of each in FY2019-FY2023.</p><p>The bill also directs the Forest Service and the BLM to (1) implement standardized procedures for tracking data relating to hazardous fuels reduction activities they carry out, and (2) develop a strategy to identify opportunities to use livestock grazing as a wildfire risk reduction tool on federal land. Additionally, the Forest Service and the Department of the Interior must establish a deployment and test bed pilot program for wildfire prevention, detection, communication, and mitigation technologies.</p><p>The bill mandates use of existing authorities for expedited environmental review for certain forest land at high risk from wildfire, insects, or disease.</p><p>Finally, the bill provides local governments and Indian tribes the right to intervene in lawsuits concerning certain projects on federal land that (1) reduce risks posed by wildfire, insects, or disease; or (2) generate revenue from harvesting timber.</p>"
        },
        "title": "Wildfire Prevention Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s140.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill establishes forest management requirements for federal lands, particularly with respect to reducing wildfires.\u00a0</p><p>For example, the bill establishes annual goals to increase (1) the number of acres of Forest Service and Bureau of Land Management (BLM) land that are mechanically thinned (i.e., a management process related to the removal of trees and vegetation); and (2) the number of acres of Forest Service and BLM land treated by prescribed fire. By FY2029, the goals must be to increase the number of acres of each by at least 40% compared to the average number of acres of each in FY2019-FY2023.</p><p>The bill also directs the Forest Service and the BLM to (1) implement standardized procedures for tracking data relating to hazardous fuels reduction activities they carry out, and (2) develop a strategy to identify opportunities to use livestock grazing as a wildfire risk reduction tool on federal land. Additionally, the Forest Service and the Department of the Interior must establish a deployment and test bed pilot program for wildfire prevention, detection, communication, and mitigation technologies.</p><p>The bill mandates use of existing authorities for expedited environmental review for certain forest land at high risk from wildfire, insects, or disease.</p><p>Finally, the bill provides local governments and Indian tribes the right to intervene in lawsuits concerning certain projects on federal land that (1) reduce risks posed by wildfire, insects, or disease; or (2) generate revenue from harvesting timber.</p>",
      "updateDate": "2025-07-25",
      "versionCode": "id119s140"
    },
    "title": "Wildfire Prevention Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill establishes forest management requirements for federal lands, particularly with respect to reducing wildfires.\u00a0</p><p>For example, the bill establishes annual goals to increase (1) the number of acres of Forest Service and Bureau of Land Management (BLM) land that are mechanically thinned (i.e., a management process related to the removal of trees and vegetation); and (2) the number of acres of Forest Service and BLM land treated by prescribed fire. By FY2029, the goals must be to increase the number of acres of each by at least 40% compared to the average number of acres of each in FY2019-FY2023.</p><p>The bill also directs the Forest Service and the BLM to (1) implement standardized procedures for tracking data relating to hazardous fuels reduction activities they carry out, and (2) develop a strategy to identify opportunities to use livestock grazing as a wildfire risk reduction tool on federal land. Additionally, the Forest Service and the Department of the Interior must establish a deployment and test bed pilot program for wildfire prevention, detection, communication, and mitigation technologies.</p><p>The bill mandates use of existing authorities for expedited environmental review for certain forest land at high risk from wildfire, insects, or disease.</p><p>Finally, the bill provides local governments and Indian tribes the right to intervene in lawsuits concerning certain projects on federal land that (1) reduce risks posed by wildfire, insects, or disease; or (2) generate revenue from harvesting timber.</p>",
      "updateDate": "2025-07-25",
      "versionCode": "id119s140"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s140is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Wildfire Prevention Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-03T12:03:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Wildfire Prevention Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-20T02:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to address the forest health crisis on the National Forest System and public lands, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-20T02:03:22Z"
    }
  ]
}
```
