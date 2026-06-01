# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4327?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4327
- Title: No Tax on Home Sales Act
- Congress: 119
- Bill type: HR
- Bill number: 4327
- Origin chamber: House
- Introduced date: 2025-07-10
- Update date: 2026-04-10T08:05:27Z
- Update date including text: 2026-04-10T08:05:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-10: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2026-01-21 16:48:50 - Floor: ASSUMING FIRST SPONSORSHIP - Mr. Alford asked unanimous consent that he may hereafter be considered as the first sponsor of H.R. 4327, a bill originally introduced by Representative Greene (GA), for the purpose of adding cosponsors and requesting reprintings pursuant to clause 7 of rule XII. Agreed to without objection.
- Latest action: 2025-07-10: Introduced in House

## Actions

- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2026-01-21 16:48:50 - Floor: ASSUMING FIRST SPONSORSHIP - Mr. Alford asked unanimous consent that he may hereafter be considered as the first sponsor of H.R. 4327, a bill originally introduced by Representative Greene (GA), for the purpose of adding cosponsors and requesting reprintings pursuant to clause 7 of rule XII. Agreed to without objection.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-10",
    "latestAction": {
      "actionDate": "2025-07-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4327",
    "number": "4327",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "G000596",
        "district": "14",
        "firstName": "Marjorie",
        "fullName": "Rep. Greene, Marjorie Taylor [R-GA-14]",
        "lastName": "Greene",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "No Tax on Home Sales Act",
    "type": "HR",
    "updateDate": "2026-04-10T08:05:27Z",
    "updateDateIncludingText": "2026-04-10T08:05:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H8D000",
      "actionDate": "2026-01-21",
      "actionTime": "16:48:50",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "ASSUMING FIRST SPONSORSHIP - Mr. Alford asked unanimous consent that he may hereafter be considered as the first sponsor of H.R. 4327, a bill originally introduced by Representative Greene (GA), for the purpose of adding cosponsors and requesting reprintings pursuant to clause 7 of rule XII. Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-10",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-10",
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
          "date": "2025-07-10T15:06:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "UT"
    },
    {
      "bioguideId": "T000490",
      "district": "2",
      "firstName": "David",
      "fullName": "Rep. Taylor, David J. [R-OH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Taylor",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "OH"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "AZ"
    },
    {
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "MO"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "NC"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "False",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "CA"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4327ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4327\nIN THE HOUSE OF REPRESENTATIVES\nJuly 10, 2025 Ms. Greene of Georgia introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to eliminate the dollar limitations on the exclusion of gain from sales of principal residences, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Tax on Home Sales Act .\n#### 2. Elimination of dollar limitations on exclusion of gain from sales of principal residences\n##### (a) In general\nSection 121(b) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking paragraphs (1), (2), and (4), and\n**(2)**\nby redesignating paragraphs (3) and (5) as paragraphs (1) and (2), respectively.\n##### (b) Conforming amendments\nSection 121(c) of such Code is amended\u2014\n**(1)**\nin paragraph (1), by striking , and subsection (b)(3) and all that follows through 2 years and inserting , and subsection (b)(1), shall not apply , and\n**(2)**\nin paragraph (2)(A)(ii), by striking subsection (b)(3) and inserting subsection (b)(1) .\n##### (c) Effective date\nThe amendments made by this section shall apply to sales and exchanges after the date of the enactment of this Act.",
      "versionDate": "2025-07-10",
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
        "actionDate": "2026-01-13",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "7034",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To amend the Internal Revenue Code of 1986 to eliminate the dollar limitations on the exclusion of gain from sales of principal residences, and for other purposes.",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-01-16",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "7131",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Middle Class Home Tax Elimination Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Housing finance and home ownership",
            "updateDate": "2026-01-23T16:12:15Z"
          },
          {
            "name": "Income tax exclusion",
            "updateDate": "2026-01-23T16:11:55Z"
          },
          {
            "name": "Sales and excise taxes",
            "updateDate": "2026-01-23T16:12:22Z"
          }
        ]
      },
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-07-29T21:29:49Z"
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
      "date": "2025-07-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4327ih.xml"
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
      "title": "No Tax on Home Sales Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-25T13:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Tax on Home Sales Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-25T13:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to eliminate the dollar limitations on the exclusion of gain from sales of principal residences, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-25T13:48:33Z"
    }
  ]
}
```
