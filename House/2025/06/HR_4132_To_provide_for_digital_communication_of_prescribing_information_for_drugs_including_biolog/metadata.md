# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4132?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4132
- Title: Prescription Information Modernization Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4132
- Origin chamber: House
- Introduced date: 2025-06-25
- Update date: 2025-12-10T09:05:38Z
- Update date including text: 2025-12-10T09:05:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-25: Introduced in House
- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-06-25: Introduced in House

## Actions

- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-25",
    "latestAction": {
      "actionDate": "2025-06-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4132",
    "number": "4132",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001086",
        "district": "1",
        "firstName": "Diana",
        "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
        "lastName": "Harshbarger",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Prescription Information Modernization Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-10T09:05:38Z",
    "updateDateIncludingText": "2025-12-10T09:05:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-25",
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
      "actionDate": "2025-06-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-25",
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
          "date": "2025-06-25T14:01:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
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
      "bioguideId": "S001207",
      "district": "11",
      "firstName": "Mikie",
      "fullName": "Rep. Sherrill, Mikie [D-NJ-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherrill",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "NJ"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
      "state": "CA"
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
      "sponsorshipDate": "2025-06-25",
      "state": "NC"
    },
    {
      "bioguideId": "C000059",
      "district": "41",
      "firstName": "Ken",
      "fullName": "Rep. Calvert, Ken [R-CA-41]",
      "isOriginalCosponsor": "True",
      "lastName": "Calvert",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
      "state": "CA"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "NC"
    },
    {
      "bioguideId": "L000595",
      "district": "5",
      "firstName": "Julia",
      "fullName": "Rep. Letlow, Julia [R-LA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Letlow",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
      "state": "LA"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "CA"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "IL"
    },
    {
      "bioguideId": "W000809",
      "district": "3",
      "firstName": "Steve",
      "fullName": "Rep. Womack, Steve [R-AR-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Womack",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
      "state": "AR"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "NY"
    },
    {
      "bioguideId": "H001067",
      "district": "9",
      "firstName": "Richard",
      "fullName": "Rep. Hudson, Richard [R-NC-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Hudson",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "NC"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "AZ"
    },
    {
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-09-23",
      "state": "SC"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "CA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
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
      "sponsorshipDate": "2025-12-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4132ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4132\nIN THE HOUSE OF REPRESENTATIVES\nJune 25, 2025 Mrs. Harshbarger (for herself, Ms. Sherrill , Mr. Valadao , Mr. Davis of North Carolina , Mr. Calvert , Ms. Ross , Ms. Letlow , Mr. Peters , Mr. Schneider , Mr. Womack , and Mr. Tonko ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo provide for digital communication of prescribing information for drugs (including biological products), and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Prescription Information Modernization Act of 2025 .\n#### 2. Digital communication of FDA-approved prescribing information for drugs (including biological products)\n##### (a) In general\nSection 502(f) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 352(f) ) is amended by adding at the end the following: Required prescribing information for drugs subject to section 503(b)(1) may be made available solely by electronic means provided that the labeling complies with all applicable requirements of law, that the manufacturer affords prescribers and dispensers the opportunity to elect to also continue to receive all such information in paper form, or to request paper labeling on an as-needed basis, and after such request, and that the manufacturer promptly provides the requested information without additional cost. .\n##### (b) Rulemaking\n**(1) In general**\nNot later than 1 year after the date of the enactment of this Act, the Secretary of Health and Human Services shall issue final regulations to\u2014\n**(A)**\nimplement the amendment made by subsection (a); and\n**(B)**\nprovide instructions on how health care professionals can receive paper copies of prescribing information directly from the manufacturer or distributor if desired.\n**(2) Economic impacts**\nThe Secretary of Health and Human Services shall design the regulations required by paragraph (1) so as to minimize the adverse economic impacts of such regulations on prescribers and dispensers.\n##### (c) Public workshop\nNot later than 2 years after the date of the enactment of this Act, the Secretary of Health and Human Services, acting through the Commissioner of Food and Drugs, shall hold a public workshop with relevant stakeholders to discuss how to continue to optimize the format, accessibility, and usability of prescribing information.\n##### (d) Effective date\nThe amendment made by subsection (a) shall apply with respect to drugs introduced or delivered for introduction into interstate commerce on or after the sooner of\u2014\n**(1)**\nthe date that is 2 years after the date of the enactment of this Act; or\n**(2)**\nthe effective date of the final regulations promulgated to implement such amendment.\n##### (e) Definition\nIn this section, the term drug has the meaning given to such term in section 201 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321 ).",
      "versionDate": "2025-06-25",
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
        "actionDate": "2025-06-11",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "2027",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Prescription Information Modernization Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-07-15T11:13:32Z"
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
      "date": "2025-06-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4132ih.xml"
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
      "title": "Prescription Information Modernization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-04T03:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Prescription Information Modernization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-04T03:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for digital communication of prescribing information for drugs (including biological products), and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-04T03:48:39Z"
    }
  ]
}
```
