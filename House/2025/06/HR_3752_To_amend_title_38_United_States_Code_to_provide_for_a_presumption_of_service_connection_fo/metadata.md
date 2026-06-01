# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3752?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3752
- Title: Specialist Fourth Class Keith Smith Glioblastoma Parity Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3752
- Origin chamber: House
- Introduced date: 2025-06-05
- Update date: 2025-12-12T09:06:59Z
- Update date including text: 2025-12-12T09:06:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-05: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-06-23 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- Latest action: 2025-06-05: Introduced in House

## Actions

- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Introduced in House
- 2025-06-05 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-06-23 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-05",
    "latestAction": {
      "actionDate": "2025-06-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3752",
    "number": "3752",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001127",
        "district": "20",
        "firstName": "Sheila",
        "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
        "lastName": "Cherfilus-McCormick",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Specialist Fourth Class Keith Smith Glioblastoma Parity Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-12T09:06:59Z",
    "updateDateIncludingText": "2025-12-12T09:06:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-23",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Disability Assistance and Memorial Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-05",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-05",
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
          "date": "2025-06-05T14:05:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-23T15:40:51Z",
              "name": "Referred to"
            }
          },
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "IA"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "MO"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "IA"
    },
    {
      "bioguideId": "M001233",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Messmer, Mark B. [R-IN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Messmer",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-10-31",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3752ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3752\nIN THE HOUSE OF REPRESENTATIVES\nJune 5, 2025 Mrs. Cherfilus-McCormick (for herself and Mrs. Hinson ) introduced the following bill; which was referred to the Committee on Veterans\u2019 Affairs\nA BILL\nTo amend title 38, United States Code, to provide for a presumption of service connection for glioblastoma multiforme for veterans who served in certain locations during the Vietnam era.\n#### 1. Short title\nThis Act may be cited as the Specialist Fourth Class Keith Smith Glioblastoma Parity Act of 2025 .\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nBetween 1961 and 1971, approximately 19,000,000 gallons of 15 different herbicides were sprayed over the southern region of Vietnam by the United States Armed Forces, including 13,000,000 gallons of Agent Orange.\n**(2)**\nBetween 1968 and 1971, a total of 6,500 spraying missions were carried out in an area of about 1,500,000 hectares, which represented about 12 percent of South Vietnam and portions of Laos and Cambodia.\n**(3)**\nStudies have found that tens of thousands of Americans were exposed to Agent Orange during the spraying operations.\n**(4)**\nAgent Orange exposure continues to negatively affect the lives of veterans of the United States Armed Forces, Vietnamese people, Vietnamese Americans, and their children, and has cut short, the lives of many victims with others living with disease, disabilities, and pain that is often untreated or unrecognized.\n#### 3. Presumption of service-connection for veterans who served in certain locations during the Vietnam era\nSection 1116(a)(2) of title 38, United States Code, is amended by adding at the end the following new subparagraph:\n(N) Glioblastoma multiforme. .",
      "versionDate": "2025-06-05",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-06-24T18:11:21Z"
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
      "date": "2025-06-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3752ih.xml"
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
      "title": "Specialist Fourth Class Keith Smith Glioblastoma Parity Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-11T09:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Specialist Fourth Class Keith Smith Glioblastoma Parity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-11T09:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to provide for a presumption of service connection for glioblastoma multiforme for veterans who served in certain locations during the Vietnam era.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-11T09:33:26Z"
    }
  ]
}
```
