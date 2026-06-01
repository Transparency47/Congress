# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/322?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/322
- Title: Supporting the goals and ideals of National Public Safety Telecommunicators Week.
- Congress: 119
- Bill type: HRES
- Bill number: 322
- Origin chamber: House
- Introduced date: 2025-04-09
- Update date: 2026-05-12T16:04:36Z
- Update date including text: 2026-05-12T16:04:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-09: Introduced in House
- 2025-04-09 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-04-09 - IntroReferral: Submitted in House
- 2025-04-09 - IntroReferral: Submitted in House
- Latest action: 2025-04-09: Submitted in House

## Actions

- 2025-04-09 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-04-09 - IntroReferral: Submitted in House
- 2025-04-09 - IntroReferral: Submitted in House

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
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/322",
    "number": "322",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "T000474",
        "district": "35",
        "firstName": "Norma",
        "fullName": "Rep. Torres, Norma J. [D-CA-35]",
        "lastName": "Torres",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Supporting the goals and ideals of National Public Safety Telecommunicators Week.",
    "type": "HRES",
    "updateDate": "2026-05-12T16:04:36Z",
    "updateDateIncludingText": "2026-05-12T16:04:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-09",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-04-09",
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
          "date": "2025-04-09T16:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres322ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 322\nIN THE HOUSE OF REPRESENTATIVES\nApril 9, 2025 Mrs. Torres of California (for herself and Mr. Fitzpatrick ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nSupporting the goals and ideals of National Public Safety Telecommunicators Week.\nThat the House of Representatives\u2014\n**(1)**\nsupports the goals and ideals of National Public Safety Telecommunicators Week;\n**(2)**\nhonors and recognizes the important and lifesaving contributions of public safety telecommunications professionals in the United States; and\n**(3)**\nencourages the people of the United States to remember the value of the work performed by public safety telecommunications professionals.",
      "versionDate": "2025-04-09",
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
        "actionDate": "2025-04-09",
        "text": "Referred to the Committee on Commerce, Science, and Transportation. (text: CR S2528)"
      },
      "number": "164",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A resolution supporting the goals and ideals of National Public Safety Telecommunicators Week.",
      "type": "SRES"
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-04-10T18:28:53Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-09",
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
          "measure-id": "id119hres322",
          "measure-number": "322",
          "measure-type": "hres",
          "orig-publish-date": "2025-04-09",
          "originChamber": "HOUSE",
          "update-date": "2026-05-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres322v00",
            "update-date": "2026-05-12"
          },
          "action-date": "2025-04-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This\u00a0resolution supports the goals and ideals of National Public Safety Telecommunicators Week and honors and recognizes the contributions of public safety telecommunications professionals.</p>"
        },
        "title": "Supporting the goals and ideals of National Public Safety Telecommunicators Week."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres322.xml",
    "summary": {
      "actionDate": "2025-04-09",
      "actionDesc": "Introduced in House",
      "text": "<p>This\u00a0resolution supports the goals and ideals of National Public Safety Telecommunicators Week and honors and recognizes the contributions of public safety telecommunications professionals.</p>",
      "updateDate": "2026-05-12",
      "versionCode": "id119hres322"
    },
    "title": "Supporting the goals and ideals of National Public Safety Telecommunicators Week."
  },
  "summaries": [
    {
      "actionDate": "2025-04-09",
      "actionDesc": "Introduced in House",
      "text": "<p>This\u00a0resolution supports the goals and ideals of National Public Safety Telecommunicators Week and honors and recognizes the contributions of public safety telecommunications professionals.</p>",
      "updateDate": "2026-05-12",
      "versionCode": "id119hres322"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres322ih.xml"
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
      "title": "Supporting the goals and ideals of National Public Safety Telecommunicators Week.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-10T10:18:21Z"
    },
    {
      "title": "Supporting the goals and ideals of National Public Safety Telecommunicators Week.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-10T08:06:32Z"
    }
  ]
}
```
