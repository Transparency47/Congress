# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8726?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8726
- Title: PARTNERS Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8726
- Origin chamber: House
- Introduced date: 2026-05-11
- Update date: 2026-05-21T19:50:31Z
- Update date including text: 2026-05-21T19:50:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-11: Introduced in House
- 2026-05-11 - IntroReferral: Introduced in House
- 2026-05-11 - IntroReferral: Introduced in House
- 2026-05-11 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-11 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-05-11: Introduced in House

## Actions

- 2026-05-11 - IntroReferral: Introduced in House
- 2026-05-11 - IntroReferral: Introduced in House
- 2026-05-11 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-11 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-11",
    "latestAction": {
      "actionDate": "2026-05-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8726",
    "number": "8726",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "D000634",
        "district": "2",
        "firstName": "Troy",
        "fullName": "Rep. Downing, Troy [R-MT-2]",
        "lastName": "Downing",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "PARTNERS Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-21T19:50:31Z",
    "updateDateIncludingText": "2026-05-21T19:50:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-11",
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
      "actionDate": "2026-05-11",
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
      "actionDate": "2026-05-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-11",
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
          "date": "2026-05-11T14:32:15Z",
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
          "date": "2026-05-11T14:32:10Z",
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
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8726ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8726\nIN THE HOUSE OF REPRESENTATIVES\nMay 11, 2026 Mr. Downing (for himself and Mr. Doggett ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to allow States to enforce Medicare Advantage plan requirements.\n#### 1. Short title\nThis Act may be cited as the Protecting Authority and Restoring Tools Necessary for Enforcement by Regulatory States Act of 2026 or the PARTNERS Act of 2026 .\n#### 2. Allowing States to enforce Medicare Advantage plan requirements\nSection 1856(b)(3) of the Social Security Act ( 42 U.S.C. 1395w\u201326(b)(3) ) is amended\u2014\n**(1)**\nby striking The standards and inserting the following:\n(A) In general Subject to subparagraph (B), the standards ; and\n**(2)**\nby adding at the end the following new subparagraphs:\n(B) State enforcement Each State may require that MA organizations that issue, sell, renew, or offer MA plans in the State meet the requirements of this part with respect to such MA plans. (C) Coordination of enforcement The Secretary shall coordinate enforcement of the standards established under this part with the State in which an MA organization is licensed and any State in which the MA organization issues, sells, renews, or offers MA plans. The Secretary may enter into a collaborative enforcement agreement with any State to further coordinate enforcement. .",
      "versionDate": "2026-05-11",
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
        "updateDate": "2026-05-21T19:50:31Z"
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
      "date": "2026-05-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8726ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PARTNERS Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-13T09:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Authority and Restoring Tools Necessary for Enforcement by Regulatory States Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-13T09:08:25Z"
    },
    {
      "title": "PARTNERS Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-13T09:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to allow States to enforce Medicare Advantage plan requirements.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-13T09:03:26Z"
    }
  ]
}
```
