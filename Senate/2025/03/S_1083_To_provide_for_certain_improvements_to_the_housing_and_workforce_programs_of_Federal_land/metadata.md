# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1083?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1083
- Title: Land Manager Housing and Workforce Improvement Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1083
- Origin chamber: Senate
- Introduced date: 2025-03-14
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-14: Introduced in Senate
- 2025-03-14 - IntroReferral: Introduced in Senate
- 2025-03-14 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources. (text: S1779-1781)
- Latest action: 2025-03-14: Introduced in Senate

## Actions

- 2025-03-14 - IntroReferral: Introduced in Senate
- 2025-03-14 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources. (text: S1779-1781)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-14",
    "latestAction": {
      "actionDate": "2025-03-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1083",
    "number": "1083",
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
    "title": "Land Manager Housing and Workforce Improvement Act of 2025",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-14",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources. (text: S1779-1781)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-14",
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
          "date": "2025-03-14T20:53:16Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
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
      "sponsorshipDate": "2025-03-14",
      "state": "MT"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-03-14",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1083is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1083\nIN THE SENATE OF THE UNITED STATES\nMarch 14, 2025 Mr. Barrasso (for himself, Mr. Daines , and Mr. King ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo provide for certain improvements to the housing and workforce programs of Federal land management agencies, and for other purposes.\n#### 1. Short title\n##### (a) Short title\nThis Act may be cited as the Land Manager Housing and Workforce Improvement Act of 2025 .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title.\nSec. 2. Definitions.\nTITLE I\u2014Expanding authority\nSec. 101. Prioritizing National Park Service workforce housing.\nSec. 102. Authorizing the National Park Service to address workforce housing off-park.\nSec. 103. Expanding National Park Service rental options.\nSec. 104. Leveraging National Park Service rental receipts for workforce housing programming.\nSec. 105. Empowering the Forest Service to address workforce housing needs.\nTITLE II\u2014Expanding partnership capacity\nSec. 201. Engaging partners to address National Park Service workforce housing.\nSec. 202. Encouraging public-private cooperative management.\nSec. 203. Leveraging philanthropic support to address National Park Service workforce housing.\nTITLE III\u2014Supporting workforce\nSec. 301. Supporting the land manager workforce.\nSec. 302. Supporting the seasonal National Park Service workforce.\nTITLE IV\u2014Reports and oversight\nSec. 401. Quantifying the workforce housing needs of land managers.\nSec. 402. Conducting oversight on the housing programming of land managers.\nSec. 403. Justifying emergency spending.\n#### 2. Definitions\nIn this Act:\n**(1) Appropriate committees of Congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Energy and Natural Resources of the Senate;\n**(B)**\nthe Committee on Agriculture, Nutrition, and Forestry of the Senate;\n**(C)**\nthe Committee on Appropriations of the Senate;\n**(D)**\nthe Committee on Natural Resources of the House of Representatives;\n**(E)**\nthe Committee on Agriculture of the House of Representatives; and\n**(F)**\nthe Committee on Appropriations of the House of Representatives.\n**(2) Covered agencies**\nThe term covered agencies means\u2014\n**(A)**\nthe National Park Service;\n**(B)**\nthe Bureau of Land Management;\n**(C)**\nthe United States Fish and Wildlife Service; and\n**(D)**\nthe Forest Service.\n**(3) Secretary**\nThe term Secretary means the Secretary of the Interior.\nI\nExpanding authority\n#### 101. Prioritizing National Park Service workforce housing\nSection 103502(a)(3) of title 54, United States Code, is amended\u2014\n**(1)**\nby inserting quarters for field employees (as those terms are defined in section 101331), after prioritize ; and\n**(2)**\nby inserting a comma after facilities .\n#### 102. Authorizing the National Park Service to address workforce housing off-park\nSection 100901 of title 54, United States Code, is amended by adding at the end the following:\n(i) Acquisition of land for administration of system units (1) In general To facilitate the administration of a System unit, the Secretary may acquire, by donation, exchange, or transfer from another Federal agency, not more than 20 acres of land or interests in land, cumulatively, within the vicinity of the System unit boundary for the development, construction, maintenance, or operation of quarters for field employees (as those terms are defined in section 101331) for the System unit. (2) Management (A) In general With respect to any land or interest in land acquired by the Secretary under paragraph (1)\u2014 (i) the land or interest in land shall not\u2014 (I) be administered as part of the System; or (II) be subject to the laws (including regulations) governing the associated System unit; but (ii) the Secretary shall\u2014 (I) have the authority to supervise, manage, and control the land; and (II) issue such rules and regulations as the Secretary may determine to be necessary and proper for the use and management of the land. (B) Authorizations The Secretary may grant exclusive privileges, leases, and permits for the use of land acquired under paragraph (1) and enter into contracts relating to such authorizations as authorized under this title, notwithstanding any restriction on such authorizations to land within a System unit boundary. (3) Disposal If the Secretary determines that any land or interest in land acquired under paragraph (1) no longer supports the administration of the System unit\u2014 (A) the Secretary may determine the land and any improvements to the land to be excess property for disposal; and (B) the proceeds from the disposal of excess property under subparagraph (A) shall be retained by the Secretary and deposited in the special fund established for the development, construction, maintenance, or operation of quarters for field employees (as so defined) described in section 101338(b), to be expended by the Secretary without further appropriation. .\n#### 103. Expanding National Park Service rental options\nSection 101336 of title 54, United States Code, is amended, in the first sentence, by striking management, repair, and maintenance of field employee quarters and inserting development, construction, maintenance, or operation of quarters for field employees .\n#### 104. Leveraging National Park Service rental receipts for workforce housing programming\nSection 101338 of title 54, United States Code, is amended by adding at the end the following:\n(c) Use of special fund by National Park Service Amounts deposited by the Service in the special fund described in subsection (b) and established under section 320 of Public Law 98\u2013473 ( 5 U.S.C. 5911 note) shall be available for the development, construction, maintenance, or operation of quarters for field employees at System units. .\n#### 105. Empowering the Forest Service to address workforce housing needs\n##### (a) Use of Forest Service structures or improvements\nSection 7 of the Act of April 24, 1950 (commonly known as the Granger-Thye Act ) (64 Stat. 84, chapter 97; 16 U.S.C. 580d ), is amended by striking thirty years as determined by him and inserting 30 years, or in the case of a permit for workforce housing and related infrastructure, 50 years, as determined to be appropriate by the Secretary of Agriculture .\n##### (b) Conveyances of Forest Service administrative sites\nTitle V of the Forest Service Facility Realignment and Enhancement Act of 2005 ( 16 U.S.C. 580d note; Public Law 109\u201354 ) is amended\u2014\n**(1)**\nin section 503\u2014\n**(A)**\nby striking subsection (f); and\n**(B)**\nby redesignating subsection (g) as subsection (f); and\n**(2)**\nin section 504(c)(2), by striking by competitive sale and inserting by soliciting not fewer than 2 competitive bids .\nII\nExpanding partnership capacity\n#### 201. Engaging partners to address National Park Service workforce housing\nSection 101701(a) of title 54, United States Code, is amended\u2014\n**(1)**\nin paragraph (1), by inserting, , including projects for quarters for field employees (as those terms are defined in section 101331), after responsibilities of the Secretary ; and\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nby inserting , Tribal, after State ;\n**(B)**\nby inserting (including an organization that has a philanthropic agreement to fundraise or otherwise generate donations on behalf of, or for the benefit of, the Service) after organization ; and\n**(C)**\nby inserting (including an individual that has a philanthropic agreement to fundraise or otherwise generate donations on behalf of, or for the benefit of, the Service) after individual .\n#### 202. Encouraging public-private cooperative management\nSection 101703 of title 54, United States Code, is amended to read as follows:\n101703. Cooperative management agreements (a) Definition of State In this section, the term State means each of the several States, the District of Columbia, and each territory of the United States. (b) Cooperative management agreements (1) In general The Secretary, in accordance with the laws generally applicable to System units and under such terms and conditions as the Secretary considers appropriate, may enter into a cooperative management agreement with a State, Indian Tribe, or local government with park land adjacent to a System unit, if the agreement would provide for more effective and efficient management of a System unit and the adjacent non-Federal park land. (2) No transfer of administrative responsibilities The Secretary may not transfer administration responsibilities for any System unit under this subsection. (c) Provision of goods and services (1) In general The Secretary may provide or acquire goods and services on a reimbursable basis as part of a cooperative management agreement entered into under subsection (b). (2) Retention of funds The Secretary may retain and expend any funds received under this section without further appropriation. (d) Co-Location The Secretary and a State, Indian Tribe, or local government may co-locate in offices or facilities owned or leased by either party as part of a cooperative management agreement entered into under subsection (b). (e) Employees (1) Assignment of employee The Secretary may arrange an assignment under section 3372 of title 5 of a Federal employee or an employee of a State, Indian Tribe, or local government, as mutually agreed on, for work, on the applicable Federal, State, local, or Tribal park land covered by the cooperative management agreement. (2) Extension of assignment An assignment under paragraph (1) may be extended if the Secretary and the State, Indian Tribe, or local government determine the extension to be mutually beneficial. .\n#### 203. Leveraging philanthropic support to address National Park Service workforce housing\nSection 103501(c)(3) of title 54, United States Code, is amended by striking (including funds and fairly valued durable goods and materials) and inserting (including any combination of cash, fairly valued services, and durable goods and materials) .\nIII\nSupporting workforce\n#### 301. Supporting the land manager workforce\n##### (a) In general\nThe Secretary or the Secretary of Agriculture, as applicable, may recruit and directly appoint qualified individuals into the competitive service who are certified, in accordance with procedures established by the Secretary or the Secretary of Agriculture, as applicable, as maintaining a permanent and exclusive residence within the vicinity of a site administered by the National Park Service, the United States Fish and Wildlife Service, or the Forest Service to a field unit which the individual would report to work into any position at or below grade GS\u20139 of the General Schedule, WG\u201315 of the Federal Wage System, or equivalent within the applicable field unit.\n##### (b) Requirements\nAn appointment by the Secretary under subsection (a) shall be considered compliant with all applicable provisions of chapter 33 of title 5, United States Code, if the Secretary ensures that the appointment action\u2014\n**(1)**\nis consistent with the merit principles of section 2301 of that title; and\n**(2)**\ncomplies with the public notice requirements of section 3327 of that title.\n##### (c) Termination of authority\nThe authority provided under subsection (a) shall terminate on September 30, 2030.\n#### 302. Supporting the seasonal National Park Service workforce\n##### (a) In general\nNotwithstanding any other provision of law, for purposes of determining the noncompetitive rehire eligibility of temporary seasonal employees of the National Park Service\u2014\n**(1)**\nthe Secretary shall establish a definition of what constitutes a major subdivision of the National Park Service; and\n**(2)**\nany requirement that a position be in the same local commuting area shall not apply.\n##### (b) Termination of authority\nThe authority provided under subsection (a) shall terminate on September 30, 2030.\nIV\nReports and oversight\n#### 401. Quantifying the workforce housing needs of land managers\nNot later than 18 months after the date of enactment of this Act, the Secretary and the Secretary of Agriculture shall jointly submit to the appropriate committees of Congress a needs assessment report that provides, with respect to housing the workforce of covered agencies, as applicable\u2014\n**(1)**\nan analysis of the unit type and condition of\u2014\n**(A)**\nhousing owned by the covered agencies; and\n**(B)**\nhousing leased by the covered agencies;\n**(2)**\nan analysis of the employment status of the occupants of the housing analyzed under paragraph (1), including\u2014\n**(A)**\nwhether the occupants are\u2014\n**(i)**\nmembers of the permanent workforce; or\n**(ii)**\nmembers of the seasonal workforce; and\n**(B)**\nwhich positions identified under subparagraph (A) required housing provided by the applicable covered agency as a condition of employment with the covered agency; and\n**(3)**\nan analysis of the private housing markets within the vicinity of a covered agency field unit, including\u2014\n**(A)**\nthe availability and affordability of housing for sale or lease; and\n**(B)**\nthe impact of vacation rental services on\u2014\n**(i)**\nthe cost of living; and\n**(ii)**\nthe available supply of housing.\n#### 402. Conducting oversight on the housing programming of land managers\n##### (a) Report to Congress\nNot later than 18 months after the date of enactment of this Act, the Comptroller General of the United States shall submit to the appropriate committees of Congress a report that\u2014\n**(1)**\nassesses, in consultation with the National Housing Council described in Office of Management and Budget Circular A\u201345, the effect of Office of Management and Budget Circular A\u201345R on the housing of the workforce of covered agencies;\n**(2)**\nassesses the effect of Office of Management and Budget Circular A\u201311 on the housing of the workforce of covered agencies;\n**(3)**\nassesses the effect of department-level guidance on the housing of the workforce of covered agencies;\n**(4)**\nassesses the effect of agency-level guidance on the housing of the workforce of covered agencies; and\n**(5)**\nidentifies suggested administrative actions and legislative proposals to reform the guidance assessed under paragraphs (1) through (4), including\u2014\n**(A)**\nimprovements to tenant experience;\n**(B)**\nimprovements to workforce housing supply, including\u2014\n**(i)**\nhousing managed by the covered agencies; and\n**(ii)**\nleased private market housing;\n**(C)**\nimprovements to financing options;\n**(D)**\nimprovements to public-private partnerships;\n**(E)**\nimprovements to philanthropic engagement; and\n**(F)**\nimprovements to commuting times to report stations, including\u2014\n**(i)**\navailable housing in the gateway communities;\n**(ii)**\navailable housing in the nearest established community (as defined in Office of Management and Budget Circular A\u201345); and\n**(iii)**\ndifferences between normal commuting conditions and peak-commute traffic conditions, including considerations for\u2014\n**(I)**\nroad quality and condition;\n**(II)**\navailability of public transportation;\n**(III)**\nwinter driving; and\n**(IV)**\nvisitor traffic.\n##### (b) Implementation\nNot later than 1 year after the date on which the report is submitted under subsection (a), the heads of the covered agencies shall carry out the administrative actions identified under paragraph (5) of that subsection.\n#### 403. Justifying emergency spending\nSection 5 of the Act of August 3, 1956 (70 Stat. 1033, chapter 950; 7 U.S.C. 2228 ), is amended\u2014\n**(1)**\nby striking the section designation and all that follows through The Department and inserting the following:\n5. Emergency subsistence for employees (a) In general The Department ; and\n**(2)**\nby adding at the end the following:\n(b) Report (1) In general Except as provided in paragraph (3), not later than 30 days after the date on which the Secretary of Agriculture furnishes subsistence to employees under subsection (a), the Secretary of Agriculture shall submit to the appropriate committees of Congress (as defined in section 2 of the Land Manager Housing and Workforce Improvement Act of 2025 ) a report providing\u2014 (A) 1 or more justifications for the use of the authority; (B) the number of employees that were furnished subsistence; (C) the estimated cost of furnishing subsistence; and (D) the expected duration for which subsistence is to be provided. (2) Office of Management and Budget The information for a report required under paragraph (1) shall be produced in coordination with, and approved by, the Director of the Office of Management and Budget. (3) Exception A report under paragraph (1) shall not be required in the case of an emergency resulting from a natural disaster, act of terrorism, or other man-made disaster. .",
      "versionDate": "2025-03-14",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-20T22:31:44Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1083is.xml"
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
      "title": "Land Manager Housing and Workforce Improvement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-09T03:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Land Manager Housing and Workforce Improvement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-09T03:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for certain improvements to the housing and workforce programs of Federal land management agencies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-09T03:48:28Z"
    }
  ]
}
```
