# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/901?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/901
- Title: LIONs Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 901
- Origin chamber: Senate
- Introduced date: 2025-03-06
- Update date: 2025-12-05T21:57:37Z
- Update date including text: 2025-12-05T21:57:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-06: Introduced in Senate
- 2025-03-06 - IntroReferral: Introduced in Senate
- 2025-03-06 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- 2025-07-30 - IntroReferral: Referred to the Committee on Small Business and Entrepreneurship.
- 2025-07-30 - Discharge: Senate Committee on Banking, Housing, and Urban Affairs discharged by Unanimous Consent.
- 2025-07-30 - Committee: Senate Committee on Banking, Housing, and Urban Affairs discharged by Unanimous Consent.
- Latest action: 2025-03-06: Introduced in Senate

## Actions

- 2025-03-06 - IntroReferral: Introduced in Senate
- 2025-03-06 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- 2025-07-30 - IntroReferral: Referred to the Committee on Small Business and Entrepreneurship.
- 2025-07-30 - Discharge: Senate Committee on Banking, Housing, and Urban Affairs discharged by Unanimous Consent.
- 2025-07-30 - Committee: Senate Committee on Banking, Housing, and Urban Affairs discharged by Unanimous Consent.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/901",
    "number": "901",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "T000476",
        "district": "",
        "firstName": "Thomas",
        "fullName": "Sen. Tillis, Thomas [R-NC]",
        "lastName": "Tillis",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "LIONs Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:57:37Z",
    "updateDateIncludingText": "2025-12-05T21:57:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-30",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Small Business and Entrepreneurship.",
      "type": "IntroReferral"
    },
    {
      "actionDate": "2025-07-30",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Banking, Housing, and Urban Affairs discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2025-07-30",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on Banking, Housing, and Urban Affairs discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-06",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
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
        "item": {
          "date": "2025-07-31T02:48:17Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Small Business and Entrepreneurship Committee",
      "systemCode": "sssb00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": [
          {
            "date": "2025-07-31T02:46:57Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-03-06T20:32:38Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s901is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 901\nIN THE SENATE OF THE UNITED STATES\nMarch 6, 2025 Mr. Tillis introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Small Business Act and the Small Business Investment Act of 1958 to increase the maximum loan amount for certain loans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Loans In Our Neighborhoods Act of 2025 or the LIONs Act of 2025 .\n#### 2. Maximum loan amount for a 7 (a) loan\nSection 7(a)(3)(A) of the Small Business Act ( 15 U.S.C. 636(a)(3)(A) ) is amended by striking $3,750,000 (or if the gross loan amount would exceed $5,000,000) and inserting $7,500,000 (or if the gross loan amount would exceed $10,000,000) .\n#### 3. Maximum loan amount for a development company loan\nSection 502(2)(A) of the Small Business Investment Act of 1958 ( 15 U.S.C. 696(2)(A) ) is amended\u2014\n**(1)**\nby striking $5,000,000 each place it appears and inserting $10,000,000 ; and\n**(2)**\nby striking $5,500,000 each place it appears and inserting $10,000,000 .",
      "versionDate": "2025-03-06",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s901rcs.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 901\nIN THE SENATE OF THE UNITED STATES\nMarch 6, 2025 Mr. Tillis introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nJuly 30, 2025 Committee discharged; referred to the Committee on Small Business and Entrepreneurship\nA BILL\nTo amend the Small Business Act and the Small Business Investment Act of 1958 to increase the maximum loan amount for certain loans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Loans In Our Neighborhoods Act of 2025 or the LIONs Act of 2025 .\n#### 2. Maximum loan amount for a 7 (a) loan\nSection 7(a)(3)(A) of the Small Business Act ( 15 U.S.C. 636(a)(3)(A) ) is amended by striking $3,750,000 (or if the gross loan amount would exceed $5,000,000) and inserting $7,500,000 (or if the gross loan amount would exceed $10,000,000) .\n#### 3. Maximum loan amount for a development company loan\nSection 502(2)(A) of the Small Business Investment Act of 1958 ( 15 U.S.C. 696(2)(A) ) is amended\u2014\n**(1)**\nby striking $5,000,000 each place it appears and inserting $10,000,000 ; and\n**(2)**\nby striking $5,500,000 each place it appears and inserting $10,000,000 .",
      "versionDate": "2025-07-30",
      "versionType": "Reference Change Senate"
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
        "actionDate": "2025-03-05",
        "text": "Referred to the House Committee on Small Business."
      },
      "number": "1893",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "LIONs Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-03-28T12:55:42Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s901is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-07-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s901rcs.xml"
        }
      ],
      "type": "Reference Change Senate"
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
      "updateDate": "2025-07-31T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "LIONs Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T03:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Loans In Our Neighborhoods Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T03:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Small Business Act and the Small Business Investment Act of 1958 to increase the maximum loan amount for certain loans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T03:18:46Z"
    }
  ]
}
```
