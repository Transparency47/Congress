# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1085?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1085
- Title: Censuring Representative Al Green of Texas.
- Congress: 119
- Bill type: HRES
- Bill number: 1085
- Origin chamber: House
- Introduced date: 2026-02-25
- Update date: 2026-04-09T13:23:20Z
- Update date including text: 2026-04-09T13:23:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-02-25: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on Ethics.
- 2026-02-25 - IntroReferral: Submitted in House
- 2026-02-25 - IntroReferral: Submitted in House
- Latest action: 2026-02-25: Submitted in House

## Actions

- 2026-02-25 - IntroReferral: Referred to the House Committee on Ethics.
- 2026-02-25 - IntroReferral: Submitted in House
- 2026-02-25 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-25",
    "latestAction": {
      "actionDate": "2026-02-25",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1085",
    "number": "1085",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "R000619",
        "district": "6",
        "firstName": "Michael",
        "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
        "lastName": "Rulli",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Censuring Representative Al Green of Texas.",
    "type": "HRES",
    "updateDate": "2026-04-09T13:23:20Z",
    "updateDateIncludingText": "2026-04-09T13:23:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-25",
      "committees": {
        "item": {
          "name": "Ethics Committee",
          "systemCode": "hsso00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ethics.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2026-02-25T14:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ethics Committee",
      "systemCode": "hsso00",
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
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2026-02-26",
      "state": "GA"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1085ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1085\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2026 Mr. Rulli submitted the following resolution; which was referred to the Committee on Ethics\nRESOLUTION\nCensuring Representative Al Green of Texas.\nThat\u2014\n**(1)**\nRepresentative Al Green be censured;\n**(2)**\nRepresentative Al Green forthwith present himself in the well of the House of Representatives for the pronouncement of censure; and\n**(3)**\nRepresentative Al Green be censured with the public reading of this resolution by the Speaker.",
      "versionDate": "2026-02-25",
      "versionType": "IH"
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
        "actionDate": "2025-03-06",
        "actionTime": "10:30:45",
        "text": "Motion to reconsider laid on the table Agreed to without objection."
      },
      "number": "189",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Censuring Representative Al Green of Texas.",
      "type": "HRES"
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
        "name": "Congress",
        "updateDate": "2026-03-02T17:53:25Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-02-25",
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
          "measure-id": "id119hres1085",
          "measure-number": "1085",
          "measure-type": "hres",
          "orig-publish-date": "2026-02-25",
          "originChamber": "HOUSE",
          "update-date": "2026-04-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres1085v00",
            "update-date": "2026-04-09"
          },
          "action-date": "2026-02-25",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution censures Representative Al Green.</p>"
        },
        "title": "Censuring Representative Al Green of Texas."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres1085.xml",
    "summary": {
      "actionDate": "2026-02-25",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution censures Representative Al Green.</p>",
      "updateDate": "2026-04-09",
      "versionCode": "id119hres1085"
    },
    "title": "Censuring Representative Al Green of Texas."
  },
  "summaries": [
    {
      "actionDate": "2026-02-25",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution censures Representative Al Green.</p>",
      "updateDate": "2026-04-09",
      "versionCode": "id119hres1085"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1085ih.xml"
        }
      ],
      "type": "IH"
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
      "title": "Censuring Representative Al Green of Texas.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-26T09:18:28Z"
    },
    {
      "title": "Censuring Representative Al Green of Texas.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-26T09:07:05Z"
    }
  ]
}
```
