# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/806?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/806
- Title: Supporting the recognition of October 2025 as "National Breast Cancer Awareness Month".
- Congress: 119
- Bill type: HRES
- Bill number: 806
- Origin chamber: House
- Introduced date: 2025-10-14
- Update date: 2025-12-11T15:38:02Z
- Update date including text: 2025-12-11T15:38:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-14: Introduced in House
- 2025-10-14 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-10-14 - IntroReferral: Submitted in House
- 2025-10-14 - IntroReferral: Submitted in House
- Latest action: 2025-10-14: Submitted in House

## Actions

- 2025-10-14 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-10-14 - IntroReferral: Submitted in House
- 2025-10-14 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-14",
    "latestAction": {
      "actionDate": "2025-10-14",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/806",
    "number": "806",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001103",
        "district": "1",
        "firstName": "Earl",
        "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
        "lastName": "Carter",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Supporting the recognition of October 2025 as \"National Breast Cancer Awareness Month\".",
    "type": "HRES",
    "updateDate": "2025-12-11T15:38:02Z",
    "updateDateIncludingText": "2025-12-11T15:38:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-14",
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
      "actionCode": "H11100",
      "actionDate": "2025-10-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-10-14",
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
          "date": "2025-10-14T18:01:50Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2025-10-14",
      "state": "OH"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "CA"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "NY"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres806ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 806\nIN THE HOUSE OF REPRESENTATIVES\nOctober 14, 2025 Mr. Carter of Georgia (for himself, Mr. Miller of Ohio , Mr. DeSaulnier , Mr. Morelle , and Ms. Wasserman Schultz ) submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nSupporting the recognition of October 2025 as National Breast Cancer Awareness Month .\nThat the House of Representatives supports the recognition of National Breast Cancer Awareness Month .",
      "versionDate": "2025-10-14",
      "versionType": "IH"
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
        "updateDate": "2025-12-11T15:38:02Z"
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
      "date": "2025-10-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres806ih.xml"
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
      "title": "Supporting the recognition of October 2025 as \"National Breast Cancer Awareness Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-15T08:48:14Z"
    },
    {
      "title": "Supporting the recognition of October 2025 as \"National Breast Cancer Awareness Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-15T08:05:36Z"
    }
  ]
}
```
