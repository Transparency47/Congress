# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7889?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7889
- Title: AWRC Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 7889
- Origin chamber: House
- Introduced date: 2026-03-09
- Update date: 2026-04-20T14:34:28Z
- Update date including text: 2026-04-20T14:34:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-09: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-03-19 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2026-03-26 - Committee: Subcommittee Hearings Held
- Latest action: 2026-03-09: Introduced in House

## Actions

- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-03-19 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2026-03-26 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-09",
    "latestAction": {
      "actionDate": "2026-03-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7889",
    "number": "7889",
    "originChamber": "House",
    "policyArea": {
      "name": "Water Resources Development"
    },
    "sponsors": [
      {
        "bioguideId": "W000804",
        "district": "1",
        "firstName": "Robert",
        "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
        "lastName": "Wittman",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "AWRC Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-20T14:34:28Z",
    "updateDateIncludingText": "2026-04-20T14:34:28Z"
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
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
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
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Water, Wildlife and Fisheries.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-09",
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
      "actionDate": "2026-03-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-09",
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
          "date": "2026-03-09T17:02:50Z",
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
                "date": "2026-03-26T14:00:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-03-19T14:00:00Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
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
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
      "state": "CA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "NY"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John J. [R-VA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "VA"
    },
    {
      "bioguideId": "G000568",
      "district": "9",
      "firstName": "H.",
      "fullName": "Rep. Griffith, H. Morgan [R-VA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Griffith",
      "middleName": "Morgan",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "VA"
    },
    {
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "CO"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "NC"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "ME"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "IN"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-04-06",
      "state": "VA"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7889ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7889\nIN THE HOUSE OF REPRESENTATIVES\nMarch 9, 2026 Mr. Wittman (for himself, Ms. Brownley , Mr. Lawler , Mr. McGuire , Mr. Griffith , Mr. Hurd of Colorado , and Mr. McDowell ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Water Resources Research Act of 1984 to reauthorize the water resources research and technology institutes program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Advancing Water Research and Collaboration Act of 2025 or the AWRC Act of 2025 .\n#### 2. Congressional declaration of purpose\nSection 103(4) of the Water Resources Research Act of 1984 ( 42 U.S.C. 10302(4) ) is amended by inserting , including the growing artificial intelligence industry, after private industry .\n#### 3. Water resources research and technology institutes\nSection 104 of the Water Resources Research Act of 1984 ( 42 U.S.C. 10303 ) is amended\u2014\n**(1)**\nin subsection (f)\u2014\n**(A)**\nin paragraph (2), by striking subsection 104(g) of this Act and inserting subsection (g) ; and\n**(B)**\nby striking the subsection designation and all that follows through Any sums in paragraph (2) and inserting the following:\n(f) General authorization of appropriations (1) In general Except as provided in paragraph (2) and subject to subsection (g)(1), there is authorized to be appropriated to carry out this section $16,000,000 for each of fiscal years 2026 through 2029. (2) Failure to obligate Any amounts ; and\n**(2)**\nin subsection (g)\u2014\n**(A)**\nin paragraph (2), by striking (2) Research funds and inserting the following:\n(4) Competitive grants Research funds ;\n**(B)**\nin paragraph (1)\u2014\n**(i)**\nin the third sentence, by striking Funds made and inserting the following:\n(3) Availability of funds Funds made ; and\n**(ii)**\nby striking by institutes which focuses in the first sentence and all that follows through Such funds when appropriated in the second sentence and inserting the following:\nby institutes with respect to any of the following: (A) Research that focuses on water problems and issues of a regional or interstate nature beyond those of concern only to a single State. (B) Research that relates to specific program priorities identified jointly by the Secretary and the institutes. (C) Research that relates to water problems identified by Congress as being of an interstate nature. (2) Federal cost-share Funds made available under this subsection ; and\n**(C)**\nby striking the subsection designation and all that follows through 2025 in the first sentence of paragraph (1) and inserting the following:\n(g) Additional funds for research focused on water problems of interstate nature (1) In general Of the amounts made available under subsection (f)(1) for each of fiscal years 2026 through 2029, 20 percent shall be used .",
      "versionDate": "2026-03-09",
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
        "actionDate": "2025-10-16",
        "text": "Read twice and referred to the Committee on Environment and Public Works."
      },
      "number": "3015",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "AWRC Act of 2025",
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
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2026-04-20T14:34:28Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2026-04-20T14:34:18Z"
          },
          {
            "name": "Research administration and funding",
            "updateDate": "2026-04-20T14:34:23Z"
          },
          {
            "name": "Water resources funding",
            "updateDate": "2026-04-20T14:34:11Z"
          }
        ]
      },
      "policyArea": {
        "name": "Water Resources Development",
        "updateDate": "2026-04-13T21:30:06Z"
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
      "date": "2026-03-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7889ih.xml"
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
      "title": "AWRC Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-08T12:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "AWRC Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-08T12:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Advancing Water Research and Collaboration Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-08T12:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Water Resources Research Act of 1984 to reauthorize the water resources research and technology institutes program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-08T12:18:31Z"
    }
  ]
}
```
