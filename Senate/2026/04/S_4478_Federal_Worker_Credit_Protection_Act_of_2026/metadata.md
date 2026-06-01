# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4478?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4478
- Title: Federal Worker Credit Protection Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4478
- Origin chamber: Senate
- Introduced date: 2026-04-30
- Update date: 2026-05-20T16:44:51Z
- Update date including text: 2026-05-20T16:44:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-30: Introduced in Senate
- 2026-04-30 - IntroReferral: Introduced in Senate
- 2026-04-30 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2026-04-30: Introduced in Senate

## Actions

- 2026-04-30 - IntroReferral: Introduced in Senate
- 2026-04-30 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4478",
    "number": "4478",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "K000377",
        "district": "",
        "firstName": "Mark",
        "fullName": "Sen. Kelly, Mark [D-AZ]",
        "lastName": "Kelly",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "Federal Worker Credit Protection Act of 2026",
    "type": "S",
    "updateDate": "2026-05-20T16:44:51Z",
    "updateDateIncludingText": "2026-05-20T16:44:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-30",
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
      "actionDate": "2026-04-30",
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
          "date": "2026-04-30T19:37:41Z",
          "name": "Referred To"
        }
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
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "AZ"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "MD"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "VA"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "VA"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4478is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4478\nIN THE SENATE OF THE UNITED STATES\nApril 30, 2026 Mr. Kelly (for himself, Mr. Gallego , Mr. Van Hollen , Mr. Kaine , Mr. Warner , and Ms. Alsobrooks ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo protect the credit of Federal workers during a government shutdown.\n#### 1. Short title\nThis Act may be cited as the Federal Worker Credit Protection Act of 2026 .\n#### 2. Prohibition on reporting adverse items of information relating to Federal workers during Government shutdowns\n##### (a) In general\nSection 605 of the Fair Credit Reporting Act ( 15 U.S.C. 1681c ) is amended\u2014\n**(1)**\nin subsection (a), by adding at the end the following:\n(9) With respect to a consumer reporting agency described in section 603(p), any item of adverse information related to the debt of Federal workers during a covered period, as those terms are defined in subsection (i). ; and\n**(2)**\nby adding at the end the following:\n(i) Government shutdowns (1) Definitions In this subsection: (A) Covered individual The term covered individual means an employee of the United States Government or the District of Columbia whose employing agency is subject to a lapse of appropriations. (B) Covered period The term covered period means the period beginning on the date on which there is more than a 24-hour lapse in appropriations and ending on the date that is 30 days after the date on which there is no longer a lapse in appropriations. (2) Request to delete A consumer reporting agency, upon receiving a direct request from a consumer who is a covered individual during a covered period shall, free of charge, delete information excluded under subsection (a)(9) in the consumer report of the consumer and prohibit the consumer reporting agency from disclosing such information in the consumer report of the consumer to any person requesting the consumer report. (3) Notification The Director of the Office of Management and Budget shall submit to each consumer reporting agency described in section 603(p) a notification of the start and end of a lapse in appropriations impacting covered individuals. .\n##### (b) Technical and conforming amendment\nSection 605(c)(1) of the Fair Credit Reporting Act ( 15 U.S.C. 1681c(c)(1) ) is amended by striking paragraphs (4) and (6) and inserting paragraphs (4), (6), and (9) .\n##### (c) Effective date\nThis Act, and the amendments made by this Act, shall apply to a covered period that begins on or after February 1, 2026.",
      "versionDate": "2026-04-30",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2026-05-20T16:44:51Z"
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
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4478is.xml"
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
      "title": "Federal Worker Credit Protection Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-08T04:23:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Federal Worker Credit Protection Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-08T04:23:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to protect the credit of Federal workers during a government shutdown.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-08T04:18:35Z"
    }
  ]
}
```
