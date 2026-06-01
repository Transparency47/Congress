# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1538?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1538
- Title: Delivering for Rural Seniors Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1538
- Origin chamber: House
- Introduced date: 2025-02-24
- Update date: 2026-02-26T09:06:53Z
- Update date including text: 2026-02-26T09:06:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-24: Introduced in House
- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-03-28 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.
- 2025-03-28 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.
- Latest action: 2025-02-24: Introduced in House

## Actions

- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Introduced in House
- 2025-02-24 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-03-28 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.
- 2025-03-28 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-24",
    "latestAction": {
      "actionDate": "2025-02-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1538",
    "number": "1538",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "N000193",
        "district": "3",
        "firstName": "Zachary",
        "fullName": "Rep. Nunn, Zachary [R-IA-3]",
        "lastName": "Nunn",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Delivering for Rural Seniors Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-26T09:06:53Z",
    "updateDateIncludingText": "2026-02-26T09:06:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-28",
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
      "actionDate": "2025-03-28",
      "committees": {
        "item": {
          "name": "Commodity Markets, Digital Assets, and Rural Development Subcommittee",
          "systemCode": "hsag22"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-24",
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
      "actionDate": "2025-02-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-24",
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
          "date": "2025-02-24T17:01:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": [
          {
            "activities": {
              "item": {
                "date": "2025-03-28T20:43:52Z",
                "name": "Referred to"
              }
            },
            "name": "Commodity Markets, Digital Assets, and Rural Development Subcommittee",
            "systemCode": "hsag22"
          },
          {
            "activities": {
              "item": {
                "date": "2025-03-28T20:43:52Z",
                "name": "Referred to"
              }
            },
            "name": "Nutrition and Foreign Agriculture Subcommittee",
            "systemCode": "hsag03"
          }
        ]
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
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
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
      "sponsorshipDate": "2025-07-14",
      "state": "NM"
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
      "sponsorshipDate": "2025-08-29",
      "state": "VA"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "IL"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "KS"
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
      "sponsorshipDate": "2025-09-04",
      "state": "PA"
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
      "sponsorshipDate": "2025-09-04",
      "state": "HI"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "CA"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "CA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-09-23",
      "state": "NY"
    },
    {
      "bioguideId": "S001199",
      "district": "11",
      "firstName": "Lloyd",
      "fullName": "Rep. Smucker, Lloyd [R-PA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Smucker",
      "party": "R",
      "sponsorshipDate": "2025-09-23",
      "state": "PA"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "PA"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-10-14",
      "state": "WV"
    },
    {
      "bioguideId": "R000610",
      "district": "14",
      "firstName": "Guy",
      "fullName": "Rep. Reschenthaler, Guy [R-PA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Reschenthaler",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "PA"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
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
      "sponsorshipDate": "2025-12-18",
      "state": "NY"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "OR"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
      "state": "WA"
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
      "sponsorshipDate": "2026-01-21",
      "state": "NC"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "IL"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "FL"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "NE"
    },
    {
      "bioguideId": "M001231",
      "district": "22",
      "firstName": "John",
      "fullName": "Rep. Mannion, John W. [D-NY-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Mannion",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1538ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1538\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 24, 2025 Mr. Nunn of Iowa (for himself and Ms. Crockett ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Agriculture and Consumer Protection Act of 1973 to establish a pilot grant program to award grants to facilitate home delivery of commodities under the commodity supplemental food program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Delivering for Rural Seniors Act of 2025 .\n#### 2. Commodity supplemental food program delivery pilot program\nThe Agriculture and Consumer Protection Act of 1973 ( 7 U.S.C. 612c note) is amended by inserting after section 5 the following:\n5A. Commodity supplemental food program delivery pilot program (a) Purpose The purposes of this section are\u2014 (1) to award grants for the operation of projects that increase the access of low-income elderly persons to commodities through home delivery; and (2) to evaluate such projects. (b) In general The Secretary shall award, on a competitive basis, grants to State agencies to carry out the activities described in subsection (e). (c) Maximum grant award A grant awarded to a State agency under this section may be in an amount not greater than the lesser of\u2014 (1) the State\u2019s commodity supplemental food program caseload at time of application multiplied by 60; or (2) $4,000,000. (d) Application A State agency seeking a grant under this section shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require. (e) Grant uses A State agency awarded a grant under this section shall distribute grant funds to eligible entities to operate projects that facilitate home delivery of commodities to participants in the commodity supplemental food program, including with respect to costs associated with\u2014 (1) transportation and distribution of commodities to participants in the commodity supplemental food program, including transportation and distribution services provided by a third party; (2) staffing required to operate home delivery services; and (3) outreach to participants or potential participants in the commodity supplemental food program with respect to home delivery. (f) Priority A State agency awarded a grant under this section shall prioritize eligible entities that serve participants in the commodity supplemental food program who reside in a rural area. (g) Report to the Secretary No later than 180 days after the end of the fiscal year in which a State agency is awarded a grant under this section and has distributed grant funds to eligible entities, and in each succeeding fiscal year until grant funds are expended, a State agency shall submit a report to the Secretary that includes\u2014 (1) a summary of the activities carried out under the project, including the quantity of commodities delivered, number of participants in the commodity supplemental food program served, and total number of deliveries; (2) an assessment of the effectiveness of the project, including\u2014 (A) a calculation of the average cost per delivery; and (B) an evaluation of any services provided by a third party; and (3) best practices regarding use of home delivery to improve the effectiveness of the commodity supplemental food program. (h) Definitions In this section: (1) Commodity supplemental food program The term commodity supplemental food program means the program established under section 4. (2) CFR terms The terms local agency , State agency , and subdistributing agency have the meanings given such terms in section 247.1 of title 7, Code of Federal Regulations (or successor regulations). (3) Eligible entity The term eligible entity means\u2014 (A) a local agency; or (B) a subdistributing agency. (4) Rural area The term rural area has the meaning given such term in section 343(a) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1991(a) ). (i) Authorization of appropriations There is authorized to be appropriated to carry out this section $10,000,000 for each of fiscal years 2026 through 2028, to remain available until expended. .",
      "versionDate": "2025-02-24",
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
        "updateDate": "2025-03-27T13:39:13Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-24",
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
          "measure-id": "id119hr1538",
          "measure-number": "1538",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-24",
          "originChamber": "HOUSE",
          "update-date": "2025-03-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1538v00",
            "update-date": "2025-03-27"
          },
          "action-date": "2025-02-24",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Delivering for Rural Seniors Act of 2025</strong></p><p>This bill directs the Food and Nutrition Service (FNS) to award competitive grants to state agencies under a home delivery pilot program for participants in the Commodity Supplemental Food Program (CSFP).\u00a0</p><p>As background,\u00a0the\u00a0CSFP works to improve the health of low-income persons at least 60 years of age by supplementing their diets with nutritious Department of Agriculture foods.</p><p>Under the pilot program, a state agency must distribute grant funds to an eligible entity (i.e., a local agency or subdistributing agency) to operate projects that facilitate home delivery of commodities to CSFP participants. Grant funds may be used for costs associated with</p><ul><li>transportation and distribution of commodities to CSFP participants,</li><li>staffing required to operate home delivery services, and</li><li>home delivery outreach to CSFP participants or potential participants.</li></ul><p>A state agency must prioritize eligible entities that serve CSFP participants who reside in rural areas.</p><p>A state agency must also submit an annual report to FNS about the project, including best practices regarding the use of home delivery to improve the effectiveness of the CSFP.</p>"
        },
        "title": "Delivering for Rural Seniors Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1538.xml",
    "summary": {
      "actionDate": "2025-02-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Delivering for Rural Seniors Act of 2025</strong></p><p>This bill directs the Food and Nutrition Service (FNS) to award competitive grants to state agencies under a home delivery pilot program for participants in the Commodity Supplemental Food Program (CSFP).\u00a0</p><p>As background,\u00a0the\u00a0CSFP works to improve the health of low-income persons at least 60 years of age by supplementing their diets with nutritious Department of Agriculture foods.</p><p>Under the pilot program, a state agency must distribute grant funds to an eligible entity (i.e., a local agency or subdistributing agency) to operate projects that facilitate home delivery of commodities to CSFP participants. Grant funds may be used for costs associated with</p><ul><li>transportation and distribution of commodities to CSFP participants,</li><li>staffing required to operate home delivery services, and</li><li>home delivery outreach to CSFP participants or potential participants.</li></ul><p>A state agency must prioritize eligible entities that serve CSFP participants who reside in rural areas.</p><p>A state agency must also submit an annual report to FNS about the project, including best practices regarding the use of home delivery to improve the effectiveness of the CSFP.</p>",
      "updateDate": "2025-03-27",
      "versionCode": "id119hr1538"
    },
    "title": "Delivering for Rural Seniors Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-24",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Delivering for Rural Seniors Act of 2025</strong></p><p>This bill directs the Food and Nutrition Service (FNS) to award competitive grants to state agencies under a home delivery pilot program for participants in the Commodity Supplemental Food Program (CSFP).\u00a0</p><p>As background,\u00a0the\u00a0CSFP works to improve the health of low-income persons at least 60 years of age by supplementing their diets with nutritious Department of Agriculture foods.</p><p>Under the pilot program, a state agency must distribute grant funds to an eligible entity (i.e., a local agency or subdistributing agency) to operate projects that facilitate home delivery of commodities to CSFP participants. Grant funds may be used for costs associated with</p><ul><li>transportation and distribution of commodities to CSFP participants,</li><li>staffing required to operate home delivery services, and</li><li>home delivery outreach to CSFP participants or potential participants.</li></ul><p>A state agency must prioritize eligible entities that serve CSFP participants who reside in rural areas.</p><p>A state agency must also submit an annual report to FNS about the project, including best practices regarding the use of home delivery to improve the effectiveness of the CSFP.</p>",
      "updateDate": "2025-03-27",
      "versionCode": "id119hr1538"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1538ih.xml"
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
      "title": "Delivering for Rural Seniors Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:53:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Delivering for Rural Seniors Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Agriculture and Consumer Protection Act of 1973 to establish a pilot grant program to award grants to facilitate home delivery of commodities under the commodity supplemental food program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:48:50Z"
    }
  ]
}
```
