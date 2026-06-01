# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5892?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5892
- Title: Keep Main Street Open Act
- Congress: 119
- Bill type: HR
- Bill number: 5892
- Origin chamber: House
- Introduced date: 2025-10-31
- Update date: 2025-11-10T14:24:29Z
- Update date including text: 2025-11-10T14:24:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-10-31: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Referred to the House Committee on Small Business.
- Latest action: 2025-10-31: Introduced in House

## Actions

- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Referred to the House Committee on Small Business.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-31",
    "latestAction": {
      "actionDate": "2025-10-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5892",
    "number": "5892",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "S001230",
        "district": "10",
        "firstName": "Suhas",
        "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
        "lastName": "Subramanyam",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Keep Main Street Open Act",
    "type": "HR",
    "updateDate": "2025-11-10T14:24:29Z",
    "updateDateIncludingText": "2025-11-10T14:24:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-31",
      "committees": {
        "item": {
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Small Business.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-31",
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
          "date": "2025-10-31T17:05:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Small Business Committee",
      "systemCode": "hssm00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5892ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5892\nIN THE HOUSE OF REPRESENTATIVES\nOctober 31, 2025 Mr. Subramanyam introduced the following bill; which was referred to the Committee on Small Business\nA BILL\nTo require the Administrator of the Small Business Administration to carry out a loan program for eligible applicants during the shutdown, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Keep Main Street Open Act .\n#### 2. Loans for eligible applicants during the shutdown\n##### (a) In general\nThe Administrator of the Small Business Administration shall carry out a program under which an eligible applicant may receive a covered loan during a shutdown.\n##### (b) Terms\nA covered loan made under this section shall\u2014\n**(1)**\nbe in an amount equal to the losses estimated by the eligible applicant due to the shutdown;\n**(2)**\nbear a maximum interest rate of one percent; and\n**(3)**\nhave a maximum maturity of one year from the date on which the shutdown is terminated.\n##### (c) Definitions\nIn this Act:\n**(1) Eligible applicant**\nThe term eligible applicant has the meaning given the term eligible recipient in section 7(a)(36) of the Small Business Act ( 15 U.S.C. 636(a)(36) ).\n**(2) Covered loan**\nThe term covered loan means a loan made under section 7(a) of the Small Business Act ( 15 U.S.C. 636(a) ).\n**(3) Shutdown**\nThe term shutdown means the period\u2014\n**(A)**\nbeginning on the first day on which there is a partial or full lapse in appropriations; and\n**(B)**\nending on the date that is 30 days after the date of the enactment of appropriations.",
      "versionDate": "2025-10-31",
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
        "name": "Commerce",
        "updateDate": "2025-11-10T14:24:29Z"
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
      "date": "2025-10-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5892ih.xml"
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
      "title": "Keep Main Street Open Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-08T05:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Keep Main Street Open Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-08T05:38:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Administrator of the Small Business Administration to carry out a loan program for eligible applicants during the shutdown, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-08T05:33:19Z"
    }
  ]
}
```
