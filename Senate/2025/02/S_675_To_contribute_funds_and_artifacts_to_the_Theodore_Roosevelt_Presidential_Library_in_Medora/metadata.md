# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/675?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/675
- Title: Theodore Roosevelt Presidential Library Museum Artifacts Act
- Congress: 119
- Bill type: S
- Bill number: 675
- Origin chamber: Senate
- Introduced date: 2025-02-20
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-20: Introduced in Senate
- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-02-20: Introduced in Senate

## Actions

- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-20",
    "latestAction": {
      "actionDate": "2025-02-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/675",
    "number": "675",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Arts, Culture, Religion"
    },
    "sponsors": [
      {
        "bioguideId": "H001061",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Hoeven, John [R-ND]",
        "lastName": "Hoeven",
        "party": "R",
        "state": "ND"
      }
    ],
    "title": "Theodore Roosevelt Presidential Library Museum Artifacts Act",
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
      "actionDate": "2025-02-20",
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
      "actionDate": "2025-02-20",
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
          "date": "2025-02-20T23:25:25Z",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-02-20",
      "state": "CT"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-02-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s675is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 675\nIN THE SENATE OF THE UNITED STATES\nFebruary 20, 2025 Mr. Hoeven (for himself, Mr. Blumenthal , and Mr. Cramer ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo contribute funds and artifacts to the Theodore Roosevelt Presidential Library in Medora, North Dakota.\n#### 1. Short title\nThis Act may be cited as the Theodore Roosevelt Presidential Library Museum Artifacts Act .\n#### 2. Definitions\nIn this Act:\n**(1) Foundation**\nThe term Foundation means the Theodore Roosevelt Presidential Library Foundation.\n**(2) Library**\nThe term Library means the Theodore Roosevelt Presidential Library to be located in Medora, North Dakota.\n**(3) Secretary**\nThe term Secretary means the Secretary of the Interior.\n#### 3. Federal contributions toward establishment of the Theodore Roosevelt Presidential Library\n##### (a) Grants\n**(1) Authorization**\nTo the extent provided in advance in appropriations Acts and subject to paragraphs (2) and (3), the Secretary may provide to the Foundation grants in an amount not to exceed a total of $50,000,000 for the establishment of the Library\u2014\n**(A)**\nto preserve and make available to the public materials relating to the life of President Theodore Roosevelt; and\n**(B)**\nto provide interpretive and educational services that communicate the meaning of the life of Theodore Roosevelt.\n**(2) Matching requirement**\nThe Secretary may not provide a grant under paragraph (1) until the date on which the Foundation certifies to the Secretary that the Foundation has received an amount equal to not less than $100,000,000 from funds for the Library\u2014\n**(A)**\ncontributed by the State of North Dakota; or\n**(B)**\nraised from non-Federal sources during the period beginning on the date on which the Foundation was established and ending on the date of the certification.\n**(3) Prohibition on use of funds**\nGrant funds provided under this subsection may not be used for the maintenance or operation of the Library.\n##### (b) Federal artifacts and objects relating to theodore roosevelt\nNot later than 180 days after the date of enactment of this Act, the Secretary may enter into 1 or more agreements with the Foundation to provide for a loan to the Foundation from Federal agencies under the administrative jurisdiction of the Secretary (including the National Park Service and the United States Fish and Wildlife Service) of historic, educational, artistic, natural, and other museum artifacts and objects, particularly artifacts and objects that are not on display to the public, without monetary consideration, subject to such terms and conditions as the Secretary determines to be necessary for the preservation and exhibition of the artifacts and objects loaned to the Foundation.\n##### (c) Non-Federal operation\nThe Secretary or any other Federal entity shall have no involvement in the operation of the Library, except at the request of the non-Federal entity responsible for the operation of the Library in accordance with applicable laws (including regulations).",
      "versionDate": "2025-02-20",
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
        "name": "Arts, Culture, Religion",
        "updateDate": "2025-03-17T16:00:00Z"
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
      "date": "2025-02-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s675is.xml"
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
      "title": "Theodore Roosevelt Presidential Library Museum Artifacts Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-15T03:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Theodore Roosevelt Presidential Library Museum Artifacts Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-15T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to contribute funds and artifacts to the Theodore Roosevelt Presidential Library in Medora, North Dakota.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-15T03:18:19Z"
    }
  ]
}
```
