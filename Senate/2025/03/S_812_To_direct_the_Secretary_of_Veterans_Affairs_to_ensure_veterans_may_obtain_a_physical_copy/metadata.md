# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/812?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/812
- Title: A bill to direct the Secretary of Veterans Affairs to ensure veterans may obtain a physical copy of a form for reimbursement of certain travel expenses by mail or at medical facilities of the Department of Veterans Affairs, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 812
- Origin chamber: Senate
- Introduced date: 2025-03-03
- Update date: 2025-07-15T10:56:25Z
- Update date including text: 2025-07-15T10:56:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-03: Introduced in Senate
- 2025-03-03 - IntroReferral: Introduced in Senate
- 2025-03-03 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- Latest action: 2025-03-03: Introduced in Senate

## Actions

- 2025-03-03 - IntroReferral: Introduced in Senate
- 2025-03-03 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-03",
    "latestAction": {
      "actionDate": "2025-03-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/812",
    "number": "812",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "A bill to direct the Secretary of Veterans Affairs to ensure veterans may obtain a physical copy of a form for reimbursement of certain travel expenses by mail or at medical facilities of the Department of Veterans Affairs, and for other purposes.",
    "type": "S",
    "updateDate": "2025-07-15T10:56:25Z",
    "updateDateIncludingText": "2025-07-15T10:56:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-03",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-03",
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
          "date": "2025-03-03T20:36:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "NV"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "KS"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "ID"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "MS"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-03-03",
      "state": "ME"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "NC"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "SD"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "MI"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s812is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 812\nIN THE SENATE OF THE UNITED STATES\nMarch 3, 2025 Mr. Scott of Florida (for himself, Ms. Rosen , Mr. Marshall , Mr. Risch , Mr. Wicker , Mr. King , Mr. Tillis , Mr. Rounds , and Mr. Peters ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo direct the Secretary of Veterans Affairs to ensure veterans may obtain a physical copy of a form for reimbursement of certain travel expenses by mail or at medical facilities of the Department of Veterans Affairs, and for other purposes.\n#### 1. Requirement for Secretary of Veterans Affairs to make available to veterans physical copies of form for reimbursement of certain travel expenses\n##### (a) In general\nThe Secretary of Veterans Affairs shall prescribe regulations to ensure that\u2014\n**(1)**\na veteran may, for the purposes of submitting a claim for the reimbursement of expenses for travel under section 111 of title 38, United States Code\u2014\n**(A)**\nobtain a physical copy of the covered form\u2014\n**(i)**\nby mail, upon the request of such veteran; or\n**(ii)**\nat any medical facility of the Department of Veterans Affairs; and\n**(B)**\nsubmit the covered form to any such medical facility in person or by mail; and\n**(2)**\nany such medical facility to which a veteran submits the covered form\u2014\n**(A)**\nevaluates such covered form; and\n**(B)**\nprocesses any claim associated with such covered form, if applicable.\n##### (b) Covered form defined\nIn this section, the term covered form means Department of Veterans Affairs Form 10\u20133452 (or any successor document).",
      "versionDate": "2025-03-03",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-04-04T20:12:23Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-03",
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
          "measure-id": "id119s812",
          "measure-number": "812",
          "measure-type": "s",
          "orig-publish-date": "2025-03-03",
          "originChamber": "SENATE",
          "update-date": "2025-05-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s812v00",
            "update-date": "2025-05-13"
          },
          "action-date": "2025-03-03",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This bill requires the Department of Veterans Affairs (VA) to ensure that a veteran may obtain a physical copy of the form needed for travel reimbursements at any VA medical facility or, upon request, by mail. The VA must also ensure a veteran may submit the form to any VA medical facility in person or by mail. Such medical facilities must evaluate the form and process any claim associated with the form.</p>"
        },
        "title": "A bill to direct the Secretary of Veterans Affairs to ensure veterans may obtain a physical copy of a form for reimbursement of certain travel expenses by mail or at medical facilities of the Department of Veterans Affairs, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s812.xml",
    "summary": {
      "actionDate": "2025-03-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill requires the Department of Veterans Affairs (VA) to ensure that a veteran may obtain a physical copy of the form needed for travel reimbursements at any VA medical facility or, upon request, by mail. The VA must also ensure a veteran may submit the form to any VA medical facility in person or by mail. Such medical facilities must evaluate the form and process any claim associated with the form.</p>",
      "updateDate": "2025-05-13",
      "versionCode": "id119s812"
    },
    "title": "A bill to direct the Secretary of Veterans Affairs to ensure veterans may obtain a physical copy of a form for reimbursement of certain travel expenses by mail or at medical facilities of the Department of Veterans Affairs, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2025-03-03",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill requires the Department of Veterans Affairs (VA) to ensure that a veteran may obtain a physical copy of the form needed for travel reimbursements at any VA medical facility or, upon request, by mail. The VA must also ensure a veteran may submit the form to any VA medical facility in person or by mail. Such medical facilities must evaluate the form and process any claim associated with the form.</p>",
      "updateDate": "2025-05-13",
      "versionCode": "id119s812"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s812is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Secretary of Veterans Affairs to ensure veterans may obtain a physical copy of a form for reimbursement of certain travel expenses by mail or at medical facilities of the Department of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T03:18:45Z"
    },
    {
      "title": "A bill to direct the Secretary of Veterans Affairs to ensure veterans may obtain a physical copy of a form for reimbursement of certain travel expenses by mail or at medical facilities of the Department of Veterans Affairs, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-04T11:56:16Z"
    }
  ]
}
```
