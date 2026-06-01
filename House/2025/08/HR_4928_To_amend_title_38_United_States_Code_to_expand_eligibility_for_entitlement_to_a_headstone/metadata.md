# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4928?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4928
- Title: GRAVE Act
- Congress: 119
- Bill type: HR
- Bill number: 4928
- Origin chamber: House
- Introduced date: 2025-08-08
- Update date: 2025-12-20T09:07:01Z
- Update date including text: 2025-12-20T09:07:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-08-08: Introduced in House
- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-12-19 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- Latest action: 2025-08-08: Introduced in House

## Actions

- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-12-19 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-08",
    "latestAction": {
      "actionDate": "2025-08-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4928",
    "number": "4928",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "L000599",
        "district": "17",
        "firstName": "Michael",
        "fullName": "Rep. Lawler, Michael [R-NY-17]",
        "lastName": "Lawler",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "GRAVE Act",
    "type": "HR",
    "updateDate": "2025-12-20T09:07:01Z",
    "updateDateIncludingText": "2025-12-20T09:07:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-19",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Disability Assistance and Memorial Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-08",
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
      "actionDate": "2025-08-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-08",
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
          "date": "2025-08-08T15:32:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-19T19:11:35Z",
              "name": "Referred to"
            }
          },
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4928ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4928\nIN THE HOUSE OF REPRESENTATIVES\nAugust 8, 2025 Mr. Lawler introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to expand eligibility for entitlement to a headstone or grave marker under the laws administered by the Secretary of Veterans Affairs to certain members of a Reserve of an Armed Force, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Giving Reservists A Valiant Eternity Act or the GRAVE Act .\n#### 2. Expansion of entitlement to headstone or grave marker under laws administered by Secretary of Veterans Affairs\nParagraph (5) of section 2306(a) of title 38, United States Code, is amended to read as follows:\n(5) A member (or former member) of a Reserve of an Armed Force who is not a veteran solely by reason of not meeting the minimum active-duty service requirements under section 5303A of this title. .",
      "versionDate": "2025-08-08",
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
        "updateDate": "2025-09-05T15:30:21Z"
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
      "date": "2025-08-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4928ih.xml"
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
      "title": "GRAVE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-12T03:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "GRAVE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-12T03:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Giving Reservists A Valiant Eternity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-12T03:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to expand eligibility for entitlement to a headstone or grave marker under the laws administered by the Secretary of Veterans Affairs to certain members of a Reserve of an Armed Force, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-12T03:18:33Z"
    }
  ]
}
```
