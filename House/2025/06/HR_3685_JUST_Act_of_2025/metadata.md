# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3685?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3685
- Title: JUST Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3685
- Origin chamber: House
- Introduced date: 2025-06-03
- Update date: 2026-03-16T18:07:52Z
- Update date including text: 2026-03-16T18:07:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-03: Introduced in House
- 2025-06-03 - IntroReferral: Introduced in House
- 2025-06-03 - IntroReferral: Introduced in House
- 2025-06-03 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-06-03: Introduced in House

## Actions

- 2025-06-03 - IntroReferral: Introduced in House
- 2025-06-03 - IntroReferral: Introduced in House
- 2025-06-03 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-03",
    "latestAction": {
      "actionDate": "2025-06-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3685",
    "number": "3685",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "J000309",
        "district": "1",
        "firstName": "Jonathan",
        "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
        "lastName": "Jackson",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "JUST Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-16T18:07:52Z",
    "updateDateIncludingText": "2026-03-16T18:07:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-03",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-06-03T16:04:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "MS"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3685ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3685\nIN THE HOUSE OF REPRESENTATIVES\nJune 3, 2025 Mr. Jackson of Illinois (for himself and Mr. Thompson of Mississippi ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo enhance civil rights accountability and enforcement in the Department of Agriculture, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Just USDA Standards and Transparency Act of 2025 or the JUST Act of 2025 .\n#### 2. Civil rights accountability for USDA employees\n##### (a) In general\nThe Secretary of Agriculture shall ensure that appropriate corrective action is taken with respect to any official or employee of the Department of Agriculture who has been found to have engaged in any of the actions, violations, or misconduct referred to in subsection (b) while in the course of such official\u2019s or employee\u2019s employment or in administering a Department of Agriculture program or service\u2014\n**(1)**\nin any administrative finding by the Department of Agriculture, including any final agency decision issued by the Assistant Secretary of Agriculture for Civil Rights and any civil rights compliance review or misconduct investigation conducted by the Department of Agriculture;\n**(2)**\nin any Federal administrative or judicial proceeding;\n**(3)**\nin any settlement with respect to civil rights;\n**(4)**\nin any audit or investigation conducted by the Office of the Inspector General of the Department of Agriculture; or\n**(5)**\nin any investigation conducted by the Office of the Special Counsel.\n##### (b) Covered actions, violations, or misconduct\nThe actions, violations, or misconduct referred to in this subsection are discriminatory actions, retaliatory actions, harassment, civil rights violations, or related misconduct, including the following:\n**(1)**\nFailure to provide a receipt for service in accordance with section 2501A(e) of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 2279\u20131(e) ) to any current or prospective applicants of, or participants in, Department of Agriculture programs.\n**(2)**\nProviding an inaccurate receipt for service under such section 2501A(e) to any such current or prospective applicants or participants.\n**(3)**\nFailure to provide appropriate information regarding relevant programs and services at the Department of Agriculture, when requested by any such current or prospective applicants or participants.\n**(4)**\nFailure to timely process applications or otherwise delaying program services to any such current or prospective applicants or participants.\n##### (c) Corrective action defined\nIn this section, the term corrective action means any action taken to respond to any of the actions, violations, or misconduct referred to in subsection (b) that\u2014\n**(1)**\nwould enhance civil rights at the Department of Agriculture, including any policy or programmatic changes to prevent similar misconduct from occurring in the future; and\n**(2)**\nmay include disciplinary actions, including\u2014\n**(A)**\nremoval from Federal service;\n**(B)**\nsuspension without pay;\n**(C)**\nany reduction in grade or pay; and\n**(D)**\na letter of reprimand.\n#### 3. Improvements to the Office of the Assistant Secretary for Civil Rights\n##### (a) In general\nThe Department of Agriculture Reorganization Act of 1994 ( 7 U.S.C. 6912 et seq. ) is amended by inserting after section 218 ( 7 U.S.C. 6918 ) the following:\n218A. Assistant Secretary of Agriculture for Civil Rights (a) Establishment The Secretary shall establish in the Department the position of Assistant Secretary of Agriculture for Civil Rights (referred to in this section as the Assistant Secretary ). (b) Appointment The Assistant Secretary shall be appointed by the President, by and with the advice and consent of the Senate. (c) Duties (1) In general The Secretary shall delegate to the Assistant Secretary responsibility for\u2014 (A) ensuring compliance with all civil rights and related laws by all agencies and under all programs of the Department; (B) coordinating administration of civil rights laws (including regulations) within the Department for employees of, and participants in, programs of the Department; and (C) ensuring that necessary and appropriate civil rights components are properly incorporated into all strategic planning initiatives of the Department and agencies of the Department. (2) Office of Legal Advisor for Civil Rights Not later than 120 days after the date of enactment of this section, the Secretary shall establish an Office of Legal Advisor for Civil Rights that shall\u2014 (A) be the sole office within the Department responsible for providing legal advice to the Assistant Secretary to\u2014 (i) ensure compliance with all civil rights and related laws and regulations by all agencies and under all programs of the Department; and (ii) carry out fair and impartial investigations of civil rights complaints; (B) report directly to the Assistant Secretary; and (C) not represent or defend the Department or any of its agencies with respect to any claims of program or employment discrimination. .\n##### (b) Conforming amendments\n**(1) Assistant Secretaries of Agriculture**\nSection 218 of the Department of Agriculture Reorganization Act of 1994 ( 7 U.S.C. 6918 ) is amended\u2014\n**(A)**\nin subsection (a)\u2014\n**(i)**\nin paragraph (1), by adding and at the end;\n**(ii)**\nin paragraph (2), by striking ; and at the end and inserting a period; and\n**(iii)**\nby striking paragraph (3);\n**(B)**\nin subsection (b), by striking any position of Assistant Secretary authorized under paragraph (1) or (3) of subsection (a) and inserting the position of Assistant Secretary of Agriculture for Congressional Relations and Intergovernmental Affairs under subsection (a)(1) ; and\n**(C)**\nby striking subsection (c).\n**(2) Termination of authority**\nSection 296(b)(5) of the Department of Agriculture Reorganization Act of 1994 ( 7 U.S.C. 7014(b)(5) ) is amended to read as follows:\n(5) The authority of the Secretary to carry out section 218A. .\n#### 4. Equitable relief\n##### (a) Equitable relief from ineligibility for loans, payments, or other benefits\nSection 1613 of the Farm Security and Rural Investment Act of 2002 ( 7 U.S.C. 7996 ) is amended\u2014\n**(1)**\nby redesignating subsections (f) through (j) as subsections (g) through (k), respectively;\n**(2)**\nby inserting after subsection (e) the following:\n(f) Equitable relief by the Assistant Secretary of Agriculture for Civil Rights (1) In general The Assistant Secretary of Agriculture for Civil Rights (or a designee of the Secretary in the Office of the Assistant Secretary for Civil Rights, if no Assistant Secretary of Agriculture for Civil Rights is appointed and confirmed in accordance with section 218A(b) of the Department of Agriculture Reorganization Act of 1994) may grant relief in accordance with subsections (b) through (d) to a participant who files a civil rights program complaint. (2) Decisions The decision by the Assistant Secretary of Agriculture for Civil Rights (or the designee of the Secretary) to grant relief under this subsection\u2014 (A) shall not require prior approval by any officer or employee of the Department of Agriculture; and (B) is subject to reversal only by the Secretary (who may not delegate the reversal authority). (3) Other authority The authority provided to the Assistant Secretary of Agriculture for Civil Rights (or the designee of the Secretary) under this subsection is in addition to any other applicable authority and does not limit other authority provided by law or the Secretary. ;\n**(3)**\nin subsection (g), as so redesignated, by striking or the State Conservationist and inserting the State Conservationist, or the Assistant Secretary of Agriculture for Civil Rights (or the designee of the Secretary) ; and\n**(4)**\nin paragraph (1) of subsection (h), as so redesignated, by striking and (e) and inserting , (e), and (f) .\n##### (b) Equitable relief for actions taken in good faith\nSection 366 of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 2008a ) is amended\u2014\n**(1)**\nby amending subsection (b) to read as follows:\n(b) Limitation The Secretary may only provide relief to a farmer or rancher under subsection (a) if the Secretary determines that the farmer or rancher\u2014 (1) acted in good faith and relied on an action of, or the advice of, the Secretary (including any authorized representative of the Secretary) to the detriment of the farming or ranching operation of the farmer or rancher; or (2) failed to comply fully with the requirements to receive a loan described in subsection (a)(1), but made a good faith effort to comply with the requirements. ;\n**(2)**\nby redesignating subsection (e) as subsection (f);\n**(3)**\nby inserting after subsection (d) the following:\n(e) Equitable relief by the Assistant Secretary of Agriculture for Civil Rights (1) In general The Assistant Secretary of Agriculture for Civil Rights (or a designee of the Secretary in the Office of the Assistant Secretary for Civil Rights, if no Assistant Secretary of Agriculture for Civil Rights is appointed and confirmed in accordance with section 218A(b) of the Department of Agriculture Reorganization Act of 1994) may grant relief in accordance with subsections (a) through (d) to an individual who files a complaint with respect to civil rights regarding a direct farm ownership, operating, or emergency loan under this title. (2) Decisions The decision by the Assistant Secretary of Agriculture for Civil Rights (or the designee of the Secretary) to grant relief under this subsection\u2014 (A) shall not require prior approval by any officer or employee of the Department of Agriculture; and (B) is subject to reversal only by the Secretary (who may not delegate the reversal authority). (3) Other authority The authority provided to the Assistant Secretary of Agriculture for Civil Rights (or the designee of the Secretary) under this subsection is in addition to any other applicable authority and does not limit other authority provided by law or the Secretary. ; and\n**(4)**\nin subsection (f), as so redesignated, by striking Secretary and inserting Secretary, or the Assistant Secretary of Agriculture for Civil Rights (or the designee of the Secretary), .\n#### 5. Office of the Civil Rights Ombudsperson\nTitle III of the Federal Crop Insurance Reform and Department of Agriculture Reorganization Act of 1994 ( 7 U.S.C. 2231b et seq. ) is amended by adding at the end the following:\n310. Office of the Civil Rights Ombudsperson (a) In general Not later than 120 days after the date of enactment of this section, the Secretary shall establish an Office of the Civil Rights Ombudsperson (in this section referred to as the Office ) within the Department. The Office shall be independent of Department agencies and offices. (b) Ombudsperson designation The Secretary shall designate a Civil Rights Ombudsperson (in this section referred to as the Ombudsperson ) for the Office. The Ombudsperson shall be considered a senior official of the Department and have a background in civil rights enforcement. (c) Office personnel The Ombudsperson shall appoint such employees as are necessary to perform the functions of the Office and for the administration of the Office. (d) Functions The functions of the Office shall be\u2014 (1) to assist producers and other customers of Department programs in navigating the civil rights review process; (2) to ensure that participants (as defined in section 271) are aware of the appeals process under subtitle H of title II, including informal hearings under section 275; (3) to promote awareness of the Office and its responsibilities among producers and other customers of Department programs; and (4) to raise issues and concerns with respect to, and make recommendations to the Secretary about, equitable access or implementation of Department programs. (e) Access to information (1) In general Subject to paragraph (2), the Secretary shall establish procedures to provide the Office access to all departmental records necessary to execute the functions of the Office under subsection (d). (2) Timelines The procedures described in paragraph (1) shall include a requirement that requests from the Office for departmental records shall be fulfilled not later than 60 days after the request is made. (f) Annual report Beginning not later than 1 year after the date of the enactment of this section, and annually thereafter, the Ombudsperson shall prepare and submit to the House Committee on Agriculture and the Senate Committee on Agriculture, Nutrition, and Forestry a report on\u2014 (1) the activities carried out by the Office; and (2) the findings and recommendations of the Office with respect to equitable access or implementation of Department programs. (g) Authorization of appropriations There is authorized to be appropriated such sums as are necessary to carry out this section for each of fiscal years 2026 through 2028. .\n#### 6. Burden of proof for national appeals division hearings\nSection 277(c)(4) of the Department of Agriculture Reorganization Act of 1994 ( 7 U.S.C. 6997(c)(4) ) is amended to read as follows:\n(4) Burden of proof The agency shall bear the burden of proving by substantial evidence that the adverse decision of the agency was valid. .",
      "versionDate": "2025-06-03",
      "versionType": "Introduced in House"
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
        "name": "Agriculture and Food",
        "updateDate": "2025-07-11T17:24:59Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-03",
    "originChamber": "House",
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
          "measure-id": "id119hr3685",
          "measure-number": "3685",
          "measure-type": "hr",
          "orig-publish-date": "2025-06-03",
          "originChamber": "HOUSE",
          "update-date": "2026-03-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3685v00",
            "update-date": "2026-03-16"
          },
          "action-date": "2025-06-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Just USDA Standards and Transparency Act of 2025 or the JUST Act of 2025</strong></p><p>This bill increases Department of Agriculture (USDA) oversight and enforcement of civil rights-related violations and actions.</p><p>USDA must take appropriate corrective action regarding any USDA official or employee who engages in certain discriminatory actions, retaliatory actions, harassment, or civil rights violations (e.g., failure to provide appropriate information regarding relevant USDA programs and services).\u00a0A corrective action (1) is any action that would enhance civil rights at USDA, including policy or programmatic changes; and (2) may include disciplinary actions (e.g., removal from federal service or a letter of reprimand).</p><p>The bill shifts the burden of proof from a farmer or rancher to USDA in an appeal to the USDA National Appeals Division. Specifically, USDA must prove by substantial evidence the validity of a USDA adverse decision.</p><p>Further, a farmer or rancher who fails to comply fully with the requirements to receive a loan may be eligible for equitable relief if the USDA determines the individual made a good faith effort to comply with the loan requirements.</p><p>The bill also</p><ul><li>directs USDA to establish an Office of the Legal Advisor for Civil Rights and Office of the Civil Rights Ombudsperson;</li><li>creates the required position of Assistant Secretary of Agriculture for Civil Rights (currently an optional USDA\u00a0position); and</li><li>allows the Assistant Secretary to grant relief, without prior approval, to farmers or ranchers who file certain civil rights complaints, including complaints\u00a0regarding direct farm ownership, operating, or emergency loans.</li></ul>"
        },
        "title": "JUST Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3685.xml",
    "summary": {
      "actionDate": "2025-06-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Just USDA Standards and Transparency Act of 2025 or the JUST Act of 2025</strong></p><p>This bill increases Department of Agriculture (USDA) oversight and enforcement of civil rights-related violations and actions.</p><p>USDA must take appropriate corrective action regarding any USDA official or employee who engages in certain discriminatory actions, retaliatory actions, harassment, or civil rights violations (e.g., failure to provide appropriate information regarding relevant USDA programs and services).\u00a0A corrective action (1) is any action that would enhance civil rights at USDA, including policy or programmatic changes; and (2) may include disciplinary actions (e.g., removal from federal service or a letter of reprimand).</p><p>The bill shifts the burden of proof from a farmer or rancher to USDA in an appeal to the USDA National Appeals Division. Specifically, USDA must prove by substantial evidence the validity of a USDA adverse decision.</p><p>Further, a farmer or rancher who fails to comply fully with the requirements to receive a loan may be eligible for equitable relief if the USDA determines the individual made a good faith effort to comply with the loan requirements.</p><p>The bill also</p><ul><li>directs USDA to establish an Office of the Legal Advisor for Civil Rights and Office of the Civil Rights Ombudsperson;</li><li>creates the required position of Assistant Secretary of Agriculture for Civil Rights (currently an optional USDA\u00a0position); and</li><li>allows the Assistant Secretary to grant relief, without prior approval, to farmers or ranchers who file certain civil rights complaints, including complaints\u00a0regarding direct farm ownership, operating, or emergency loans.</li></ul>",
      "updateDate": "2026-03-16",
      "versionCode": "id119hr3685"
    },
    "title": "JUST Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-06-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Just USDA Standards and Transparency Act of 2025 or the JUST Act of 2025</strong></p><p>This bill increases Department of Agriculture (USDA) oversight and enforcement of civil rights-related violations and actions.</p><p>USDA must take appropriate corrective action regarding any USDA official or employee who engages in certain discriminatory actions, retaliatory actions, harassment, or civil rights violations (e.g., failure to provide appropriate information regarding relevant USDA programs and services).\u00a0A corrective action (1) is any action that would enhance civil rights at USDA, including policy or programmatic changes; and (2) may include disciplinary actions (e.g., removal from federal service or a letter of reprimand).</p><p>The bill shifts the burden of proof from a farmer or rancher to USDA in an appeal to the USDA National Appeals Division. Specifically, USDA must prove by substantial evidence the validity of a USDA adverse decision.</p><p>Further, a farmer or rancher who fails to comply fully with the requirements to receive a loan may be eligible for equitable relief if the USDA determines the individual made a good faith effort to comply with the loan requirements.</p><p>The bill also</p><ul><li>directs USDA to establish an Office of the Legal Advisor for Civil Rights and Office of the Civil Rights Ombudsperson;</li><li>creates the required position of Assistant Secretary of Agriculture for Civil Rights (currently an optional USDA\u00a0position); and</li><li>allows the Assistant Secretary to grant relief, without prior approval, to farmers or ranchers who file certain civil rights complaints, including complaints\u00a0regarding direct farm ownership, operating, or emergency loans.</li></ul>",
      "updateDate": "2026-03-16",
      "versionCode": "id119hr3685"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3685ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "JUST Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-09T13:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "JUST Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-09T13:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Just USDA Standards and Transparency Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-09T13:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To enhance civil rights accountability and enforcement in the Department of Agriculture, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-09T13:18:22Z"
    }
  ]
}
```
