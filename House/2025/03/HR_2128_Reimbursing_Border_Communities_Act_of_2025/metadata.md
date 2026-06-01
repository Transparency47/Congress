# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2128?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2128
- Title: Reimbursing Border Communities Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2128
- Origin chamber: House
- Introduced date: 2025-03-14
- Update date: 2026-01-17T01:46:41Z
- Update date including text: 2026-01-17T01:46:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-14: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-03-14 - Committee: Referred to the Subcommittee on Border Security and Enforcement.
- Latest action: 2025-03-14: Introduced in House

## Actions

- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-03-14 - Committee: Referred to the Subcommittee on Border Security and Enforcement.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-14",
    "latestAction": {
      "actionDate": "2025-03-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2128",
    "number": "2128",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "J000304",
        "district": "13",
        "firstName": "Ronny",
        "fullName": "Rep. Jackson, Ronny [R-TX-13]",
        "lastName": "Jackson",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Reimbursing Border Communities Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-17T01:46:41Z",
    "updateDateIncludingText": "2026-01-17T01:46:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-14",
      "committees": {
        "item": {
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Border Security and Enforcement.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-14",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Homeland Security.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-14",
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
          "date": "2025-03-14T13:03:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-14T17:50:42Z",
              "name": "Referred to"
            }
          },
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "systemCode": "hshm00",
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
      "bioguideId": "D000594",
      "district": "15",
      "firstName": "Monica",
      "fullName": "Rep. De La Cruz, Monica [R-TX-15]",
      "isOriginalCosponsor": "True",
      "lastName": "De La Cruz",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "TX"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "TX"
    },
    {
      "bioguideId": "L000603",
      "district": "8",
      "firstName": "Morgan",
      "fullName": "Rep. Luttrell, Morgan [R-TX-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Luttrell",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "TX"
    },
    {
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "TX"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "TX"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "TX"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "TX"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "TX"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "TX"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "AZ"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig A. [R-TX-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2128ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2128\nIN THE HOUSE OF REPRESENTATIVES\nMarch 14, 2025 Mr. Jackson of Texas (for himself, Ms. De La Cruz , Mr. Crenshaw , Mr. Luttrell , Mr. Ellzey , Mr. Pfluger , Mr. Gooden , Mr. Babin , Mr. Gill of Texas , Mr. Sessions , and Mr. Gosar ) introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo direct the Secretary of Homeland Security to make grants to certain border communities for the purpose of reimbursing such communities for expenses related to security measures along the United States land border with Mexico, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Reimbursing Border Communities Act of 2025 .\n#### 2. Border community reimbursement grant program\n##### (a) In general\nSubject to the availability of appropriations, the Secretary of Homeland Security shall make grants to certain border communities for the purpose of reimbursing such communities for expenses related to security measures along the United States land border with Mexico, including additional wages for local law enforcement providing security for such border.\n##### (b) Eligibility\nTo be eligible for a grant under this section, a border community\u2014\n**(1)**\nshall be a unit of local government located in the United States within 200 miles of the land border with Mexico;\n**(2)**\nshall submit to the Secretary of Homeland Security an application in such form, at such time, and containing such information as the Secretary determines appropriate; and\n**(3)**\nmay not be a sanctuary jurisdiction.\n##### (c) Grant amount\nA grant made under subsection (a) may not exceed $500,000 for each fiscal year.\n##### (d) Limitation on use of funds\nAny grant awarded under this section may not be used to reimburse nonprofit organizations, to fund legal representation, or to provide educational, housing, food, or healthcare resources to an alien.\n##### (e) Report\nNot later than one year after the date of the enactment of this Act and annually thereafter through 2035, the Secretary, acting through the Commissioner of U.S. Customs and Border Protection, shall submit to the Committee on Homeland Security of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate a report that includes\u2014\n**(1)**\ninformation relating to the\u2014\n**(A)**\nuse of each grant made under subsection (a); and\n**(B)**\nimplementation of this section; and\n**(2)**\nany recommendations of the Secretary for improving the implementation of this section, including with respect to the amount of funding provided to each recipient of a grant under this section.\n##### (f) Definitions\nIn this section:\n**(1)**\nThe term sanctuary jurisdiction means a State or unit of local government that\u2014\n**(A)**\nviolates section 642 of the Illegal Immigration Reform and Immigrant Responsibility Act of 1996 ( 8 U.S.C. 1373 );\n**(B)**\nrestricts compliance with a detainer issued by the Secretary of Homeland Security (or the Secretary\u2019s designee); or\n**(C)**\nhas any law or policy in effect that violates the immigration laws.\n**(2)**\nThe term alien has the meaning given such term in section 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 ).\n##### (g) Authorization of appropriations\nThere is authorized to be appropriated $25,000,000 for each of fiscal years 2026 through 2036 to carry out this section.",
      "versionDate": "2025-03-14",
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
        "name": "Immigration",
        "updateDate": "2025-04-03T11:38:59Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-14",
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
          "measure-id": "id119hr2128",
          "measure-number": "2128",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-14",
          "originChamber": "HOUSE",
          "update-date": "2026-01-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2128v00",
            "update-date": "2026-01-17"
          },
          "action-date": "2025-03-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Reimbursing Border Communities Act of 2025</strong></p><p>This bill requires the Department of Homeland Security to make grants to certain border communities for expenses related to security measures along the southern border.</p><p>Specifically, the local government of a community is eligible for a grant if it is located within 200 miles of the border and is not a sanctuary jurisdiction as defined by the bill.</p><p>Additionally, no grant may be used to reimburse nonprofit organizations, fund legal representation, or provide educational, housing, food, or health care resources to a non-U.S. national (<em>alien</em> under federal law).</p>"
        },
        "title": "Reimbursing Border Communities Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2128.xml",
    "summary": {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Reimbursing Border Communities Act of 2025</strong></p><p>This bill requires the Department of Homeland Security to make grants to certain border communities for expenses related to security measures along the southern border.</p><p>Specifically, the local government of a community is eligible for a grant if it is located within 200 miles of the border and is not a sanctuary jurisdiction as defined by the bill.</p><p>Additionally, no grant may be used to reimburse nonprofit organizations, fund legal representation, or provide educational, housing, food, or health care resources to a non-U.S. national (<em>alien</em> under federal law).</p>",
      "updateDate": "2026-01-17",
      "versionCode": "id119hr2128"
    },
    "title": "Reimbursing Border Communities Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Reimbursing Border Communities Act of 2025</strong></p><p>This bill requires the Department of Homeland Security to make grants to certain border communities for expenses related to security measures along the southern border.</p><p>Specifically, the local government of a community is eligible for a grant if it is located within 200 miles of the border and is not a sanctuary jurisdiction as defined by the bill.</p><p>Additionally, no grant may be used to reimburse nonprofit organizations, fund legal representation, or provide educational, housing, food, or health care resources to a non-U.S. national (<em>alien</em> under federal law).</p>",
      "updateDate": "2026-01-17",
      "versionCode": "id119hr2128"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2128ih.xml"
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
      "title": "Reimbursing Border Communities Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-02T04:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Reimbursing Border Communities Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-02T04:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Homeland Security to make grants to certain border communities for the purpose of reimbursing such communities for expenses related to security measures along the United States land border with Mexico, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-02T04:18:31Z"
    }
  ]
}
```
