# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8109?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8109
- Title: Save Struggling Hospitals Act
- Congress: 119
- Bill type: HR
- Bill number: 8109
- Origin chamber: House
- Introduced date: 2026-03-26
- Update date: 2026-04-29T08:06:58Z
- Update date including text: 2026-04-29T08:06:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-03-26: Introduced in House

## Actions

- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8109",
    "number": "8109",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "K000392",
        "district": "8",
        "firstName": "David",
        "fullName": "Rep. Kustoff, David [R-TN-8]",
        "lastName": "Kustoff",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Save Struggling Hospitals Act",
    "type": "HR",
    "updateDate": "2026-04-29T08:06:58Z",
    "updateDateIncludingText": "2026-04-29T08:06:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-26",
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
      "actionDate": "2026-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-26",
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
          "date": "2026-03-26T14:01:15Z",
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
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "AL"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "TN"
    },
    {
      "bioguideId": "F000459",
      "district": "3",
      "firstName": "Charles",
      "fullName": "Rep. Fleischmann, Charles J. \"Chuck\" [R-TN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Fleischmann",
      "middleName": "J. \"Chuck\"",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "TN"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "AL"
    },
    {
      "bioguideId": "D000616",
      "district": "4",
      "firstName": "Scott",
      "fullName": "Rep. DesJarlais, Scott [R-TN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "DesJarlais",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8109ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8109\nIN THE HOUSE OF REPRESENTATIVES\nMarch 26, 2026 Mr. Kustoff (for himself and Ms. Sewell ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend title XVIII of the Social Security Act to codify the Medicare low-wage index hospital policy.\n#### 1. Short title\nThis Act may be cited as the Save Struggling Hospitals Act .\n#### 2. Codification of the Medicare low-wage index hospital policy\nSection 1886(d)(3)(E) of the Social Security Act ( 42 U.S.C. 1395ww(d)(3)(E) ) is amended\u2014\n**(1)**\nin clause (i), in the first sentence, by striking or (iv) and inserting , (iv), or (v) ; and\n**(2)**\nby adding at the end the following new clause:\n(v) Area wage index adjustment for low-wage hospitals (I) In general For discharges occurring on or after October 1, 2019, the area wage index applicable under this subparagraph for a fiscal year to a hospital with an area wage index (determined without regard to this clause) below the 25th percentile area wage index shall be increased by \u00bd of the difference between the otherwise applicable final area wage index for such fiscal year for such hospital and the 25th percentile area wage index for such fiscal year across all hospitals. (II) Budget neutrality Pursuant to the fourth sentence of clause (i), this clause shall be applied in a budget neutral manner. Any adjustments made for the purposes of such application of budget neutrality may not\u2014 (aa) decrease the area wage index applicable under this subparagraph to a hospital with an area wage index (determined without regard to this clause) below the 75th percentile area wage index for the fiscal year; or (bb) result in an area wage index applicable under this subparagraph to a hospital for such fiscal year that is less than 95 percent of the area wage index applicable under this subparagraph to such hospital for the preceding fiscal year. .",
      "versionDate": "2026-03-26",
      "versionType": "Introduced in House"
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
        "actionDate": "2026-03-26",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "4233",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Save Struggling Hospitals Act",
      "type": "S"
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
        "updateDate": "2026-04-13T18:29:04Z"
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
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8109ih.xml"
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
      "title": "Save Struggling Hospitals Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-10T06:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Save Struggling Hospitals Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-10T06:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to codify the Medicare low-wage index hospital policy.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-10T06:03:34Z"
    }
  ]
}
```
