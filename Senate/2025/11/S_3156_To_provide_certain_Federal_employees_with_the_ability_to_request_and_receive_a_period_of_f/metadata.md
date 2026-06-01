# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3156?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3156
- Title: Federal Worker Mortgage Forbearance Act
- Congress: 119
- Bill type: S
- Bill number: 3156
- Origin chamber: Senate
- Introduced date: 2025-11-07
- Update date: 2025-11-19T15:16:35Z
- Update date including text: 2025-11-19T15:16:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-07: Introduced in Senate
- 2025-11-07 - IntroReferral: Introduced in Senate
- 2025-11-07 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-11-07: Introduced in Senate

## Actions

- 2025-11-07 - IntroReferral: Introduced in Senate
- 2025-11-07 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-07",
    "latestAction": {
      "actionDate": "2025-11-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3156",
    "number": "3156",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "A000382",
        "district": "",
        "firstName": "Angela",
        "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
        "lastName": "Alsobrooks",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "Federal Worker Mortgage Forbearance Act",
    "type": "S",
    "updateDate": "2025-11-19T15:16:35Z",
    "updateDateIncludingText": "2025-11-19T15:16:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-07",
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
      "actionDate": "2025-11-07",
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
          "date": "2025-11-07T18:20:21Z",
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
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
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
      "sponsorshipDate": "2025-11-07",
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
      "sponsorshipDate": "2025-11-07",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3156is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3156\nIN THE SENATE OF THE UNITED STATES\nNovember 7, 2025 Ms. Alsobrooks (for herself, Mr. Van Hollen , Mr. Kaine , and Mr. Warner ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo provide certain Federal employees with the ability to request and receive a period of forbearance on certain mortgage loans during a period during which there is a lapse in appropriations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Federal Worker Mortgage Forbearance Act .\n#### 2. Right of affected individuals to request forbearance\n##### (a) Definitions\nIn this section:\n**(1) Agency**\nThe term agency means each authority of the executive, legislative, or judicial branch of the Government of the United States.\n**(2) Covered individual**\nThe term covered individual \u2014\n**(A)**\nmeans an employee of an agency, without regard to whether the individual is, during a period during which there is a lapse in appropriations with respect to the agency\u2014\n**(i)**\ndetermined to be an excepted employee or an employee performing emergency work, as those terms are defined by the Office of Personnel Management; or\n**(ii)**\nsubject to furlough;\n**(B)**\nincludes a contractor who\u2014\n**(i)**\nas part of the ordinary job duties of the individual, provides support to any employee described in subparagraph (A); and\n**(ii)**\nduring a period during which there is a lapse in appropriations with respect to the applicable agency, does not provide the services described in clause (i); and\n**(C)**\ndoes not include an individual described in subparagraph (A) or (B) who, during a period during which there is a lapse in appropriations with respect to the applicable agency, is paid the basic pay ordinarily paid to the individual.\n**(3) Covered period**\nThe term covered period means, with respect to a period during which there is a lapse in appropriations with respect to an agency, the period beginning on the date on which that lapse begins and ending on the date that is 180 days after the date on which that lapse ends.\n**(4) Federally backed mortgage loan**\nThe term Federally backed mortgage loan means a loan that is\u2014\n**(A)**\nsecured by a first or subordinate lien on residential real property (including individual units of condominiums and cooperatives) designed principally for the occupancy of from 1- to 4- families; and\n**(B)**\n**(i)**\npurchased or securitized by the Federal Home Loan Mortgage Corporation or the Federal National Mortgage Association;\n**(ii)**\ninsured by the Federal Housing Administration under title II of the National Housing Act ( 12 U.S.C. 1707 et seq. );\n**(iii)**\ninsured under section 255 of the National Housing Act ( 12 U.S.C. 1715z\u201320 );\n**(iv)**\nguaranteed under section 184 or 184A of the Housing and Community Development Act of 1992 (12 U.S.C. 1715z\u201313a, 1715z\u201313b);\n**(v)**\nguaranteed or insured by the Department of Veterans Affairs; or\n**(vi)**\nguaranteed, made, or insured by the Department of Agriculture.\n##### (b) Forbearance of loan payments for holders of Federally backed mortgage loans during covered periods\n**(1) In general**\nDuring any covered period with respect to an agency that begins on or after the effective date of this section described in subsection (d), a covered individual with respect to the agency with a Federally backed mortgage loan may request forbearance on the Federally backed mortgage loan, regardless of delinquency status, by\u2014\n**(A)**\nsubmitting a request to the servicer of the Federally backed mortgage loan; and\n**(B)**\naffirming that the covered individual is experiencing a financial hardship because of the applicable lapse in appropriations.\n**(2) Grant of forbearance**\nUpon a request by a covered individual for forbearance under paragraph (1), the servicer to which the request was submitted shall promptly, and without unreasonable delay, grant forbearance with respect to the applicable Federally backed mortgage loan\u2014\n**(A)**\nfor a period of 90 days; and\n**(B)**\nregardless of the delinquency status of the Federally backed mortgage loan.\n**(3) Right to discontinue**\nA covered individual with respect to whom forbearance is granted under this subsection may, at any time, request that the applicable servicer discontinue the forbearance.\n**(4) Accrual of interest or fees**\nDuring a period of forbearance under this subsection, no fees, penalties, or interest, beyond the amounts scheduled or calculated as if the applicable covered individual made all contractual payments on time and in full under the terms of the mortgage contract, shall accrue on the account of the covered individual.\n**(5) No lump-sum payment required**\nAfter the end of a period of forbearance under this subsection with respect to a Federally backed mortgage loan, the servicer of the Federally backed mortgage loan may not require the applicable covered individual to pay a lump-sum payment for the payments on the Federally backed mortgage loan that were not paid during that period of forbearance.\n**(6) Criminal penalty for false statements**\nKnowingly making a false statement in, or in connection with, a request for forbearance under paragraph (1) shall constitute a violation of section 1014 of title 18, United States Code.\n**(7) Notice**\nNot later than 10 days after the date on which a lapse in appropriations with respect to an agency begins, the head of the agency shall provide notice to covered individuals with respect to the agency of the rights of the covered individuals under this subsection.\n**(8) Rule of construction**\nNothing in this subsection may be construed to grant forgiveness with respect to a Federally backed mortgage loan.\n##### (c) Furnishing of credit information\nSection 623(a)(1) of the Fair Credit Reporting Act ( 15 U.S.C. 1681s\u20132(a)(1) ) is amended by adding at the end the following:\n(G) Reporting information relating to certain forbearances (i) Definition In this subsection, the term accommodation means an agreement to grant a period of forbearance pursuant to section 2(b) of the Federal Worker Mortgage Forbearance Act . (ii) Reporting Except as provided in clause (iii), if a furnisher makes an accommodation with respect to 1 or more payments on a credit obligation or account of a consumer, and the consumer makes the payments or is not required to make 1 or more payments pursuant to the accommodation, the furnisher shall\u2014 (I) report the credit obligation or account as current; or (II) if the credit obligation or account was delinquent before the accommodation\u2014 (aa) maintain the delinquent status during the period in which the accommodation is in effect; and (bb) if the consumer brings the credit obligation or account current during the period described in item (aa), report the credit obligation or account as current. (iii) Exception Clause (ii) shall not apply with respect to a credit obligation or account of a consumer that has been charged-off. .\n##### (d) Retroactive effective date\nThis section, and the amendments made by this section, shall take effect as if enacted on September 30, 2025.",
      "versionDate": "2025-11-07",
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
        "updateDate": "2025-11-19T15:16:35Z"
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
      "date": "2025-11-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3156is.xml"
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
      "title": "Federal Worker Mortgage Forbearance Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-13T12:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Federal Worker Mortgage Forbearance Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-13T12:08:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide certain Federal employees with the ability to request and receive a period of forbearance on certain mortgage loans during a period during which there is a lapse in appropriations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-13T12:03:24Z"
    }
  ]
}
```
