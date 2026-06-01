# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2402?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2402
- Title: No Hungry Kids in Schools Act
- Congress: 119
- Bill type: HR
- Bill number: 2402
- Origin chamber: House
- Introduced date: 2025-03-27
- Update date: 2026-01-14T09:07:13Z
- Update date including text: 2026-01-14T09:07:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-27: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-03-27: Introduced in House

## Actions

- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-27",
    "latestAction": {
      "actionDate": "2025-03-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2402",
    "number": "2402",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "A000371",
        "district": "33",
        "firstName": "Pete",
        "fullName": "Rep. Aguilar, Pete [D-CA-33]",
        "lastName": "Aguilar",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "No Hungry Kids in Schools Act",
    "type": "HR",
    "updateDate": "2026-01-14T09:07:13Z",
    "updateDateIncludingText": "2026-01-14T09:07:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-27",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-27",
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
          "date": "2025-03-27T13:09:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "IN"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CA"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CA"
    },
    {
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "KY"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "True",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "NJ"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "DC"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CA"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "ME"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "MI"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "NJ"
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
      "sponsorshipDate": "2025-04-08",
      "state": "NC"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "HI"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "CA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "MI"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NY"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NY"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "NC"
    },
    {
      "bioguideId": "C001123",
      "district": "31",
      "firstName": "Gilbert",
      "fullName": "Rep. Cisneros, Gilbert Ray [D-CA-31]",
      "isOriginalCosponsor": "False",
      "lastName": "Cisneros",
      "middleName": "Ray",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "CA"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "AL"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "MO"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2402ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2402\nIN THE HOUSE OF REPRESENTATIVES\nMarch 27, 2025 Mr. Aguilar (for himself, Mr. Carson , Ms. Chu , Mr. DeSaulnier , Mr. McGarvey , Ms. Jacobs , Mr. Gottheimer , Mr. Mullin , Ms. Norton , Mr. Panetta , Ms. Pingree , Ms. Tlaib , and Mrs. Watson Coleman ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Richard B. Russell National School Lunch Act to establish statewide community eligibility for certain special assistance payments, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Hungry Kids in Schools Act .\n#### 2. Statewide community eligibility\nSection 11(a)(1)(F) of the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1759a(a)(1)(F) ) is amended by adding at the end the following:\n(xiv) Statewide community eligibility For each school year beginning on or after July 1, 2025, the Secretary shall establish an option for States to utilize a statewide community eligibility program, for purposes of which, in the case of a State agency that agrees to provide funding from sources other than Federal funds to ensure that local educational agencies in the State receive the free reimbursement rate for 100 percent of the meals served at applicable schools, as defined by the Secretary\u2014 (I) the multiplier described in clause (vii) shall apply; (II) the threshold described in clause (viii) shall be zero; and (III) the percentage of enrolled students who were identified students shall be calculated across all applicable schools in the State regardless of local educational agency. .",
      "versionDate": "2025-03-27",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-05-06T21:12:05Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-27",
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
          "measure-id": "id119hr2402",
          "measure-number": "2402",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-27",
          "originChamber": "HOUSE",
          "update-date": "2025-06-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2402v00",
            "update-date": "2025-06-27"
          },
          "action-date": "2025-03-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>No Hungry Kids in Schools Act</strong></p><p>This bill directs the Department of Agriculture\u00a0(USDA) to establish an option for states to utilize a statewide Community Eligibility Provision (CEP) for USDA school meal programs. As background, the CEP allows eligible schools, groups of schools, and school districts the option to offer free breakfast and lunch to all enrolled students without collecting household applications.</p><p>Specifically, USDA must establish a statewide CEP option that may be used by a state agency. The state agency must provide state (nonfederal) funding to local educational agencies to reimburse applicable schools at the free reimbursement rate for 100% of the meals served.</p><p>Eligibility for the statewide CEP must be based on a statewide calculation of the percentage of identified enrolled students, regardless of a school's local educational agency. Further, the bill lowers the CEP participation threshold for a statewide CEP to an identified student percentage (ISP) of zero, from a minimum of 25% under current regulations.\u00a0The ISP is the percentage of students who are eligible for free school meals without a household application, primarily those who are directly certified through the Supplemental Nutrition Assistance Program (SNAP).</p><p>In addition, the bill specifies that the reimbursement multiplier for school meals remains at the current level of 1.6. The reimbursement multiplier is used to calculate how many meals will be reimbursed at the free meal rate.</p>"
        },
        "title": "No Hungry Kids in Schools Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2402.xml",
    "summary": {
      "actionDate": "2025-03-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Hungry Kids in Schools Act</strong></p><p>This bill directs the Department of Agriculture\u00a0(USDA) to establish an option for states to utilize a statewide Community Eligibility Provision (CEP) for USDA school meal programs. As background, the CEP allows eligible schools, groups of schools, and school districts the option to offer free breakfast and lunch to all enrolled students without collecting household applications.</p><p>Specifically, USDA must establish a statewide CEP option that may be used by a state agency. The state agency must provide state (nonfederal) funding to local educational agencies to reimburse applicable schools at the free reimbursement rate for 100% of the meals served.</p><p>Eligibility for the statewide CEP must be based on a statewide calculation of the percentage of identified enrolled students, regardless of a school's local educational agency. Further, the bill lowers the CEP participation threshold for a statewide CEP to an identified student percentage (ISP) of zero, from a minimum of 25% under current regulations.\u00a0The ISP is the percentage of students who are eligible for free school meals without a household application, primarily those who are directly certified through the Supplemental Nutrition Assistance Program (SNAP).</p><p>In addition, the bill specifies that the reimbursement multiplier for school meals remains at the current level of 1.6. The reimbursement multiplier is used to calculate how many meals will be reimbursed at the free meal rate.</p>",
      "updateDate": "2025-06-27",
      "versionCode": "id119hr2402"
    },
    "title": "No Hungry Kids in Schools Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Hungry Kids in Schools Act</strong></p><p>This bill directs the Department of Agriculture\u00a0(USDA) to establish an option for states to utilize a statewide Community Eligibility Provision (CEP) for USDA school meal programs. As background, the CEP allows eligible schools, groups of schools, and school districts the option to offer free breakfast and lunch to all enrolled students without collecting household applications.</p><p>Specifically, USDA must establish a statewide CEP option that may be used by a state agency. The state agency must provide state (nonfederal) funding to local educational agencies to reimburse applicable schools at the free reimbursement rate for 100% of the meals served.</p><p>Eligibility for the statewide CEP must be based on a statewide calculation of the percentage of identified enrolled students, regardless of a school's local educational agency. Further, the bill lowers the CEP participation threshold for a statewide CEP to an identified student percentage (ISP) of zero, from a minimum of 25% under current regulations.\u00a0The ISP is the percentage of students who are eligible for free school meals without a household application, primarily those who are directly certified through the Supplemental Nutrition Assistance Program (SNAP).</p><p>In addition, the bill specifies that the reimbursement multiplier for school meals remains at the current level of 1.6. The reimbursement multiplier is used to calculate how many meals will be reimbursed at the free meal rate.</p>",
      "updateDate": "2025-06-27",
      "versionCode": "id119hr2402"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2402ih.xml"
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
      "title": "No Hungry Kids in Schools Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-05T05:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Hungry Kids in Schools Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-05T05:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Richard B. Russell National School Lunch Act to establish statewide community eligibility for certain special assistance payments, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-05T05:48:28Z"
    }
  ]
}
```
