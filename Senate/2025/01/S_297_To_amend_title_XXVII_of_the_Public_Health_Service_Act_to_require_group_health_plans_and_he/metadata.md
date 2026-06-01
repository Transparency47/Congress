# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/297?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/297
- Title: PSA Screening for HIM Act
- Congress: 119
- Bill type: S
- Bill number: 297
- Origin chamber: Senate
- Introduced date: 2025-01-29
- Update date: 2026-03-20T11:03:17Z
- Update date including text: 2026-03-20T11:03:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-01-29: Introduced in Senate
- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.
- Latest action: 2025-01-29: Introduced in Senate

## Actions

- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-29",
    "latestAction": {
      "actionDate": "2025-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/297",
    "number": "297",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001236",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Boozman, John [R-AR]",
        "lastName": "Boozman",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "PSA Screening for HIM Act",
    "type": "S",
    "updateDate": "2026-03-20T11:03:17Z",
    "updateDateIncludingText": "2026-03-20T11:03:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-29",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-29",
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
            "date": "2026-03-19T14:00:00Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-01-29T17:51:41Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-01-29",
      "state": "NJ"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "CA"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "GA"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "WA"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "NH"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s297is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 297\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2025 Mr. Boozman (for himself and Mr. Booker ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend title XXVII of the Public Health Service Act to require group health plans and health insurance issuers offering group or individual health insurance coverage to provide coverage for prostate cancer screenings without the imposition of cost-sharing requirements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Prostate-Specific Antigen Screening for High-risk Insured Men Act or the PSA Screening for HIM Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nProstate cancer is the second leading cause of cancer death in men in the United States with 1 in 44 men dying from prostate cancer and more than 35,700 men estimated to die from prostate cancer in 2025.\n**(2)**\nProstate cancer is the second most commonly diagnosed cancer in the Nation with 1 in 8 men being diagnosed in their lifetimes, 3,300,000 men in the United States living with a diagnosis, and over 310,000 men estimated to be diagnosed in 2025.\n**(3)**\nThe survival rate for prostate cancer diagnosed in early stage is near 100 percent but prostate cancer diagnosed in late stage has only a 37-percent survival rate.\n**(4)**\nThere are few, if any, symptoms of prostate cancer before it reaches late stage.\n**(5)**\nAfrican-American men have a disproportionately higher rate of prostate cancer and are 70 percent more likely to be diagnosed with prostate cancer than White men, with 1 in 6 African-American men developing prostate cancer in their lifetimes.\n**(6)**\nAfrican-American men are 2.1 times more likely to die from prostate cancer than White men.\n**(7)**\nMen with a father or brother with prostate cancer are more than twice as likely to be diagnosed with prostate cancer than men without a family history.\n**(8)**\nThe common clinical definition for men at high-risk of prostate cancer includes African-American men and men with a family history.\n**(9)**\nMost of the major cancer and urological societies recommend beginning screening discussions earlier for African-American men and those with a family history of prostate cancer.\n**(10)**\nThe United States Preventive Services Task Force has encouraged research on screening African-American men, including whether to screen African-American men at younger ages, and has identified this research as a high-priority cancer research gap.\n**(11)**\nBarriers to screening should be minimized for high-risk men in order to catch asymptomatic prostate cancer before it metastasizes and the survival rate is dramatically reduced.\n**(12)**\nThe cost of treating metastatic prostate cancer in the United States health care system is hundreds of millions of dollars more annually than the cost of treating localized, early-stage cancer.\n#### 3. Requirement for group health plans and health insurance issuers offering group or individual health insurance coverage to provide coverage for prostate cancer screenings without imposition of cost-sharing requirements\n##### (a) In general\nSection 2713(a) of the Public Health Service Act ( 42 U.S.C. 300gg\u201313(a) ) is amended\u2014\n**(1)**\nby striking paragraph (5);\n**(2)**\nby redesignating paragraphs (1) through (4) as subparagraphs (A) through (D), respectively, and adjusting the margins accordingly;\n**(3)**\nby striking (a) In general\u2014 A group health and inserting the following:\n(a) Coverage of preventive health services (1) In general A group health ;\n**(4)**\nin paragraph (1), as so designated\u2014\n**(A)**\nin subparagraph (B), as so redesignated, by striking ; and and inserting a semicolon;\n**(B)**\nin subparagraph (C), as so redesignated, by striking the period and inserting a semicolon;\n**(C)**\nin subparagraph (D), as so redesignated\u2014\n**(i)**\nby striking paragraph (1) and inserting subparagraph (A) ; and\n**(ii)**\nby striking the period and inserting ; and ;\n**(D)**\nby inserting after subparagraph (D), as so redesignated, the following:\n(E) with respect to men who are age 40 and over and are at high risk of developing prostate cancer (including African-American men and men with a family history of prostate cancer (as defined in paragraph (2))), such additional evidence-based preventive care and screenings not described in subparagraph (A) for prostate cancer. ; and\n**(5)**\nby striking the flush text at the end and inserting the following:\n(2) Men with a family history of prostate cancer defined For purposes of paragraph (1)(E), the term men with a family history of prostate cancer means men who have a first-degree relative\u2014 (A) who was diagnosed with prostate cancer; (B) who developed prostate cancer; (C) whose death was a result of prostate cancer; (D) who have been diagnosed with a cancer known to be associated with increased risk of prostate cancer; or (E) who has a genetic alteration known to be associated with increased risk of prostate cancer. (3) Clarification regarding breast cancer screening, mammography, and prevention recommendations For the purposes of this Act, and for the purposes of any other provision of law, the current recommendations of the United States Preventive Service Task Force regarding breast cancer screening, mammography, and prevention shall be considered the most current other than those issued in or around November 2009. (4) Rule of construction Nothing in this subsection shall be construed to prohibit a plan or issuer from providing coverage for services in addition to those recommended by the United States Preventive Services Task Force or to deny coverage for services that are not recommended by such Task Force. .\n##### (b) Effective date\nThe amendments made by subsection (a) shall apply with respect to plan years beginning on or after January 1, 2025.",
      "versionDate": "2025-01-29",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Cancer",
            "updateDate": "2025-04-01T15:20:39Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-04-01T15:20:30Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-04-01T15:20:34Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2025-04-01T15:20:53Z"
          },
          {
            "name": "Medical tests and diagnostic methods",
            "updateDate": "2025-04-01T15:20:47Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-03T16:12:33Z"
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
      "date": "2025-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s297is.xml"
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
      "title": "PSA Screening for HIM Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PSA Screening for HIM Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-01T04:53:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Prostate-Specific Antigen Screening for High-risk Insured Men Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-01T04:53:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XXVII of the Public Health Service Act to require group health plans and health insurance issuers offering group or individual health insurance coverage to provide coverage for prostate cancer screenings without the imposition of cost-sharing requirements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-01T04:48:38Z"
    }
  ]
}
```
