# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3723?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3723
- Title: Tribal Gaming Regulatory Compliance Act
- Congress: 119
- Bill type: HR
- Bill number: 3723
- Origin chamber: House
- Introduced date: 2025-06-04
- Update date: 2026-05-20T08:06:51Z
- Update date including text: 2026-05-20T08:06:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-06-04: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-06-04: Introduced in House

## Actions

- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-04",
    "latestAction": {
      "actionDate": "2025-06-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3723",
    "number": "3723",
    "originChamber": "House",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "L000603",
        "district": "8",
        "firstName": "Morgan",
        "fullName": "Rep. Luttrell, Morgan [R-TX-8]",
        "lastName": "Luttrell",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Tribal Gaming Regulatory Compliance Act",
    "type": "HR",
    "updateDate": "2026-05-20T08:06:51Z",
    "updateDateIncludingText": "2026-05-20T08:06:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-04",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-04",
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
          "date": "2025-06-04T14:06:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
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
      "sponsorshipDate": "2025-06-04",
      "state": "TX"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "NM"
    },
    {
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "TX"
    },
    {
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "TX"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "TX"
    },
    {
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "TX"
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
      "sponsorshipDate": "2025-09-03",
      "state": "TX"
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
      "sponsorshipDate": "2025-09-03",
      "state": "TX"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "False",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "TX"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "TX"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "TX"
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
      "sponsorshipDate": "2026-03-02",
      "state": "TX"
    },
    {
      "bioguideId": "F000246",
      "district": "4",
      "firstName": "Pat",
      "fullName": "Rep. Fallon, Pat [R-TX-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Fallon",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "TX"
    },
    {
      "bioguideId": "J000304",
      "district": "13",
      "firstName": "Ronny",
      "fullName": "Rep. Jackson, Ronny [R-TX-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "TX"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "TX"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "TX"
    },
    {
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "False",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3723ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3723\nIN THE HOUSE OF REPRESENTATIVES\nJune 4, 2025 Mr. Luttrell (for himself, Ms. Escobar , and Mr. Babin ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo ensure all federally recognized Tribes that are eligible for gaming in the United States are regulated under the Indian Gaming Regulatory Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Tribal Gaming Regulatory Compliance Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nIn 1987, the Supreme Court ruled in California v. Cabazon Band of Mission Indians that if California regulated, rather than prohibited, gaming in the State, then an Indian Tribe could offer similar forms of gaming on its land.\n**(2)**\nIn response to the Cabazon decision, the Indian Gaming Regulatory Act ( Public Law 100\u2013497 ) was enacted, which has since supported and promoted Tribal economic development and self-sufficiency and continues to provide a regulatory structure for gaming on Tribal lands.\n**(3)**\nOver 200 Indian Tribes in 28 States are currently regulated under the Indian Gaming Regulatory Act.\n**(4)**\nOn June 15, 2022, the Supreme Court ruled that the Ysleta del Sur Pueblo and Alabama-Coushatta Indian Tribes of Texas Restoration Act ( Public Law 100\u201389 ; 101 Stat. 666) allows the Ysleta del Sur Pueblo and the Alabama-Coushatta Tribe to offer, on Tribal lands, gaming activities that are not fully prohibited by Texas law and without regard to any Texas regulations over such gaming activities.\n**(5)**\nAs a result of the Supreme Court decision, the Ysleta del Sur Pueblo and the Alabama-Coushatta Tribe are the only two Indian Tribes in the United States that have overlapping regulatory language governing their gaming activities (Public Law 497 and Public Law 100\u201389 ; 101 Stat. 666).\n**(6)**\nThis Act will eliminate any redundant regulatory language and ensure the Ysleta del Sur Pueblo and the Alabama-Coushatta Tribe are regulated in the same form and manner as all other gaming by Indian Tribes in the United States.\n#### 3. Amendment\nThe Ysleta del Sur Pueblo and Alabama and Coushatta Indian Tribes of Texas Restoration Act ( Public Law 100\u201389 ; 101 Stat. 666 et seq.) is amended\u2014\n**(1)**\nby inserting after section 2, the following:\n3 Rule of construction This Act shall be construed to ensure the full applicability of the Indian Gaming Regulatory Act ( 25 U.S.C. 2701 et seq. ) to gaming activities on Indian lands of the Ysleta del Sur Pueblo and Indian lands of the Alabama-Coushatta Tribe. ;\n**(2)**\nby striking section 107; and\n**(3)**\nby striking section 207.",
      "versionDate": "2025-06-04",
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
        "actionDate": "2025-07-31",
        "text": "Read twice and referred to the Committee on Indian Affairs."
      },
      "number": "2564",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Tribal Gaming Regulatory Compliance Act",
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
        "name": "Native Americans",
        "updateDate": "2025-07-01T16:37:33Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-04",
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
          "measure-id": "id119hr3723",
          "measure-number": "3723",
          "measure-type": "hr",
          "orig-publish-date": "2025-06-04",
          "originChamber": "HOUSE",
          "update-date": "2026-03-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3723v00",
            "update-date": "2026-03-27"
          },
          "action-date": "2025-06-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Tribal Gaming Regulatory Compliance Act</b></p> <p>This bill allows the Ysleta del Sur Pueblo and Alabama-Coushatta tribes to conduct gaming activities on their land in Texas if certain conditions are met.</p> <p>Currently, the Ysleta del Sur Pueblo and Alabama-Coushatta Indian Tribes of Texas Restoration Act prohibits the tribes from conducting gaming activities on their land if those activities are prohibited by Texas law. The bill repeals those provisions and instead applies the Indian Gaming Regulatory Act (IGRA) to gaming activities on Indian lands of the tribes.</p>"
        },
        "title": "Tribal Gaming Regulatory Compliance Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3723.xml",
    "summary": {
      "actionDate": "2025-06-04",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Tribal Gaming Regulatory Compliance Act</b></p> <p>This bill allows the Ysleta del Sur Pueblo and Alabama-Coushatta tribes to conduct gaming activities on their land in Texas if certain conditions are met.</p> <p>Currently, the Ysleta del Sur Pueblo and Alabama-Coushatta Indian Tribes of Texas Restoration Act prohibits the tribes from conducting gaming activities on their land if those activities are prohibited by Texas law. The bill repeals those provisions and instead applies the Indian Gaming Regulatory Act (IGRA) to gaming activities on Indian lands of the tribes.</p>",
      "updateDate": "2026-03-27",
      "versionCode": "id119hr3723"
    },
    "title": "Tribal Gaming Regulatory Compliance Act"
  },
  "summaries": [
    {
      "actionDate": "2025-06-04",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Tribal Gaming Regulatory Compliance Act</b></p> <p>This bill allows the Ysleta del Sur Pueblo and Alabama-Coushatta tribes to conduct gaming activities on their land in Texas if certain conditions are met.</p> <p>Currently, the Ysleta del Sur Pueblo and Alabama-Coushatta Indian Tribes of Texas Restoration Act prohibits the tribes from conducting gaming activities on their land if those activities are prohibited by Texas law. The bill repeals those provisions and instead applies the Indian Gaming Regulatory Act (IGRA) to gaming activities on Indian lands of the tribes.</p>",
      "updateDate": "2026-03-27",
      "versionCode": "id119hr3723"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3723ih.xml"
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
      "title": "Tribal Gaming Regulatory Compliance Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:32:58Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Tribal Gaming Regulatory Compliance Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-11T09:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To ensure all federally recognized Tribes that are eligible for gaming in the United States are regulated under the Indian Gaming Regulatory Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-11T09:33:25Z"
    }
  ]
}
```
