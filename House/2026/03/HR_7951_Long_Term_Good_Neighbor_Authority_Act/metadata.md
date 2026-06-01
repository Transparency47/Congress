# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7951?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7951
- Title: Long-Term Good Neighbor Authority Act
- Congress: 119
- Bill type: HR
- Bill number: 7951
- Origin chamber: House
- Introduced date: 2026-03-16
- Update date: 2026-04-22T20:33:34Z
- Update date including text: 2026-04-22T20:33:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-16: Introduced in House
- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-16 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-19 - Committee: Referred to the Subcommittee on Federal Lands.
- 2026-03-26 - Committee: Subcommittee Hearings Held
- Latest action: 2026-03-16: Introduced in House

## Actions

- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-16 - IntroReferral: Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-19 - Committee: Referred to the Subcommittee on Federal Lands.
- 2026-03-26 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-16",
    "latestAction": {
      "actionDate": "2026-03-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7951",
    "number": "7951",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "V000129",
        "district": "22",
        "firstName": "David",
        "fullName": "Rep. Valadao, David G. [R-CA-22]",
        "lastName": "Valadao",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Long-Term Good Neighbor Authority Act",
    "type": "HR",
    "updateDate": "2026-04-22T20:33:34Z",
    "updateDateIncludingText": "2026-04-22T20:33:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
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
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Federal Lands.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-16",
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
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-16",
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
      "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-16",
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
          "date": "2026-03-16T16:01:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-03-26T19:33:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-03-20T02:00:00Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Federal Lands Subcommittee",
          "systemCode": "hsii10"
        }
      },
      "systemCode": "hsii00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-03-16T16:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
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
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2026-03-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7951ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7951\nIN THE HOUSE OF REPRESENTATIVES\nMarch 16, 2026 Mr. Valadao (for himself and Mr. Panetta ) introduced the following bill; which was referred to the Committee on Natural Resources , and in addition to the Committee on Agriculture , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Agricultural Act of 2014 and the EXPLORE Act to provide for long-term Good Neighbor Authority, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Long-Term Good Neighbor Authority Act .\n#### 2. Good Neighbor Authority\n##### (a) Agricultural Act of 2014\n**(1) Definitions**\nSection 8206(a) of the Agricultural Act of 2014 ( 16 U.S.C. 2113a(a) ) is amended\u2014\n**(A)**\nin paragraph (1)(B), by striking Governor and inserting Governor, Indian tribe, ;\n**(B)**\nin paragraph (5), by striking Governor and inserting Governor, Indian tribe, ; and\n**(C)**\nin paragraph (6), by striking or Indian tribe .\n**(2) GNA**\nSection 8206(b) of the Agricultural Act of 2014 ( 16 U.S.C. 2113a(b)(1) ) is amended\u2014\n**(A)**\nin paragraph (1), by amending subparagraph (A) to read as follows:\n(A) In general The Secretary may enter into a good neighbor agreement with a Governor, Indian tribe, or county\u2014 (i) to carry out authorized restoration services in accordance with this section; and (ii) for a term not to exceed 20 years. ; and\n**(B)**\nin paragraph (3), by striking Governor and inserting Governor, Indian tribe, .\n**(3) Technical amendment**\nSection 8206(b)(2)(C)(i) of the Agricultural Act of 2014 ( 16 U.S.C. 2113a(b)(2)(C)(i) ) is amended\u2014\n**(A)**\nin subclause (I), by striking on ; and\n**(B)**\nin subclause (II)\u2014\n**(i)**\nby striking clause (i) and inserting subclause (I) ; and\n**(ii)**\nin item (bb), by striking the Good Neighbor Authority for Recreation Act and inserting section 351 of the EXPLORE Act ( 16 U.S.C. 8571 ) .\n##### (b) EXPLORE Act\nSection 351(b)(1) of the EXPLORE Act ( 16 U.S.C. 8571(b)(1) ) is amended\u2014\n**(1)**\nby striking county and inserting county\u2014 ; and\n**(2)**\nby striking to carry out authorized recreation services in accordance with this title. and inserting the following:\n(A) to carry out authorized recreation services in accordance with this title; and (B) for a term not to exceed 20 years. .",
      "versionDate": "2026-03-16",
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
            "name": "Fires",
            "updateDate": "2026-04-22T20:33:04Z"
          },
          {
            "name": "Forests, forestry, trees",
            "updateDate": "2026-04-22T20:33:11Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2026-04-22T20:33:20Z"
          },
          {
            "name": "Outdoor recreation",
            "updateDate": "2026-04-22T20:33:27Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2026-04-22T20:33:34Z"
          }
        ]
      },
      "policyArea": {
        "name": "Agriculture and Food",
        "updateDate": "2026-04-03T14:51:00Z"
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
      "date": "2026-03-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7951ih.xml"
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
      "title": "Long-Term Good Neighbor Authority Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-02T05:38:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Long-Term Good Neighbor Authority Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-02T05:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Agricultural Act of 2014 and the EXPLORE Act to provide for long-term Good Neighbor Authority, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-02T05:33:35Z"
    }
  ]
}
```
