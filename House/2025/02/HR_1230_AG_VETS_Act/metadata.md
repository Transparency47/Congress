# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1230?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1230
- Title: AG VETS Act
- Congress: 119
- Bill type: HR
- Bill number: 1230
- Origin chamber: House
- Introduced date: 2025-02-12
- Update date: 2026-04-24T08:07:04Z
- Update date including text: 2026-04-24T08:07:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-12: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-12 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-20 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.
- 2025-12-19 - Committee: Referred to the Subcommittee on Economic Opportunity.
- Latest action: 2025-02-12: Introduced in House

## Actions

- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-12 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-20 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.
- 2025-12-19 - Committee: Referred to the Subcommittee on Economic Opportunity.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-12",
    "latestAction": {
      "actionDate": "2025-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1230",
    "number": "1230",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "V000135",
        "district": "3",
        "firstName": "Derrick",
        "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
        "lastName": "Van Orden",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "AG VETS Act",
    "type": "HR",
    "updateDate": "2026-04-24T08:07:04Z",
    "updateDateIncludingText": "2026-04-24T08:07:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-19",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Opportunity.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-20",
      "committees": {
        "item": {
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Conservation, Research, and Biotechnology.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-12",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-12",
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
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-12",
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
          "date": "2025-02-12T15:07:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-19T19:05:26Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "systemCode": "hsvr00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-12T15:07:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-20T20:37:57Z",
              "name": "Referred to"
            }
          },
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
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
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "NC"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-12-19",
      "state": "CO"
    },
    {
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2026-04-23",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1230ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1230\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2025 Mr. Van Orden (for himself and Mr. Davis of North Carolina ) introduced the following bill; which was referred to the Committee on Agriculture , and in addition to the Committee on Veterans' Affairs , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Agricultural Research, Extension, and Education Reform Act of 1998 to direct the Secretary of Agriculture to establish a program under which the Secretary will award competitive grants to eligible entities for the purpose of establishing and enhancing farming and ranching opportunities for veterans.\n#### 1. Short title\nThis Act may be cited as the Agriculture Grants for Veterans Education and Training Services Act or the AG VETS Act .\n#### 2. Agriculture grants for veteran education and training services\nTitle IV of the Agricultural Research, Extension, and Education Reform Act of 1998 ( 7 U.S.C. 7624 et seq. ) is amended by adding at the end the following:\n414. Agriculture grants for veteran education and training services (a) In general The Secretary shall establish a program under which the Secretary will award competitive grants to eligible entities for the purpose of establishing and enhancing farming and ranching opportunities for veterans (as defined in section 101(2) of title 38, United States Code). (b) Eligible entities An entity is eligible for a grant under this section if such entity is\u2014 (1) a cooperative extension service; (2) a land-grant college or university (as defined in section 1404 of the National Agricultural Research, Extension, and Teaching Policy Act of 1977 ( 7 U.S.C. 3103 )); (3) a non-land-grant college of agriculture (as defined in such section); (4) a Hispanic-serving agricultural college and university (as defined in such section); (5) a State department of agriculture; (6) a nonprofit organization; (7) a community-based organization; or (8) a combination of 2 or more eligible entities described in paragraphs (1) through (7). (c) Use of funds An eligible entity that receives a grant under this section shall use the funds received through the grant\u2014 (1) to provide training and classroom education that leads to a comprehensive understanding of farm and ranch business operations and management practices; (2) to develop or identify curriculum that veteran farmers and ranchers can adopt to help manage their enterprise; (3) to offer education, workshops, tours, and instructor-supervised field experiences; or (4) to support any other activity, as identified by the Secretary, to increase the number of military veterans pursuing knowledge and skills development in agriculture. (d) Matching funds An entity that receives a grant under this section shall provide non-Federal matching funds for the purposes of carrying out this section in an amount equal to not less than the amount of the grant. (e) Authorization of appropriations There are authorized to be appropriated to carry out this section $5,000,000 for each of fiscal years 2026 through 2030. .",
      "versionDate": "2025-02-12",
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
        "actionDate": "2026-04-21",
        "text": "Placed on the Union Calendar, Calendar No. 537."
      },
      "number": "7567",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Farm, Food, and National Security Act of 2026",
      "type": "HR"
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
        "updateDate": "2025-03-20T16:26:49Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-12",
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
          "measure-id": "id119hr1230",
          "measure-number": "1230",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-12",
          "originChamber": "HOUSE",
          "update-date": "2025-03-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1230v00",
            "update-date": "2025-03-21"
          },
          "action-date": "2025-02-12",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Agriculture Grants for Veterans Education and Training Services Act or the AG VETS Act</strong></p><p>This bill directs the Department of Agriculture to provide competitive grants to eligible entities for the purpose of establishing and enhancing farming and ranching opportunities for veterans through education and training services.</p><p>Entities eligible for the grants include cooperative extension services, land-grant colleges and universities, non-land-grant colleges of agriculture, state departments of agriculture, and nonprofit organizations.</p>"
        },
        "title": "AG VETS Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1230.xml",
    "summary": {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Agriculture Grants for Veterans Education and Training Services Act or the AG VETS Act</strong></p><p>This bill directs the Department of Agriculture to provide competitive grants to eligible entities for the purpose of establishing and enhancing farming and ranching opportunities for veterans through education and training services.</p><p>Entities eligible for the grants include cooperative extension services, land-grant colleges and universities, non-land-grant colleges of agriculture, state departments of agriculture, and nonprofit organizations.</p>",
      "updateDate": "2025-03-21",
      "versionCode": "id119hr1230"
    },
    "title": "AG VETS Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Agriculture Grants for Veterans Education and Training Services Act or the AG VETS Act</strong></p><p>This bill directs the Department of Agriculture to provide competitive grants to eligible entities for the purpose of establishing and enhancing farming and ranching opportunities for veterans through education and training services.</p><p>Entities eligible for the grants include cooperative extension services, land-grant colleges and universities, non-land-grant colleges of agriculture, state departments of agriculture, and nonprofit organizations.</p>",
      "updateDate": "2025-03-21",
      "versionCode": "id119hr1230"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1230ih.xml"
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
      "title": "AG VETS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T11:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "AG VETS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T11:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Agriculture Grants for Veterans Education and Training Services Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T11:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Agricultural Research, Extension, and Education Reform Act of 1998 to direct the Secretary of Agriculture to establish a program under which the Secretary will award competitive grants to eligible entities for the purpose of establishing and enhancing farming and ranching opportunities for veterans.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T11:18:27Z"
    }
  ]
}
```
