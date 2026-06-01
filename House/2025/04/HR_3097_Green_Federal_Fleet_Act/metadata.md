# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3097?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3097
- Title: Green Federal Fleet Act
- Congress: 119
- Bill type: HR
- Bill number: 3097
- Origin chamber: House
- Introduced date: 2025-04-30
- Update date: 2025-07-03T19:46:58Z
- Update date including text: 2025-07-03T19:46:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-30: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-04-30: Introduced in House

## Actions

- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-30",
    "latestAction": {
      "actionDate": "2025-04-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3097",
    "number": "3097",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "B001285",
        "district": "26",
        "firstName": "Julia",
        "fullName": "Rep. Brownley, Julia [D-CA-26]",
        "lastName": "Brownley",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Green Federal Fleet Act",
    "type": "HR",
    "updateDate": "2025-07-03T19:46:58Z",
    "updateDateIncludingText": "2025-07-03T19:46:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-30",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-30",
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
          "date": "2025-04-30T14:01:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3097ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3097\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2025 Ms. Brownley introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo prohibit Federal agencies from purchasing or leasing new vehicles that are not zero-emission vehicles, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Green Federal Fleet Act .\n#### 2. Prohibition on the purchase or lease of vehicles that are not zero-emissions vehicles by Federal agencies\n##### (a) Prohibition\nNotwithstanding any other provision of law, except as provided in paragraph (2), the head of a Federal agency may not purchase or lease a non-tactical passenger vehicle from a non-Federal entity unless that vehicle is a zero-emission vehicle.\n##### (b) Exemption\nThe head of a Federal agency may purchase or lease a non-tactical passenger vehicle from a non-Federal entity that is not a zero-emission vehicle if the head determines that, with respect to a particular circumstance, using a zero-emission vehicle will not be technically feasible.\n##### (c) Application\nThe prohibition established under subsection (a) shall not apply with respect to purchases made and leases entered into before the date of the enactment of this Act.\n##### (d) Definitions\nIn this Act:\n**(1) Zero-emission vehicle**\nThe term zero-emission vehicle means a passenger vehicle that produces zero exhaust emissions of any criteria pollutant, precursor pollutant, or greenhouse gas, other than water vapor, in any mode of operation or condition, as determined by the Administrator of the Environmental Protection Agency.\n**(2) Federal agency**\nThe term Federal Agency means an establishment in the legislative, judicial, or executive branch of the Federal Government.",
      "versionDate": "2025-04-30",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-29T15:42:03Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-30",
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
          "measure-id": "id119hr3097",
          "measure-number": "3097",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-30",
          "originChamber": "HOUSE",
          "update-date": "2025-07-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3097v00",
            "update-date": "2025-07-03"
          },
          "action-date": "2025-04-30",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Green Federal Fleet Act</b></p> <p>This bill requires passenger vehicles that are purchased or leased from a nonfederal entity by a federal agency to be zero-emission vehicles. This requirement does not apply to tactical vehicles or in circumstances where a zero-emission vehicle is not technically feasible.</p>"
        },
        "title": "Green Federal Fleet Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3097.xml",
    "summary": {
      "actionDate": "2025-04-30",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Green Federal Fleet Act</b></p> <p>This bill requires passenger vehicles that are purchased or leased from a nonfederal entity by a federal agency to be zero-emission vehicles. This requirement does not apply to tactical vehicles or in circumstances where a zero-emission vehicle is not technically feasible.</p>",
      "updateDate": "2025-07-03",
      "versionCode": "id119hr3097"
    },
    "title": "Green Federal Fleet Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-30",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Green Federal Fleet Act</b></p> <p>This bill requires passenger vehicles that are purchased or leased from a nonfederal entity by a federal agency to be zero-emission vehicles. This requirement does not apply to tactical vehicles or in circumstances where a zero-emission vehicle is not technically feasible.</p>",
      "updateDate": "2025-07-03",
      "versionCode": "id119hr3097"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3097ih.xml"
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
      "title": "Green Federal Fleet Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-09T03:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Green Federal Fleet Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-09T03:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit Federal agencies from purchasing or leasing new vehicles that are not zero-emission vehicles, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-09T03:33:18Z"
    }
  ]
}
```
