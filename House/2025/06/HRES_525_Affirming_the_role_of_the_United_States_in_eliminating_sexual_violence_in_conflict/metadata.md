# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/525?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/525
- Title: Affirming the role of the United States in eliminating sexual violence in conflict.
- Congress: 119
- Bill type: HRES
- Bill number: 525
- Origin chamber: House
- Introduced date: 2025-06-20
- Update date: 2026-01-21T09:05:23Z
- Update date including text: 2026-01-21T09:05:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-20: Introduced in House
- 2025-06-20 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-06-20 - IntroReferral: Submitted in House
- 2025-06-20 - IntroReferral: Submitted in House
- Latest action: 2025-06-20: Submitted in House

## Actions

- 2025-06-20 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-06-20 - IntroReferral: Submitted in House
- 2025-06-20 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-20",
    "latestAction": {
      "actionDate": "2025-06-20",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/525",
    "number": "525",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "M001188",
        "district": "6",
        "firstName": "Grace",
        "fullName": "Rep. Meng, Grace [D-NY-6]",
        "lastName": "Meng",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Affirming the role of the United States in eliminating sexual violence in conflict.",
    "type": "HRES",
    "updateDate": "2026-01-21T09:05:23Z",
    "updateDateIncludingText": "2026-01-21T09:05:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-20",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-06-20",
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
          "date": "2025-06-20T15:00:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-06-20",
      "state": "FL"
    },
    {
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "FL"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "PA"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2026-01-20",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres525ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 525\nIN THE HOUSE OF REPRESENTATIVES\nJune 20, 2025 Ms. Meng (for herself and Ms. Salazar ) submitted the following resolution; which was referred to the Committee on Foreign Affairs\nRESOLUTION\nAffirming the role of the United States in eliminating sexual violence in conflict.\nThat the House of Representatives\u2014\n**(1)**\naffirms the leadership and commitment of the United States Government in efforts to prevent and respond to conflict-related sexual violence and to support and protect all survivors of conflict-related sexual violence;\n**(2)**\nrecognizes that accountability for the perpetration of conflict-related sexual violence is important for comprehensive and lasting peace agreements;\n**(3)**\ncalls on the United States to ensure mechanisms to hold perpetrators of sexual violence accountable are included in peacebuilding resolutions and processes, and that women participate in such peace processes in accordance with the Women, Peace, and Security Act of 2017 ( Public Law 115\u201368 );\n**(4)**\ncalls on the United States to commit to strengthening justice for all conflict-related sexual violence survivors;\n**(5)**\nstands in solidarity with the survivors of conflict-related sexual violence, and those working to support them, to ensure survivors are not forgotten and get the care they need and deserve.",
      "versionDate": "2025-06-20",
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
        "name": "International Affairs",
        "updateDate": "2025-07-17T22:21:17Z"
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
      "date": "2025-06-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres525ih.xml"
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
      "title": "Affirming the role of the United States in eliminating sexual violence in conflict.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-21T08:18:22Z"
    },
    {
      "title": "Affirming the role of the United States in eliminating sexual violence in conflict.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-21T08:05:30Z"
    }
  ]
}
```
