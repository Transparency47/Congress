# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4701?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4701
- Title: Charting My Path for Future Success Act
- Congress: 119
- Bill type: HR
- Bill number: 4701
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2025-12-05T22:56:40Z
- Update date including text: 2025-12-05T22:56:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4701",
    "number": "4701",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "M001208",
        "district": "6",
        "firstName": "Lucy",
        "fullName": "Rep. McBath, Lucy [D-GA-6]",
        "lastName": "McBath",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Charting My Path for Future Success Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:56:40Z",
    "updateDateIncludingText": "2025-12-05T22:56:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
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
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:06:15Z",
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
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "VA"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "True",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "True",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4701ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4701\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Mrs. McBath (for herself, Mr. Vindman , Mr. Vargas , Mr. DeSaulnier , and Ms. Jacobs ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo direct the Secretary of Education to reissue the solicitation and award the contract relating to the Charting My Path for Future Success project.\n#### 1. Short title\nThis Act may be cited as the Charting My Path for Future Success Act .\n#### 2. Charting My Path for Future Success Project\n##### (a) In general\nNot later than 90 days after the date of enactment of this Act, the Secretary of Education shall reissue the solicitation and award a contract described in subsection (b) as if the contract described in such subsection had not previously been awarded.\n##### (b) Contract description\nThe contract described in this subsection is the contract that was awarded, pursuant to section 664(e)(1) of the Individuals with Disabilities Education Act ( 20 U.S.C. 1464(e)(1) ), to a nonprofit organization to carry out the Charting My Path for Future Success project that\u2014\n**(1)**\naims to help families and high schools to support students with disabilities to reach their goals during and after high school, by training educators to assist such students to\u2014\n**(A)**\nset goals that help build skills to be successful in school and life;\n**(B)**\ndevelop action plans related to those goals; and\n**(C)**\nreflect on their progress toward those goals and adjust goals or action plans when needed; and\n**(2)**\nunder which, in January 2025, following the completion of training with the project, 61 educators began to assist 1,600 high school students in 62 high schools in 13 local educational agencies.\n##### (c) Prohibition of cancellation of contract\nA contract awarded under this section may not be canceled without the approval of Congress.",
      "versionDate": "2025-07-23",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-07-23",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "2407",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Charting My Path for Future Success Act",
      "type": "S"
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
        "name": "Education",
        "updateDate": "2025-09-17T16:46:56Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4701ih.xml"
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
      "title": "Charting My Path for Future Success Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-08T04:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Charting My Path for Future Success Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-08T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Education to reissue the solicitation and award the contract relating to the Charting My Path for Future Success project.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-08T04:33:18Z"
    }
  ]
}
```
