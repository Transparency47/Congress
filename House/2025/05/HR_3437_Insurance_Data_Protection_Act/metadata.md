# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3437?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3437
- Title: Insurance Data Protection Act
- Congress: 119
- Bill type: HR
- Bill number: 3437
- Origin chamber: House
- Introduced date: 2025-05-15
- Update date: 2026-04-24T08:07:14Z
- Update date including text: 2026-04-24T08:07:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-15: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-15 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-05-15: Introduced in House

## Actions

- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-15 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3437",
    "number": "3437",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "F000471",
        "district": "5",
        "firstName": "Scott",
        "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
        "lastName": "Fitzgerald",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "Insurance Data Protection Act",
    "type": "HR",
    "updateDate": "2026-04-24T08:07:14Z",
    "updateDateIncludingText": "2026-04-24T08:07:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-15",
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
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-15",
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
          "date": "2025-05-15T14:06:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-15T14:06:05Z",
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
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "NE"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "PA"
    },
    {
      "bioguideId": "D000594",
      "district": "15",
      "firstName": "Monica",
      "fullName": "Rep. De La Cruz, Monica [R-TX-15]",
      "isOriginalCosponsor": "True",
      "lastName": "De La Cruz",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "TX"
    },
    {
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "SC"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "NY"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "TN"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "NC"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "FL"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "MI"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "TX"
    },
    {
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "SC"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "IA"
    },
    {
      "bioguideId": "L000583",
      "district": "11",
      "firstName": "Barry",
      "fullName": "Rep. Loudermilk, Barry [R-GA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Loudermilk",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "GA"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "WI"
    },
    {
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "WY"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "MI"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "TX"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "NY"
    },
    {
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "KY"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "MN"
    },
    {
      "bioguideId": "S001213",
      "district": "1",
      "firstName": "Bryan",
      "fullName": "Rep. Steil, Bryan [R-WI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Steil",
      "party": "R",
      "sponsorshipDate": "2025-07-02",
      "state": "WI"
    },
    {
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "OH"
    },
    {
      "bioguideId": "D000634",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Downing, Troy [R-MT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Downing",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "MT"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2026-04-23",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3437ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3437\nIN THE HOUSE OF REPRESENTATIVES\nMay 15, 2025 Mr. Fitzgerald (for himself, Mr. Flood , Mr. Meuser , Ms. De La Cruz , Mr. Timmons , Mr. Garbarino , Mr. Ogles , Mr. Moore of North Carolina , Mr. Donalds , Mr. Huizenga , Mr. Williams of Texas , Mr. Norman , Mr. Nunn of Iowa , Mr. Loudermilk , Mr. Grothman , Ms. Hageman , and Mr. Moolenaar ) introduced the following bill; which was referred to the Committee on Financial Services , and in addition to the Committee on Agriculture , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo prohibit the Federal Insurance Office of the Department of the Treasury and other financial regulators from collecting data directly from an insurance company.\n#### 1. Short title\nThis Act may be cited as the Insurance Data Protection Act .\n#### 2. Repeal of subpoena and enforcement authority\nSection 313(e) of title 31, United States Code, is amended by striking paragraph (6).\n#### 3. Confidentiality by Federal Insurance Office\nSection 313(e)(5) of title 31, United States Code, is amended\u2014\n**(1)**\nin subparagraph (A), by inserting after Office the following: , or the sharing of any nonpublicly available data and information with or by the Office among any other Federal agency, any State insurance regulator (or any agent of such a regulator), or any other entity, ;\n**(2)**\nin subparagraph (C)(ii), by inserting any privilege described in subparagraph (A) or after including ; and\n**(3)**\nin subparagraph (D), by inserting including the exceptions under that section, after United States Code, .\n#### 4. Limitation on subpoenas by the Office of Financial Research\nSection 153(f)(1) of the Financial Stability Act of 2010 ( 12 U.S.C. 5343(f)(1) ) is amended, in the matter preceding subparagraph (A), by inserting after financial company the following: (other than an insurance company, as defined in section 201(a)) .\n#### 5. Confidentiality by financial regulators\n##### (a) In general\nThe Financial Stability Act of 2010 ( 12 U.S.C. 5311 et seq. ) is amended by adding at the end the following:\nD Treatment of data collected from insurance companies 181. Treatment of data collected from insurance companies by financial regulators (a) Definitions In this section: (1) Covered entity The term covered entity means a nonbank financial company that is an insurance company. (2) Financial regulator The term financial regulator means the Commission, the Commodity Futures Trading Commission, the Council, the Federal banking agencies, and the Office of Financial Research. (3) Insurance company The term insurance company has the meaning given the term in section 201(a). (b) Advance coordination (1) In general (A) Pre-collection Before collecting any data or information pursuant to this title or title II from a covered entity, a financial regulator shall coordinate with each relevant Federal agency, State insurance regulator, and other Federal or State regulatory agency, and with any publicly available source, to determine if the data or information to be collected is available from, and may be obtained in a timely manner by, that agency, regulator, or regulatory agency, individually or collectively, or that publicly available source. (B) Determinations (i) Information available If a financial regulator, under subparagraph (A), determines that the data or information described in that subparagraph is available, and may be obtained in a timely manner, from an agency, regulator, regulatory agency, or source described in that subparagraph, the financial regulator shall obtain the data or information from that agency, regulator, regulatory agency, or source. (ii) Information unavailable If a financial regulator, under subparagraph (A) determines that the data or information described in that subparagraph is not available, the financial regulatory may collect that data or information from the applicable covered entity only if the financial regulator complies with the requirements of subchapter I of chapter 35 of title 44, United States Code (commonly referred to as the \u2018Paperwork Reduction Act \u2019), in collecting that data or information. (2) Authority to provide information Notwithstanding any other provision of law, for the purposes of paragraph (1), each relevant Federal agency and State insurance regulator or other Federal or State regulatory agency may provide to a financial regulator data or information described in that paragraph. (c) Confidentiality (1) Retention of privilege The sharing by a covered entity of any nonpublicly available data or information with a financial regulator under this title or title II shall not constitute a waiver of, or otherwise affect, any privilege arising under Federal or State law (including the rules of any Federal or State court) to which the data or information is otherwise subject. (2) Continued application of prior confidentiality agreements Any requirement under Federal or State law to the extent otherwise applicable, or any requirement pursuant to a written agreement in effect between the original source of any nonpublicly available data or information and the source of that data or information to a financial regulator, regarding the privacy or confidentiality of any data or information in the possession of the source to a financial regulator, shall continue to apply to that data or information after the data or information has been provided under this section to the financial regulator. (3) Information-sharing agreement Any data or information obtained by a financial regulator may be made available to State insurance regulators, individually or collectively, through an information-sharing agreement that\u2014 (A) shall comply with applicable Federal law; and (B) shall not constitute a waiver of, or otherwise affect, any privilege under Federal or State law (including any privilege described in paragraph (1) and the rules of any Federal or State court) to which the data or information is otherwise subject. (4) Agency disclosure requirements Section 552 of title 5, United States Code, including the exceptions under that section, shall apply to any data or information submitted to a financial regulator by a covered entity under this section. .\n##### (b) Technical amendment\nThe table of contents in section 1(b) of the Dodd-Frank Wall Street Reform and Consumer Protection Act ( Public Law 111\u2013203 ) is amended by inserting after the item relating to section 176 the following:\nSubtitle D\u2014Treatment of data collected from insurance companies Sec. 181. Treatment of data collected from insurance companies by financial regulators. .",
      "versionDate": "2025-05-15",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-04-30",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "1544",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Insurance Data Protection Act",
      "type": "S"
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
        "updateDate": "2025-05-28T12:54:23Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-15",
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
          "measure-id": "id119hr3437",
          "measure-number": "3437",
          "measure-type": "hr",
          "orig-publish-date": "2025-05-15",
          "originChamber": "HOUSE",
          "update-date": "2026-04-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3437v00",
            "update-date": "2026-04-13"
          },
          "action-date": "2025-05-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Insurance Data Protection Act</strong></p><p>This bill limits the ability of federal entities to compel insurance companies to share information.</p><p>Specifically, the bill eliminates the subpoena power of the Federal Insurance Office. Under current law, the office has the power to subpoena information from insurers to, among other purposes, identify issues that could contribute to a systemic crisis in the insurance industry or the U.S. financial system.</p><p>The bill also eliminates the ability of the Office of Financial Research to subpoena insurance companies.</p><p>When seeking to collect insurance company data under specified consumer protection laws, a financial regulator must obtain the data from other regulators or from publicly available sources if possible. Otherwise, the financial regulator may only collect this data directly from the insurance company if the regulator complies with the Paperwork Reduction Act.\u00a0 \u00a0</p>"
        },
        "title": "Insurance Data Protection Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3437.xml",
    "summary": {
      "actionDate": "2025-05-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Insurance Data Protection Act</strong></p><p>This bill limits the ability of federal entities to compel insurance companies to share information.</p><p>Specifically, the bill eliminates the subpoena power of the Federal Insurance Office. Under current law, the office has the power to subpoena information from insurers to, among other purposes, identify issues that could contribute to a systemic crisis in the insurance industry or the U.S. financial system.</p><p>The bill also eliminates the ability of the Office of Financial Research to subpoena insurance companies.</p><p>When seeking to collect insurance company data under specified consumer protection laws, a financial regulator must obtain the data from other regulators or from publicly available sources if possible. Otherwise, the financial regulator may only collect this data directly from the insurance company if the regulator complies with the Paperwork Reduction Act.\u00a0 \u00a0</p>",
      "updateDate": "2026-04-13",
      "versionCode": "id119hr3437"
    },
    "title": "Insurance Data Protection Act"
  },
  "summaries": [
    {
      "actionDate": "2025-05-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Insurance Data Protection Act</strong></p><p>This bill limits the ability of federal entities to compel insurance companies to share information.</p><p>Specifically, the bill eliminates the subpoena power of the Federal Insurance Office. Under current law, the office has the power to subpoena information from insurers to, among other purposes, identify issues that could contribute to a systemic crisis in the insurance industry or the U.S. financial system.</p><p>The bill also eliminates the ability of the Office of Financial Research to subpoena insurance companies.</p><p>When seeking to collect insurance company data under specified consumer protection laws, a financial regulator must obtain the data from other regulators or from publicly available sources if possible. Otherwise, the financial regulator may only collect this data directly from the insurance company if the regulator complies with the Paperwork Reduction Act.\u00a0 \u00a0</p>",
      "updateDate": "2026-04-13",
      "versionCode": "id119hr3437"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3437ih.xml"
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
      "title": "Insurance Data Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-22T02:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Insurance Data Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-22T02:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the Federal Insurance Office of the Department of the Treasury and other financial regulators from collecting data directly from an insurance company.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-22T02:18:25Z"
    }
  ]
}
```
