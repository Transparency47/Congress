# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1193?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1193
- Title: Future in Logging Careers Act
- Congress: 119
- Bill type: HR
- Bill number: 1193
- Origin chamber: House
- Introduced date: 2025-02-11
- Update date: 2025-07-21T19:44:15Z
- Update date including text: 2025-07-21T19:44:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-11: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-02-11: Introduced in House

## Actions

- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-11",
    "latestAction": {
      "actionDate": "2025-02-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1193",
    "number": "1193",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "G000592",
        "district": "2",
        "firstName": "Jared",
        "fullName": "Rep. Golden, Jared F. [D-ME-2]",
        "lastName": "Golden",
        "party": "D",
        "state": "ME"
      }
    ],
    "title": "Future in Logging Careers Act",
    "type": "HR",
    "updateDate": "2025-07-21T19:44:15Z",
    "updateDateIncludingText": "2025-07-21T19:44:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-11",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-11",
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
          "date": "2025-02-11T15:01:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "PA"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "ME"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "ID"
    },
    {
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "WA"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1193ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1193\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 11, 2025 Mr. Golden of Maine (for himself, Mr. Thompson of Pennsylvania , Ms. Pingree , and Mr. Fulcher ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Fair Labor Standards Act of 1938 to exempt certain 16- and 17-year-old individuals employed in timber harvesting entities or mechanized timber harvesting entities from child labor laws, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Future in Logging Careers Act .\n#### 2. Child labor law exemptions for timber harvesting entities and mechanized timber harvesting entities\nThe Fair Labor Standards Act of 1938 ( 29 U.S.C. 201 et seq. ) is amended\u2014\n**(1)**\nin section 3 ( 29 U.S.C. 203 ), by adding at the end the following:\n(z) (1) Timber harvesting employer means an employer engaged in\u2014 (A) the felling, skidding, yarding, loading and processing of timber by equipment other than manually operated chainsaws and cable skidders; (B) the felling of timber in mechanized operations; (C) the bucking or converting of timber into logs, poles, ties, bolts, pulpwood, chemical wood, excelsior wood, cordwood, fence posts, or similar products; (D) the collecting, skidding, yarding, loading, transporting and unloading of such products in connection with logging; (E) the constructing, repairing and maintaining of roads or camps used in connection with logging; the constructing, repairing, and maintenance of machinery or equipment used in logging; and (F) other work performed in connection with logging. (2) Mechanized timber harvesting employer \u2014 (A) means an employer engaged in the felling, skidding, yarding, loading and processing of timber by equipment other than manually operated chain\u00adsaws and cable skidders; and (B) includes an employer engaged in the use of whole tree processors, cut-to-length processors, stroke boom delimbers, wheeled and track feller-bunchers, pull thru delimbers, wheeled and track forwarders, chippers, grinders, mechanical de\u00adbark\u00aders, wheeled and track grapple skidders, yarders, bulldozers, excavators, and log loaders. ; and\n**(2)**\nin section 13(c) ( 29 U.S.C. 213(c) ), by adding at the end the following:\n(8) The provisions of section 12 relating to child labor shall apply to an employee who is 16 or 17 years old employed by a timber harvesting employer or mechanized timber harvesting employer in an occupation that the Secretary of Labor finds and declares to be particularly hazardous for the employment of children ages 16 or 17, except where such employee is employed by a timber harvesting employer or mechanized timber harvesting employer owned or operated by a parent or a person standing in the place of a parent of such employee. .",
      "versionDate": "2025-02-11",
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
            "name": "Child safety and welfare",
            "updateDate": "2025-04-23T17:36:31Z"
          },
          {
            "name": "Family relationships",
            "updateDate": "2025-04-23T17:36:31Z"
          },
          {
            "name": "Forests, forestry, trees",
            "updateDate": "2025-04-23T17:36:31Z"
          },
          {
            "name": "Labor standards",
            "updateDate": "2025-04-23T17:36:31Z"
          },
          {
            "name": "Worker safety and health",
            "updateDate": "2025-04-23T17:36:31Z"
          },
          {
            "name": "Youth employment and child labor",
            "updateDate": "2025-04-23T17:36:31Z"
          }
        ]
      },
      "policyArea": {
        "name": "Labor and Employment",
        "updateDate": "2025-03-17T14:24:00Z"
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
      "date": "2025-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1193ih.xml"
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
      "title": "Future in Logging Careers Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T05:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Future in Logging Careers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T05:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Fair Labor Standards Act of 1938 to exempt certain 16- and 17-year-old individuals employed in timber harvesting entities or mechanized timber harvesting entities from child labor laws, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T05:18:38Z"
    }
  ]
}
```
