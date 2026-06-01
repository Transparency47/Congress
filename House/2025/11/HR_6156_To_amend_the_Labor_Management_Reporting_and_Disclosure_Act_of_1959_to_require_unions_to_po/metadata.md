# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6156?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6156
- Title: Endorsement Transparency Act
- Congress: 119
- Bill type: HR
- Bill number: 6156
- Origin chamber: House
- Introduced date: 2025-11-19
- Update date: 2026-05-16T08:07:40Z
- Update date including text: 2026-05-16T08:07:40Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6156",
    "number": "6156",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "O000177",
        "district": "3",
        "firstName": "Robert",
        "fullName": "Rep. Onder, Robert F. [R-MO-3]",
        "lastName": "Onder",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Endorsement Transparency Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:40Z",
    "updateDateIncludingText": "2026-05-16T08:07:40Z"
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
          "date": "2025-11-19T15:01:40Z",
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
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "NC"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2026-05-15",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6156ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6156\nIN THE HOUSE OF REPRESENTATIVES\nNovember 19, 2025 Mr. Onder (for himself and Mr. Harris of North Carolina ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Labor-Management Reporting and Disclosure Act of 1959 to require unions to poll their members prior to endorsing a presidential candidate.\n#### 1. Short title\nThis Act may be cited as the Endorsement Transparency Act .\n#### 2. Requirement to poll members prior to presidential endorsement\n##### (a) In general\nTitle I of the Labor-Management Reporting and Disclosure Act of 1959 ( 29 U.S.C. 411 et seq. ) is amended by adding at the end the following:\n106. Requirement to endorse a presidential candidate No labor organization may endorse a candidate in an election for the office of President of the United States unless the labor organization\u2014 (1) polls the members of the labor organization with respect to such an endorsement; and (2) discloses the result of the poll described in paragraph (1) to the members of the labor organization. .\n##### (b) Effective date\nThe amendment made by this Act shall take effect on the date that is 12 months after the date of enactment of this Act.",
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
        "updateDate": "2025-12-09T13:45:19Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6156ih.xml"
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
      "title": "Endorsement Transparency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-04T13:08:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Endorsement Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-04T13:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Labor-Management Reporting and Disclosure Act of 1959 to require unions to poll their members prior to endorsing a presidential candidate.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-04T13:03:43Z"
    }
  ]
}
```
