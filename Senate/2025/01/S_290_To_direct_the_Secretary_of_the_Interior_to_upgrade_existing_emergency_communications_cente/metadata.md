# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/290?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/290
- Title: Making National Parks Safer Act
- Congress: 119
- Bill type: S
- Bill number: 290
- Origin chamber: Senate
- Introduced date: 2025-01-29
- Update date: 2026-04-10T23:28:44Z
- Update date including text: 2026-04-10T23:28:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-29: Introduced in Senate
- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S481-482)
- 2025-12-09 - Committee: Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.
- 2026-02-04 - Committee: Committee on Energy and Natural Resources. Ordered to be reported without amendment favorably.
- Latest action: 2025-01-29: Introduced in Senate

## Actions

- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S481-482)
- 2025-12-09 - Committee: Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.
- 2026-02-04 - Committee: Committee on Energy and Natural Resources. Ordered to be reported without amendment favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-29",
    "latestAction": {
      "actionDate": "2025-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/290",
    "number": "290",
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
    "title": "Making National Parks Safer Act",
    "type": "S",
    "updateDate": "2026-04-10T23:28:44Z",
    "updateDateIncludingText": "2026-04-10T23:28:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-04",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-09",
      "committees": {
        "item": {
          "name": "National Parks Subcommittee",
          "systemCode": "sseg04"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-29",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S481-482)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-29",
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
        "item": [
          {
            "date": "2026-02-04T22:03:57Z",
            "name": "Markup By"
          },
          {
            "date": "2025-01-29T17:37:24Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-09T18:12:37Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "National Parks Subcommittee",
          "systemCode": "sseg04"
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
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-01-29",
      "state": "ME"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-01-29",
      "state": "CO"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s290is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 290\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2025 Mr. Barrasso (for himself, Mr. King , Mr. Hickenlooper , and Mrs. Hyde-Smith ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources -\nA BILL\nTo direct the Secretary of the Interior to upgrade existing emergency communications centers in units of the National Park System to Next Generation 9\u20131\u20131 systems, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Making National Parks Safer Act .\n#### 2. Definitions\nIn this Act:\n**(1) Appropriate committees of congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Energy and Natural Resources of the Senate; and\n**(B)**\nthe Committee on Natural Resources of the House of Representatives.\n**(2) Emergency communications center**\n**(A) In general**\nThe term emergency communications center means\u2014\n**(i)**\na facility that\u2014\n**(I)**\nis designated to receive a 9\u20131\u20131 request for emergency assistance; and\n**(II)**\nperforms 1 or more of the functions described in subparagraph (B); or\n**(ii)**\na public safety answering point (as defined in section 222 of the Communications Act of 1934 ( 47 U.S.C. 222 )).\n**(B) Functions described**\nThe functions described in this subparagraph are the following:\n**(i)**\nProcessing and analyzing 9\u20131\u20131 requests for emergency assistance and information and data related to the requests.\n**(ii)**\nDispatching appropriate emergency response providers.\n**(iii)**\nTransferring or exchanging 9\u20131\u20131 requests for emergency assistance and information and data related to the requests with 1 or more other emergency communications centers and emergency response providers.\n**(iv)**\nAnalyzing any communications received from emergency response providers.\n**(v)**\nSupporting incident command functions.\n**(3) Interoperability**\nThe term interoperability means the capability of emergency communications centers\u2014\n**(A)**\nto receive 9\u20131\u20131 requests for emergency assistance and information and data related to the requests, such as location information and callback numbers from a person initiating the request; and\n**(B)**\nto process and share 9\u20131\u20131 requests for emergency assistance and information and data related to the requests with other emergency communications centers and emergency response providers without the need for proprietary interfaces and regardless of jurisdiction, equipment, device, software, service provider, or other relevant factors.\n**(4) Next Generation 9\u20131\u20131 system**\nThe term Next Generation 9\u20131\u20131 system has the meaning given the term Next Generation 911 in section 9.28 of title 47, Code of Federal Regulations (or a successor regulation).\n**(5) Secretary**\nThe term Secretary means the Secretary of the Interior, acting through the Director of the National Park Service.\n#### 3. Assessment of emergency communications centers located in units of the National Park System\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Secretary shall complete an assessment of emergency communications centers located in units of the National Park System to identify\u2014\n**(1)**\nthe implementation status of Next Generation 9\u20131\u20131 systems at existing emergency communications centers in units of the National Park System;\n**(2)**\nestimated costs to purchase Next Generation 9\u20131\u20131 systems for emergency communications centers in units of the National Park System that have not begun to implement Next Generation 9\u20131\u20131 systems; and\n**(3)**\nestimated costs to maintain and operate Next Generation 9\u20131\u20131 systems across all emergency communications centers in units of the National Park System.\n##### (b) Report\nOn completion of the assessment under subsection (a), the Secretary shall submit to the appropriate committees of Congress, and make available on the website of the Department of the Interior, a report\u2014\n**(1)**\ndescribing the results of the assessment; and\n**(2)**\nidentifying issues that may affect the implementation of Next Generation 9\u20131\u20131 systems across all emergency communications centers in units of the National Park System, including\u2014\n**(A)**\njurisdictional issues;\n**(B)**\ntechnological issues;\n**(C)**\nissues relating to relevant authorities; and\n**(D)**\nissues relating to legal agreements.\n#### 4. Plan to install Next Generation 9\u20131\u20131 systems in units of the National Park System\n##### (a) In general\nNot later than 1 year after the date on which the report under section 3(b) is submitted, the Secretary shall develop a plan, based on the results of the assessment completed under section 3(a) and subject to subsection (c), to install Next Generation 9\u20131\u20131 systems at identified emergency communications centers in units of the National Park System.\n##### (b) Consultation\nIn developing the plan under subsection (a), the Secretary shall consult with\u2014\n**(1)**\nState and local emergency operations officials to ensure interoperability of the Next Generation 9\u20131\u20131 systems;\n**(2)**\nState and local stakeholders that the superintendent of the applicable unit of the National Park System determines to be appropriate; and\n**(3)**\nrelevant Federal agencies, including\u2014\n**(A)**\nthe Department of Commerce;\n**(B)**\nthe Department of Transportation; and\n**(C)**\nthe Federal Communications Commission.\n##### (c) Limitation\nNotwithstanding subsection (a), a plan developed under that subsection shall not be required to address emergency communications centers in any unit of the National Park System at which the superintendent of the unit of the National Park System determines that sufficient Next Generation 9\u20131\u20131 systems have already been installed or are being installed, as applicable.",
      "versionDate": "2025-01-29",
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
        "actionDate": "2026-03-18",
        "text": "Subcommittee Hearings Held"
      },
      "number": "7031",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Making National Parks Safer Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2025-09-29T14:09:12Z"
          },
          {
            "name": "Emergency communications systems",
            "updateDate": "2025-09-29T14:09:17Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-09-29T14:09:23Z"
          },
          {
            "name": "Parks, recreation areas, trails",
            "updateDate": "2025-09-29T14:09:07Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-01T20:17:58Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-29",
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
          "measure-id": "id119s290",
          "measure-number": "290",
          "measure-type": "s",
          "orig-publish-date": "2025-01-29",
          "originChamber": "SENATE",
          "update-date": "2026-02-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s290v00",
            "update-date": "2026-02-10"
          },
          "action-date": "2025-01-29",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Making National Parks Safer Act</strong></p><p>This bill directs the National Park Service (NPS) to develop a plan to install Next Generation 911 (NG911) systems, which are certain interoperable, digital, and secure Internet Protocol-based systems for receiving 9-1-1 calls.\u00a0</p><p>Specifically, the NPS must assess the implementation status and estimated costs of such NG911 systems at existing emergency communications centers in NPS units. The NPS must also develop a plan, based on the assessment, to install NG911 systems at centers.</p>"
        },
        "title": "Making National Parks Safer Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s290.xml",
    "summary": {
      "actionDate": "2025-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Making National Parks Safer Act</strong></p><p>This bill directs the National Park Service (NPS) to develop a plan to install Next Generation 911 (NG911) systems, which are certain interoperable, digital, and secure Internet Protocol-based systems for receiving 9-1-1 calls.\u00a0</p><p>Specifically, the NPS must assess the implementation status and estimated costs of such NG911 systems at existing emergency communications centers in NPS units. The NPS must also develop a plan, based on the assessment, to install NG911 systems at centers.</p>",
      "updateDate": "2026-02-10",
      "versionCode": "id119s290"
    },
    "title": "Making National Parks Safer Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Making National Parks Safer Act</strong></p><p>This bill directs the National Park Service (NPS) to develop a plan to install Next Generation 911 (NG911) systems, which are certain interoperable, digital, and secure Internet Protocol-based systems for receiving 9-1-1 calls.\u00a0</p><p>Specifically, the NPS must assess the implementation status and estimated costs of such NG911 systems at existing emergency communications centers in NPS units. The NPS must also develop a plan, based on the assessment, to install NG911 systems at centers.</p>",
      "updateDate": "2026-02-10",
      "versionCode": "id119s290"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s290is.xml"
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
      "title": "Making National Parks Safer Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-05T12:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Making National Parks Safer Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-04T12:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Secretary of the Interior to upgrade existing emergency communications centers in units of the National Park System to Next Generation 9-1-1 systems, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-04T12:48:24Z"
    }
  ]
}
```
