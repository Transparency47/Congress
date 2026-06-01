# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2836?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2836
- Title: FEMA Loan Interest Payment Relief Act
- Congress: 119
- Bill type: HR
- Bill number: 2836
- Origin chamber: House
- Introduced date: 2025-04-10
- Update date: 2026-05-20T14:21:02Z
- Update date including text: 2026-05-20T14:21:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-10: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-04-10 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-04-10: Introduced in House

## Actions

- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-04-10 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2836",
    "number": "2836",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
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
    "title": "FEMA Loan Interest Payment Relief Act",
    "type": "HR",
    "updateDate": "2026-05-20T14:21:02Z",
    "updateDateIncludingText": "2026-05-20T14:21:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-10",
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
          "date": "2025-04-10T13:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-10T21:11:32Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "systemCode": "hspw00",
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
      "sponsorshipDate": "2025-04-10",
      "state": "FL"
    },
    {
      "bioguideId": "L000597",
      "district": "15",
      "firstName": "Laurel",
      "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "FL"
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
      "sponsorshipDate": "2025-04-10",
      "state": "LA"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "LA"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "AL"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "FL"
    },
    {
      "bioguideId": "G000593",
      "district": "28",
      "firstName": "Carlos",
      "fullName": "Rep. Gimenez, Carlos A. [R-FL-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Gimenez",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "FL"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "FL"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "FL"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "FL"
    },
    {
      "bioguideId": "M001216",
      "district": "7",
      "firstName": "Cory",
      "fullName": "Rep. Mills, Cory [R-FL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mills",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "FL"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "FL"
    },
    {
      "bioguideId": "B001314",
      "district": "4",
      "firstName": "Aaron",
      "fullName": "Rep. Bean, Aaron [R-FL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Bean",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "FL"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "FL"
    },
    {
      "bioguideId": "C001039",
      "district": "3",
      "firstName": "Kat",
      "fullName": "Rep. Cammack, Kat [R-FL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Cammack",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "FL"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "FL"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "MI"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2836ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2836\nIN THE HOUSE OF REPRESENTATIVES\nApril 10, 2025 Mr. Dunn of Florida (for himself, Mr. Soto , Ms. Lee of Florida , Mr. Carter of Louisiana , Mr. Higgins of Louisiana , Mr. Moore of Alabama , Mr. Webster of Florida , Mr. Gimenez , Mr. Bilirakis , Mr. Moskowitz , Mr. Donalds , and Mr. Mills ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend the Robert T. Stafford Disaster Relief and Emergency Assistance Act to provide for the authority to reimburse local governments or electric cooperatives for interest expenses, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the FEMA Loan Interest Payment Relief Act .\n#### 2. Reimbursement of interest payments related to public assistance\n##### (a) In general\nTitle IV of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170 et seq. ) is amended by adding at the end the following:\n431. Reimbursement of interest payments related to public assistance (a) In general The President, acting through the Administrator of the Federal Emergency Management Agency, shall provide financial assistance to a local government or electric cooperative as reimbursement for qualifying interest. (b) Definitions (1) In general In this section, the following definitions apply: (A) Qualifying interest The term qualifying interest means, with respect to a qualifying loan, the lesser of\u2014 (i) the actual interest paid to a lender for such qualifying loan; and (ii) the interest that would have been paid to a lender if such qualifying loan had an interest rate equal to the prime rate most recently published on the Federal Reserve Statistical Release on selected interest rates. (B) Qualifying loan The term qualifying loan means a loan\u2014 (i) obtained by a local government or electric cooperative; and (ii) of which not less than 90 percent of the proceeds are used to fund activities for which such local government or electric cooperative receives assistance under this Act after the date on which such loan is disbursed. (2) Local government For purposes of this section, the term local government includes the District of Columbia. .\n##### (b) Rules of applicability\n**(1) Eligibility**\nAny qualifying interest (as such term is defined in section 431 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act, as added by this Act) incurred by a local government or electric cooperative in the 9 years preceding the date of enactment of this Act shall be treated as eligible for financial assistance for purposes of such section.\n**(2) Appropriations**\nOnly amounts appropriated on or after the date of enactment of this Act may be made available to carry out the amendment made by this section.\n##### (c) Alternative procedures for outstanding qualifying interest reimbursement\n**(1) In general**\nNotwithstanding any other provision of law, not later than 30 days after the date of enactment of this Act, the President, acting through the Administrator of the Federal Emergency Management Agency, shall establish and publish in the Federal Register alternative procedures for States to obtain reimbursement for qualifying loan interest (as such term is defined in section 431(b) of the Robert T. Stafford Disaster Relief and Emergency Assistance Act, as added by this Act) eligible under the Robert T. Stafford Disaster Relief and Emergency Assistance Act (42 U.S.C. 5121 et. seq) for all projects pending obligation as of the date of enactment of this Act.\n**(2) Application**\nA State requesting reimbursement pursuant to paragraph (1) shall submit an application to the President, acting through the Administrator of the Federal Emergency Management Agency, for outstanding qualifying interest reimbursement not later than 60 days after the date of publication of the procedures in such subsection.\n**(3) Reimbursement timing**\nIn carrying out paragraph (1), the President, acting through the Administrator of the Federal Emergency Management Agency, shall reimburse States requesting assistance pursuant to paragraph (1) not later than 1 year after the date of enactment of this Act.",
      "versionDate": "2025-04-10",
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
        "name": "Emergency Management",
        "updateDate": "2025-05-27T16:51:45Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-10",
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
          "measure-id": "id119hr2836",
          "measure-number": "2836",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-10",
          "originChamber": "HOUSE",
          "update-date": "2026-05-20"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2836v00",
            "update-date": "2026-05-20"
          },
          "action-date": "2025-04-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>FEMA Loan Interest Payment Relief Act</strong></p><p>This bill requires the Federal Emergency Management Agency (FEMA) to reimburse a local government or electric cooperative for interest paid on a loan used for emergency or disaster-related activities later paid for by FEMA assistance. The bill provides for similar reimbursement of interest to states for projects\u00a0that are pending obligation.</p><p>The bill retroactively applies to interest incurred by a local government or electric cooperative in the nine years preceding enactment of the bill.</p><p>FEMA must reimburse states for loan interest for emergency or disaster-related projects that are pending obligation on the date of the bill\u2019s enactment.\u00a0FEMA must publish procedures for such reimbursement within 30 days after the bill\u2019s enactment and states must apply within 60 days after publication of the procedures.</p><p>The interest that qualifies for reimbursement may not exceed the amount of interest that would have been paid if the loan's interest rate were equal to the most recent prime rate.</p>"
        },
        "title": "FEMA Loan Interest Payment Relief Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2836.xml",
    "summary": {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>FEMA Loan Interest Payment Relief Act</strong></p><p>This bill requires the Federal Emergency Management Agency (FEMA) to reimburse a local government or electric cooperative for interest paid on a loan used for emergency or disaster-related activities later paid for by FEMA assistance. The bill provides for similar reimbursement of interest to states for projects\u00a0that are pending obligation.</p><p>The bill retroactively applies to interest incurred by a local government or electric cooperative in the nine years preceding enactment of the bill.</p><p>FEMA must reimburse states for loan interest for emergency or disaster-related projects that are pending obligation on the date of the bill\u2019s enactment.\u00a0FEMA must publish procedures for such reimbursement within 30 days after the bill\u2019s enactment and states must apply within 60 days after publication of the procedures.</p><p>The interest that qualifies for reimbursement may not exceed the amount of interest that would have been paid if the loan's interest rate were equal to the most recent prime rate.</p>",
      "updateDate": "2026-05-20",
      "versionCode": "id119hr2836"
    },
    "title": "FEMA Loan Interest Payment Relief Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>FEMA Loan Interest Payment Relief Act</strong></p><p>This bill requires the Federal Emergency Management Agency (FEMA) to reimburse a local government or electric cooperative for interest paid on a loan used for emergency or disaster-related activities later paid for by FEMA assistance. The bill provides for similar reimbursement of interest to states for projects\u00a0that are pending obligation.</p><p>The bill retroactively applies to interest incurred by a local government or electric cooperative in the nine years preceding enactment of the bill.</p><p>FEMA must reimburse states for loan interest for emergency or disaster-related projects that are pending obligation on the date of the bill\u2019s enactment.\u00a0FEMA must publish procedures for such reimbursement within 30 days after the bill\u2019s enactment and states must apply within 60 days after publication of the procedures.</p><p>The interest that qualifies for reimbursement may not exceed the amount of interest that would have been paid if the loan's interest rate were equal to the most recent prime rate.</p>",
      "updateDate": "2026-05-20",
      "versionCode": "id119hr2836"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2836ih.xml"
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
      "title": "FEMA Loan Interest Payment Relief Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:33:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FEMA Loan Interest Payment Relief Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-24T04:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Robert T. Stafford Disaster Relief and Emergency Assistance Act to provide for the authority to reimburse local governments or electric cooperatives for interest expenses, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-24T04:48:26Z"
    }
  ]
}
```
