# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2101?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2101
- Title: Delivering Digitally to Our Veterans Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2101
- Origin chamber: Senate
- Introduced date: 2025-06-17
- Update date: 2026-03-30T16:53:59Z
- Update date including text: 2026-03-30T16:53:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-06-17: Introduced in Senate
- 2025-06-17 - IntroReferral: Introduced in Senate
- 2025-06-17 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- Latest action: 2025-06-17: Introduced in Senate

## Actions

- 2025-06-17 - IntroReferral: Introduced in Senate
- 2025-06-17 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-17",
    "latestAction": {
      "actionDate": "2025-06-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2101",
    "number": "2101",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001299",
        "district": "",
        "firstName": "Jim",
        "fullName": "Sen. Banks, Jim [R-IN]",
        "lastName": "Banks",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Delivering Digitally to Our Veterans Act of 2025",
    "type": "S",
    "updateDate": "2026-03-30T16:53:59Z",
    "updateDateIncludingText": "2026-03-30T16:53:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-17",
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
      "actionDate": "2025-06-17",
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
          "date": "2025-06-17T21:36:09Z",
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
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-17",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2101is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2101\nIN THE SENATE OF THE UNITED STATES\nJune 17, 2025 Mr. Banks (for himself and Ms. Hirono ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to direct the Secretary of Veterans Affairs to provide for electronic communication relating to educational assistance benefits under the laws administered by the Secretary, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Delivering Digitally to Our Veterans Act of 2025 .\n#### 2. Department of Veterans Affairs electronic communication relating to educational assistance benefits\nSection 3680 of title 38, United States Code, is amended by adding at the end the following new subsection:\n(i) Electronic correspondence (1) The Secretary shall provide a mechanism by which an eligible veteran or eligible person may electronically send and receive correspondence with the Department of Veterans Affairs relating to entitlement to and use of educational assistance benefits under the laws administered by the Secretary. The Secretary shall ensure that an eligible veteran or eligible person is provided with an opportunity to opt into sending and receiving such correspondence electronically rather than by mail. (2) The Secretary shall provide to eligible veterans and eligible persons who are enrolled in a course or program of education or training notice of the opportunity to opt in to sending and receiving correspondence electronically pursuant to paragraph (1). .",
      "versionDate": "2025-06-17",
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
        "actionDate": "2025-09-18",
        "text": "Received in the Senate and Read twice and referred to the Committee on Veterans' Affairs."
      },
      "number": "3481",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Delivering Digitally to Our Veterans Act of 2025",
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
        "updateDate": "2025-07-01T16:29:16Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-17",
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
          "measure-id": "id119s2101",
          "measure-number": "2101",
          "measure-type": "s",
          "orig-publish-date": "2025-06-17",
          "originChamber": "SENATE",
          "update-date": "2026-03-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2101v00",
            "update-date": "2026-03-30"
          },
          "action-date": "2025-06-17",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Delivering Digitally to Our Veterans Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to provide a way for individuals who are entitled to VA educational assistance to electronically send and receive correspondence with the VA related to such assistance. The VA must ensure individuals are provided an opportunity to opt in to electronic correspondence.\u00a0</p>"
        },
        "title": "Delivering Digitally to Our Veterans Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2101.xml",
    "summary": {
      "actionDate": "2025-06-17",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Delivering Digitally to Our Veterans Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to provide a way for individuals who are entitled to VA educational assistance to electronically send and receive correspondence with the VA related to such assistance. The VA must ensure individuals are provided an opportunity to opt in to electronic correspondence.\u00a0</p>",
      "updateDate": "2026-03-30",
      "versionCode": "id119s2101"
    },
    "title": "Delivering Digitally to Our Veterans Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-06-17",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Delivering Digitally to Our Veterans Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to provide a way for individuals who are entitled to VA educational assistance to electronically send and receive correspondence with the VA related to such assistance. The VA must ensure individuals are provided an opportunity to opt in to electronic correspondence.\u00a0</p>",
      "updateDate": "2026-03-30",
      "versionCode": "id119s2101"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2101is.xml"
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
      "title": "Delivering Digitally to Our Veterans Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-28T02:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Delivering Digitally to Our Veterans Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-28T02:38:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to direct the Secretary of Veterans Affairs to provide for electronic communication relating to educational assistance benefits under the laws administered by the Secretary, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-28T02:33:29Z"
    }
  ]
}
```
