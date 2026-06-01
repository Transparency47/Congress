# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6990?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6990
- Title: PROTECT Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 6990
- Origin chamber: House
- Introduced date: 2026-01-08
- Update date: 2026-02-27T14:23:51Z
- Update date including text: 2026-02-27T14:23:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-08: Introduced in House
- 2026-01-08 - IntroReferral: Introduced in House
- 2026-01-08 - IntroReferral: Introduced in House
- 2026-01-08 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-01-08: Introduced in House

## Actions

- 2026-01-08 - IntroReferral: Introduced in House
- 2026-01-08 - IntroReferral: Introduced in House
- 2026-01-08 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-08",
    "latestAction": {
      "actionDate": "2026-01-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6990",
    "number": "6990",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "S001215",
        "district": "11",
        "firstName": "Haley",
        "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
        "lastName": "Stevens",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "PROTECT Act of 2026",
    "type": "HR",
    "updateDate": "2026-02-27T14:23:51Z",
    "updateDateIncludingText": "2026-02-27T14:23:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-08",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-08",
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
          "date": "2026-01-08T15:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "MI"
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
      "sponsorshipDate": "2026-01-08",
      "state": "PA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "MI"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "NY"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "MI"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "VA"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6990ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 6990\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 8, 2026 Ms. Stevens (for herself, Mrs. Dingell , Mr. Fitzpatrick , Ms. Tlaib , Mr. Lawler , Ms. Scholten , and Mrs. Kiggans of Virginia ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Administrator of the Environmental Protection Agency to issue a final rule adding as a class all perfluoroalkyl and polyfluoroalkyl substances with at least one fully fluorinated carbon atom to the list of hazardous air pollutants under section 112(b) of the Clean Air Act ( 42 U.S.C. 7412(b) ), and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Prevent Release Of Toxic Emissions, Contamination, and Transfer Act of 2026 or the PROTECT Act of 2026 .\n#### 2. Listing of perfluoroalkyl and polyfluoroalkyl substances as hazardous air pollutants\n##### (a) Listing\nNot later than 180 days after the date of enactment of this Act, the Administrator of the Environmental Protection Agency shall issue a final rule adding as a class all perfluoroalkyl and polyfluoroalkyl substances with at least one fully fluorinated carbon atom to the list of hazardous air pollutants under section 112(b) of the Clean Air Act ( 42 U.S.C. 7412(b) ).\n##### (b) Sources categories\nNot later than 365 days after the final rule is issued pursuant to subsection (a), the Administrator of the Environmental Protection Agency shall revise the list under section 112(c)(1) of the Clean Air Act ( 42 U.S.C. 7412(c)(1) ) to include categories and subcategories of major sources and area sources of perfluoroalkyl and polyfluoroalkyl substances listed pursuant to such final rule.",
      "versionDate": "2026-01-08",
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
        "name": "Environmental Protection",
        "updateDate": "2026-02-27T14:23:51Z"
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
      "date": "2026-01-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6990ih.xml"
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
      "title": "PROTECT Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-24T08:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PROTECT Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-24T08:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Prevent Release Of Toxic Emissions, Contamination, and Transfer Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-24T08:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Administrator of the Environmental Protection Agency to issue a final rule adding as a class all perfluoroalkyl and polyfluoroalkyl substances with at least one fully fluorinated carbon atom to the list of hazardous air pollutants under section 112(b) of the Clean Air Act (42 U.S.C. 7412(b)), and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-24T08:48:31Z"
    }
  ]
}
```
