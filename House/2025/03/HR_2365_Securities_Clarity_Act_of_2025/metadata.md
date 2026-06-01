# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2365?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2365
- Title: Securities Clarity Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2365
- Origin chamber: House
- Introduced date: 2025-03-26
- Update date: 2025-08-06T03:41:15Z
- Update date including text: 2025-08-06T03:41:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-26: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-03-26: Introduced in House

## Actions

- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-26",
    "latestAction": {
      "actionDate": "2025-03-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2365",
    "number": "2365",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "E000294",
        "district": "6",
        "firstName": "Tom",
        "fullName": "Rep. Emmer, Tom [R-MN-6]",
        "lastName": "Emmer",
        "party": "R",
        "state": "MN"
      }
    ],
    "title": "Securities Clarity Act of 2025",
    "type": "HR",
    "updateDate": "2025-08-06T03:41:15Z",
    "updateDateIncludingText": "2025-08-06T03:41:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-26",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-26",
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
          "date": "2025-03-26T14:02:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2365ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2365\nIN THE HOUSE OF REPRESENTATIVES\nMarch 26, 2025 Mr. Emmer (for himself and Mr. Soto ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the securities laws to exclude investment contract assets from the definition of a security.\n#### 1. Short title\nThis Act may be referred to as the Securities Clarity Act of 2025 .\n#### 2. Treatment of investment contract assets\n##### (a) Securities Act of 1933\nSection 2(a) of the Securities Act of 1933 ( 15 U.S.C. 77b(a) ) is amended\u2014\n**(1)**\nin paragraph (1), by adding at the end the following: The term security does not include an investment contract asset. ; and\n**(2)**\nby adding at the end the following:\n(20) The term investment contract asset means a fungible digital representation of value\u2014 (A) that can be exclusively possessed and transferred, person to person, without necessary reliance on an intermediary, and is recorded on a cryptographically secured public distributed ledger; (B) sold or otherwise transferred, or intended to be sold or otherwise transferred, pursuant to an investment contract; and (C) that is not otherwise a security pursuant to the first sentence of paragraph (1). .\n##### (b) Investment Advisers Act of 1940\nSection 202(a)(18) of the Investment Advisers Act of 1940 ( 15 U.S.C. 80b\u20132(a)(18) ) is amended by adding at the end the following: The term security does not include an investment contract asset (as such term is defined under section 2(a) of the Securities Act of 1933). .\n##### (c) Investment Company Act of 1940\nSection 2(a)(36) of the Investment Company Act of 1940 ( 15 U.S.C. 80a\u20132(a)(36) ) is amended by adding at the end the following: The term security does not include an investment contract asset (as such term is defined under section 2(a) of the Securities Act of 1933). .\n##### (d) Securities Exchange Act of 1934\nSection 3(a)(10) of the Securities Exchange Act of 1934 ( 15 U.S.C. 78c(a)(10) ) is amended by adding at the end the following: The term security does not include an investment contract asset (as such term is defined under section 2(a) of the Securities Act of 1933). .\n##### (e) Securities Investor Protection Act of 1970\nSection 16(14) of the Securities Investor Protection Act of 1970 ( 15 U.S.C. 78lll(14) ) is amended by adding at the end the following: The term security does not include an investment contract asset (as such term is defined under section 2(a) of the Securities Act of 1933). .",
      "versionDate": "2025-03-26",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-04-04T16:38:00Z"
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
      "date": "2025-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2365ih.xml"
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
      "title": "Securities Clarity Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-04T05:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Securities Clarity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T05:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the securities laws to exclude investment contract assets from the definition of a security.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-04T05:03:33Z"
    }
  ]
}
```
