# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2074?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2074
- Title: Servicemembers’ Credit Monitoring Enhancement Act
- Congress: 119
- Bill type: S
- Bill number: 2074
- Origin chamber: Senate
- Introduced date: 2025-06-12
- Update date: 2026-03-17T11:29:12Z
- Update date including text: 2026-03-17T11:29:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-12: Introduced in Senate
- 2025-06-12 - IntroReferral: Introduced in Senate
- 2025-06-12 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- 2026-03-05 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S877-878; text: CR S877-878)
- 2026-03-05 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2026-03-05 - Discharge: Senate Committee on Banking, Housing, and Urban Affairs discharged by Unanimous Consent.
- 2026-03-05 - Committee: Senate Committee on Banking, Housing, and Urban Affairs discharged by Unanimous Consent.
- 2026-03-16 - Floor: Message on Senate action sent to the House.
- 2026-03-16 15:00:33 - Floor: Received in the House.
- 2026-03-16 15:06:10 - Floor: Held at the desk.
- Latest action: 2025-06-12: Introduced in Senate

## Actions

- 2025-06-12 - IntroReferral: Introduced in Senate
- 2025-06-12 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- 2026-03-05 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S877-878; text: CR S877-878)
- 2026-03-05 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2026-03-05 - Discharge: Senate Committee on Banking, Housing, and Urban Affairs discharged by Unanimous Consent.
- 2026-03-05 - Committee: Senate Committee on Banking, Housing, and Urban Affairs discharged by Unanimous Consent.
- 2026-03-16 - Floor: Message on Senate action sent to the House.
- 2026-03-16 15:00:33 - Floor: Received in the House.
- 2026-03-16 15:06:10 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2074",
    "number": "2074",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Servicemembers\u2019 Credit Monitoring Enhancement Act",
    "type": "S",
    "updateDate": "2026-03-17T11:29:12Z",
    "updateDateIncludingText": "2026-03-17T11:29:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2026-03-16",
      "actionTime": "15:06:10",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2026-03-16",
      "actionTime": "15:00:33",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-03-16",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-03-05",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate without amendment by Unanimous Consent. (consideration: CR S877-878; text: CR S877-878)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2026-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-03-05",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Banking, Housing, and Urban Affairs discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2026-03-05",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on Banking, Housing, and Urban Affairs discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-12",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-12",
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
        "item": [
          {
            "date": "2026-03-05T21:26:45Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-06-12T19:39:22Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "ND"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "NJ"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "MT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2074is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2074\nIN THE SENATE OF THE UNITED STATES\nJune 12, 2025 Ms. Klobuchar (for herself, Mr. Cramer , Mr. Kim , and Mr. Daines ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Fair Credit Reporting Act to expand the definition of an active duty military consumer for purposes of certain credit monitoring requirements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Servicemembers\u2019 Credit Monitoring Enhancement Act .\n#### 2. Credit monitoring\n##### (a) In general\nThe Fair Credit Reporting Act ( 15 U.S.C. 1681 et seq. ) is amended\u2014\n**(1)**\nin section 605A(k) ( 15 U.S.C. 1681c\u20131(k) )\u2014\n**(A)**\nby striking paragraph (1) and inserting the following:\n(1) Definitions In this subsection: (A) Armed forces The term armed forces has the meaning given the term in section 101(a) of title 10, United States Code. (B) Armed forces member consumer The term armed forces member consumer means a consumer who, regardless of duty status, is a member of the armed forces. ; and\n**(B)**\nin paragraph (2)(A), by striking active duty military consumer and inserting armed forces member consumer ; and\n**(2)**\nin section 625(b)(1)(K) ( 15 U.S.C. 1681t(b)(1)(K) ), by striking active duty military consumers and inserting armed forces member consumers .\n##### (b) Effective date\nThe amendments made by subsection (a) shall take effect on the date that is 1 year after the date of enactment of this Act.",
      "versionDate": "2025-06-12",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s2074es.xml",
      "text": "119th CONGRESS\n2d Session\nS. 2074\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo amend the Fair Credit Reporting Act to expand the definition of an active duty military consumer for purposes of certain credit monitoring requirements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Servicemembers\u2019 Credit Monitoring Enhancement Act .\n#### 2. Credit monitoring\n##### (a) In general\nThe Fair Credit Reporting Act ( 15 U.S.C. 1681 et seq. ) is amended\u2014\n**(1)**\nin section 605A(k) ( 15 U.S.C. 1681c\u20131(k) )\u2014\n**(A)**\nby striking paragraph (1) and inserting the following:\n(1) Definitions In this subsection: (A) Armed forces The term armed forces has the meaning given the term in section 101(a) of title 10, United States Code. (B) Armed forces member consumer The term armed forces member consumer means a consumer who, regardless of duty status, is a member of the armed forces. ; and\n**(B)**\nin paragraph (2)(A), by striking active duty military consumer and inserting armed forces member consumer ; and\n**(2)**\nin section 625(b)(1)(K) ( 15 U.S.C. 1681t(b)(1)(K) ), by striking active duty military consumers and inserting armed forces member consumers .\n##### (b) Effective date\nThe amendments made by subsection (a) shall take effect on the date that is 1 year after the date of enactment of this Act.",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
            "name": "Consumer affairs",
            "updateDate": "2026-03-06T20:52:27Z"
          },
          {
            "name": "Credit and credit markets",
            "updateDate": "2026-03-06T20:52:10Z"
          },
          {
            "name": "Military personnel and dependents",
            "updateDate": "2026-03-11T14:39:53Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-07-08T13:22:15Z"
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
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2074is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s2074es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Servicemembers\u2019 Credit Monitoring Enhancement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-17T11:03:20Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Servicemembers\u2019 Credit Monitoring Enhancement Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2026-03-06T04:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Servicemembers\u2019 Credit Monitoring Enhancement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-26T06:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Fair Credit Reporting Act to expand the definition of an active duty military consumer for purposes of certain credit monitoring requirements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-26T06:48:23Z"
    }
  ]
}
```
