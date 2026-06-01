# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/585?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/585
- Title: Supporting Veteran Families in Need Act
- Congress: 119
- Bill type: HR
- Bill number: 585
- Origin chamber: House
- Introduced date: 2025-01-21
- Update date: 2026-04-22T08:06:48Z
- Update date including text: 2026-04-22T08:06:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-21: Introduced in House
- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-02-25 - Committee: Referred to the Subcommittee on Economic Opportunity.
- Latest action: 2025-01-21: Introduced in House

## Actions

- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-02-25 - Committee: Referred to the Subcommittee on Economic Opportunity.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-21",
    "latestAction": {
      "actionDate": "2025-01-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/585",
    "number": "585",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "L000598",
        "district": "1",
        "firstName": "Nick",
        "fullName": "Rep. LaLota, Nick [R-NY-1]",
        "lastName": "LaLota",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Supporting Veteran Families in Need Act",
    "type": "HR",
    "updateDate": "2026-04-22T08:06:48Z",
    "updateDateIncludingText": "2026-04-22T08:06:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-25",
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
      "actionCode": "H11100",
      "actionDate": "2025-01-21",
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
      "actionDate": "2025-01-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-21",
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
          "date": "2025-01-21T17:03:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-25T22:39:16Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
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
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
      "state": "HI"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
      "state": "NV"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "NY"
    },
    {
      "bioguideId": "R000579",
      "district": "18",
      "firstName": "Patrick",
      "fullName": "Rep. Ryan, Patrick [D-NY-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Ryan",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
      "state": "NY"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
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
      "sponsorshipDate": "2025-01-22",
      "state": "CO"
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
      "sponsorshipDate": "2025-05-07",
      "state": "VA"
    },
    {
      "bioguideId": "L000560",
      "district": "2",
      "firstName": "Rick",
      "fullName": "Rep. Larsen, Rick [D-WA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Larsen",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "WA"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "NY"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr585ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 585\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 21, 2025 Mr. LaLota (for himself, Mr. Case , Ms. Lee of Nevada , Ms. Malliotakis , Mr. Ryan , and Mr. Davis of North Carolina ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to make permanent the authority of the Secretary of Veterans Affairs to provide financial assistance for supportive services for very low-income veteran families in permanent housing.\n#### 1. Short title\nThis Act may be cited as the Supporting Veteran Families in Need Act .\n#### 2. Permanent authority to provide financial assistance for supportive services for very low-income veteran families in permanent housing\nSection 2044(e) of title 38, United States Code, is amended\u2014\n**(1)**\nby redesignating subparagraphs (A) through (H) as paragraphs (1) through (8), respectively; and\n**(2)**\nby adding at the end the following new paragraph:\n(9) The amounts that are appropriated to carry out such subsections for fiscal year 2027 and each fiscal year thereafter. .",
      "versionDate": "2025-01-21",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Family services",
            "updateDate": "2025-03-13T15:41:39Z"
          },
          {
            "name": "Low- and moderate-income housing",
            "updateDate": "2025-03-13T15:41:39Z"
          },
          {
            "name": "Veterans' education, employment, rehabilitation",
            "updateDate": "2025-03-13T15:41:39Z"
          },
          {
            "name": "Veterans' loans, housing, homeless programs",
            "updateDate": "2025-03-13T15:41:39Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-03-13T15:41:39Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-02-25T14:42:52Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-21",
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
          "measure-id": "id119hr585",
          "measure-number": "585",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-21",
          "originChamber": "HOUSE",
          "update-date": "2025-03-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr585v00",
            "update-date": "2025-03-01"
          },
          "action-date": "2025-01-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Supporting Veteran Families in Need Act</b></p> <p>This bill permanently extends authorization for the Supportive Services for Veteran Families program of the Department of Veterans Affairs, which provides supportive services to very low-income veterans (and their families) occupying or transitioning to permanent housing.</p>"
        },
        "title": "Supporting Veteran Families in Need Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr585.xml",
    "summary": {
      "actionDate": "2025-01-21",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Supporting Veteran Families in Need Act</b></p> <p>This bill permanently extends authorization for the Supportive Services for Veteran Families program of the Department of Veterans Affairs, which provides supportive services to very low-income veterans (and their families) occupying or transitioning to permanent housing.</p>",
      "updateDate": "2025-03-01",
      "versionCode": "id119hr585"
    },
    "title": "Supporting Veteran Families in Need Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-21",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Supporting Veteran Families in Need Act</b></p> <p>This bill permanently extends authorization for the Supportive Services for Veteran Families program of the Department of Veterans Affairs, which provides supportive services to very low-income veterans (and their families) occupying or transitioning to permanent housing.</p>",
      "updateDate": "2025-03-01",
      "versionCode": "id119hr585"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr585ih.xml"
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
      "title": "Supporting Veteran Families in Need Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-21T03:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Supporting Veteran Families in Need Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T03:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to make permanent the authority of the Secretary of Veterans Affairs to provide financial assistance for supportive services for very low-income veteran families in permanent housing.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T03:18:24Z"
    }
  ]
}
```
