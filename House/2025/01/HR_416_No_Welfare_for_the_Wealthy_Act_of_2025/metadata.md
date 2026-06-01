# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/416?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/416
- Title: No Welfare for the Wealthy Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 416
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2026-04-10T08:05:54Z
- Update date including text: 2026-04-10T08:05:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-02-14 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.
- Latest action: 2025-01-15: Introduced in House

## Actions

- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-02-14 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-15",
    "latestAction": {
      "actionDate": "2025-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/416",
    "number": "416",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "C001118",
        "district": "6",
        "firstName": "Ben",
        "fullName": "Rep. Cline, Ben [R-VA-6]",
        "lastName": "Cline",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "No Welfare for the Wealthy Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-10T08:05:54Z",
    "updateDateIncludingText": "2026-04-10T08:05:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-14",
      "committees": {
        "item": {
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Nutrition and Foreign Agriculture.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-15",
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
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-15",
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
          "date": "2025-01-15T15:01:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-14T18:04:37Z",
              "name": "Referred to"
            }
          },
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "systemCode": "hsag00",
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
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "LA"
    },
    {
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "TX"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "OK"
    },
    {
      "bioguideId": "G000590",
      "district": "7",
      "firstName": "Mark",
      "fullName": "Rep. Green, Mark E. [R-TN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "TN"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "TX"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "NJ"
    },
    {
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "TX"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "NC"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
      "state": "PA"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
      "state": "MS"
    },
    {
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr416ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 416\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Mr. Cline (for himself, Mr. Higgins of Louisiana , Mr. Ellzey , Mr. Brecheen , and Mr. Green of Tennessee ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food and Nutrition Act of 2008 to close the nominal benefits loophole.\n#### 1. Short title\nThis Act may be cited as the No Welfare for the Wealthy Act of 2025 .\n#### 2. Amendment\nSection 5(a) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2014(a) ) is amended to read as follows:\nNo household shall be eligible to receive benefits pursuant to this section if it does not meet the income and resource criteria under subsections (c) and (g). .\n#### 3. Effective date; application of amendment\n##### (a) Effective date\nExcept as provided in subsection (b), this Act and the amendment made by this Act shall take effect 1 year after the date of the enactment of this Act.\n##### (b) Application of amendment\nThe amendment made by this Act shall not apply with respect to certification periods that begin before the effective date of this Act.",
      "versionDate": "2025-01-15",
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
        "updateDate": "2025-02-21T12:20:44Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-15",
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
          "measure-id": "id119hr416",
          "measure-number": "416",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-15",
          "originChamber": "HOUSE",
          "update-date": "2025-04-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr416v00",
            "update-date": "2025-04-03"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>No Welfare for the Wealthy Act of 2025</strong></p><p>This bill requires all households participating in the Supplemental Nutrition Assistance Program (SNAP) to meet the program's income and asset requirements, thereby eliminating certain alternative SNAP eligibility\u00a0pathways.</p><p>Currently, a\u00a0household may be eligible for SNAP by meeting\u00a0program-specific federal eligibility requirements, which include both income and asset tests. A household may also be automatically or <em>categorically eligible</em> for SNAP based on eligibility for or receiving cash benefits from other specified low-income assistance programs (e.g., Temporary Assistance for Needy Families [TANF]). Under this categorical eligibility, households that already meet financial eligibility rules in a program like TANF are not required to go through a SNAP financial eligibility determination.\u00a0</p><p>A\u00a0majority of states also provide broad-based categorical eligibility (BBCE), a policy that makes most households with an income below a certain threshold categorically eligible for SNAP. Under BBCE, these states typically make households categorically eligible through receiving or being authorized to receive a minimal non-cash TANF benefit or service (e.g., a pamphlet). A state may set its own BBCE financial eligibility requirements for a household so long as the gross income requirement is below a certain level. A state's requirements do not have to match SNAP program-specific eligibility requirements. For example,\u00a0most states\u00a0that provide BBCE\u00a0do not have an asset test for SNAP eligibility.</p><p>The bill requires all SNAP households, including those that qualify under categorical eligibility, to meet the program's income and asset requirements.</p>"
        },
        "title": "No Welfare for the Wealthy Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr416.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Welfare for the Wealthy Act of 2025</strong></p><p>This bill requires all households participating in the Supplemental Nutrition Assistance Program (SNAP) to meet the program's income and asset requirements, thereby eliminating certain alternative SNAP eligibility\u00a0pathways.</p><p>Currently, a\u00a0household may be eligible for SNAP by meeting\u00a0program-specific federal eligibility requirements, which include both income and asset tests. A household may also be automatically or <em>categorically eligible</em> for SNAP based on eligibility for or receiving cash benefits from other specified low-income assistance programs (e.g., Temporary Assistance for Needy Families [TANF]). Under this categorical eligibility, households that already meet financial eligibility rules in a program like TANF are not required to go through a SNAP financial eligibility determination.\u00a0</p><p>A\u00a0majority of states also provide broad-based categorical eligibility (BBCE), a policy that makes most households with an income below a certain threshold categorically eligible for SNAP. Under BBCE, these states typically make households categorically eligible through receiving or being authorized to receive a minimal non-cash TANF benefit or service (e.g., a pamphlet). A state may set its own BBCE financial eligibility requirements for a household so long as the gross income requirement is below a certain level. A state's requirements do not have to match SNAP program-specific eligibility requirements. For example,\u00a0most states\u00a0that provide BBCE\u00a0do not have an asset test for SNAP eligibility.</p><p>The bill requires all SNAP households, including those that qualify under categorical eligibility, to meet the program's income and asset requirements.</p>",
      "updateDate": "2025-04-03",
      "versionCode": "id119hr416"
    },
    "title": "No Welfare for the Wealthy Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Welfare for the Wealthy Act of 2025</strong></p><p>This bill requires all households participating in the Supplemental Nutrition Assistance Program (SNAP) to meet the program's income and asset requirements, thereby eliminating certain alternative SNAP eligibility\u00a0pathways.</p><p>Currently, a\u00a0household may be eligible for SNAP by meeting\u00a0program-specific federal eligibility requirements, which include both income and asset tests. A household may also be automatically or <em>categorically eligible</em> for SNAP based on eligibility for or receiving cash benefits from other specified low-income assistance programs (e.g., Temporary Assistance for Needy Families [TANF]). Under this categorical eligibility, households that already meet financial eligibility rules in a program like TANF are not required to go through a SNAP financial eligibility determination.\u00a0</p><p>A\u00a0majority of states also provide broad-based categorical eligibility (BBCE), a policy that makes most households with an income below a certain threshold categorically eligible for SNAP. Under BBCE, these states typically make households categorically eligible through receiving or being authorized to receive a minimal non-cash TANF benefit or service (e.g., a pamphlet). A state may set its own BBCE financial eligibility requirements for a household so long as the gross income requirement is below a certain level. A state's requirements do not have to match SNAP program-specific eligibility requirements. For example,\u00a0most states\u00a0that provide BBCE\u00a0do not have an asset test for SNAP eligibility.</p><p>The bill requires all SNAP households, including those that qualify under categorical eligibility, to meet the program's income and asset requirements.</p>",
      "updateDate": "2025-04-03",
      "versionCode": "id119hr416"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr416ih.xml"
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
      "title": "No Welfare for the Wealthy Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-11T12:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Welfare for the Wealthy Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T12:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food and Nutrition Act of 2008 to close the nominal benefits loophole.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T12:48:21Z"
    }
  ]
}
```
