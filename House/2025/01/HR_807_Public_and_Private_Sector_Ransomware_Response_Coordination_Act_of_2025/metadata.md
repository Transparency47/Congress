# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/807?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/807
- Title: Public and Private Sector Ransomware Response Coordination Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 807
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2025-09-12T08:07:04Z
- Update date including text: 2025-09-12T08:07:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-01-28: Introduced in House

## Actions

- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/807",
    "number": "807",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "N000193",
        "district": "3",
        "firstName": "Zachary",
        "fullName": "Rep. Nunn, Zachary [R-IA-3]",
        "lastName": "Nunn",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Public and Private Sector Ransomware Response Coordination Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-12T08:07:04Z",
    "updateDateIncludingText": "2025-09-12T08:07:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-28",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-28",
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
          "date": "2025-01-28T16:06:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "NJ"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr807ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 807\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Mr. Nunn of Iowa (for himself and Mr. Gottheimer ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo direct the Secretary of the Treasury to submit a report on coordination in the public and private sectors in responding to ransomware attacks on financial institutions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Public and Private Sector Ransomware Response Coordination Act of 2025 .\n#### 2. Report on coordination in the public and private sectors in responding to ransomware attacks on financial institutions\n##### (a) In general\nNot later than one year after the date of the enactment of this section, the Secretary of the Treasury shall submit to the appropriate congressional committees a report that describes the following:\n**(1)**\nThe current level of coordination and collaboration between the public and private sectors, including entities in the public and private sectors that manage cybersecurity, in response to, and for the prevention of, a ransomware attack on a financial institution.\n**(2)**\nThe coordination among relevant governmental agencies in response to, and for the prevention of, a ransomware attack on a financial institution.\n**(3)**\nWhether relevant governmental agencies have timely access to relevant information reported by a financial institution following a ransomware attack on the financial institution.\n**(4)**\nThe utility of such information to any relevant governmental agency in the prevention or investigation of a ransomware attack on a financial institution, or the prosecution of a person responsible for such attack.\n**(5)**\nAn analysis of reporting requirements applicable to a financial institution with respect to a ransomware attack in relation to the utility to any relevant governmental agency of the reported information in the prevention or investigation of a ransomware attack on a financial institution, or the prosecution of a person responsible for such attack.\n**(6)**\nWhether further legislation is required to increase the utility and timely access of such information to any relevant governmental agency following a ransomware attack on a financial institution.\n**(7)**\nAny recommended policy initiatives to bolster public-private partnerships, increase incident report sharing, and decrease incident response time.\n**(8)**\nThe extent to which, and reasons that, financial institutions withhold or delay reporting to relevant governmental agencies information about a ransomware attack.\n**(9)**\nAny feedback on the contents of the report received from cybersecurity and ransomware response entities that provide services to financial institutions.\n##### (b) Form of report\nThe report described in subsection (a) shall be submitted in unclassified form, but may include a classified annex.\n##### (c) Briefing\nNot later than 15 months after the date of the enactment of this section, the Secretary of the Treasury shall brief the appropriate congressional committees on the findings of the report described in subsection (a).\n##### (d) Definitions\nIn this section:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Financial Services of the House of Representatives;\n**(B)**\nthe Permanent Select Committee on Intelligence of the House of Representatives;\n**(C)**\nthe Committee on Banking, Housing, and Urban Affairs of the Senate; and\n**(D)**\nthe Select Committee on Intelligence of the Senate.\n**(2) Cybersecurity and ransomware incident response entity**\nThe term cybersecurity and ransomware incident response entity means an entity that provides incident responses, managed services, or advisory services that\u2014\n**(A)**\nsupports investigation and risk management related to ransomware attacks in the public and private sectors;\n**(B)**\nstrengthens cybersecurity technology in the financial sector; and\n**(C)**\nreduces overall cyber risk in the financial sector by assessing the security posture of a financial institution, assisting a financial institution with regulatory compliance, and providing recommendations to a financial institution for recovery after a ransomware attack and prevention of any future attacks.\n**(3) Financial institution**\nThe term financial institution has the meaning given that term under section 5312(a) of title 31, United States Code.",
      "versionDate": "2025-01-28",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-03-03T17:18:50Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-28",
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
          "measure-id": "id119hr807",
          "measure-number": "807",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-28",
          "originChamber": "HOUSE",
          "update-date": "2025-05-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr807v00",
            "update-date": "2025-05-28"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Public and Private Sector Ransomware Response Coordination Act of 2025</strong></p><p>This bill requires the Department of the Treasury to report on the coordination between the public and private sectors and among government agencies in response to, and for the prevention of, a\u00a0ransomware attack on a financial institution.</p>"
        },
        "title": "Public and Private Sector Ransomware Response Coordination Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr807.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Public and Private Sector Ransomware Response Coordination Act of 2025</strong></p><p>This bill requires the Department of the Treasury to report on the coordination between the public and private sectors and among government agencies in response to, and for the prevention of, a\u00a0ransomware attack on a financial institution.</p>",
      "updateDate": "2025-05-28",
      "versionCode": "id119hr807"
    },
    "title": "Public and Private Sector Ransomware Response Coordination Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Public and Private Sector Ransomware Response Coordination Act of 2025</strong></p><p>This bill requires the Department of the Treasury to report on the coordination between the public and private sectors and among government agencies in response to, and for the prevention of, a\u00a0ransomware attack on a financial institution.</p>",
      "updateDate": "2025-05-28",
      "versionCode": "id119hr807"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr807ih.xml"
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
      "title": "Public and Private Sector Ransomware Response Coordination Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-26T11:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Public and Private Sector Ransomware Response Coordination Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T11:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of the Treasury to submit a report on coordination in the public and private sectors in responding to ransomware attacks on financial institutions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T11:18:27Z"
    }
  ]
}
```
