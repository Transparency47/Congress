# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4711?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4711
- Title: REMOVE Act
- Congress: 119
- Bill type: HR
- Bill number: 4711
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2025-12-05T22:55:19Z
- Update date including text: 2025-12-05T22:55:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-11-18 - Committee: Committee Consideration and Mark-up Session Held
- 2025-11-20 - Committee: Committee Consideration and Mark-up Session Held
- 2025-11-20 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 14 - 9.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-11-18 - Committee: Committee Consideration and Mark-up Session Held
- 2025-11-20 - Committee: Committee Consideration and Mark-up Session Held
- 2025-11-20 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 14 - 9.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4711",
    "number": "4711",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "N000026",
        "district": "22",
        "firstName": "Troy",
        "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
        "lastName": "Nehls",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "REMOVE Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:55:19Z",
    "updateDateIncludingText": "2025-12-05T22:55:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 14 - 9.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
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
      "actionDate": "2025-11-18",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
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
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
            "date": "2025-11-20T18:23:24Z",
            "name": "Markup By"
          },
          {
            "date": "2025-11-19T20:13:36Z",
            "name": "Markup By"
          },
          {
            "date": "2025-11-18T19:55:59Z",
            "name": "Markup By"
          },
          {
            "date": "2025-07-23T14:03:50Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "AL"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "TX"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4711ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4711\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Mr. Nehls (for himself, Mr. Moore of Alabama , and Mr. Gill of Texas ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to ensure the timely completion of all removal proceedings.\n#### 1. Short title\nThis Act may be cited as the Rapid Expulsion of Migrant Offenders who Violate and Evade Act or the REMOVE Act .\n#### 2. Timely removal of aliens ordered removed\nSection 239(d) of the Immigration and Nationality Act ( 8 U.S.C. 1229(d) ) is amended\u2014\n**(1)**\nby redesignating paragraph (2) as paragraph (3); and\n**(2)**\nby striking paragraph (1) and inserting the following:\n(1) The Attorney General shall commence removal proceedings as promptly as possible after U.S. Immigration and Customs Enforcement files, with the immigration court, a Notice to Appear that has been served on an alien. If such alien was convicted of an offense making the alien deportable under section 237(a), the Attorney General shall commence any removal proceeding with respect to such alien as expeditiously as possible after the date on which such alien was convicted of such offense. (2) Notwithstanding any other provision of law, including section 208(d)(5)(A), the Attorney General shall take all actions, including promulgating relevant regulations, issuing relevant guidance, and any other relevant actions, to ensure all immigration court proceedings with respect to an alien referred to in paragraph (1) are completed not later than 15 days after they are commenced. .",
      "versionDate": "2025-07-23",
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
        "actionDate": "2025-06-05",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "1977",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Rapid Expulsion of Migrant Offenders who Violate and Evade (REMOVE) Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Border security and unlawful immigration",
            "updateDate": "2025-12-03T16:06:42Z"
          },
          {
            "name": "Detention of persons",
            "updateDate": "2025-12-03T16:06:52Z"
          },
          {
            "name": "Immigration status and procedures",
            "updateDate": "2025-12-03T16:06:33Z"
          }
        ]
      },
      "policyArea": {
        "name": "Immigration",
        "updateDate": "2025-09-16T17:30:44Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4711ih.xml"
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
      "title": "REMOVE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-06T04:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "REMOVE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-06T04:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rapid Expulsion of Migrant Offenders who Violate and Evade Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-06T04:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Immigration and Nationality Act to ensure the timely completion of all removal proceedings.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-06T04:48:34Z"
    }
  ]
}
```
