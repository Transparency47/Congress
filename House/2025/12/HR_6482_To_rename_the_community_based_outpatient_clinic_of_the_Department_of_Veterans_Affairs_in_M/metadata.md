# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6482?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6482
- Title: To rename the community-based outpatient clinic of the Department of Veterans Affairs in Michigan Center, Michigan, as the "Captain Herbert Elfring VA Clinic".
- Congress: 119
- Bill type: HR
- Bill number: 6482
- Origin chamber: House
- Introduced date: 2025-12-04
- Update date: 2026-01-09T09:06:50Z
- Update date including text: 2026-01-09T09:06:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-05 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-12-04: Introduced in House

## Actions

- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-05 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6482",
    "number": "6482",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "W000798",
        "district": "5",
        "firstName": "Tim",
        "fullName": "Rep. Walberg, Tim [R-MI-5]",
        "lastName": "Walberg",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "To rename the community-based outpatient clinic of the Department of Veterans Affairs in Michigan Center, Michigan, as the \"Captain Herbert Elfring VA Clinic\".",
    "type": "HR",
    "updateDate": "2026-01-09T09:06:50Z",
    "updateDateIncludingText": "2026-01-09T09:06:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-05",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-04",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-04",
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
          "date": "2025-12-04T14:00:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-05T14:10:33Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6482ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6482\nIN THE HOUSE OF REPRESENTATIVES\nDecember 4, 2025 Mr. Walberg introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo rename the community-based outpatient clinic of the Department of Veterans Affairs in Michigan Center, Michigan, as the Captain Herbert Elfring VA Clinic .\n#### 1. Designation of Captain Herbert Elfring VA Clinic\n##### (a) Designation\nThe outpatient clinic of the Department of Veterans Affairs located at 4328 Page Avenue in Michigan Center, Michigan, shall, after the date of the enactment of this Act, be known and designated as the Captain Herbert Elfring Department of Veterans Affairs Clinic or the Captain Herbert Elfring VA Clinic .\n##### (b) Reference\nAny reference in any law, regulation, map, document, paper, or other record of the United States to the community-based outpatient clinic referred to in subsection (a) shall be considered to be a reference to the Captain Herbert Elfring VA Clinic.",
      "versionDate": "2025-12-04",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-01-06T16:26:24Z"
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
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6482ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To rename the community-based outpatient clinic of the Department of Veterans Affairs in Michigan Center, Michigan, as the \"Captain Herbert Elfring VA Clinic\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-27T05:33:22Z"
    },
    {
      "title": "To rename the community-based outpatient clinic of the Department of Veterans Affairs in Michigan Center, Michigan, as the \"Captain Herbert Elfring VA Clinic\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-05T09:06:17Z"
    }
  ]
}
```
