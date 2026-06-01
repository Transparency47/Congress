# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7258?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7258
- Title: Energy Emergency Leadership Act
- Congress: 119
- Bill type: HR
- Bill number: 7258
- Origin chamber: House
- Introduced date: 2026-01-27
- Update date: 2026-05-27T18:41:27Z
- Update date including text: 2026-05-27T18:41:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-27: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-01-27 - Committee: Referred to the Subcommittee on Energy.
- 2026-02-04 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-02-04 - Committee: Subcommittee Consideration and Mark-up Session Held
- 2026-05-11 - Calendars: Placed on the Union Calendar, Calendar No. 562.
- 2026-05-11 - Committee: Reported by the Committee on Energy and Commerce. H. Rept. 119-645.
- 2026-05-11 - Committee: Reported by the Committee on Energy and Commerce. H. Rept. 119-645.
- Latest action: 2026-01-27: Introduced in House

## Actions

- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-01-27 - Committee: Referred to the Subcommittee on Energy.
- 2026-02-04 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-02-04 - Committee: Subcommittee Consideration and Mark-up Session Held
- 2026-05-11 - Calendars: Placed on the Union Calendar, Calendar No. 562.
- 2026-05-11 - Committee: Reported by the Committee on Energy and Commerce. H. Rept. 119-645.
- 2026-05-11 - Committee: Reported by the Committee on Energy and Commerce. H. Rept. 119-645.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-27",
    "latestAction": {
      "actionDate": "2026-01-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7258",
    "number": "7258",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "L000597",
        "district": "15",
        "firstName": "Laurel",
        "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
        "lastName": "Lee",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Energy Emergency Leadership Act",
    "type": "HR",
    "updateDate": "2026-05-27T18:41:27Z",
    "updateDateIncludingText": "2026-05-27T18:41:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2026-05-11",
      "calendarNumber": {
        "calendar": "U00562"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 562.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2026-05-11",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Reported by the Committee on Energy and Commerce. H. Rept. 119-645.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2026-05-11",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Reported by the Committee on Energy and Commerce. H. Rept. 119-645.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-04",
      "committees": {
        "item": {
          "name": "Energy Subcommittee",
          "systemCode": "hsif03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Forwarded by Subcommittee to Full Committee by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-04",
      "committees": {
        "item": {
          "name": "Energy Subcommittee",
          "systemCode": "hsif03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-27",
      "committees": {
        "item": {
          "name": "Energy Subcommittee",
          "systemCode": "hsif03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Energy.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-27",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-27",
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
            "date": "2026-05-11T15:19:37Z",
            "name": "Reported By"
          },
          {
            "date": "2026-01-27T17:31:45Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-02-04T22:36:22Z",
                "name": "Reported by"
              },
              {
                "date": "2026-02-04T22:35:55Z",
                "name": "Markup by"
              },
              {
                "date": "2026-01-27T22:35:28Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Energy Subcommittee",
          "systemCode": "hsif03"
        }
      },
      "systemCode": "hsif00",
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
      "bioguideId": "W000798",
      "district": "5",
      "firstName": "Tim",
      "fullName": "Rep. Walberg, Tim [R-MI-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Walberg",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "MI"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "OH"
    },
    {
      "bioguideId": "B001306",
      "district": "12",
      "firstName": "Troy",
      "fullName": "Rep. Balderson, Troy [R-OH-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Balderson",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "OH"
    },
    {
      "bioguideId": "O000177",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Onder, Robert F. [R-MO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Onder",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2026-04-22",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7258ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7258\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 27, 2026 Ms. Lee of Florida (for herself and Mr. Walberg ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Department of Energy Organization Act with respect to functions assigned to Assistant Secretaries, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Energy Emergency Leadership Act .\n#### 2. Functions assigned to Assistant Secretaries\n##### (a) In general\nSubsection (a) of section 203 of the Department of Energy Organization Act ( 42 U.S.C. 7133(a) ) is amended by adding at the end the following new paragraph:\n(12) Energy emergency and energy security functions, including\u2014 (A) responsibilities with respect to energy infrastructure, security and resilience, emerging threats, cybersecurity, supply, and emergency planning and preparedness, coordination, response, and restoration, as appropriate; and (B) upon request of a State, local, or Tribal government or energy sector entity, and in coordination with other Federal agencies as appropriate, provision of technical assistance and support to protect against, detect, and respond to energy security threats, risks, and incidents. .\n##### (b) Coordination\nThe Secretary of Energy shall ensure that the functions of the Secretary described in section 203(a)(12) of the Department of Energy Organization Act (as added by this Act) are performed in coordination with relevant Federal agencies.",
      "versionDate": "2026-01-27",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7258rh.xml",
      "text": "IB\nUnion Calendar No. 562\n119th CONGRESS\n2d Session\nH. R. 7258\n[Report No. 119\u2013645]\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 27, 2026 Ms. Lee of Florida (for herself and Mr. Walberg ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nMay 11, 2026 Additional sponsors: Mr. Landsman , Mr. Balderson , and Mr. Onder\nMay 11, 2026 Committed to the Committee of the Whole House on the State of the Union and ordered to be printed\nA BILL\nTo amend the Department of Energy Organization Act with respect to functions assigned to Assistant Secretaries, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Energy Emergency Leadership Act .\n#### 2. Functions assigned to Assistant Secretaries\n##### (a) In general\nSubsection (a) of section 203 of the Department of Energy Organization Act ( 42 U.S.C. 7133(a) ) is amended by adding at the end the following new paragraph:\n(12) Energy emergency and energy security functions, including\u2014 (A) responsibilities with respect to energy infrastructure, security and resilience, emerging threats, cybersecurity, supply, and emergency planning and preparedness, coordination, response, and restoration, as appropriate; and (B) upon request of a State, local, or Tribal government or energy sector entity, and in coordination with other Federal agencies as appropriate, provision of technical assistance and support to protect against, detect, and respond to energy security threats, risks, and incidents. .\n##### (b) Coordination\nThe Secretary of Energy shall ensure that the functions of the Secretary described in section 203(a)(12) of the Department of Energy Organization Act (as added by this Act) are performed in coordination with relevant Federal agencies.",
      "versionDate": "2026-05-11",
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
            "name": "Computer security and identity theft",
            "updateDate": "2026-02-18T14:55:50Z"
          },
          {
            "name": "Department of Energy",
            "updateDate": "2026-02-18T14:55:50Z"
          },
          {
            "name": "Emergency planning and evacuation",
            "updateDate": "2026-02-18T14:55:50Z"
          },
          {
            "name": "Energy storage, supplies, demand",
            "updateDate": "2026-02-18T14:55:50Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2026-02-18T14:55:50Z"
          },
          {
            "name": "Federal officials",
            "updateDate": "2026-02-18T14:55:50Z"
          },
          {
            "name": "Federal-Indian relations",
            "updateDate": "2026-02-18T14:55:50Z"
          },
          {
            "name": "Infrastructure development",
            "updateDate": "2026-02-18T14:55:50Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2026-02-18T14:55:50Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2026-02-18T14:55:50Z"
          }
        ]
      },
      "policyArea": {
        "name": "Emergency Management",
        "updateDate": "2026-05-13T16:17:17Z"
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
      "date": "2026-01-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7258ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2026-05-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7258rh.xml"
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
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Energy Emergency Leadership Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2026-05-12T05:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Energy Emergency Leadership Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-29T05:08:17Z"
    },
    {
      "title": "Energy Emergency Leadership Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-29T05:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Department of Energy Organization Act with respect to functions assigned to Assistant Secretaries, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-29T05:03:19Z"
    }
  ]
}
```
