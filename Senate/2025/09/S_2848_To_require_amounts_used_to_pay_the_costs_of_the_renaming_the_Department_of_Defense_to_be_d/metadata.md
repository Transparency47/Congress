# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2848?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2848
- Title: DoD COW Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2848
- Origin chamber: Senate
- Introduced date: 2025-09-17
- Update date: 2026-01-28T12:03:16Z
- Update date including text: 2026-01-28T12:03:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-17: Introduced in Senate
- 2025-09-17 - IntroReferral: Introduced in Senate
- 2025-09-17 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-09-17: Introduced in Senate

## Actions

- 2025-09-17 - IntroReferral: Introduced in Senate
- 2025-09-17 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-17",
    "latestAction": {
      "actionDate": "2025-09-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2848",
    "number": "2848",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "A000382",
        "district": "",
        "firstName": "Angela",
        "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
        "lastName": "Alsobrooks",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "DoD COW Act of 2025",
    "type": "S",
    "updateDate": "2026-01-28T12:03:16Z",
    "updateDateIncludingText": "2026-01-28T12:03:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-17",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-17",
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
            "date": "2025-09-17T20:48:21Z",
            "name": "Referred To"
          },
          {
            "date": "2025-09-17T20:48:21Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "MD"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-09-29",
      "state": "OR"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2848is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2848\nIN THE SENATE OF THE UNITED STATES\nSeptember 17 (legislative day, September 16), 2025 Ms. Alsobrooks (for herself and Mr. Van Hollen ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo require amounts used to pay the costs of the renaming the Department of Defense to be derived from the travel budget of the Secretary of Defense, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Department of Defense\u2019s Cost of \u2018War\u2019 Act of 2025 or the DoD COW Act of 2025 .\n#### 2. Designation of funds to pay costs of renaming Department of Defense\n##### (a) Finding\nCongress finds that\u2014\n**(1)**\ntitle II of the National Security Act of 1947 (61 Stat. 499, chapter 343) established the National Military Establishment to replace the Department of War; and\n**(2)**\nthe National Military Establishment was subsequently renamed the Department of Defense, by an amendment to the National Security Act of 1947 made by section 4 of the National Security Act Amendments of 1949 (63 Stat. 578, chapter 412).\n##### (b) Sense of Congress\nIt is the sense of Congress that, as the Department was established and named by an Act of Congress, the name of the Department can be changed only by an Act of Congress.\n##### (c) Designation of funds\n**(1) In general**\nThe Secretary shall pay covered costs by reallocating amounts available to the Secretary for travel expenses to pay such costs.\n**(2) Additional funds**\nIf the total amount of covered costs exceeds the total amount available to the Secretary for travel, the Secretary shall pay the remaining amount of covered costs by reallocating amounts available to the secretaries of the military departments for travel to pay such costs.\n##### (d) Report required\nNot later than one year after the date of the enactment of this Act, the Secretary shall submit to Congress a report on the total amount obligated or expended to pay covered costs.\n##### (e) Definitions\nIn this section:\n**(1) Covered costs**\nThe term covered costs means costs accrued by the Department and associated with the changing of Department of Defense to Department of War on physical signage, websites, stationary, printed media, and digital media owned or operated by the United States Government.\n**(2) Department**\nThe term Department means the executive department established by section 111 of title 10, United States Code.\n**(3) Secretary**\nThe term Secretary means the official established by and appointed under section 113 of such title.",
      "versionDate": "2025-09-17",
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
        "updateDate": "2025-11-25T18:36:53Z"
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
      "date": "2025-09-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2848is.xml"
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
      "title": "DoD COW Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-28T12:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "DoD COW Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-10T06:08:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Department of Defense\u2019s Cost of \u2018War\u2019 Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-10T06:08:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require amounts used to pay the costs of the renaming the Department of Defense to be derived from the travel budget of the Secretary of Defense, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-10T06:03:30Z"
    }
  ]
}
```
