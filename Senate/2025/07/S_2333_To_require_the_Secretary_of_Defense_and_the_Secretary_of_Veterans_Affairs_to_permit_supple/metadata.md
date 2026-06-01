# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2333?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2333
- Title: Health Records Enhancement Act
- Congress: 119
- Bill type: S
- Bill number: 2333
- Origin chamber: Senate
- Introduced date: 2025-07-17
- Update date: 2026-03-19T11:03:27Z
- Update date including text: 2026-03-19T11:03:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-17: Introduced in Senate
- 2025-07-17 - IntroReferral: Introduced in Senate
- 2025-07-17 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-12-10 - Committee: Committee on Veterans' Affairs. Hearings held.
- 2026-03-18 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-07-17: Introduced in Senate

## Actions

- 2025-07-17 - IntroReferral: Introduced in Senate
- 2025-07-17 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-12-10 - Committee: Committee on Veterans' Affairs. Hearings held.
- 2026-03-18 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2333",
    "number": "2333",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "W000800",
        "district": "",
        "firstName": "Peter",
        "fullName": "Sen. Welch, Peter [D-VT]",
        "lastName": "Welch",
        "party": "D",
        "state": "VT"
      }
    ],
    "title": "Health Records Enhancement Act",
    "type": "S",
    "updateDate": "2026-03-19T11:03:27Z",
    "updateDateIncludingText": "2026-03-19T11:03:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-10",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-17",
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
      "actionDate": "2025-07-17",
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
        "item": [
          {
            "date": "2026-03-18T20:00:22Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-10T21:00:26Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-07-17T17:32:37Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2333is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2333\nIN THE SENATE OF THE UNITED STATES\nJuly 17, 2025 Mr. Welch introduced the following bill; which was read twice and referred to the Committee on Veterans\u2019 Affairs\nA BILL\nTo require the Secretary of Defense and the Secretary of Veterans Affairs to permit supplementation of health records of deceased veterans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Health Records Enhancement Act .\n#### 2. Supplementation of health records of deceased veterans\n##### (a) In general\nNot later than one year after the date of the enactment of this Act, the Secretary of Defense and the Secretary of Veterans Affairs shall jointly take actions necessary to ensure that the health records of the Department of Defense and the Department of Veterans Affairs may be updated with observed health conditions and other relevant health information of a deceased enrollee by\u2014\n**(1)**\nan individual designated by such deceased enrollee; or\n**(2)**\nif no such individual is designated, an immediate family member of such deceased enrollee.\n##### (b) Designation\nThe Secretary of Defense and the Secretary of Veterans Affairs shall jointly provide for a process by which an individual may make a designation for purposes of subsection (a)(1).\n##### (c) No modification of health information\nAny update under subsection (a) shall supplement information contained in the health records of a deceased enrollee and shall not modify information contained in such records.\n##### (d) Definitions\nIn this section:\n**(1) Immediate family member**\nThe term immediate family member , with respect to a deceased enrollee, means\u2014\n**(A)**\nthe spouse, parent, brother, sister, or adult child of the individual; or\n**(B)**\nan adult person to whom the individual stands in loco parentis.\n**(2) Deceased enrollee**\nThe term deceased enrollee means any individual who, at the time of his or her death\u2014\n**(A)**\nwas enrolled in the patient enrollment system of the Department of Veterans Affairs established and operated under section 1705(a) of title 38, United States Code; or\n**(B)**\nwas entitled to care under the TRICARE program, as defined in section 1072 of title 10, United States Code.",
      "versionDate": "2025-07-17",
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
        "actionDate": "2025-12-19",
        "text": "Referred to the Subcommittee on Health."
      },
      "number": "4527",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Health Records Enhancement Act",
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
            "name": "Health information and medical records",
            "updateDate": "2026-01-09T16:23:19Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2026-01-09T16:23:14Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-08-07T18:45:04Z"
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
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2333is.xml"
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
      "title": "Health Records Enhancement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T11:03:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Health Records Enhancement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-01T03:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Defense and the Secretary of Veterans Affairs to permit supplementation of health records of deceased veterans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-01T03:48:27Z"
    }
  ]
}
```
