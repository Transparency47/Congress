# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1362?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1362
- Title: SAFE Supply Chains Act
- Congress: 119
- Bill type: S
- Bill number: 1362
- Origin chamber: Senate
- Introduced date: 2025-04-09
- Update date: 2026-01-14T05:17:41Z
- Update date including text: 2026-01-14T05:17:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-09: Introduced in Senate
- 2025-04-09 - IntroReferral: Introduced in Senate
- 2025-04-09 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-04-09: Introduced in Senate

## Actions

- 2025-04-09 - IntroReferral: Introduced in Senate
- 2025-04-09 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-09",
    "latestAction": {
      "actionDate": "2025-04-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1362",
    "number": "1362",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "SAFE Supply Chains Act",
    "type": "S",
    "updateDate": "2026-01-14T05:17:41Z",
    "updateDateIncludingText": "2026-01-14T05:17:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-09",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-09",
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
          "date": "2025-04-09T15:40:49Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1362is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1362\nIN THE SENATE OF THE UNITED STATES\nApril 9, 2025 Mr. Cornyn (for himself and Mr. Peters ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo require the Department of Defense to use information and communications technology products obtained from original equipment manufacturers or authorized resellers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Securing America\u2019s Federal Equipment Supply Chains Act or the SAFE Supply Chains Act .\n#### 2. Agency use of IT products\n##### (a) Definitions\nIn this section:\n**(1) Authorized reseller**\nThe term authorized reseller means a reseller, after market manufacturer, supplier, or distributor of a covered product with a direct or prime contractual arrangement with, or the express written authority of, the original equipment manufacturer of the covered product to manufacture, buy, stock, repackage, sell, resell, repair, service, otherwise support, or distribute the covered product.\n**(2) Covered product**\nThe term covered product \u2014\n**(A)**\nmeans an information and communications technology end-use hardware product or component, including software and firmware that comprise the end-use hardware product or component; and\n**(B)**\ndoes not include\u2014\n**(i)**\nother software; or\n**(ii)**\nan end-use hardware product\u2014\n**(I)**\nin which there is embedded information and communications technology; and\n**(II)**\nthe principal function of which is not the creation, manipulation, storage, display, receipt, or transmission of electronic data and information.\n**(3) End-use product**\nThe term end-use product means a product ready for use by the maintainer, integrator, or end user of the product.\n**(4) Information and communications technology**\nThe term information and communications technology \u2014\n**(A)**\nhas the meaning given the term in section 4713 of title 41, United States Code; and\n**(B)**\nincludes information and communications technologies covered by definitions contained in the Federal Acquisition Regulation, including definitions added after the date of the enactment of this Act by the Federal Acquisition Regulatory Council pursuant to notice and comment.\n**(5) Original equipment manufacturer**\nThe term original equipment manufacturer means a company that manufactures a covered product that the company\u2014\n**(A)**\ndesigned from self-sourced or purchased components; and\n**(B)**\nsells under the name of the company.\n##### (b) Prohibition on procurement and use\nSubject to subsection (c) and notwithstanding sections 1905 through 1907 of title 41, United States Code, the Secretary of Defense may not procure or obtain, renew a contract to procure or obtain, or use a covered product that is procured from an entity other than\u2014\n**(1)**\nan original equipment manufacturer; or\n**(2)**\nan authorized reseller.\n##### (c) Waiver\n**(1) In general**\nUpon notice to congressional defense committees, the Secretary of Defense may waive the prohibition under subsection (b) with respect to a covered product if the Secretary determines that procuring, obtaining, or using the covered product is necessary\u2014\n**(A)**\nfor the purpose of scientifically valid research (as defined in section 102 the Education Sciences Reform Act of 2002 ( 20 U.S.C. 9501 )); or\n**(B)**\nto avoid jeopardizing the performance of mission critical functions.\n**(2) Notice**\nThe notice described in paragraph (1)\u2014\n**(A)**\nshall\u2014\n**(i)**\nspecify, with respect to the waiver under paragraph (1)\u2014\n**(I)**\nthe justification for the waiver;\n**(II)**\nany security mitigations that have been implemented; and\n**(III)**\nwith respect to a waiver that necessitates a security mitigation, the plan of action and milestones to avoid future waivers for subsequent similar purchases;\n**(ii)**\nprovide a declaration that covered product is not being purchased from an entity that is under the influence or control of a foreign adversary; and\n**(iii)**\nbe submitted in an unclassified form; and\n**(B)**\nmay include a classified annex.\n**(3) Duration**\nWith respect to a waiver for the purpose of research, as described in paragraph (1)(A), the waiver shall be effective for the duration of the research identified in the waiver.\n##### (d) Vendor technical assistance\nThe Secretary of Defense shall establish procurement guidance to provide assistance to entities that are not eligible for procurements of covered products due to the prohibition under subsection (b) on the process of becoming an authorized reseller for covered products.\n##### (e) Reports to congress\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, and annually thereafter until the date that is 6 years after the date of enactment of this Act, the Secretary of Defense shall submit to the Committee on Armed Services of the Senate and the Committee on Armed Services of the House of Representatives a report that provides\u2014\n**(A)**\nthe number and types of covered products for which a waiver under subsection (c)(1) was granted during the 1-year period preceding the date of the submission of the report;\n**(B)**\nthe legal authority under which each waiver described in subparagraph (A) was granted, such as whether the waiver was granted pursuant to subparagraph (A) or (B) of subsection (c)(1); and\n**(C)**\nany actions taken by the Secretary to reduce the number of waivers issued by the Department of Defense under subsection (c)(1) with the goal of achieving full compliance with the prohibition under subsection (b).\n**(2) Classification of report**\nEach report submitted under this subsection\u2014\n**(A)**\nshall be submitted in unclassified form; and\n**(B)**\nmay include a classified annex that contains the information described in paragraph (1)(B).\n##### (f) No new funds\nNo additional amounts are authorized to be appropriated for the purpose of carrying out this Act.\n##### (g) Effective date\nThis section shall take effect on the date that is 1 year after the date of enactment of this Act.",
      "versionDate": "2025-04-09",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-04-09",
        "text": "Referred to the House Committee on Armed Services."
      },
      "number": "2765",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "SAFE Supply Chains Act",
      "type": "HR"
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-22T01:22:50Z"
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
      "date": "2025-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1362is.xml"
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
      "title": "SAFE Supply Chains Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-25T03:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SAFE Supply Chains Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-25T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Securing America\u2019s Federal Equipment Supply Chains Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-25T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Department of Defense to use information and communications technology products obtained from original equipment manufacturers or authorized resellers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-25T03:18:16Z"
    }
  ]
}
```
