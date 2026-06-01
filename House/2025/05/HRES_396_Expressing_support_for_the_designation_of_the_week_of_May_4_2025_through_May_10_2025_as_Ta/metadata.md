# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/396?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/396
- Title: Expressing support for the designation of the week of May 4, 2025, through May 10, 2025, as "Tardive Dyskinesia Awareness Week".
- Congress: 119
- Bill type: HRES
- Bill number: 396
- Origin chamber: House
- Introduced date: 2025-05-07
- Update date: 2026-05-21T14:27:08Z
- Update date including text: 2026-05-21T14:27:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-07: Introduced in House
- 2025-05-07 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-05-07 - IntroReferral: Submitted in House
- 2025-05-07 - IntroReferral: Submitted in House
- Latest action: 2025-05-07: Submitted in House

## Actions

- 2025-05-07 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-05-07 - IntroReferral: Submitted in House
- 2025-05-07 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-07",
    "latestAction": {
      "actionDate": "2025-05-07",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/396",
    "number": "396",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "P000608",
        "district": "50",
        "firstName": "Scott",
        "fullName": "Rep. Peters, Scott H. [D-CA-50]",
        "lastName": "Peters",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Expressing support for the designation of the week of May 4, 2025, through May 10, 2025, as \"Tardive Dyskinesia Awareness Week\".",
    "type": "HRES",
    "updateDate": "2026-05-21T14:27:08Z",
    "updateDateIncludingText": "2026-05-21T14:27:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-07",
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
      "actionDate": "2025-05-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-05-07",
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
          "date": "2025-05-07T14:04:20Z",
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
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "FL"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "CA"
    },
    {
      "bioguideId": "B001314",
      "district": "4",
      "firstName": "Aaron",
      "fullName": "Rep. Bean, Aaron [R-FL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Bean",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres396ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 396\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2025 Mr. Peters (for himself, Mr. Bilirakis , Mr. Mullin , and Mr. Bean of Florida ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nExpressing support for the designation of the week of May 4, 2025, through May 10, 2025, as Tardive Dyskinesia Awareness Week .\nThat the House of Representatives\u2014\n**(1)**\nexpresses support for the designation of Tardive Dyskinesia Awareness Week ; and\n**(2)**\nencourages each individual in the United States to become better informed about and aware of tardive dyskinesia.",
      "versionDate": "2025-05-07",
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
        "actionDate": "2026-05-07",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "1265",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Expressing support for the designation of the week of May 3, 2026, through May 9, 2026, as \"Tardive Dyskinesia Awareness Week\".",
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
        "name": "Health",
        "updateDate": "2025-05-21T10:45:34Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-07",
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
          "measure-id": "id119hres396",
          "measure-number": "396",
          "measure-type": "hres",
          "orig-publish-date": "2025-05-07",
          "originChamber": "HOUSE",
          "update-date": "2026-04-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres396v00",
            "update-date": "2026-04-07"
          },
          "action-date": "2025-05-07",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution supports the designation of Tardive Dyskinesia Awareness Week. Tardive dyskinesia is a movement disorder characterized by involuntary and uncontrolled movements of muscles in the face, torso, and extremities.</p>"
        },
        "title": "Expressing support for the designation of the week of May 4, 2025, through May 10, 2025, as \"Tardive Dyskinesia Awareness Week\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres396.xml",
    "summary": {
      "actionDate": "2025-05-07",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of Tardive Dyskinesia Awareness Week. Tardive dyskinesia is a movement disorder characterized by involuntary and uncontrolled movements of muscles in the face, torso, and extremities.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hres396"
    },
    "title": "Expressing support for the designation of the week of May 4, 2025, through May 10, 2025, as \"Tardive Dyskinesia Awareness Week\"."
  },
  "summaries": [
    {
      "actionDate": "2025-05-07",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of Tardive Dyskinesia Awareness Week. Tardive dyskinesia is a movement disorder characterized by involuntary and uncontrolled movements of muscles in the face, torso, and extremities.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hres396"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres396ih.xml"
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
      "title": "Expressing support for the designation of the week of May 4, 2025, through May 10, 2025, as \"Tardive Dyskinesia Awareness Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-08T08:18:36Z"
    },
    {
      "title": "Expressing support for the designation of the week of May 4, 2025, through May 10, 2025, as \"Tardive Dyskinesia Awareness Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-08T08:06:15Z"
    }
  ]
}
```
