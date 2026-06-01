# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3572?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3572
- Title: To make projects in certain counties eligible for funding under the rural surface transportation grant program, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 3572
- Origin chamber: House
- Introduced date: 2025-05-21
- Update date: 2025-11-20T09:06:49Z
- Update date including text: 2025-11-20T09:06:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-21: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-22 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-05-21: Introduced in House

## Actions

- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-22 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-21",
    "latestAction": {
      "actionDate": "2025-05-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3572",
    "number": "3572",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "V000129",
        "district": "22",
        "firstName": "David",
        "fullName": "Rep. Valadao, David G. [R-CA-22]",
        "lastName": "Valadao",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "To make projects in certain counties eligible for funding under the rural surface transportation grant program, and for other purposes.",
    "type": "HR",
    "updateDate": "2025-11-20T09:06:49Z",
    "updateDateIncludingText": "2025-11-20T09:06:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-22",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-21",
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
          "date": "2025-05-21T14:02:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-05-22T18:50:13Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "F000480",
      "district": "20",
      "firstName": "Vince",
      "fullName": "Rep. Fong, Vince [R-CA-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Fong",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "CA"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "FL"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "CA"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "CA"
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
      "sponsorshipDate": "2025-10-17",
      "state": "VA"
    },
    {
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3572ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3572\nIN THE HOUSE OF REPRESENTATIVES\nMay 21, 2025 Mr. Valadao (for himself, Mr. Fong , Mrs. Cherfilus-McCormick , and Mr. Costa ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo make projects in certain counties eligible for funding under the rural surface transportation grant program, and for other purposes.\n#### 1. Rural surface transportation grant program\nSection 173 of title 23, United States Code, is amended\u2014\n**(1)**\nin subsection (a) by adding at the end the following:\n(3) Covered county The term covered county means a county that has an annual gross agricultural production value of at least $1,000,000,000 and agricultural production of at least $500,000 per square mile, for all crops and livestock sold, adjusted annually for inflation in accordance with the Consumer Price Index published by the Bureau of Labor Statistics of the Department of Labor. (4) Farm-to-market road The term farm-to-market road means a road located within a covered county. ;\n**(2)**\nin subsection (i) by striking subsection (k)(1) and inserting paragraphs (1) and (4) of subsection (k) ;\n**(3)**\nin subsection (k)\u2014\n**(A)**\nby redesignating paragraph (4) as paragraph (5);\n**(B)**\nby inserting after paragraph (3) the following:\n(4) Farm-to-market roads The Secretary shall reserve 10 percent of the amounts made available for the program for each fiscal year to provide grants for eligible projects located on farm-to-market roads in any amount. ; and\n**(C)**\nin paragraph (5) (as so redesignated) by striking or (3) and inserting (3), or (4) ; and\n**(4)**\nby adding at the end the following:\n(p) Eligible covered counties The Secretary, in consultation with the Secretary of Agriculture, shall create, and annually update, a list of covered counties. .",
      "versionDate": "2025-05-21",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-06-02T14:52:02Z"
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
      "date": "2025-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3572ih.xml"
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
      "title": "To make projects in certain counties eligible for funding under the rural surface transportation grant program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-31T04:18:35Z"
    },
    {
      "title": "To make projects in certain counties eligible for funding under the rural surface transportation grant program, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-22T12:22:31Z"
    }
  ]
}
```
