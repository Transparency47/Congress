# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5974?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5974
- Title: Bureau of Prisons Pay Protection Act
- Congress: 119
- Bill type: HR
- Bill number: 5974
- Origin chamber: House
- Introduced date: 2025-11-07
- Update date: 2025-12-10T09:06:02Z
- Update date including text: 2025-12-10T09:06:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-11-07: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Referred to the House Committee on Appropriations.
- Latest action: 2025-11-07: Introduced in House

## Actions

- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Referred to the House Committee on Appropriations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-07",
    "latestAction": {
      "actionDate": "2025-11-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5974",
    "number": "5974",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "P000620",
        "district": "7",
        "firstName": "Brittany",
        "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
        "lastName": "Pettersen",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Bureau of Prisons Pay Protection Act",
    "type": "HR",
    "updateDate": "2025-12-10T09:06:02Z",
    "updateDateIncludingText": "2025-12-10T09:06:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-07",
      "committees": {
        "item": {
          "name": "Appropriations Committee",
          "systemCode": "hsap00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Appropriations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-07",
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
          "date": "2025-11-07T19:02:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Appropriations Committee",
      "systemCode": "hsap00",
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
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "CO"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5974ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5974\nIN THE HOUSE OF REPRESENTATIVES\nNovember 7, 2025 Ms. Pettersen (for herself and Mr. Neguse ) introduced the following bill; which was referred to the Committee on Appropriations\nA BILL\nTo provide funding for personnel of Bureau of Prisons facilities.\n#### 1. Short title\nThis Act may be cited as the Bureau of Prisons Pay Protection Act .\n#### 2. Funding for personnel of Bureau of Prison facilities\nOut of any money in the Treasury not otherwise appropriated, there is appropriated such sums as are necessary to pay, during any period of a lapse in discretionary appropriations during any fiscal year, the salaries of the personnel, both correctional and non-correctional, of a facility of the Bureau of Prisons during such lapse.",
      "versionDate": "2025-11-07",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-11-19T13:05:24Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-07",
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
          "measure-id": "id119hr5974",
          "measure-number": "5974",
          "measure-type": "hr",
          "orig-publish-date": "2025-11-07",
          "originChamber": "HOUSE",
          "update-date": "2025-11-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5974v00",
            "update-date": "2025-11-19"
          },
          "action-date": "2025-11-07",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Bureau of Prisons Pay Protection Act</strong></p><p>This bill provides appropriations for the salaries of Bureau of Prisons (BOP) personnel during any lapse in discretionary appropriations for any fiscal year (i.e., a government shutdown).\u00a0During a lapse in appropriations, the bill provides appropriations for the salaries of correctional and non-correctional personnel at BOP facilities.\u00a0</p>"
        },
        "title": "Bureau of Prisons Pay Protection Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5974.xml",
    "summary": {
      "actionDate": "2025-11-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Bureau of Prisons Pay Protection Act</strong></p><p>This bill provides appropriations for the salaries of Bureau of Prisons (BOP) personnel during any lapse in discretionary appropriations for any fiscal year (i.e., a government shutdown).\u00a0During a lapse in appropriations, the bill provides appropriations for the salaries of correctional and non-correctional personnel at BOP facilities.\u00a0</p>",
      "updateDate": "2025-11-19",
      "versionCode": "id119hr5974"
    },
    "title": "Bureau of Prisons Pay Protection Act"
  },
  "summaries": [
    {
      "actionDate": "2025-11-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Bureau of Prisons Pay Protection Act</strong></p><p>This bill provides appropriations for the salaries of Bureau of Prisons (BOP) personnel during any lapse in discretionary appropriations for any fiscal year (i.e., a government shutdown).\u00a0During a lapse in appropriations, the bill provides appropriations for the salaries of correctional and non-correctional personnel at BOP facilities.\u00a0</p>",
      "updateDate": "2025-11-19",
      "versionCode": "id119hr5974"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5974ih.xml"
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
      "title": "Bureau of Prisons Pay Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-12T15:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Bureau of Prisons Pay Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-12T15:08:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide funding for personnel of Bureau of Prisons facilities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-12T15:03:14Z"
    }
  ]
}
```
