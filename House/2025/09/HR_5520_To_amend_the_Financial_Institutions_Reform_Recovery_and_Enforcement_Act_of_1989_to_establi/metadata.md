# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5520?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5520
- Title: Portal for Appraisal Licensing Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5520
- Origin chamber: House
- Introduced date: 2025-09-19
- Update date: 2026-05-30T08:05:59Z
- Update date including text: 2026-05-30T08:05:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-19: Introduced in House
- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-09-19: Introduced in House

## Actions

- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-19",
    "latestAction": {
      "actionDate": "2025-09-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5520",
    "number": "5520",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "L000583",
        "district": "11",
        "firstName": "Barry",
        "fullName": "Rep. Loudermilk, Barry [R-GA-11]",
        "lastName": "Loudermilk",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Portal for Appraisal Licensing Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-30T08:05:59Z",
    "updateDateIncludingText": "2026-05-30T08:05:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-19",
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
      "actionDate": "2025-09-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-19",
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
          "date": "2025-09-19T13:04:40Z",
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
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "PA"
    },
    {
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "WI"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "NV"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "CO"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "CO"
    },
    {
      "bioguideId": "K000392",
      "district": "8",
      "firstName": "David",
      "fullName": "Rep. Kustoff, David [R-TN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Kustoff",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "TN"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "VA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "NY"
    },
    {
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "SC"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-05-29",
      "state": "NJ"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-05-29",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5520ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5520\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 19, 2025 Mr. Loudermilk (for himself, Mr. Meuser , Mr. Fitzgerald , Ms. Lee of Nevada , Mr. Neguse , Ms. Pettersen , and Mr. Kustoff ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Financial Institutions Reform, Recovery, and Enforcement Act of 1989 to establish a Portal for Appraiser Credentialing and AMC Registration Information, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Portal for Appraisal Licensing Act of 2025 .\n#### 2. Portal for Appraiser Credentialing and AMC Registration Information\nSection 1103 of the Financial Institutions Reform, Recovery, and Enforcement Act of 1989 ( 12 U.S.C. 3332 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (3), by striking and at the end;\n**(B)**\nin paragraph (4), by striking the period on the end and inserting a semicolon;\n**(C)**\nin paragraph (5)\u2014\n**(i)**\nby striking . The report and inserting , and which ; and\n**(ii)**\nby striking the period on the end and inserting a semicolon;\n**(D)**\nin paragraph (6), by striking the period on the end and inserting ; and ; and\n**(E)**\nby adding at the end the following:\n(7) establish and maintain the Portal for Appraiser Credentialing and AMC Registration Information described under subsection (c). ; and\n**(2)**\nby adding at the end the following:\n(c) Portal for Appraiser Credentialing and AMC Registration Information (1) In general The Appraisal Subcommittee shall establish and maintain a cloud-based system to be called the Portal for Appraiser Credentialing and AMC Registration Information (the Portal ), which\u2014 (A) shall provide appraisers and appraisal management companies a central depository for license, certification, and registration applications and renewals; (B) shall provide connectivity with State appraiser certifying and licensing agencies for their access to all application and renewal information, including completed qualifying and continuing education, experience logs, examination results, background check information, where applicable, and any other information the Appraisal Subcommittee determines appropriate (after consideration of any advice from the advisory committee established under paragraph (6)); (C) shall make available payment of all license, certification, and registration fees and delivery of letters of good standing to State appraiser certifying and licensing agencies; and (D) may utilize an existing platform, if available. (2) Background checks (A) Access to records Not\u00adwith\u00adstand\u00ading any other provision of law, in providing appraisal functions, the Attorney General shall provide access to all criminal history information to the appropriate State officials responsible for regulating State-licensed and State-certified appraisers or appraisal management companies to the extent criminal history background checks are required under the laws of the State for the licensing or certification of such appraisers and registering appraisal management companies. (B) Agent For the purposes of this paragraph and in order to reduce the points of contact which the Federal Bureau of Investigation may have to maintain for purposes of subparagraph (A), the Appraisal Subcommittee may be used as a channeling agent of the States for requesting and distributing information between the Department of Justice and the appropriate State agencies. (C) Other persons requiring a background check To the extent FBI criminal history background checks are required under the laws of a State, appraisers and any other person that may require such a background check shall submit fingerprints to the Portal and authorize the Appraisal Subcommittee to process a criminal background check with the Federal Bureau of Investigation. (D) Treatment of background checks Background checks completed under this paragraph shall satisfy any third-party oversight requirements imposed by Federal financial institutions regulatory agencies. (3) Additional content information (A) Education courses For purposes of the education information maintained by the Portal\u2014 (i) a State appraiser certifying and licensing agency may notify the Portal of which particular courses have been approved by the agency; and (ii) both education providers and State appraiser certifying and licensing agencies of States may submit to the Portal lists of individuals who have completed such courses. (B) Unique identifiers The Appraisal Subcommittee shall use a unique identifier to identify each individual who submits an application through the Portal or otherwise makes use of the Portal. The Appraisal Subcommittee may also use a unique identifier to identify each appraisal management company that submits an application through the Portal or otherwise makes use of the Portal. (4) No effect on States\u2019 rights States shall retain the ability to act independently upon license, certification, and registration applications and renewals for appraisers and appraisal management companies. (5) Treatment of fees State cre\u00adden\u00adtial\u00ading fees and any State-specific information shall continue to be provided to States by appraisers and appraisal management companies, but transmitted through the Portal via a streamlined process and application. (6) Advisory committee (A) In general The Appraisal Subcommittee shall establish an advisory committee to advise the Appraisal Subcommittee on the establishment of the Portal. (B) Membership The advisory committee shall consist of representatives of industry associations, appraisers, lenders, appraisal management companies, and State appraiser certifying and licensing agencies, to be determined by the Appraisal Subcommittee. (7) Funding (A) User fees For the sole purpose of paying for the cost of establishing and maintaining the Portal and carrying out the background checks required under paragraph (2)(A), the Appraisal Subcommittee may charge a reasonable fee to individuals and appraisal management companies making use of the Portal. The fee shall be revenue neutral to the costs of developing and maintaining the Portal. (B) State grants The Appraisal Subcommittee shall make grants available to State appraiser certifying and licensing agencies, in accordance with policies to be developed by the Appraisal Subcommittee, to support the efforts of such agencies to connect State systems with the Portal. .",
      "versionDate": "2025-09-19",
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
        "updateDate": "2025-12-17T15:39:26Z"
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
      "date": "2025-09-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5520ih.xml"
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
      "title": "Portal for Appraisal Licensing Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-04T10:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Portal for Appraisal Licensing Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-04T10:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Financial Institutions Reform, Recovery, and Enforcement Act of 1989 to establish a Portal for Appraiser Credentialing and AMC Registration Information, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-04T10:18:24Z"
    }
  ]
}
```
