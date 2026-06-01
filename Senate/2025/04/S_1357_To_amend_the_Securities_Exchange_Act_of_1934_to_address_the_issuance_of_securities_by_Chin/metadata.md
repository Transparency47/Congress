# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1357?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1357
- Title: SAFE Act
- Congress: 119
- Bill type: S
- Bill number: 1357
- Origin chamber: Senate
- Introduced date: 2025-04-08
- Update date: 2025-05-19T14:37:16Z
- Update date including text: 2025-05-19T14:37:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-08: Introduced in Senate
- 2025-04-08 - IntroReferral: Introduced in Senate
- 2025-04-08 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-04-08: Introduced in Senate

## Actions

- 2025-04-08 - IntroReferral: Introduced in Senate
- 2025-04-08 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-08",
    "latestAction": {
      "actionDate": "2025-04-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1357",
    "number": "1357",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "SAFE Act",
    "type": "S",
    "updateDate": "2025-05-19T14:37:16Z",
    "updateDateIncludingText": "2025-05-19T14:37:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-08",
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
      "actionDate": "2025-04-08",
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
          "date": "2025-04-08T21:56:14Z",
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
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "TN"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "LA"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "MS"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1357is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1357\nIN THE SENATE OF THE UNITED STATES\nApril 8, 2025 Mr. Scott of Florida (for himself, Mrs. Blackburn , Mr. Cassidy , Mrs. Hyde-Smith , and Mr. Kennedy ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Securities Exchange Act of 1934 to address the issuance of securities by Chinese entities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Secure America\u2019s Financial Exchanges Act or the SAFE Act .\n#### 2. Securities\n##### (a) In general\nSection 6(b) of the Securities Exchange Act of 1934 ( 15 U.S.C. 78f(b) ) is amended by adding at the end the following:\n(11) The rules of the exchange require an issuer, before the initial listing of any security of the issuer on the exchange, and in each annual report filed with the Commission and the exchange under section 13(a), to disclose the following information: (A) Whether the Government of the People\u2019s Republic of China has provided the issuer with any financial support, including\u2014 (i) any direct subsidy, grant, loan, loan guarantee, tax concession, or benefit with respect to procurement policy; or (ii) any other form of support. (B) If the Government of the People\u2019s Republic of China has provided support described in subparagraph (A), the conditions under which that Government provided that support, including whether that Government required the issuer to\u2014 (i) satisfy certain requirements with respect to exports; (ii) purchase items from certain entities; (iii) use certain intellectual property; or (iv) employ members of the Chinese Communist Party or other employees of that Government. (C) Whether there are any committees of the Chinese Communist Party established within the issuer, which shall include the disclosure of\u2014 (i) which employees of the issuer comprise that committee; and (ii) the roles played by the employees described in clause (i). (D) Information regarding each individual who, as of the date on which the disclosure is made, is an officer or director of the issuer (or a subsidiary of the issuer) and holds, or previously held, a position with the Chinese Communist Party or the Government of the People\u2019s Republic of China, including the title of that position and the geographic location in which the individual holds or held that position, as applicable. .\n##### (b) Rules\nNot later than 180 days after the date of enactment of this Act, the Securities and Exchange Commission shall make any amendments to the rules of the Commission that are necessary as a result of the amendments made by subsection (a).",
      "versionDate": "2025-04-08",
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
        "updateDate": "2025-05-19T14:37:16Z"
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
      "date": "2025-04-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1357is.xml"
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
      "title": "SAFE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-23T02:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SAFE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-23T02:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Secure America\u2019s Financial Exchanges Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-23T02:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Securities Exchange Act of 1934 to address the issuance of securities by Chinese entities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-23T02:48:22Z"
    }
  ]
}
```
