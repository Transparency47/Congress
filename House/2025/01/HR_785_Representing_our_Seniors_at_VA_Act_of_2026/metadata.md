# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/785?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/785
- Title: Representing our Seniors at VA Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 785
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2026-04-08T18:41:20Z
- Update date including text: 2026-04-08T18:41:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-04 - Committee: Referred to the Subcommittee on Health.
- 2025-06-12 - Committee: Subcommittee Hearings Held
- 2026-02-05 - Committee: Subcommittee on Health Discharged
- 2026-02-12 - Committee: Committee Consideration and Mark-up Session Held
- 2026-02-12 - Committee: Ordered to be Reported in the Nature of a Substitute (Amended) by Voice Vote.
- 2026-04-02 - Calendars: Placed on the Union Calendar, Calendar No. 498.
- 2026-04-02 - Committee: Reported (Amended) by the Committee on Veterans' Affairs. H. Rept. 119-578.
- 2026-04-02 - Committee: Reported (Amended) by the Committee on Veterans' Affairs. H. Rept. 119-578.
- Latest action: 2025-01-28: Introduced in House

## Actions

- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-04 - Committee: Referred to the Subcommittee on Health.
- 2025-06-12 - Committee: Subcommittee Hearings Held
- 2026-02-05 - Committee: Subcommittee on Health Discharged
- 2026-02-12 - Committee: Committee Consideration and Mark-up Session Held
- 2026-02-12 - Committee: Ordered to be Reported in the Nature of a Substitute (Amended) by Voice Vote.
- 2026-04-02 - Calendars: Placed on the Union Calendar, Calendar No. 498.
- 2026-04-02 - Committee: Reported (Amended) by the Committee on Veterans' Affairs. H. Rept. 119-578.
- 2026-04-02 - Committee: Reported (Amended) by the Committee on Veterans' Affairs. H. Rept. 119-578.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/785",
    "number": "785",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "K000399",
        "district": "2",
        "firstName": "Jennifer",
        "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
        "lastName": "Kiggans",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Representing our Seniors at VA Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-08T18:41:20Z",
    "updateDateIncludingText": "2026-04-08T18:41:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2026-04-02",
      "calendarNumber": {
        "calendar": "U00498"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 498.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2026-04-02",
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
      "text": "Reported (Amended) by the Committee on Veterans' Affairs. H. Rept. 119-578.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2026-04-02",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Reported (Amended) by the Committee on Veterans' Affairs. H. Rept. 119-578.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-12",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported in the Nature of a Substitute (Amended) by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-12",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-05",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee on Health Discharged",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-12",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-04",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-28",
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
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-28",
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
        "item": [
          {
            "date": "2026-04-02T13:25:39Z",
            "name": "Reported By"
          },
          {
            "date": "2026-02-12T19:01:55Z",
            "name": "Markup By"
          },
          {
            "date": "2026-02-05T18:57:24Z",
            "name": "Discharged from"
          },
          {
            "date": "2025-01-28T16:04:50Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-06-12T18:06:57Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-03-04T22:41:35Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "FL"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "SC"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "NY"
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
      "sponsorshipDate": "2025-02-21",
      "state": "NC"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "NY"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "NY"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "ID"
    },
    {
      "bioguideId": "T000490",
      "district": "2",
      "firstName": "David",
      "fullName": "Rep. Taylor, David [R-OH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Taylor",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "OH"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "NY"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "NY"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "MI"
    },
    {
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "MI"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "WA"
    },
    {
      "bioguideId": "K000009",
      "district": "9",
      "firstName": "Marcy",
      "fullName": "Rep. Kaptur, Marcy [D-OH-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaptur",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "OH"
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
      "sponsorshipDate": "2025-07-15",
      "state": "VA"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "NV"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "UT"
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
      "sponsorshipDate": "2026-02-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr785ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 785\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Mrs. Kiggans of Virginia (for herself, Mrs. Cherfilus-McCormick , and Mrs. Biggs of South Carolina ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to include a representative of the National Association of State Veterans Homes on the Geriatrics and Gerontology Advisory Committee of the Department of Veterans Affairs.\n#### 1. Short title\nThis Act may be cited as the Representing our Seniors at VA Act of 2025 .\n#### 2. Inclusion of representative of National Association of State Veterans Homes on Department of Veterans Affairs Geriatrics and Gerontology Advisory Committee\nSection 7315(a) of title 38, United States Code, is amended\u2014\n**(1)**\nby inserting , in consultation with the President of the National Association of State Veterans Homes with respect to matters concerning such association after Under Secretary for Health ; and\n**(2)**\nby inserting and one representative of the National Association of State Veterans Homes who holds a professional license in nursing home administration before the period at the end of the second sentence.",
      "versionDate": "2025-01-28",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr785rh.xml",
      "text": "IB\nUnion Calendar No. 498\n119th CONGRESS\n2d Session\nH. R. 785\n[Report No. 119\u2013578]\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Mrs. Kiggans of Virginia (for herself, Mrs. Cherfilus-McCormick , and Mrs. Biggs of South Carolina ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nApril 2, 2026 Additional sponsors: Mr. Suozzi , Mr. Davis of North Carolina , Ms. Gillen , Mr. LaLota , Mr. Fulcher , Mr. Taylor , Mr. Garbarino , Ms. Meng , Ms. Tlaib , Mr. Barrett , Ms. Strickland , Ms. Kaptur , Mr. Vindman , Ms. Lee of Nevada , Mr. Owens , and Mr. Goldman of New York\nApril 2, 2026 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as introduced on January 28, 2025\nA BILL\nTo amend title 38, United States Code, to include a representative of the National Association of State Veterans Homes on the Geriatrics and Gerontology Advisory Committee of the Department of Veterans Affairs.\n#### 1. Short title\nThis Act may be cited as the Representing our Seniors at VA Act of 2026 .\n#### 2. Membership of Department of Veterans Affairs Geriatrics and Gerontology Advisory Committee\nSection 7315 of title 38, United States Code, is amended, in subsection (a)\u2014\n**(1)**\nin the second sentence, by striking and at least one representative of a national veterans service organization and inserting , at least one individual who represents a national veterans service organization, at least one individual who has served veterans or families of veterans in a State home, and at least one individual who holds a professional license in nursing home administration ; and\n**(2)**\nby designating the first, second, and third sentences as paragraphs (1) through (3), respectively (and adjusting the margins accordingly).",
      "versionDate": "2026-04-02",
      "versionType": "Reported in House"
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
            "name": "Advisory bodies",
            "updateDate": "2025-03-27T15:45:08Z"
          },
          {
            "name": "Aging",
            "updateDate": "2025-03-27T15:45:32Z"
          },
          {
            "name": "Department of Veterans Affairs",
            "updateDate": "2025-03-27T15:45:18Z"
          },
          {
            "name": "Long-term, rehabilitative, and terminal care",
            "updateDate": "2025-03-27T15:45:36Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-02-26T21:13:08Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-28",
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
          "measure-id": "id119hr785",
          "measure-number": "785",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-28",
          "originChamber": "HOUSE",
          "update-date": "2025-04-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr785v00",
            "update-date": "2025-04-25"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Representing our Seniors at VA Act of 2025</strong></p><p>This bill expands the membership of the Geriatrics and Gerontology Advisory Committee within the Veterans Health Administration by requiring the addition of one representative from the National Association of State Veterans Homes who holds a professional license in nursing home administration. Additionally, the committee must consult with the National Association of Veterans State Homes with respect to matters concerning the association.</p>"
        },
        "title": "Representing our Seniors at VA Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr785.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Representing our Seniors at VA Act of 2025</strong></p><p>This bill expands the membership of the Geriatrics and Gerontology Advisory Committee within the Veterans Health Administration by requiring the addition of one representative from the National Association of State Veterans Homes who holds a professional license in nursing home administration. Additionally, the committee must consult with the National Association of Veterans State Homes with respect to matters concerning the association.</p>",
      "updateDate": "2025-04-25",
      "versionCode": "id119hr785"
    },
    "title": "Representing our Seniors at VA Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Representing our Seniors at VA Act of 2025</strong></p><p>This bill expands the membership of the Geriatrics and Gerontology Advisory Committee within the Veterans Health Administration by requiring the addition of one representative from the National Association of State Veterans Homes who holds a professional license in nursing home administration. Additionally, the committee must consult with the National Association of Veterans State Homes with respect to matters concerning the association.</p>",
      "updateDate": "2025-04-25",
      "versionCode": "id119hr785"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr785ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2026-04-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr785rh.xml"
        }
      ],
      "type": "Reported in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Representing our Seniors at VA Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-03T05:38:28Z"
    },
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Representing our Seniors at VA Act of 2026",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2026-04-03T05:38:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Representing our Seniors at VA Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T06:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to include a representative of the National Association of State Veterans Homes on the Geriatrics and Gerontology Advisory Committee of the Department of Veterans Affairs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T06:49:22Z"
    }
  ]
}
```
