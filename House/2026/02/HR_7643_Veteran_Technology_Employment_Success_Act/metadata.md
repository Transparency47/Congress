# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7643?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7643
- Title: Veteran Technology Employment Success Act
- Congress: 119
- Bill type: HR
- Bill number: 7643
- Origin chamber: House
- Introduced date: 2026-02-23
- Update date: 2026-05-08T08:06:07Z
- Update date including text: 2026-05-08T08:06:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-23: Introduced in House
- 2026-02-23 - IntroReferral: Introduced in House
- 2026-02-23 - IntroReferral: Introduced in House
- 2026-02-23 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-03-16 - Committee: Referred to the Subcommittee on Economic Opportunity.
- Latest action: 2026-02-23: Introduced in House

## Actions

- 2026-02-23 - IntroReferral: Introduced in House
- 2026-02-23 - IntroReferral: Introduced in House
- 2026-02-23 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-03-16 - Committee: Referred to the Subcommittee on Economic Opportunity.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-23",
    "latestAction": {
      "actionDate": "2026-02-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7643",
    "number": "7643",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "W000831",
        "district": "11",
        "firstName": "James",
        "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
        "lastName": "Walkinshaw",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Veteran Technology Employment Success Act",
    "type": "HR",
    "updateDate": "2026-05-08T08:06:07Z",
    "updateDateIncludingText": "2026-05-08T08:06:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-16",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Opportunity.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-23",
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
      "actionDate": "2026-02-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-23",
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
          "date": "2026-02-23T17:01:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-03-16T17:54:44Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
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
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "KY"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-05-07",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7643ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7643\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 23, 2026 Mr. Walkinshaw (for himself and Mr. McGarvey ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to improve the manner in which the Secretary of Veterans Affairs calculates the average employment rate of veterans participating in the VET TEC high technology program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veteran Technology Employment Success Act .\n#### 2. Employment rate calculation for VET-TEC high technology program\nSection 3699C of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (f)\u2014\n**(A)**\nin the matter preceding paragraph (1) by inserting after House of Representatives the following: , and make available to the public, ; and\n**(B)**\nin paragraph (3) by adding at the end the following: Such rate shall be calculated as a fraction, the denominator of which is the number of covered individuals who completed such a program during such year and the numerator of which is the number of individuals counted in the denominator who are employed on the date that is 180 days after the date on which the individual completed the program, and expressed as a percentage. Notwithstanding the previous sentence, the numerator shall not count a case in which the individual is employed by the same organization that was the provider of the individual\u2019s program of education or a case in which the individual is employed, by a parent or affiliate of such organization, as an instructor for a substantially similar program of education. To the maximum extent practicable, the Secretary shall also report the rates of full-time employment, part-time employment, and self-employment. ; and\n**(2)**\nin subsection (g) by adding at the end the following new paragraph:\n(3) The Secretary on an ongoing basis shall solicit, collect, and analyze feedback about the program from covered individuals who participate in the program and from the GI Bill School Feedback Tool. The Secretary shall use such feedback to evaluate and improve the implementation of the program. .",
      "versionDate": "2026-02-23",
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
        "updateDate": "2026-03-11T23:02:48Z"
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
      "date": "2026-02-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7643ih.xml"
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
      "title": "Veteran Technology Employment Success Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-10T06:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veteran Technology Employment Success Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-10T06:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to improve the manner in which the Secretary of Veterans Affairs calculates the average employment rate of veterans participating in the VET TEC high technology program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-10T06:48:28Z"
    }
  ]
}
```
