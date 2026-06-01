# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2959?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2959
- Title: Passport Sanity Act
- Congress: 119
- Bill type: S
- Bill number: 2959
- Origin chamber: Senate
- Introduced date: 2025-10-01
- Update date: 2026-01-06T21:48:46Z
- Update date including text: 2026-01-06T21:48:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-01: Introduced in Senate
- 2025-10-01 - IntroReferral: Introduced in Senate
- 2025-10-01 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-10-01: Introduced in Senate

## Actions

- 2025-10-01 - IntroReferral: Introduced in Senate
- 2025-10-01 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-01",
    "latestAction": {
      "actionDate": "2025-10-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2959",
    "number": "2959",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "M001198",
        "district": "",
        "firstName": "Roger",
        "fullName": "Sen. Marshall, Roger [R-KS]",
        "lastName": "Marshall",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Passport Sanity Act",
    "type": "S",
    "updateDate": "2026-01-06T21:48:46Z",
    "updateDateIncludingText": "2026-01-06T21:48:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-01",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-10-01T14:46:47Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-10-01",
      "state": "TN"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-10-01",
      "state": "NE"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-10-01",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2959is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2959\nIN THE SENATE OF THE UNITED STATES\nOctober 1, 2025 Mr. Marshall (for himself, Mrs. Blackburn , Mr. Ricketts , and Mrs. Moody ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo prohibit the Secretary of State from issuing a passport, passport card, or Consular Report of Birth Abroad that includes the unspecified X gender designation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Passport Sanity Act .\n#### 2. Prohibition regarding certain gender designation on passports, passport cards, and Consular Reports of Birth Abroad issued by Department of State\n##### (a) Defined term\nIn this section, the term covered document means a passport, passport card, or Consular Report of Birth Abroad issued by the Department of State.\n##### (b) In general\nThe Secretary of State shall\u2014\n**(1)**\nensure each application for a covered document only includes the gender designation male or female; and\n**(2)**\nprohibit the issuance of a covered document that includes the unspecified X gender designation.",
      "versionDate": "2025-10-01",
      "versionType": "Introduced in Senate"
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
        "name": "International Affairs",
        "updateDate": "2026-01-06T21:48:46Z"
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
      "date": "2025-10-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2959is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Passport Sanity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-16T02:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Passport Sanity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-16T02:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the Secretary of State from issuing a passport, passport card, or Consular Report of Birth Abroad that includes the unspecified \"X\" gender designation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-16T02:48:25Z"
    }
  ]
}
```
