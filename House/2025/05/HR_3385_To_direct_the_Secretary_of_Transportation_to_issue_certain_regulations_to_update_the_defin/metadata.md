# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3385?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3385
- Title: To direct the Secretary of Transportation to issue certain regulations to update the definition of motorcycle, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 3385
- Origin chamber: House
- Introduced date: 2025-05-14
- Update date: 2026-05-20T08:08:16Z
- Update date including text: 2026-05-20T08:08:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-14: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-05-14 - Committee: Referred to the Subcommittee on Commerce, Manufacturing, and Trade.
- 2026-02-10 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-02-10 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2025-05-14: Introduced in House

## Actions

- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-05-14 - Committee: Referred to the Subcommittee on Commerce, Manufacturing, and Trade.
- 2026-02-10 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-02-10 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-14",
    "latestAction": {
      "actionDate": "2025-05-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3385",
    "number": "3385",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
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
    "title": "To direct the Secretary of Transportation to issue certain regulations to update the definition of motorcycle, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:16Z",
    "updateDateIncludingText": "2026-05-20T08:08:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-10",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
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
      "actionDate": "2026-02-10",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
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
      "actionDate": "2025-05-14",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Commerce, Manufacturing, and Trade.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-14",
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
      "actionDate": "2025-05-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-14",
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
          "date": "2025-05-14T14:05:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-02-10T20:58:30Z",
                "name": "Reported by"
              },
              {
                "date": "2026-02-10T20:58:05Z",
                "name": "Markup by"
              },
              {
                "date": "2025-05-14T19:57:35Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
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
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "CA"
    },
    {
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "WI"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "IL"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3385ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3385\nIN THE HOUSE OF REPRESENTATIVES\nMay 14, 2025 Mr. Van Orden introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Secretary of Transportation to issue certain regulations to update the definition of motorcycle, and for other purposes.\n#### 1. Motorcycle definition\n##### (a) In general\nNot later than 120 days after the date of enactment of this Act, the Secretary of Transportation shall issue such regulations as are necessary to amend the definition of the term motorcycle in section 571.3 of title 49, Code of Federal Regulations, to match the definition in this section.\n##### (b) Motor cycle defined\nIn this section, the term motorcycle means a motor vehicle, as was originally manufactured, with motive power, having a seat or saddle requiring the rider to sit astride, designed to travel on not more than three wheels in contact with the ground, steering controlled by handlebars, acceleration and braking controlled by handlebar and foot controls and capable of reaching speeds in excess of 30 mph.",
      "versionDate": "2025-05-14",
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2026-04-13T20:08:09Z"
          },
          {
            "name": "Department of Transportation",
            "updateDate": "2026-04-13T20:08:03Z"
          },
          {
            "name": "Motor vehicles",
            "updateDate": "2026-04-13T20:07:56Z"
          }
        ]
      },
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2025-05-28T12:35:27Z"
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
      "date": "2025-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3385ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Transportation to issue certain regulations to update the definition of motorcycle, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T04:48:34Z"
    },
    {
      "title": "To direct the Secretary of Transportation to issue certain regulations to update the definition of motorcycle, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-15T08:11:58Z"
    }
  ]
}
```
