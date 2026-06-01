# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/881?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/881
- Title: Renewable Fuel for Ocean-Going Vessels Act
- Congress: 119
- Bill type: S
- Bill number: 881
- Origin chamber: Senate
- Introduced date: 2025-03-06
- Update date: 2025-12-06T07:01:14Z
- Update date including text: 2025-12-06T07:01:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-06: Introduced in Senate
- 2025-03-06 - IntroReferral: Introduced in Senate
- 2025-03-06 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- 2025-09-10 - Committee: Committee on Environment and Public Works. Hearings held.
- Latest action: 2025-03-06: Introduced in Senate

## Actions

- 2025-03-06 - IntroReferral: Introduced in Senate
- 2025-03-06 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- 2025-09-10 - Committee: Committee on Environment and Public Works. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/881",
    "number": "881",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "R000618",
        "district": "",
        "firstName": "Pete",
        "fullName": "Sen. Ricketts, Pete [R-NE]",
        "lastName": "Ricketts",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Renewable Fuel for Ocean-Going Vessels Act",
    "type": "S",
    "updateDate": "2025-12-06T07:01:14Z",
    "updateDateIncludingText": "2025-12-06T07:01:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-10",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Environment and Public Works. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-06",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-06",
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
            "date": "2025-09-10T14:48:53Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-03-06T17:41:10Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "MN"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "IA"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s881is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 881\nIN THE SENATE OF THE UNITED STATES\nMarch 6, 2025 Mr. Ricketts (for himself and Ms. Klobuchar ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo amend the Clean Air Act to include fuel for ocean-going vessels as additional renewable fuel for which credits may be generated under the renewable fuel program.\n#### 1. Short title\nThis Act may be cited as the Renewable Fuel for Ocean-Going Vessels Act .\n#### 2. Renewable fuel for ocean-going vessels\n##### (a) Definitions\nSection 211(o)(1)(A) of the Clean Air Act ( 42 U.S.C. 7545(o)(1)(A) ) is amended by striking fossil fuel present in home heating oil or jet fuel and inserting fossil fuel present in home heating oil, fuel for ocean-going vessels, or jet fuel .\n##### (b) Applicability\nThe amendment made by subsection (a) shall apply beginning with respect to the second calendar year beginning after the date of enactment of this Act.\n##### (c) Regulations\nNot later than 1 year after the date of enactment of this Act, the Administrator of the Environmental Protection Agency shall promulgate such regulations as may be necessary to implement the amendment made by subsection (a).\n##### (d) Report to Congress\nNot later than 1 year after the date of promulgating the final regulations required under subsection (c), the Administrator of the Environmental Protection Agency shall submit to the Committee on Energy and Commerce of the House of Representatives and the Committee on Environment and Public Works of the Senate a report describing the implementation of the amendment made by subsection (a) and the regulations promulgated under subsection (c).",
      "versionDate": "2025-03-06",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-06",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "1896",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Renewable Fuel for Ocean-Going Vessels Act",
      "type": "HR"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Alternative and renewable resources",
            "updateDate": "2025-09-12T16:17:24Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-09-12T16:17:24Z"
          },
          {
            "name": "Marine and inland water transportation",
            "updateDate": "2025-09-12T16:17:24Z"
          },
          {
            "name": "Marine pollution",
            "updateDate": "2025-09-12T16:17:24Z"
          },
          {
            "name": "Oil and gas",
            "updateDate": "2025-09-12T16:17:24Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-03-28T13:11:36Z"
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
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s881is.xml"
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
      "title": "Renewable Fuel for Ocean-Going Vessels Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-11T11:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Renewable Fuel for Ocean-Going Vessels Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T18:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Clean Air Act to include fuel for ocean-going vessels as additional renewable fuel for which credits may be generated under the renewable fuel program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T18:03:18Z"
    }
  ]
}
```
