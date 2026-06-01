# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6361?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6361
- Title: Ban AI Denials in Medicare Act
- Congress: 119
- Bill type: HR
- Bill number: 6361
- Origin chamber: House
- Introduced date: 2025-12-02
- Update date: 2026-01-08T09:07:02Z
- Update date including text: 2026-01-08T09:07:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-02: Introduced in House
- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-02 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-12-02: Introduced in House

## Actions

- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-02 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-02",
    "latestAction": {
      "actionDate": "2025-12-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6361",
    "number": "6361",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "L000601",
        "district": "1",
        "firstName": "Greg",
        "fullName": "Rep. Landsman, Greg [D-OH-1]",
        "lastName": "Landsman",
        "party": "D",
        "state": "OH"
      }
    ],
    "title": "Ban AI Denials in Medicare Act",
    "type": "HR",
    "updateDate": "2026-01-08T09:07:02Z",
    "updateDateIncludingText": "2026-01-08T09:07:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-02",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-02",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-02",
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
          "date": "2025-12-02T15:01:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-12-02T15:01:20Z",
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
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "NJ"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "CA"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6361ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6361\nIN THE HOUSE OF REPRESENTATIVES\nDecember 2, 2025 Mr. Landsman (for himself and Mrs. Watson Coleman ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo prohibit the Secretary of Health and Human Services from testing the WISeR model, and to amend title XI of the Social Security Act to prohibit the implementation of payment models testing prior authorization under traditional Medicare.\n#### 1. Short title\nThis Act may be cited as the Ban AI Denials in Medicare Act .\n#### 2. Prohibiting implementation of Center for Medicare and Medicaid Innovation models testing prior authorization under traditional Medicare\n##### (a) Prohibiting implementation of WISeR model\nThe Secretary of Health and Human Services may not implement the innovative payment and service delivery model described in the notice titled Medicare Program; Implementation of Prior Authorization for Select Services for the Wasteful and Inappropriate Services Reduction (WISeR) Model (90 Fed. Reg. 28749 (July 1, 2025)), or any substantially similar model.\n##### (b) Prohibiting implementation of future CMI models testing prior authorization (including through the use of AI) under traditional Medicare\nSection 1115A(b)(2) of the Social Security Act ( 42 U.S.C. 1315a(b)(2) ) is amended\u2014\n**(1)**\nin subparagraph (A), by striking The Secretary shall select and inserting Subject to the limitation under subparagraph (D), the Secretary shall select ; and\n**(2)**\nby adding at the end the following new subparagraph:\n(D) Limitation on models to be tested Beginning on the date of the enactment of this subparagraph, the Secretary may not select a model to be tested under subparagraph (A) if such model would provide for the implementation of prior authorization (including through the use of artificial intelligence) with respect to items or services for which payment may be made under part A or part B of title XVIII. .",
      "versionDate": "2025-12-02",
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
        "name": "Health",
        "updateDate": "2025-12-04T15:45:17Z"
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
      "date": "2025-12-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6361ih.xml"
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
      "title": "Ban AI Denials in Medicare Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-03T09:23:34Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Ban AI Denials in Medicare Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-03T09:23:34Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the Secretary of Health and Human Services from testing the WISeR model, and to amend title XI of the Social Security Act to prohibit the implementation of payment models testing prior authorization under traditional Medicare.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-03T09:18:31Z"
    }
  ]
}
```
