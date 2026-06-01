# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6406?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6406
- Title: Parental Workforce Training Act
- Congress: 119
- Bill type: HR
- Bill number: 6406
- Origin chamber: House
- Introduced date: 2025-12-03
- Update date: 2026-01-05T16:30:04Z
- Update date including text: 2026-01-05T16:30:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-03: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-12-03: Introduced in House

## Actions

- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-03",
    "latestAction": {
      "actionDate": "2025-12-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6406",
    "number": "6406",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "M001226",
        "district": "8",
        "firstName": "Robert",
        "fullName": "Rep. Menendez, Robert [D-NJ-8]",
        "lastName": "Menendez",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Parental Workforce Training Act",
    "type": "HR",
    "updateDate": "2026-01-05T16:30:04Z",
    "updateDateIncludingText": "2026-01-05T16:30:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-03",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-03",
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
          "date": "2025-12-03T15:02:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "MN"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "MI"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "IN"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-12-05",
      "state": "OH"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "RI"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6406ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6406\nIN THE HOUSE OF REPRESENTATIVES\nDecember 3, 2025 Mr. Menendez (for himself, Ms. Omar , Ms. Tlaib , Ms. Simon , and Mr. Carson ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo establish a grant program to provide assistance to eligible individuals to cover the costs of childcare services.\n#### 1. Short title\nThis Act may be cited as the Parental Workforce Training Act .\n#### 2. Childcare grant program\n##### (a) Grants authorized\nFrom the amount appropriated under subsection (f), and not later than 1 year after the date of enactment of this Act, the Secretary of Labor shall award grants, on a competitive basis, to local boards to provide assistance to eligible individuals to cover the costs of childcare services as supportive services.\n##### (b) Application\nTo be eligible to receive a grant under this Act, a local board shall submit an application to the Secretary, at such time, in such manner, and containing such information as the Secretary may require.\n##### (c) Uses of funds\nA local board that receives a grant under this Act shall provide funds to eligible individuals who are participating in an employment and training activity in the local area served by such local board, for such individuals to cover the costs of childcare services as supportive services with the childcare provider of their choice, so long as such childcare provider is in compliance with all applicable State and local laws related to quality requirements and standards for providing childcare services.\n##### (d) Report\nNot later than 1 year after the date that the Secretary awards the first grant under subsection (a), the Secretary shall submit to Congress a report on the effect of the grants on the individuals who received assistance, including the enrollment and completion rates of such individuals in employment and training activities.\n##### (e) Definitions\nIn this Act:\n**(1) Eligible individuals**\nThe term eligible individual means an individual who\u2014\n**(A)**\nhas one or more dependent children; and\n**(B)**\nis participating in an employment and training activity.\n**(2) WIOA terms**\nThe terms employment and training activity , local area , local board , and supportive services have the meanings given such terms in section 3 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3102 ).\n##### (f) Authorization of appropriations\nThere are authorized to be appropriated $10,000,000 to carry out this Act.",
      "versionDate": "2025-12-03",
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
        "name": "Labor and Employment",
        "updateDate": "2026-01-05T16:30:03Z"
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
      "date": "2025-12-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6406ih.xml"
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
      "title": "Parental Workforce Training Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-23T06:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Parental Workforce Training Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-23T06:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a grant program to provide assistance to eligible individuals to cover the costs of childcare services.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-23T06:18:23Z"
    }
  ]
}
```
