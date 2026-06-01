# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/157?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/157
- Title: CONTAINER Act
- Congress: 119
- Bill type: S
- Bill number: 157
- Origin chamber: Senate
- Introduced date: 2025-01-21
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-21: Introduced in Senate
- 2025-01-21 - IntroReferral: Introduced in Senate
- 2025-01-21 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-01-21: Introduced in Senate

## Actions

- 2025-01-21 - IntroReferral: Introduced in Senate
- 2025-01-21 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/157",
    "number": "157",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "CONTAINER Act",
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
      "actionDate": "2025-01-21",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-21",
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
          "date": "2025-01-21T17:19:51Z",
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
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "LA"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "ND"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "TX"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MS"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "NC"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "TX"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "OK"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "OH"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "False",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "SD"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "ND"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s157is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 157\nIN THE SENATE OF THE UNITED STATES\nJanuary 21, 2025 Mrs. Blackburn (for herself, Mr. Cassidy , Mr. Cramer , and Mr. Cruz ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo authorize certain States to take certain actions on certain Federal land to secure an international border of the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Creating Obstructions Necessary To Address Illegal and Nefarious Entry Rapidly Act or the CONTAINER Act .\n#### 2. Placement of movable, temporary structures on certain Federal land to secure an international border of the United States\n##### (a) Definitions\nIn this section:\n**(1) Border state**\nThe term Border State means a State that is adjacent to the northern border or southern border.\n**(2) Federal land**\nThe term Federal land means land under the jurisdiction and management of a Federal land management agency that is adjacent to the northern border or southern border.\n**(3) Federal land management agency**\nThe term Federal land management agency means\u2014\n**(A)**\nthe Bureau of Indian Affairs;\n**(B)**\nthe Bureau of Land Management;\n**(C)**\nthe Bureau of Reclamation;\n**(D)**\nthe Forest Service;\n**(E)**\nthe United States Fish and Wildlife Service; and\n**(F)**\nthe National Park Service.\n**(4) Northern border**\nThe term northern border means the international border between the United States and Canada.\n**(5) Operational control**\nThe term operational control has the meaning given such term in section 2(b) of the Secure Fence Act of 2006 ( 8 U.S.C. 1701 note; Public Law 109\u2013367 ).\n**(6) Secretary concerned**\nThe term Secretary concerned means\u2014\n**(A)**\nthe Secretary of the Interior, with respect to Federal land under the jurisdiction and management of the Secretary of the Interior, acting through, as applicable\u2014\n**(i)**\nthe Director of the Bureau of Indian Affairs;\n**(ii)**\nthe Director of the Bureau of Land Management;\n**(iii)**\nthe Commissioner of Reclamation;\n**(iv)**\nthe Director of the United States Fish and Wildlife Service; and\n**(v)**\nthe Director of the National Park Service; and\n**(B)**\nthe Secretary of Agriculture, with respect to National Forest System land, acting through the Chief of the Forest Service.\n**(7) Southern border**\nThe term southern border means the international border between the United States and Mexico.\n##### (b) Special use authorization\nSubject to subsection (c), the Secretary concerned shall not require a Border State to obtain a special use authorization for the temporary placement on Federal land within the Border State of a movable, temporary structure for the purpose of securing the northern border or southern border, if the Border State submits to the Secretary concerned notice of the proposed placement not later than 45 days before the date of the proposed placement.\n##### (c) Temporary placement\n**(1) In general**\nA movable, temporary structure described in subsection (b) may be placed by a Border State on Federal land in accordance with that subsection for a period of not more than 1 year, subject to paragraph (2).\n**(2) Extension**\n**(A) In general**\nThe period described in paragraph (1) may be extended in 90-day increments, on approval by the Secretary concerned.\n**(B) Consultation required**\nThe Secretary concerned shall consult with the Commissioner of U.S. Customs and Border Protection for purposes of determining whether to approve an extension under subparagraph (A).\n**(C) Approval**\nThe Secretary concerned shall approve a request for an extension under this paragraph if the Commissioner of U.S. Customs and Border Protection determines that operational control has not been achieved as of the date of the consultation required under subparagraph (B).",
      "versionDate": "2025-01-21",
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
        "actionDate": "2025-02-20",
        "text": "Referred to the Subcommittee on Forestry and Horticulture."
      },
      "number": "534",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "CONTAINER Act",
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
            "name": "Border security and unlawful immigration",
            "updateDate": "2025-03-12T13:45:17Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2025-03-12T13:45:17Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-03-12T13:45:17Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-02-27T20:20:14Z"
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
          "measure-id": "id119s157",
          "measure-number": "157",
          "measure-type": "s",
          "orig-publish-date": "2025-01-21",
          "originChamber": "SENATE",
          "update-date": "2025-06-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s157v00",
            "update-date": "2025-06-03"
          },
          "action-date": "2025-01-21",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Creating Obstructions Necessary to Address Illegal and Nefarious Entry Rapidly Act or CONTAINER Act</strong></p><p>This bill requires the Department of the Interior and the Forest Service to allow border states to place temporary, movable structures on federal lands adjacent to the U.S.-Canada and U.S.-Mexico borders without a special use authorization.</p><p>Border states may place these structures on such lands for the purpose of securing the northern or southern border for a period of not more than one year. Interior and the Forest Service must approve extension requests in 90-day increments if U.S. Customs and Border Protection determines that operational control of the border area has not been achieved.</p>"
        },
        "title": "CONTAINER Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s157.xml",
    "summary": {
      "actionDate": "2025-01-21",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Creating Obstructions Necessary to Address Illegal and Nefarious Entry Rapidly Act or CONTAINER Act</strong></p><p>This bill requires the Department of the Interior and the Forest Service to allow border states to place temporary, movable structures on federal lands adjacent to the U.S.-Canada and U.S.-Mexico borders without a special use authorization.</p><p>Border states may place these structures on such lands for the purpose of securing the northern or southern border for a period of not more than one year. Interior and the Forest Service must approve extension requests in 90-day increments if U.S. Customs and Border Protection determines that operational control of the border area has not been achieved.</p>",
      "updateDate": "2025-06-03",
      "versionCode": "id119s157"
    },
    "title": "CONTAINER Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-21",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Creating Obstructions Necessary to Address Illegal and Nefarious Entry Rapidly Act or CONTAINER Act</strong></p><p>This bill requires the Department of the Interior and the Forest Service to allow border states to place temporary, movable structures on federal lands adjacent to the U.S.-Canada and U.S.-Mexico borders without a special use authorization.</p><p>Border states may place these structures on such lands for the purpose of securing the northern or southern border for a period of not more than one year. Interior and the Forest Service must approve extension requests in 90-day increments if U.S. Customs and Border Protection determines that operational control of the border area has not been achieved.</p>",
      "updateDate": "2025-06-03",
      "versionCode": "id119s157"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s157is.xml"
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
      "title": "CONTAINER Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-21T03:38:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "CONTAINER Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T03:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Creating Obstructions Necessary To Address Illegal and Nefarious Entry Rapidly Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T03:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to authorize certain States to take certain actions on certain Federal land to secure an international border of the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T03:33:28Z"
    }
  ]
}
```
