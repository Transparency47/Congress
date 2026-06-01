# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/590?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/590
- Title: _______ Act of 2024
- Congress: 119
- Bill type: HR
- Bill number: 590
- Origin chamber: House
- Introduced date: 2025-01-21
- Update date: 2025-09-09T08:05:38Z
- Update date including text: 2025-09-09T08:05:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-21: Introduced in House
- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-01-21: Introduced in House

## Actions

- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-21",
    "latestAction": {
      "actionDate": "2025-01-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/590",
    "number": "590",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001207",
        "district": "11",
        "firstName": "Mikie",
        "fullName": "Rep. Sherrill, Mikie [D-NJ-11]",
        "lastName": "Sherrill",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "_______ Act of 2024",
    "type": "HR",
    "updateDate": "2025-09-09T08:05:38Z",
    "updateDateIncludingText": "2025-09-09T08:05:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-21",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-21",
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
          "date": "2025-01-21T17:02:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "DC"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr590ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 590\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 21, 2025 Ms. Sherrill introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo amend title 32, United States Code, to clarify certain limitations on full-time National Guard duty performed in a State, Territory, or the District of Columbia, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the _______ Act of 2024 .\n#### 2. Requirement of consent of the chief executive officer for certain full-time National Guard duty performed in a State, Territory, or the District of Columbia\nSubsection (f) of section 502 of title 32, United States Code, is amended\u2014\n**(1)**\nin paragraph (1), by striking Under and inserting Subject to paragraph (2) and under ;\n**(2)**\nin paragraph (2), by striking subsection (A) and inserting the following:\n(A) Support of operations or missions undertaken by the member's unit at the request of the President or Secretary of Defense, with the consent of\u2014 (i) the chief executive officer of each State (as that term is defined in section 901 of this title) in which such operations or missions shall take place; and (ii) if such operations or missions shall take place in the District of Columbia, the Mayor of the District of Columbia. ; and\n**(3)**\nby adding at the end the following new paragraph:\n(3) The training or duty ordered to be performed under paragraph (1) shall be subject to the limitations of section 1385 of title 18, commonly referred to as the Posse Comitatus Act . .",
      "versionDate": "2025-01-21",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Federal officials",
            "updateDate": "2025-05-09T20:09:11Z"
          },
          {
            "name": "National Guard and reserves",
            "updateDate": "2025-05-09T20:09:06Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-01T21:28:33Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-21",
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
          "measure-id": "id119hr590",
          "measure-number": "590",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-21",
          "originChamber": "HOUSE",
          "update-date": "2025-06-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr590v00",
            "update-date": "2025-06-13"
          },
          "action-date": "2025-01-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong></strong>This bill requires the consent of the chief executive officers (e.g., governors) of involved states when the President or Department of Defense orders National Guard units to perform training or other duty in such states. Under the bill, the term <em>state</em>\u00a0includes the District of Columbia and territories or possessions of the United States. The bill also subjects the ordered training or duty to the limitations of the Posse Comitatus Act of 1878, which prohibits the use of the military for civil law enforcement purposes.</p>"
        },
        "title": "_______ Act of 2024"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr590.xml",
    "summary": {
      "actionDate": "2025-01-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong></strong>This bill requires the consent of the chief executive officers (e.g., governors) of involved states when the President or Department of Defense orders National Guard units to perform training or other duty in such states. Under the bill, the term <em>state</em>\u00a0includes the District of Columbia and territories or possessions of the United States. The bill also subjects the ordered training or duty to the limitations of the Posse Comitatus Act of 1878, which prohibits the use of the military for civil law enforcement purposes.</p>",
      "updateDate": "2025-06-13",
      "versionCode": "id119hr590"
    },
    "title": "_______ Act of 2024"
  },
  "summaries": [
    {
      "actionDate": "2025-01-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong></strong>This bill requires the consent of the chief executive officers (e.g., governors) of involved states when the President or Department of Defense orders National Guard units to perform training or other duty in such states. Under the bill, the term <em>state</em>\u00a0includes the District of Columbia and territories or possessions of the United States. The bill also subjects the ordered training or duty to the limitations of the Posse Comitatus Act of 1878, which prohibits the use of the military for civil law enforcement purposes.</p>",
      "updateDate": "2025-06-13",
      "versionCode": "id119hr590"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr590ih.xml"
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
      "title": "_______ Act of 2024",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-02T02:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "_______ Act of 2024",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-02T02:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 32, United States Code, to clarify certain limitations on full-time National Guard duty performed in a State, Territory, or the District of Columbia, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-02T02:48:34Z"
    }
  ]
}
```
