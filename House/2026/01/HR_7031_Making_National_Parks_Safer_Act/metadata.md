# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7031?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7031
- Title: Making National Parks Safer Act
- Congress: 119
- Bill type: HR
- Bill number: 7031
- Origin chamber: House
- Introduced date: 2026-01-13
- Update date: 2026-04-13T12:10:14Z
- Update date including text: 2026-04-13T12:10:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-01-13: Introduced in House
- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-03-11 - Committee: Referred to the Subcommittee on Federal Lands.
- 2026-03-18 - Committee: Subcommittee Hearings Held
- Latest action: 2026-01-13: Introduced in House

## Actions

- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-03-11 - Committee: Referred to the Subcommittee on Federal Lands.
- 2026-03-18 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-13",
    "latestAction": {
      "actionDate": "2026-01-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7031",
    "number": "7031",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "F000469",
        "district": "1",
        "firstName": "Russ",
        "fullName": "Rep. Fulcher, Russ [R-ID-1]",
        "lastName": "Fulcher",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "Making National Parks Safer Act",
    "type": "HR",
    "updateDate": "2026-04-13T12:10:14Z",
    "updateDateIncludingText": "2026-04-13T12:10:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-11",
      "committees": {
        "item": {
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Federal Lands.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-13",
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
          "date": "2026-01-13T15:02:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-03-18T14:00:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-03-11T14:00:00Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
        }
      },
      "systemCode": "hsii00",
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
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7031ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7031\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 13, 2026 Mr. Fulcher introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo direct the Secretary of the Interior to upgrade existing emergency communications centers in units of the National Park System to Next Generation 9\u20131\u20131 systems, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Making National Parks Safer Act .\n#### 2. Definitions\nIn this Act:\n**(1) Appropriate committees of congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Energy and Natural Resources of the Senate; and\n**(B)**\nthe Committee on Natural Resources of the House of Representatives.\n**(2) Emergency communications center**\n**(A) In general**\nThe term emergency communications center means\u2014\n**(i)**\na facility that\u2014\n**(I)**\nis designated to receive a 9\u20131\u20131 request for emergency assistance; and\n**(II)**\nperforms 1 or more of the functions described in subparagraph (B); or\n**(ii)**\na public safety answering point (as defined in section 222 of the Communications Act of 1934 ( 47 U.S.C. 222 )).\n**(B) Functions described**\nThe functions described in this subparagraph are the following:\n**(i)**\nProcessing and analyzing 9\u20131\u20131 requests for emergency assistance and information and data related to the requests.\n**(ii)**\nDispatching appropriate emergency response providers.\n**(iii)**\nTransferring or exchanging 9\u20131\u20131 requests for emergency assistance and information and data related to the requests with 1 or more other emergency communications centers and emergency response providers.\n**(iv)**\nAnalyzing any communications received from emergency response providers.\n**(v)**\nSupporting incident command functions.\n**(3) Interoperability**\nThe term interoperability means the capability of emergency communications centers\u2014\n**(A)**\nto receive 9\u20131\u20131 requests for emergency assistance and information and data related to the requests, such as location information and callback numbers from a person initiating the request; and\n**(B)**\nto process and share 9\u20131\u20131 requests for emergency assistance and information and data related to the requests with other emergency communications centers and emergency response providers without the need for proprietary interfaces and regardless of jurisdiction, equipment, device, software, service provider, or other relevant factors.\n**(4) Next Generation 9\u20131\u20131 system**\nThe term Next Generation 9\u20131\u20131 system has the meaning given the term Next Generation 911 in section 9.28 of title 47, Code of Federal Regulations (or a successor regulation).\n**(5) Secretary**\nThe term Secretary means the Secretary of the Interior, acting through the Director of the National Park Service.\n#### 3. Assessment of emergency communications centers located in units of the National Park System\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Secretary shall complete an assessment of emergency communications centers located in units of the National Park System to identify\u2014\n**(1)**\nthe implementation status of Next Generation 9\u20131\u20131 systems at existing emergency communications centers in units of the National Park System;\n**(2)**\nestimated costs to purchase Next Generation 9\u20131\u20131 systems for emergency communications centers in units of the National Park System that have not begun to implement Next Generation 9\u20131\u20131 systems; and\n**(3)**\nestimated costs to maintain and operate Next Generation 9\u20131\u20131 systems across all emergency communications centers in units of the National Park System.\n##### (b) Report\nOn completion of the assessment under subsection (a), the Secretary shall submit to the appropriate committees of Congress, and make available on the website of the Department of the Interior, a report\u2014\n**(1)**\ndescribing the results of the assessment; and\n**(2)**\nidentifying issues that may affect the implementation of Next Generation 9\u20131\u20131 systems across all emergency communications centers in units of the National Park System, including\u2014\n**(A)**\njurisdictional issues;\n**(B)**\ntechnological issues;\n**(C)**\nissues relating to relevant authorities; and\n**(D)**\nissues relating to legal agreements.\n#### 4. Plan to install Next Generation 9\u20131\u20131 systems in units of the National Park System\n##### (a) In general\nNot later than 1 year after the date on which the report under section 3(b) is submitted, the Secretary shall develop a plan, based on the results of the assessment completed under section 3(a) and subject to subsection (c), to install Next Generation 9\u20131\u20131 systems at identified emergency communications centers in units of the National Park System.\n##### (b) Consultation\nIn developing the plan under subsection (a), the Secretary shall consult with\u2014\n**(1)**\nState and local emergency operations officials to ensure interoperability of the Next Generation 9\u20131\u20131 systems;\n**(2)**\nState and local stakeholders that the superintendent of the applicable unit of the National Park System determines to be appropriate; and\n**(3)**\nrelevant Federal agencies, including\u2014\n**(A)**\nthe Department of Commerce;\n**(B)**\nthe Department of Transportation; and\n**(C)**\nthe Federal Communications Commission.\n##### (c) Limitation\nNotwithstanding subsection (a), a plan developed under that subsection shall not be required to address emergency communications centers in any unit of the National Park System at which the superintendent of the unit of the National Park System determines that sufficient Next Generation 9\u20131\u20131 systems have already been installed or are being installed, as applicable.",
      "versionDate": "2026-01-13",
      "versionType": "Introduced in House"
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
        "actionDate": "2026-02-04",
        "text": "Committee on Energy and Natural Resources. Ordered to be reported without amendment favorably."
      },
      "number": "290",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Making National Parks Safer Act",
      "type": "S"
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
            "updateDate": "2026-03-30T18:17:27Z"
          },
          {
            "name": "Emergency communications systems",
            "updateDate": "2026-03-30T18:17:11Z"
          },
          {
            "name": "First responders and emergency personnel",
            "updateDate": "2026-03-30T18:17:15Z"
          },
          {
            "name": "Parks, recreation areas, trails",
            "updateDate": "2026-03-30T18:17:20Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2026-01-22T20:48:29Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-01-13",
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
          "measure-id": "id119hr7031",
          "measure-number": "7031",
          "measure-type": "hr",
          "orig-publish-date": "2026-01-13",
          "originChamber": "HOUSE",
          "update-date": "2026-04-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr7031v00",
            "update-date": "2026-04-13"
          },
          "action-date": "2026-01-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Making National Parks Safer Act</strong></p><p>This bill directs the National Park Service (NPS) to develop a plan to install Next Generation 911 (NG911) systems, which are certain interoperable, digital, and secure Internet Protocol-based systems for receiving 9-1-1 calls.\u00a0</p><p>Specifically, the NPS must assess the implementation status and estimated costs of such NG911 systems at existing emergency communications centers in NPS units. The NPS must also develop a plan, based on the assessment, to install NG911 systems at centers.</p>"
        },
        "title": "Making National Parks Safer Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr7031.xml",
    "summary": {
      "actionDate": "2026-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Making National Parks Safer Act</strong></p><p>This bill directs the National Park Service (NPS) to develop a plan to install Next Generation 911 (NG911) systems, which are certain interoperable, digital, and secure Internet Protocol-based systems for receiving 9-1-1 calls.\u00a0</p><p>Specifically, the NPS must assess the implementation status and estimated costs of such NG911 systems at existing emergency communications centers in NPS units. The NPS must also develop a plan, based on the assessment, to install NG911 systems at centers.</p>",
      "updateDate": "2026-04-13",
      "versionCode": "id119hr7031"
    },
    "title": "Making National Parks Safer Act"
  },
  "summaries": [
    {
      "actionDate": "2026-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Making National Parks Safer Act</strong></p><p>This bill directs the National Park Service (NPS) to develop a plan to install Next Generation 911 (NG911) systems, which are certain interoperable, digital, and secure Internet Protocol-based systems for receiving 9-1-1 calls.\u00a0</p><p>Specifically, the NPS must assess the implementation status and estimated costs of such NG911 systems at existing emergency communications centers in NPS units. The NPS must also develop a plan, based on the assessment, to install NG911 systems at centers.</p>",
      "updateDate": "2026-04-13",
      "versionCode": "id119hr7031"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7031ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of the Interior to upgrade existing emergency communications centers in units of the National Park System to Next Generation 9-1-1 systems, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-22T14:18:26Z"
    },
    {
      "title": "Making National Parks Safer Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-22T14:14:38Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Making National Parks Safer Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-22T14:14:38Z"
    }
  ]
}
```
