# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1300?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1300
- Title: PSA Screening for HIM Act
- Congress: 119
- Bill type: HR
- Bill number: 1300
- Origin chamber: House
- Introduced date: 2025-02-13
- Update date: 2026-05-11T19:52:50Z
- Update date including text: 2026-05-11T19:52:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-02-13: Introduced in House

## Actions

- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1300",
    "number": "1300",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "D000628",
        "district": "2",
        "firstName": "Neal",
        "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
        "lastName": "Dunn",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "PSA Screening for HIM Act",
    "type": "HR",
    "updateDate": "2026-05-11T19:52:50Z",
    "updateDateIncludingText": "2026-05-11T19:52:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-13",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-13",
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
          "date": "2025-02-13T14:00:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "NY"
    },
    {
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "NC"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "LA"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "FL"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "MN"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "OH"
    },
    {
      "bioguideId": "E000235",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Ezell, Mike [R-MS-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Ezell",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "MS"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "OH"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "MI"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "CA"
    },
    {
      "bioguideId": "C001078",
      "district": "11",
      "firstName": "Gerald",
      "fullName": "Rep. Connolly, Gerald E. [D-VA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Connolly",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "VA"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "VA"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "KS"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "MD"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "VA"
    },
    {
      "bioguideId": "M001214",
      "district": "1",
      "firstName": "Frank",
      "fullName": "Rep. Mrvan, Frank J. [D-IN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mrvan",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "IN"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "FL"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "CA"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "TN"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "AZ"
    },
    {
      "bioguideId": "J000302",
      "district": "13",
      "firstName": "John",
      "fullName": "Rep. Joyce, John [R-PA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Joyce",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "PA"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "MS"
    },
    {
      "bioguideId": "S001157",
      "district": "13",
      "firstName": "David",
      "fullName": "Rep. Scott, David [D-GA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "GA"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-06-24",
      "state": "FL"
    },
    {
      "bioguideId": "S001207",
      "district": "11",
      "firstName": "Mikie",
      "fullName": "Rep. Sherrill, Mikie [D-NJ-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherrill",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "NJ"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "NC"
    },
    {
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "NC"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "False",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "TX"
    },
    {
      "bioguideId": "B001306",
      "district": "12",
      "firstName": "Troy",
      "fullName": "Rep. Balderson, Troy [R-OH-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Balderson",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "OH"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NV"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "NH"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NY"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "CA"
    },
    {
      "bioguideId": "S001223",
      "district": "13",
      "firstName": "Emilia",
      "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Sykes",
      "middleName": "Strong",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "OH"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "DC"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1300ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1300\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2025 Mr. Dunn of Florida (for himself, Ms. Clarke of New York , Mr. Murphy , and Mr. Carter of Louisiana ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XXVII of the Public Health Service Act to require group health plans and health insurance issuers offering group or individual health insurance coverage to provide coverage for prostate cancer screenings without the imposition of cost-sharing requirements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Prostate-Specific Antigen Screening for High-risk Insured Men Act or the PSA Screening for HIM Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nProstate cancer is the second leading cause of cancer death in men in the United States with 1 in 44 men dying from prostate cancer and more than 35,700 men estimated to die from prostate cancer in 2025.\n**(2)**\nProstate cancer is the second most commonly diagnosed cancer in the Nation with 1 in 8 men being diagnosed in their lifetimes, 3.3 million men in the United States living with a diagnosis, and over 310,000 men estimated to be diagnosed in 2025.\n**(3)**\nThe survival rate for prostate cancer diagnosed in early stage is near 100 percent but prostate cancer diagnosed in late stage has only a 37 percent survival rate.\n**(4)**\nThere are few, if any, symptoms of prostate cancer before it reaches late stage.\n**(5)**\nAfrican-American men have a disproportionately higher rate of prostate cancer and are 70 percent more likely to be diagnosed with prostate cancer than White men, with 1 in 6 African-American men developing prostate cancer in their lifetimes.\n**(6)**\nAfrican-American men are 2.1 times more likely to die from prostate cancer than White men.\n**(7)**\nMen with a father or brother with prostate cancer are more than twice as likely to be diagnosed with prostate cancer than men without a family history.\n**(8)**\nThe common clinical definition for men at high-risk of prostate cancer includes African-American men and men with a family history.\n**(9)**\nMost of the major cancer and urological societies recommend beginning screening discussions earlier for African-American men and those with a family history of prostate cancer.\n**(10)**\nThe United States Preventive Services Task Force has encouraged research on screening African-American men, including whether to screen African-American men at younger ages, and has identified this research as a high-priority cancer research gap.\n**(11)**\nBarriers to screening should be minimized for high-risk men in order to catch asymptomatic prostate cancer before it metastasizes and the survival rate is dramatically reduced.\n**(12)**\nThe cost of treating metastatic prostate cancer in the United States health care system is hundreds of millions of dollars more annually than the cost of treating localized, early-stage cancer.\n#### 3. Requirement for group health plans and health insurance issuers offering group or individual health insurance coverage to provide coverage for prostate cancer screenings without imposition of cost-sharing requirements\n##### (a) In general\nSubsection (a) of section 2713 of the Public Health Service Act ( 42 U.S.C. 300gg\u201313 ) is amended to read as follows:\n(a) Coverage of preventive health services (1) In general A group health plan and a health insurance issuer offering group or individual health insurance coverage shall, at a minimum, provide coverage for and shall not impose any cost-sharing requirements for\u2014 (A) evidence-based items or services that have in effect a rating of A or B in the current recommendations of the United States Preventive Services Task Force; (B) immunizations that have in effect a recommendation from the Advisory Committee on Immunization Practices of the Centers for Disease Control and Prevention with respect to the individual involved; (C) with respect to infants, children, and adolescents, evidence-informed preventive care and screenings provided for in the comprehensive guidelines supported by the Health Resources and Services Administration; (D) with respect to women, such additional preventive care and screenings not described in subparagraph (A) as provided for in comprehensive guidelines supported by the Health Resources and Services Administration for purposes of this subparagraph; and (E) with respect to men who are age 40 and over and are at high risk of developing prostate cancer (including African-American men and men with a family history of prostate cancer (as defined in paragraph (2))), such additional evidence-based preventive care and screenings not described in subparagraph (A) for prostate cancer. (2) Men with a family history of prostate cancer defined For purposes of paragraph (1)(E), the term men with a family history of prostate cancer means men who have a first-degree relative\u2014 (A) who was diagnosed with prostate cancer; (B) who developed prostate cancer; (C) whose death was a result of prostate cancer; (D) who have been diagnosed with a cancer known to be associated with increased risk of prostate cancer; or (E) who has a genetic alteration known to be associated with increased risk of prostate cancer. (3) Clarification regarding breast cancer screening, mammography, and prevention recommendations For the purposes of this Act, and for the purposes of any other provision of law, the current recommendations of the United States Preventive Service Task Force regarding breast cancer screening, mammography, and prevention shall be considered the most current other than those issued in or around November 2009. (4) Rule of construction Nothing in this subsection shall be construed to prohibit a plan or issuer from providing coverage for services in addition to those recommended by the United States Preventive Services Task Force or to deny coverage for services that are not recommended by such Task Force. .\n##### (b) Effective date\nThe amendment made by subsection (a) shall apply with respect to plan years beginning on or after January 1, 2026.",
      "versionDate": "2025-02-13",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Cancer",
            "updateDate": "2025-07-08T12:32:49Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-07-08T12:32:49Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2025-07-08T12:32:49Z"
          },
          {
            "name": "Medical tests and diagnostic methods",
            "updateDate": "2025-07-08T12:32:49Z"
          },
          {
            "name": "Minority health",
            "updateDate": "2025-07-08T12:32:49Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-17T17:53:34Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr1300",
          "measure-number": "1300",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-13",
          "originChamber": "HOUSE",
          "update-date": "2026-05-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1300v00",
            "update-date": "2026-05-11"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Prostate-Specific Antigen Screening for High-risk Insured Men Act or the PSA Screening for HIM Act</strong></p><p>This bill requires private health insurance plans to cover evidence-based, preventive care and screenings for prostate cancer that are not already covered under the recommendations of the U.S. Preventive Services Task Force for certain men.</p><p>Specifically, plans must cover such care and\u00a0screenings for men\u00a0who are age 40 and over and are at high risk of developing prostate cancer (e.g., with a family history of prostrate cancer). Such coverage must be provided without imposing any cost-sharing requirement.</p>"
        },
        "title": "PSA Screening for HIM Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1300.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Prostate-Specific Antigen Screening for High-risk Insured Men Act or the PSA Screening for HIM Act</strong></p><p>This bill requires private health insurance plans to cover evidence-based, preventive care and screenings for prostate cancer that are not already covered under the recommendations of the U.S. Preventive Services Task Force for certain men.</p><p>Specifically, plans must cover such care and\u00a0screenings for men\u00a0who are age 40 and over and are at high risk of developing prostate cancer (e.g., with a family history of prostrate cancer). Such coverage must be provided without imposing any cost-sharing requirement.</p>",
      "updateDate": "2026-05-11",
      "versionCode": "id119hr1300"
    },
    "title": "PSA Screening for HIM Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Prostate-Specific Antigen Screening for High-risk Insured Men Act or the PSA Screening for HIM Act</strong></p><p>This bill requires private health insurance plans to cover evidence-based, preventive care and screenings for prostate cancer that are not already covered under the recommendations of the U.S. Preventive Services Task Force for certain men.</p><p>Specifically, plans must cover such care and\u00a0screenings for men\u00a0who are age 40 and over and are at high risk of developing prostate cancer (e.g., with a family history of prostrate cancer). Such coverage must be provided without imposing any cost-sharing requirement.</p>",
      "updateDate": "2026-05-11",
      "versionCode": "id119hr1300"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1300ih.xml"
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
      "title": "PSA Screening for HIM Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PSA Screening for HIM Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Prostate-Specific Antigen Screening for High-risk Insured Men Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XXVII of the Public Health Service Act to require group health plans and health insurance issuers offering group or individual health insurance coverage to provide coverage for prostate cancer screenings without the imposition of cost-sharing requirements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:33:26Z"
    }
  ]
}
```
