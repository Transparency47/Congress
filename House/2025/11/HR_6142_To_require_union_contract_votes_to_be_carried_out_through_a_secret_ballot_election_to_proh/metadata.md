# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6142?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6142
- Title: Ask the Union Members Act
- Congress: 119
- Bill type: HR
- Bill number: 6142
- Origin chamber: House
- Introduced date: 2025-11-19
- Update date: 2025-12-09T13:43:29Z
- Update date including text: 2025-12-09T13:43:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-19: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-11-19: Introduced in House

## Actions

- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-19",
    "latestAction": {
      "actionDate": "2025-11-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6142",
    "number": "6142",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "H001102",
        "district": "8",
        "firstName": "Mark",
        "fullName": "Rep. Harris, Mark [R-NC-8]",
        "lastName": "Harris",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Ask the Union Members Act",
    "type": "HR",
    "updateDate": "2025-12-09T13:43:29Z",
    "updateDateIncludingText": "2025-12-09T13:43:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-19",
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
      "actionDate": "2025-11-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-19",
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
          "date": "2025-11-19T15:02:15Z",
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
      "bioguideId": "O000177",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Onder, Robert F. [R-MO-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Onder",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "MO"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6142ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6142\nIN THE HOUSE OF REPRESENTATIVES\nNovember 19, 2025 Mr. Harris of North Carolina (for himself, Mr. Onder , and Mr. Fine ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo require union contract votes to be carried out through a secret ballot election, to prohibit unions from authorizing strikes unless a majority of members of the union vote to authorize a strike, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Ask the Union Members Act .\n#### 2. Secret ballot for ratification and strike authorization\n##### (a) Contract ratification requirements\nSection 101(a) of the Labor-Management Reporting and Disclosure Act of 1959 ( 29 U.S.C. 411(a) ) is amended by adding at the end the following:\n(6) Contract ratification A collective bargaining agreement may not be executed by a labor organization unless such agreement is approved to be ratified by a majority vote of the members of such labor organization in good standing voting in a referendum conducted by secret ballot, after providing such agreement to each member of the labor organization not later than 72 hours prior to such referendum. .\n##### (b) Strike authorization requirements\nSection 8(b) of the National Labor Relations Act ( 29 U.S.C. 158(b) ) is amended\u2014\n**(1)**\nin paragraph (6), by striking and at the end;\n**(2)**\nin paragraph (7), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(8) to authorize a strike, unless such strike is approved to be authorized by a majority vote of the members in good standing voting in a referendum conducted by secret ballot. .\n##### (c) Effective date\nThe amendments made by this Act shall take effect beginning on the date that is 18 months after the date of enactment of this Act.",
      "versionDate": "2025-11-19",
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
        "updateDate": "2025-12-09T13:43:29Z"
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
      "date": "2025-11-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6142ih.xml"
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
      "title": "Ask the Union Members Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-29T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Ask the Union Members Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-29T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require union contract votes to be carried out through a secret ballot election, to prohibit unions from authorizing strikes unless a majority of members of the union vote to authorize a strike, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-29T05:18:19Z"
    }
  ]
}
```
