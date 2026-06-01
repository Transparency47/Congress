# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7341?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7341
- Title: GRAD Act
- Congress: 119
- Bill type: HR
- Bill number: 7341
- Origin chamber: House
- Introduced date: 2026-02-04
- Update date: 2026-02-20T19:28:40Z
- Update date including text: 2026-02-20T19:28:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-04: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2026-02-04: Introduced in House

## Actions

- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-04",
    "latestAction": {
      "actionDate": "2026-02-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7341",
    "number": "7341",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "M001227",
        "district": "4",
        "firstName": "Jennifer",
        "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
        "lastName": "McClellan",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "GRAD Act",
    "type": "HR",
    "updateDate": "2026-02-20T19:28:40Z",
    "updateDateIncludingText": "2026-02-20T19:28:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-04",
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
      "actionDate": "2026-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-04",
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
          "date": "2026-02-04T15:01:45Z",
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
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "NC"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "NY"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "PA"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "LA"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "TN"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "LA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "IN"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "GA"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "AL"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "NC"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "IL"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "VA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "DC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7341ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7341\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2026 Ms. McClellan (for herself, Ms. Adams , Ms. Clarke of New York , Ms. Lee of Pennsylvania , Mr. Carter of Louisiana , Mr. Cohen , Mr. Fields , Mr. Carson , Mr. Johnson of Georgia , Ms. Simon , Ms. Sewell , Mrs. Foushee , Mr. Davis of Illinois , and Mr. Vindman ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Higher Education Act of 1965 to include certain part B institutions to be eligible for certain grants, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Growing Reputable Academic Departments Act or the GRAD Act .\n#### 2. Graduate education programs\n##### (a) Historically Black colleges and universities\nSection 723 of the Higher Education Act of 1965 ( 20 U.S.C. 1136a ) is amended\u2014\n**(1)**\nin subsection (b)(1), by adding at the end the following:\n(S) A part B institution (as defined in section 322) that\u2014 (i) offers a qualified masters degree program; and (ii) is not listed under subparagraphs (A) through (R). ; and\n**(2)**\nin subsection (f)(3), in the matter preceding subparagraph (A)\u2014\n**(A)**\nby striking any amount in excess of $9,000,000 and inserting after the application of paragraph (2), any remaining amount ; and\n**(B)**\nby striking (R) and inserting (S) .\n##### (b) Predominantly Black Institutions\nSection 724 of the Higher Education Act of 1965 ( 20 U.S.C. 1136b ) is amended\u2014\n**(1)**\nin subsection (b)(1), by adding at the end the following:\n(F) A Predominantly Black Institution (as defined in section 318) that\u2014 (i) offers a qualified masters degree program; and (ii) is not listed in subparagraphs (A) through (E). ; and\n**(2)**\nin subsection (f)(3), in the matter preceding subparagraph (A)\u2014\n**(A)**\nby striking any amount in excess of $2,500,000 and inserting after the application of paragraph (2), any remaining amount ; and\n**(B)**\nby striking through (E) and inserting through (F) .",
      "versionDate": "2026-02-04",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Education",
        "updateDate": "2026-02-20T19:28:40Z"
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
      "date": "2026-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7341ih.xml"
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
      "title": "GRAD Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-19T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "GRAD Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T03:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Growing Reputable Academic Departments Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T03:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Higher Education Act of 1965 to include certain part B institutions to be eligible for certain grants, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T03:48:21Z"
    }
  ]
}
```
