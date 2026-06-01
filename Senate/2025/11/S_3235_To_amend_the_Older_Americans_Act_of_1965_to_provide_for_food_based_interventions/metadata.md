# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3235?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3235
- Title: DINE Act
- Congress: 119
- Bill type: S
- Bill number: 3235
- Origin chamber: Senate
- Introduced date: 2025-11-20
- Update date: 2025-12-06T13:34:10Z
- Update date including text: 2025-12-06T13:34:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in Senate
- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-11-20: Introduced in Senate

## Actions

- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3235",
    "number": "3235",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "DINE Act",
    "type": "S",
    "updateDate": "2025-12-06T13:34:10Z",
    "updateDateIncludingText": "2025-12-06T13:34:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T17:05:21Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "CT"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "NJ"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "NY"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3235is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3235\nIN THE SENATE OF THE UNITED STATES\nNovember 20, 2025 Mr. Markey (for himself, Mr. Blumenthal , Mr. Kim , and Mrs. Gillibrand ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Older Americans Act of 1965 to provide for food-based interventions.\n#### 1. Short title\nThis Act may be cited as the Disease Intervention through Nutrition Education Act or the DINE Act .\n#### 2. Food-based interventions\n##### (a) Definition of disease prevention and health promotion services\nSection 102(14) of the Older Americans Act of 1965 ( 42 U.S.C. 3002(14) ) is amended\u2014\n**(1)**\nin subparagraph (B), by inserting screening for eligibility for Federal and non-Federal (including community-based) food is medicine programs and before routine ;\n**(2)**\nin subparagraph (C), by inserting , including referrals to Federal and non-Federal (including community-based) food is medicine programs, if appropriate after caregivers ; and\n**(3)**\nin subparagraph (D), by inserting (including from medically tailored meals and produce prescriptions) after improved nutrition .\n##### (b) Administration of nutrition services\nSection 205(a)(2)(A) of the Older Americans Act of 1965 ( 42 U.S.C. 3016(a)(2)(A) ) is amended\u2014\n**(1)**\nin clause (vi), by inserting , including the use of innovative approaches, including food-based interventions, such as produce prescriptions after systems ; and\n**(2)**\nin clause (viii), by inserting and innovative approaches, including intervention programs, such as produce prescriptions, after including strategies .\n##### (c) Nutrition education\nSection 214(2)(C) of the Older Americans Act of 1965 ( 42 U.S.C. 3020e(2)(C) ) is amended\u2014\n**(1)**\nby inserting interventions and after other ; and\n**(2)**\nby inserting and referral to food-based intervention programs after and counseling .",
      "versionDate": "2025-11-20",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2025-12-06T13:34:10Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3235is.xml"
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
      "title": "DINE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-05T04:08:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "DINE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-05T04:08:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Disease Intervention through Nutrition Education Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-05T04:08:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Older Americans Act of 1965 to provide for food-based interventions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-05T04:03:51Z"
    }
  ]
}
```
