# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6799?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6799
- Title: BRIDGE for Young-Onset Alzheimer’s Disease Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6799
- Origin chamber: House
- Introduced date: 2025-12-17
- Update date: 2026-05-21T08:07:52Z
- Update date including text: 2026-05-21T08:07:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-12-17: Introduced in House

## Actions

- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-17",
    "latestAction": {
      "actionDate": "2025-12-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6799",
    "number": "6799",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "K000397",
        "district": "40",
        "firstName": "Young",
        "fullName": "Rep. Kim, Young [R-CA-40]",
        "lastName": "Kim",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "BRIDGE for Young-Onset Alzheimer\u2019s Disease Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-21T08:07:52Z",
    "updateDateIncludingText": "2026-05-21T08:07:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-17",
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
      "actionDate": "2025-12-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-17",
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
          "date": "2025-12-17T14:06:25Z",
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
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NY"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "NE"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NC"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "CT"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "MO"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "VA"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "NY"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6799ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6799\nIN THE HOUSE OF REPRESENTATIVES\nDecember 17, 2025 Mrs. Kim (for herself, Mr. Goldman of New York , Mr. Bacon , and Mrs. Foushee ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend title II of the Social Security Act to eliminate the waiting periods for disability insurance benefits and Medicare coverage for individuals with young-onset Alzheimer\u2019s, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Bridging Relief in Delayed Government Enrollment for Young-Onset Alzheimer\u2019s Disease Act of 2025 or the BRIDGE for Young-Onset Alzheimer\u2019s Disease Act of 2025 .\n#### 2. Elimination of waiting period for individuals with young-onset Alzheimer\u2019s\n##### (a) In general\nSection 223(a) of the Social Security Act ( 42 U.S.C. 423(a) ) is amended\u2014\n**(1)**\nin paragraph (1), in the matter following subparagraph (E), by inserting or young-onset Alzheimer\u2019s (as defined by the Commissioner through the Program Operations Manual System or a successor document) after amyotrophic lateral sclerosis ; and\n**(2)**\nin paragraph (2)(B), by inserting or (iii) after clause (ii) .\n##### (b) Effective date\nThe amendments made by this section shall apply with respect to applications for disability insurance benefits filed after the date that is 5 months before the date of the enactment of this Act.\n#### 3. Waiver of 24-month waiting period for Medicare coverage of individuals with young-onset Alzheimers\u2019s\n##### (a) In general\nSection 226(h) of the Social Security Act ( 42 U.S.C. 426(h) ) is amended by inserting or young-onset Alzheimer\u2019s (as defined by the Commissioner through the Program Operations Manual System or a successor document) after amyotrophic lateral sclerosis (ALS) .\n##### (b) Effective date\nThe amendments made by this section shall apply to benefits for months beginning after the date of the enactment of this Act.",
      "versionDate": "2025-12-17",
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
        "updateDate": "2026-01-22T15:16:52Z"
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
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6799ih.xml"
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
      "title": "BRIDGE for Young-Onset Alzheimer\u2019s Disease Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "BRIDGE for Young-Onset Alzheimer\u2019s Disease Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T05:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Bridging Relief in Delayed Government Enrollment for Young-Onset Alzheimer\u2019s Disease Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T05:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title II of the Social Security Act to eliminate the waiting periods for disability insurance benefits and Medicare coverage for individuals with young-onset Alzheimer's, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T05:18:38Z"
    }
  ]
}
```
