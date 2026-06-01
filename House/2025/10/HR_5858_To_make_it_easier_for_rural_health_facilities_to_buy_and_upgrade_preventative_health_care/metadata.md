# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5858?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5858
- Title: CATCH IT Act
- Congress: 119
- Bill type: HR
- Bill number: 5858
- Origin chamber: House
- Introduced date: 2025-10-28
- Update date: 2026-04-03T08:05:48Z
- Update date including text: 2026-04-03T08:05:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-28: Introduced in House
- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-10-28: Introduced in House

## Actions

- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Introduced in House
- 2025-10-28 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-28",
    "latestAction": {
      "actionDate": "2025-10-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5858",
    "number": "5858",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "S001221",
        "district": "3",
        "firstName": "Hillary",
        "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
        "lastName": "Scholten",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "CATCH IT Act",
    "type": "HR",
    "updateDate": "2026-04-03T08:05:48Z",
    "updateDateIncludingText": "2026-04-03T08:05:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-28",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-28",
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
          "date": "2025-10-28T17:03:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "IA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5858ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5858\nIN THE HOUSE OF REPRESENTATIVES\nOctober 28, 2025 Ms. Scholten (for herself and Mrs. Hinson ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo make it easier for rural health facilities to buy and upgrade preventative health care equipment through the Community Facilities Grant Program of the Department of Agriculture.\n#### 1. Short title\nThis Act may be cited as the Community Access to Treatment and Care for Health through Increased Testing Act or the CATCH IT Act .\n#### 2. Increase in Federal share of cost of preventative health care equipment for rural health facility under the Community Facilities Grant Program\nSection 306(a)(19)(B) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1926(a)(19)(B) ) is amended\u2014\n**(1)**\nin clause (iii), by adding at the end the following: The Federal share determined under the preceding sentence shall be increased by 25 percentage points if the development of the facility includes the purchase or upgrading of preventative health care equipment. ; and\n**(2)**\nby adding at the end the following:\n(iv) Preventative health care equipment defined In clause (iii), the term preventative health care equipment includes equipment such as the following: (I) Advanced breast imaging equipment that may be used in a digital breast tomosynthesis or 3-dimensional mammography. (II) Mobile cancer screening unit. (III) Laboratory equipment that may be used in multi-cancer early detection or diagnostic cancer screening. (IV) Colorectal cancer screening equipment. (V) Computerized tomography scanner. (VI) Diagnostic ultrasound equipment. .\n#### 3. Effective date\nThe amendments made by this Act shall take effect on the 1st day of the 1st Federal fiscal year that begins on or after the date of the enactment of this Act.",
      "versionDate": "2025-10-28",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-11-26T15:25:05Z"
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
      "date": "2025-10-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5858ih.xml"
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
      "title": "CATCH IT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-30T09:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CATCH IT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-30T09:38:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Community Access to Treatment and Care for Health through Increased Testing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-30T09:38:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To make it easier for rural health facilities to buy and upgrade preventative health care equipment through the Community Facilities Grant Program of the Department of Agriculture.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-30T09:33:18Z"
    }
  ]
}
```
