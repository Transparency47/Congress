# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3700?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3700
- Title: MEALS Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3700
- Origin chamber: House
- Introduced date: 2025-06-04
- Update date: 2025-07-21T19:44:15Z
- Update date including text: 2025-07-21T19:44:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-04: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-06-04: Introduced in House

## Actions

- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-04",
    "latestAction": {
      "actionDate": "2025-06-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3700",
    "number": "3700",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "B001278",
        "district": "1",
        "firstName": "Suzanne",
        "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
        "lastName": "Bonamici",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "MEALS Act of 2025",
    "type": "HR",
    "updateDate": "2025-07-21T19:44:15Z",
    "updateDateIncludingText": "2025-07-21T19:44:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-04",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-04",
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
          "date": "2025-06-04T14:06:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3700ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3700\nIN THE HOUSE OF REPRESENTATIVES\nJune 4, 2025 Ms. Bonamici (for herself and Mr. Goldman of New York ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Richard B. Russell National School Lunch Act to require certain State agencies and covered Indian Tribal organizations to replace summer EBT benefits that are determined to have been stolen, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Mitigating Electronic Access Losses for Students Act of 2025 or the MEALS Act of 2025 .\n#### 2. Summer EBT fraud prevention\nSection 13A of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1762 ) is amended\u2014\n**(1)**\nby redesignating subsection (h) as subsection (i); and\n**(2)**\nby inserting after subsection (g) the following:\n(h) Summer EBT fraud prevention (1) Guidance; rulemaking The Secretary shall\u2014 (A) issue guidance to State agencies and covered Indian Tribal organizations, on an ongoing basis, as informed by the process outlined in subparagraph (D), that describes security measures that\u2014 (i) are effective, as determined by the Secretary, in detecting and preventing theft of summer EBT benefits, including through card skimming, card cloning, and other similar fraudulent methods; (ii) are consistent with industry standards for detecting, identifying, and preventing debit and credit card skimming, card cloning, and other similar fraudulent methods; and (iii) consider the feasibility of cost, availability, and implementation for State agencies and covered Indian Tribal organizations; (B) promulgate regulations through notice-and-comment rulemaking to require State agencies and covered Indian Tribal organizations that elect to participate in the program under this section to take the appropriate security measures, as determined by the Secretary, described in the guidance issued under subparagraph (A); (C) not later than 1 year after the date of enactment of this subsection, promulgate regulations (including an interim final rule) to require State agencies and covered Indian Tribal organizations that elect to participate in the program under this section to implement procedures for the replacement of summer EBT benefits consistent with paragraph (2); (D) coordinate with the Director of the Office of Family Assistance of the Administration for Children and Families of the Department of Health and Human Services, the Attorney General of the United States, State agencies, covered Indian Tribal organizations, retailers (including retail food stores described in subparagraph (A) of subsection (b)(1) and vendors described in subparagraph (B) of such subsection), and EBT contractors\u2014 (i) to determine\u2014 (I) how summer EBT benefits are being stolen through card skimming, card cloning, and other similar fraudulent methods; (II) how those stolen benefits are used; and (III) the locations where card skimming, card cloning, and other similar fraudulent methods are taking place; (ii) to establish measures, including equipment enhancements for retail food stores described in subparagraph (A) of subsection (b)(1) and vendors described in subparagraph (B) of such subsection, to prevent summer EBT benefits from being stolen through card skimming, card cloning, and other similar fraudulent methods; and (iii) to establish standard reporting methods for State agencies and covered Indian Tribal organizations that elect to participate in the program under this section to collect and share data with the Secretary on the scope of summer EBT benefits being stolen through card skimming, card cloning, and other similar fraudulent methods; and (E) not later than 2 years after the date of enactment of this subsection, submit to the Committee on Agriculture, Nutrition, and Forestry of the Senate and the Committee on Education and Workforce of the House of Representatives a report that includes\u2014 (i) information on the frequency of theft of summer EBT benefits and the location of those thefts, including benefits stolen through card skimming, card cloning, and other similar fraudulent methods; (ii) a description of the determinations made under subparagraph (D)(i), the measures established under subparagraph (D)(ii), and methods established in subparagraph (D)(iii); (iii) a description of the industry standards described in subparagraph (A)(ii); (iv) a comparison of State agency and covered Indian Tribal organization plans related to reimbursement, prevention, and other relevant procedures approved in accordance with paragraph (2)(A)(i); and (v) a description of actions taken by the Secretary, and actions the Secretary plans to take, to detect and prevent theft of summer EBT benefits, including benefits stolen through card skimming, card cloning, and other similar fraudulent methods. (2) Replacement of benefits (A) In general The Secretary shall use funds appropriated pursuant to this section to require State agencies and covered Indian Tribal organizations that elect to participate in the program under this section to replace summer EBT benefits that are determined by the State agency or covered Indian Tribal organization to have been stolen through card skimming, card cloning, or similar fraudulent methods, subject to the conditions that\u2014 (i) the State agency or covered Indian Tribal organization shall include as part of each plan for operations and management of the State agency or covered Indian Tribal organization required under section 292.8 of title 7, Code of Federal Regulations (or a successor regulation), and submitted after the date of enactment of this Act a plan for the replacement of stolen summer EBT benefits that\u2014 (I) includes appropriate procedures, as determined by the Secretary, for the timely submission of claims to, timely validation of claims by, and replacement issuance by the State agency or covered Indian Tribal organization that includes\u2014 (aa) a signed statement by the affected eligible household on the benefit theft, consistent with the signature requirements and options, including electronic signatures, provided by section 11(e)(2)(C) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2020(e)(2)(C) ); (bb) criteria to determine if a submitted claim is valid; (cc) procedures for the documentation of replacement issuances, including the submitted claims and findings from the validation; (dd) the submission of data reports on benefit theft and replacement activity to the Secretary; (ee) procedures to inform eligible households of their right to appeal an adverse decision regarding a submitted claim; and (ff) the State agency\u2019s or covered Indian Tribal organization\u2019s use and planned use of benefit theft prevention measures, including any additional guidance that may be issued under subsection (h)(1); (II) includes appropriate procedures, as determined by the Secretary, for reporting the scope and frequency of card skimming affecting eligible households to the Secretary; and (III) includes appropriate procedures, as determined by the Secretary, in the case of theft involving a card or other account that stores summer EBT benefits and other benefits (including supplemental nutrition assistance program benefits), for determining, to the extent possible, the total portion of stolen benefits that is attributable to summer EBT benefits; and (ii) the replacement of stolen summer EBT benefits for an eligible household shall not exceed the lesser of\u2014 (I) the amount of summer EBT benefits stolen from the eligible household\u2014 (aa) during the calendar year that the claim reporting such theft was submitted; and (bb) that have not been replaced or otherwise supplemented by a prior approved claim; or (II) the amount equal to the summer EBT benefit allotment of the eligible household issued to the eligible household immediately prior to the date on which the benefits were stolen. (B) Plan deadline for current participants In the case of a State agency or covered Indian Tribal organization participating in the program under this section on the date of enactment of this subsection, such State Agency or covered Indian Tribal organization shall be required to\u2014 (i) submit an initial version of the plan for the replacement of stolen summer EBT benefits described in subparagraph (A)(i) to the Secretary for approval not later than 60 days after the date of enactment of this subsection; and (ii) implement such initial plan upon approval by the Secretary. (3) Comptroller General (A) In general Not later than 2 years after the date of enactment of this subsection, the Comptroller General of the United States shall submit to the Committee on Education and Workforce of the House of Representatives and the Committee on Agriculture, Nutrition, and Forestry of the Senate a report that examines risks related to summer EBT benefit payment system security, including the risk of stolen benefits through card skimming, card cloning, and other similar methods. (B) Contents The report under subparagraph (A) shall include an assessment of\u2014 (i) the extent to which the Department of Agriculture manages summer EBT benefit payment system security, including risks related to stolen benefits, compared to leading industry practices; (ii) the manner in which State agencies, covered Indian Tribal organizations, retailers, and other relevant entities manage risks related to stolen summer EBT benefits; (iii) the oversight of and guidance provided by the Secretary to State agencies and covered Indian Tribal organizations regarding stolen summer EBT benefits; and (iv) recommendations and policy options for\u2014 (I) improving how the Department of Agriculture and other relevant entities manage summer EBT benefit payment system security risks, including those related to stolen benefits; and (II) how the Department of Agriculture may best share those improvements with State agencies, covered Indian Tribal organizations, retailers, and other relevant entities. .",
      "versionDate": "2025-06-04",
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
        "updateDate": "2025-07-11T17:27:07Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-04",
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
          "measure-id": "id119hr3700",
          "measure-number": "3700",
          "measure-type": "hr",
          "orig-publish-date": "2025-06-04",
          "originChamber": "HOUSE",
          "update-date": "2026-05-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3700v00",
            "update-date": "2026-05-07"
          },
          "action-date": "2025-06-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Mitigating Electronic Access Losses for Students Act of 2025 or the MEALS Act of 2025</strong></p><p>This bill requires the Food and Nutrition Service (FNS) to prescribe fraud prevention measures for the\u00a0Summer Electronic Benefits Transfer (or Summer\u00a0EBT) program and provide for the replacement of the full amount of a student's stolen benefits. Summer EBT provides electronic benefits that can be redeemed for groceries to households with eligible children over the summer months.</p><p>Specifically, using funds provided by FNS, a participating state agency must provide a household with replacement Summer\u00a0EBT benefits\u00a0if the state agency determines that the benefits were stolen, and the agency meets certain requirements. The benefits must be equal to the amount of benefits stolen through card skimming, card cloning, or similar fraudulent methods.</p><p>Further, for state agencies and Indian tribal organizations\u00a0that administer the Summer EBT program, FNS must</p><ul><li>issue\u00a0guidance on security measures that are effective in detecting and preventing\u00a0the theft of benefits (e.g., through card skimming or card cloning), and</li><li>promulgate\u00a0regulations to require them to take the appropriate security measures and\u00a0implement procedures for the replacement of benefits.</li></ul><p>In addition, FNS must\u00a0coordinate with the Department of Justice and the Department of Health and Human Services to\u00a0establish (1) measures to prevent Summer EBT benefits from being stolen, and (2) standard reporting methods.</p><p>Finally, the Government Accountability Office must submit a report to Congress that examines the risks related to Summer\u00a0EBT benefit payment system security.</p>"
        },
        "title": "MEALS Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3700.xml",
    "summary": {
      "actionDate": "2025-06-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Mitigating Electronic Access Losses for Students Act of 2025 or the MEALS Act of 2025</strong></p><p>This bill requires the Food and Nutrition Service (FNS) to prescribe fraud prevention measures for the\u00a0Summer Electronic Benefits Transfer (or Summer\u00a0EBT) program and provide for the replacement of the full amount of a student's stolen benefits. Summer EBT provides electronic benefits that can be redeemed for groceries to households with eligible children over the summer months.</p><p>Specifically, using funds provided by FNS, a participating state agency must provide a household with replacement Summer\u00a0EBT benefits\u00a0if the state agency determines that the benefits were stolen, and the agency meets certain requirements. The benefits must be equal to the amount of benefits stolen through card skimming, card cloning, or similar fraudulent methods.</p><p>Further, for state agencies and Indian tribal organizations\u00a0that administer the Summer EBT program, FNS must</p><ul><li>issue\u00a0guidance on security measures that are effective in detecting and preventing\u00a0the theft of benefits (e.g., through card skimming or card cloning), and</li><li>promulgate\u00a0regulations to require them to take the appropriate security measures and\u00a0implement procedures for the replacement of benefits.</li></ul><p>In addition, FNS must\u00a0coordinate with the Department of Justice and the Department of Health and Human Services to\u00a0establish (1) measures to prevent Summer EBT benefits from being stolen, and (2) standard reporting methods.</p><p>Finally, the Government Accountability Office must submit a report to Congress that examines the risks related to Summer\u00a0EBT benefit payment system security.</p>",
      "updateDate": "2026-05-07",
      "versionCode": "id119hr3700"
    },
    "title": "MEALS Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-06-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Mitigating Electronic Access Losses for Students Act of 2025 or the MEALS Act of 2025</strong></p><p>This bill requires the Food and Nutrition Service (FNS) to prescribe fraud prevention measures for the\u00a0Summer Electronic Benefits Transfer (or Summer\u00a0EBT) program and provide for the replacement of the full amount of a student's stolen benefits. Summer EBT provides electronic benefits that can be redeemed for groceries to households with eligible children over the summer months.</p><p>Specifically, using funds provided by FNS, a participating state agency must provide a household with replacement Summer\u00a0EBT benefits\u00a0if the state agency determines that the benefits were stolen, and the agency meets certain requirements. The benefits must be equal to the amount of benefits stolen through card skimming, card cloning, or similar fraudulent methods.</p><p>Further, for state agencies and Indian tribal organizations\u00a0that administer the Summer EBT program, FNS must</p><ul><li>issue\u00a0guidance on security measures that are effective in detecting and preventing\u00a0the theft of benefits (e.g., through card skimming or card cloning), and</li><li>promulgate\u00a0regulations to require them to take the appropriate security measures and\u00a0implement procedures for the replacement of benefits.</li></ul><p>In addition, FNS must\u00a0coordinate with the Department of Justice and the Department of Health and Human Services to\u00a0establish (1) measures to prevent Summer EBT benefits from being stolen, and (2) standard reporting methods.</p><p>Finally, the Government Accountability Office must submit a report to Congress that examines the risks related to Summer\u00a0EBT benefit payment system security.</p>",
      "updateDate": "2026-05-07",
      "versionCode": "id119hr3700"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3700ih.xml"
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
      "title": "MEALS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-09T13:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "MEALS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-09T13:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Mitigating Electronic Access Losses for Students Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-09T13:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Richard B. Russell National School Lunch Act to require certain State agencies and covered Indian Tribal organizations to replace summer EBT benefits that are determined to have been stolen, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-09T13:18:21Z"
    }
  ]
}
```
