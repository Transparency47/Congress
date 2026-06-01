# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1264?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1264
- Title: USA Batteries Act
- Congress: 119
- Bill type: HR
- Bill number: 1264
- Origin chamber: House
- Introduced date: 2025-02-12
- Update date: 2025-05-05T19:58:18Z
- Update date including text: 2025-05-05T19:58:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-12: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-12: Introduced in House

## Actions

- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-12",
    "latestAction": {
      "actionDate": "2025-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1264",
    "number": "1264",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M001204",
        "district": "9",
        "firstName": "Daniel",
        "fullName": "Rep. Meuser, Daniel [R-PA-9]",
        "lastName": "Meuser",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "USA Batteries Act",
    "type": "HR",
    "updateDate": "2025-05-05T19:58:18Z",
    "updateDateIncludingText": "2025-05-05T19:58:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-12",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-12",
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
          "date": "2025-02-12T15:00:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "MI"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "TX"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "PA"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "NY"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1264ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1264\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2025 Mr. Meuser (for himself, Mr. Moolenaar , Mr. Nehls , Mr. Fitzpatrick , Ms. Malliotakis , and Mr. Perry ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to eliminate lead oxide, antimony, and sulfuric acid as taxable chemicals under the Superfund excise taxes.\n#### 1. Short title\nThis Act may be cited as the USA Batteries Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe Superfund fee established in Public Law 117\u201358 makes American manufacturing less competitive by imposing a tax on chemicals used in domestic battery production that is not levied on imported batteries.\n**(2)**\nAmerica\u2019s lead battery industry has a manufacturing capacity of more than 165 GWh, a $23.6 billion domestic economic impact annually, and creates more than 25,000 direct jobs in 38 States.\n**(3)**\nLead batteries have a 99 percent recycling rate and are a truly sustainable energy storage technology.\n**(4)**\nLead batteries are critical for many sectors, including defense, transportation, logistics, telecommunications, and energy generation.\n**(5)**\nIncreased taxes on domestic production create a disadvantage for American manufacturers and reduce the global competitiveness of the domestic lead battery industry by increasing the costs of key raw materials.\n#### 3. Elimination of lead oxide, antimony, and sulfuric acid as taxable chemicals under Superfund excise taxes\nThe table in section 4661(b) of the Internal Revenue Code of 1986 is amended by striking the rows relating to lead oxide, antimony, and sulfuric acid.",
      "versionDate": "2025-02-12",
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
        "name": "Taxation",
        "updateDate": "2025-05-05T19:58:18Z"
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
      "date": "2025-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1264ih.xml"
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
      "title": "USA Batteries Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T15:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "USA Batteries Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T15:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to eliminate lead oxide, antimony, and sulfuric acid as taxable chemicals under the Superfund excise taxes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T15:18:33Z"
    }
  ]
}
```
