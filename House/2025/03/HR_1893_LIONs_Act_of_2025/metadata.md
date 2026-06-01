# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1893?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1893
- Title: LIONs Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1893
- Origin chamber: House
- Introduced date: 2025-03-05
- Update date: 2026-01-22T09:06:11Z
- Update date including text: 2026-01-22T09:06:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-05: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Small Business.
- Latest action: 2025-03-05: Introduced in House

## Actions

- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Small Business.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1893",
    "number": "1893",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "T000488",
        "district": "13",
        "firstName": "Shri",
        "fullName": "Rep. Thanedar, Shri [D-MI-13]",
        "lastName": "Thanedar",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "LIONs Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-22T09:06:11Z",
    "updateDateIncludingText": "2026-01-22T09:06:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-05",
      "committees": {
        "item": {
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Small Business.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-05",
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
          "date": "2025-03-05T15:05:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Small Business Committee",
      "systemCode": "hssm00",
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
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "MO"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "IL"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "FL"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "IA"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "CA"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "WI"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-06-17",
      "state": "IL"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "OR"
    },
    {
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1893ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1893\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2025 Mr. Thanedar (for himself and Mr. Alford ) introduced the following bill; which was referred to the Committee on Small Business\nA BILL\nTo amend the Small Business Act and the Small Business Investment Act of 1958 to increase the maximum loan amount for certain loans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Loans In Our Neighborhoods Act of 2025 or the LIONs Act of 2025 .\n#### 2. Maximum loan amount for a 7 (a) loan\nSection 7(a)(3)(A) of the Small Business Act ( 15 U.S.C. 636(a)(3)(A) ) is amended by striking $3,750,000 (or if the gross loan amount would exceed $5,000,000) and inserting $7,500,000 (or if the gross loan amount would exceed $10,000,000) .\n#### 3. Maximum loan amount for a development company loan\nSection 502(2)(A) of the Small Business Investment Act of 1958 ( 15 U.S.C. 696(2)(A) ) is amended\u2014\n**(1)**\nby striking $5,000,000 each place it appears and inserting $10,000,000 ; and\n**(2)**\nby striking $5,500,000 each place it appears and inserting $10,000,000 .",
      "versionDate": "2025-03-05",
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
        "actionDate": "2025-06-26",
        "text": "Referred to the House Committee on Small Business."
      },
      "number": "4153",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Supporting Trade and Rebuilding Opportunity for National Growth Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-07-30",
        "text": "Referred to the Committee on Small Business and Entrepreneurship."
      },
      "number": "901",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "LIONs Act of 2025",
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
        "name": "Commerce",
        "updateDate": "2025-03-21T16:18:34Z"
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
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1893ih.xml"
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
      "title": "LIONs Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:08:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "LIONs Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Loans In Our Neighborhoods Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Small Business Act and the Small Business Investment Act of 1958 to increase the maximum loan amount for certain loans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:03:49Z"
    }
  ]
}
```
