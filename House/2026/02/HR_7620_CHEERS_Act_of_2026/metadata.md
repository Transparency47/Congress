# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7620?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7620
- Title: CHEERS Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7620
- Origin chamber: House
- Introduced date: 2026-02-20
- Update date: 2026-04-22T08:07:32Z
- Update date including text: 2026-04-22T08:07:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-20: Introduced in House
- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-02-20: Introduced in House

## Actions

- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-20",
    "latestAction": {
      "actionDate": "2026-02-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7620",
    "number": "7620",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "L000585",
        "district": "16",
        "firstName": "Darin",
        "fullName": "Rep. LaHood, Darin [R-IL-16]",
        "lastName": "LaHood",
        "party": "R",
        "state": "IL"
      }
    ],
    "title": "CHEERS Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-22T08:07:32Z",
    "updateDateIncludingText": "2026-04-22T08:07:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-20",
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
      "actionDate": "2026-02-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-20",
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
          "date": "2026-02-20T16:30:50Z",
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
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "NV"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "NY"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "WA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "DC"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7620ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7620\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 20, 2026 Mr. LaHood (for himself, Mr. Horsford , Ms. Tenney , and Ms. DelBene ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to classify qualified energy-efficient draft alcohol property as 15-year property for purposes of depreciation.\n#### 1. Short title\nThis Act may be cited as the Creating Hospitality Economic Enhancement for Restaurants and Servers Act of 2026 or the CHEERS Act of 2026 .\n#### 2. Classification of qualified energy-efficient draft alcohol property as 15-year property for purposes of depreciation\n##### (a) Classification as 15-year property\nSection 168(e)(3)(E) of the Internal Revenue Code of 1986 is amended by striking and at the end of clause (vi), by striking the period at the end of clause (vii) and inserting , and , and by adding at the end the following new clause:\n(viii) any qualified energy-efficient draft alcohol property. .\n##### (b) Definition of qualified energy-efficient draft alcohol property\nSection 168(i) of such Code is amended by adding at the end the following new paragraph:\n(20) Qualified energy-efficient draft alcohol property The term qualified energy-efficient draft alcohol property means any property\u2014 (A) which is installed on or in any building which is located in the United States, (B) which is principally used in the conduct of a trade or business of operating a restaurant, bar, or entertainment venue, and (C) which is a stainless steel or aluminum container or related commercial tap equipment used for the distribution and sale of alcohol. .\n##### (c) Effective date\nThe amendments made by subsections (a) and (b) shall apply to property placed in service after December 31, 2025.\n##### (d) Regulatory authority\nThe Secretary of the Treasury shall prescribe such regulations or other guidance as may be necessary or appropriate to carry out the purposes of the amendments made by subsections (a) and (b), including to provide for the appropriate application of section 168 of the Internal Revenue Code of 1986 with respect to taxpayers who rent or lease qualified energy-efficient draft alcohol property (as defined in section 168(i)(20) of the Internal Revenue Code of 1986).",
      "versionDate": "2026-02-20",
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
        "updateDate": "2026-02-23T22:15:09Z"
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
      "date": "2026-02-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7620ih.xml"
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
      "title": "CHEERS Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-21T09:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CHEERS Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-21T09:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Creating Hospitality Economic Enhancement for Restaurants and Servers Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-21T09:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to classify qualified energy-efficient draft alcohol property as 15-year property for purposes of depreciation.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-21T09:18:36Z"
    }
  ]
}
```
