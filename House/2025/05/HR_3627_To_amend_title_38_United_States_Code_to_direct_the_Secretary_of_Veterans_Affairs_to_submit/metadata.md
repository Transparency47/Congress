# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3627?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3627
- Title: Justice for America’s Veterans and Survivors Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3627
- Origin chamber: House
- Introduced date: 2025-05-29
- Update date: 2026-02-04T04:26:32Z
- Update date including text: 2026-02-04T04:26:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-29: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-06-06 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- 2025-06-24 - Committee: Subcommittee Hearings Held
- Latest action: 2025-05-29: Introduced in House

## Actions

- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-06-06 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- 2025-06-24 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-29",
    "latestAction": {
      "actionDate": "2025-05-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3627",
    "number": "3627",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "E000246",
        "district": "11",
        "firstName": "Chuck",
        "fullName": "Rep. Edwards, Chuck [R-NC-11]",
        "lastName": "Edwards",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Justice for America\u2019s Veterans and Survivors Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-04T04:26:32Z",
    "updateDateIncludingText": "2026-02-04T04:26:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-24",
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
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-06",
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
      "actionDate": "2025-05-29",
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
      "actionDate": "2025-05-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-29",
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
          "date": "2025-05-29T15:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-06-24T18:14:39Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-06-06T18:14:21Z",
                "name": "Referred to"
              }
            ]
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
      "bioguideId": "M001234",
      "district": "3",
      "firstName": "Kelly",
      "fullName": "Rep. Morrison, Kelly [D-MN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Morrison",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "MN"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "NC"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-08-29",
      "state": "VA"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NV"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "CO"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-12-23",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3627ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3627\nIN THE HOUSE OF REPRESENTATIVES\nMay 29, 2025 Mr. Edwards (for himself and Ms. Morrison ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to direct the Secretary of Veterans Affairs to submit an annual report that contains data and information on the causes of deaths among veterans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Justice for America\u2019s Veterans and Survivors Act of 2025 .\n#### 2. Department of Veterans Affairs annual report on causes of death among veterans\n##### (a) In general\nSubchaper II of chapter 5 of title 38, United States Code, is amended by adding at the end the following new section:\n534. Annual report on causes of death among veterans (a) In general The Secretary shall submit to the Committees on Veterans\u2019 Affairs of the House of Representatives and the Senate an annual report that contains data and information on causes of death among veterans. (b) Elements Such report shall include\u2014 (1) for each veteran that died during the period covered by the report\u2014 (A) an identification of\u2014 (i) whether such veteran had a service-connected disability rated as total; (ii) the primary cause of death; and (iii) the secondary cause of death, if applicable; and (B) a statement of whether such veteran died by suicide secondary to a service-connected disability rated as total; (2) for each primary cause of death identified pursuant to paragraph (1), a statement of the total number of veterans that died from such primary cause of death during the period covered by the report. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of chapter 5 of such title is amended by inserting after the item relating to section 533 the following new item:\n534. Annual report on causes of death among veterans .",
      "versionDate": "2025-05-29",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-26T17:49:40Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-06-26T17:49:46Z"
          },
          {
            "name": "Veterans' pensions and compensation",
            "updateDate": "2025-06-26T17:49:50Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-06-10T22:50:27Z"
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
      "date": "2025-05-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3627ih.xml"
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
      "title": "Justice for America\u2019s Veterans and Survivors Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-03T04:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Justice for America\u2019s Veterans and Survivors Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to direct the Secretary of Veterans Affairs to submit an annual report that contains data and information on the causes of deaths among veterans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T04:18:34Z"
    }
  ]
}
```
