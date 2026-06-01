# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2352?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2352
- Title: PROTECTED Act
- Congress: 119
- Bill type: S
- Bill number: 2352
- Origin chamber: Senate
- Introduced date: 2025-07-17
- Update date: 2025-09-05T15:42:50Z
- Update date including text: 2025-09-05T15:42:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-17: Introduced in Senate
- 2025-07-17 - IntroReferral: Introduced in Senate
- 2025-07-17 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-07-17: Introduced in Senate

## Actions

- 2025-07-17 - IntroReferral: Introduced in Senate
- 2025-07-17 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2352",
    "number": "2352",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "B001319",
        "district": "",
        "firstName": "Katie",
        "fullName": "Sen. Britt, Katie Boyd [R-AL]",
        "lastName": "Britt",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "PROTECTED Act",
    "type": "S",
    "updateDate": "2025-09-05T15:42:50Z",
    "updateDateIncludingText": "2025-09-05T15:42:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-17",
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
      "actionDate": "2025-07-17",
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
          "date": "2025-07-17T21:08:54Z",
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
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "AR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2352is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2352\nIN THE SENATE OF THE UNITED STATES\nJuly 17, 2025 Mrs. Britt (for herself and Mr. Boozman ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Equal Credit Opportunity Act to modify the requirements associated with small business loan data collection, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Preventing Regulatory Overreach to Empower Communities to Thrive and Ensure Data Privacy Act or the PROTECTED Act .\n#### 2. Small business loan data collection\nSection 704B of the Equal Credit Opportunity Act ( 15 U.S.C. 1691c\u20132 ) is amended\u2014\n**(1)**\nin subsection (c)\u2014\n**(A)**\nby striking Any applicant and inserting the following:\n(1) In general Any applicant ; and\n**(B)**\nby striking the period at the end and inserting the following:\n, and the financial institution may, when requesting such information, inform the applicant in writing that\u2014 (A) the Bureau of Consumer Financial Protection requires the financial institution to ask, collect, and report such information to the Federal Government annually pursuant to this section; (B) the applicant's response will not affect the financial institution\u2019s evaluation of the request for credit; and (C) the applicant is not required to provide such information. ; and\n**(2)**\nin subsection (e)\u2014\n**(A)**\nin paragraph (2)\u2014\n**(i)**\nby striking subparagraphs (C), (G), and (H); and\n**(ii)**\nby redesignating subparagraphs (D), (E), and (F) as subparagraphs (C), (D), and (E), respectively;\n**(B)**\nin paragraph (4)\u2014\n**(i)**\nby striking The and inserting the following:\n(A) In general The ; and\n**(ii)**\nby adding at the end the following:\n(B) Rulemaking The Bureau shall, before deleting or modifying data under this paragraph, and after notice and an opportunity for comment, issue rules that include a description of what modifications and deletions the Bureau intends to make to the data and how such modifications and deletions will advance a privacy interest. ; and\n**(C)**\nby adding at the end the following:\n(5) Prohibition on information not reported by an applicant A financial institution may not compile and maintain information described under subsection (b) that was determined by the financial institution using visual observation or any other manner other than being provided by an applicant. (6) Treatment of response rate The percentage of applicants providing a financial institution with the information described under subsection (b) may not be used as a factor in determining whether a financial institution is in compliance with the requirements under this subsection. (7) Safe harbor The Bureau may not enforce compliance with the requirements of this subsection during the 2-year period beginning on the effective date described in paragraph (8). (8) Effective date This subsection shall take effect on the date that is 3 years after the date on which the Bureau completes the cost-benefit analysis under chapter 6 of part I of title 5, United States Code (commonly referred to as the Regulatory Flexibility Act ) and subchapter I of chapter 35 of title 44, United States Code (commonly referred to as the Paperwork Reduction Act )). (9) Definitions In this subsection: (A) Financial institution The term financial institution \u2014 (i) means\u2014 (I) any partnership, company, corporation, association (incorporated or unincorporated), trust, estate, cooperative organization, or other entity that\u2014 (aa) engages in any financial activity; and (bb) in each of the preceding 2 calendar years, originated not less than 2,500 credit transactions for small businesses; and (ii) does not include\u2014 (I) any financial institution with less than $10,000,000,000 in assets; (II) a Farm Credit System institution chartered under and subject to the provisions of the Farm Credit Act of 1971 ( 12 U.S.C. 2001 et seq. ); (III) community development financial institutions, as defined in section 103 of the Community Development Banking and Financial Institutions Act of 1994 ( 12 U.S.C. 4702 ); or (IV) lenders involved in equipment and vehicle financing. (B) Small business The term small business means an entity with gross annual revenues of not more than $1,000,000 in the preceding fiscal year. .",
      "versionDate": "2025-07-17",
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
        "updateDate": "2025-09-05T15:42:50Z"
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
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2352is.xml"
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
      "title": "PROTECTED Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-01T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PROTECTED Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-01T03:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Preventing Regulatory Overreach to Empower Communities to Thrive and Ensure Data Privacy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-01T03:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Equal Credit Opportunity Act to modify the requirements associated with small business loan data collection, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-01T03:48:24Z"
    }
  ]
}
```
