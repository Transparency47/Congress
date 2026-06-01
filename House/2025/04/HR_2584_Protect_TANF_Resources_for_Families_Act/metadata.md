# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2584?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2584
- Title: Protect TANF Resources for Families Act
- Congress: 119
- Bill type: HR
- Bill number: 2584
- Origin chamber: House
- Introduced date: 2025-04-01
- Update date: 2026-05-30T19:41:22Z
- Update date including text: 2026-05-30T19:41:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-01: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-04-01: Introduced in House

## Actions

- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-01",
    "latestAction": {
      "actionDate": "2025-04-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2584",
    "number": "2584",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "T000478",
        "district": "24",
        "firstName": "Claudia",
        "fullName": "Rep. Tenney, Claudia [R-NY-24]",
        "lastName": "Tenney",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Protect TANF Resources for Families Act",
    "type": "HR",
    "updateDate": "2026-05-30T19:41:22Z",
    "updateDateIncludingText": "2026-05-30T19:41:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-01",
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
      "actionDate": "2025-04-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-01",
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
          "date": "2025-04-01T14:05:00Z",
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
      "bioguideId": "B001314",
      "district": "4",
      "firstName": "Aaron",
      "fullName": "Rep. Bean, Aaron [R-FL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Bean",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "FL"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2584ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2584\nIN THE HOUSE OF REPRESENTATIVES\nApril 1, 2025 Ms. Tenney (for herself and Mr. Bean of Florida ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend part A of title IV of the Social Security Act to ensure that Federal funds provided under the program of block grants to States for temporary assistance for needy families are used to supplement State spending, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protect TANF Resources for Families Act .\n#### 2. Prohibition on State diversion of Federal funds to replace State spending\n##### (a) In general\nSection 404 of the Social Security Act ( 42 U.S.C. 604 ) is amended by adding at the end the following:\n(l) Limitation on use of Federal funds To replace State general revenue funds A State shall use Federal funds received under this part only to supplement funds that, in the absence of the Federal funds, would be made available from State and local sources for programs assisted under this part, and not to supplant the funds. .\n##### (b) State certification\nSection 402(a) of such Act ( 42 U.S.C. 602(a) ) is amended by adding at the end the following:\n(9) Certification of State supplementation A certification by the chief executive officer of the State that the funds provided to the State under this part will not be used to supplant State or non-Federal funds for services and activities that promote the purposes of this part. .\n##### (c) Effective date\nThe amendments made by this section shall take effect on October 1, 2025.\n#### 3. Two-year reauthorization of the Temporary Assistance for Needy Families program\nActivities authorized by part A of title IV (other than under section 403(c) or 418) and section 1108(b) of the Social Security Act shall continue through September 30, 2026, in the manner authorized for fiscal year 2023, and out of any money in the Treasury of the United States not otherwise appropriated, there are hereby appropriated such sums as may be necessary for such purpose.",
      "versionDate": "2025-04-01",
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
        "name": "Social Welfare",
        "updateDate": "2025-04-09T13:58:58Z"
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
      "date": "2025-04-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2584ih.xml"
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
      "title": "Protect TANF Resources for Families Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-09T03:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protect TANF Resources for Families Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-09T03:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend part A of title IV of the Social Security Act to ensure that Federal funds provided under the program of block grants to States for temporary assistance for needy families are used to supplement State spending, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-09T03:33:20Z"
    }
  ]
}
```
