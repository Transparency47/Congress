# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7163?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7163
- Title: PUBLIC SAFETY Act
- Congress: 119
- Bill type: HR
- Bill number: 7163
- Origin chamber: House
- Introduced date: 2026-01-20
- Update date: 2026-04-07T08:05:26Z
- Update date including text: 2026-04-07T08:05:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-20: Introduced in House
- 2026-01-20 - IntroReferral: Introduced in House
- 2026-01-20 - IntroReferral: Introduced in House
- 2026-01-20 - IntroReferral: Referred to the Committee on Appropriations, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-20 - IntroReferral: Referred to the Committee on Appropriations, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-01-20: Introduced in House

## Actions

- 2026-01-20 - IntroReferral: Introduced in House
- 2026-01-20 - IntroReferral: Introduced in House
- 2026-01-20 - IntroReferral: Referred to the Committee on Appropriations, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-20 - IntroReferral: Referred to the Committee on Appropriations, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-20",
    "latestAction": {
      "actionDate": "2026-01-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7163",
    "number": "7163",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "P000614",
        "district": "1",
        "firstName": "Chris",
        "fullName": "Rep. Pappas, Chris [D-NH-1]",
        "lastName": "Pappas",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "PUBLIC SAFETY Act",
    "type": "HR",
    "updateDate": "2026-04-07T08:05:26Z",
    "updateDateIncludingText": "2026-04-07T08:05:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-20",
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
      "text": "Referred to the Committee on Appropriations, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-20",
      "committees": {
        "item": {
          "name": "Appropriations Committee",
          "systemCode": "hsap00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Appropriations, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-20",
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
          "date": "2026-01-20T17:02:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-01-20T17:02:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Appropriations Committee",
      "systemCode": "hsap00",
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
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2026-01-20",
      "state": "AZ"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2026-01-20",
      "state": "NV"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "NH"
    },
    {
      "bioguideId": "I000058",
      "district": "4",
      "firstName": "Glenn",
      "fullName": "Rep. Ivey, Glenn [D-MD-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Ivey",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "MD"
    },
    {
      "bioguideId": "S001215",
      "district": "11",
      "firstName": "Haley",
      "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Stevens",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "MI"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "NV"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "NY"
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
      "sponsorshipDate": "2026-02-03",
      "state": "CA"
    },
    {
      "bioguideId": "L000607",
      "district": "16",
      "firstName": "Sam",
      "fullName": "Rep. Liccardo, Sam T. [D-CA-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Liccardo",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "C001123",
      "district": "31",
      "firstName": "Gilbert",
      "fullName": "Rep. Cisneros, Gilbert Ray [D-CA-31]",
      "isOriginalCosponsor": "False",
      "lastName": "Cisneros",
      "middleName": "Ray",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "NY"
    },
    {
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "MD"
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
      "sponsorshipDate": "2026-02-11",
      "state": "VA"
    },
    {
      "bioguideId": "M001231",
      "district": "22",
      "firstName": "John",
      "fullName": "Rep. Mannion, John W. [D-NY-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Mannion",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "NY"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "P000034",
      "district": "6",
      "firstName": "Frank",
      "fullName": "Rep. Pallone, Frank [D-NJ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Pallone",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7163ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7163\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 20, 2026 Mr. Pappas (for himself, Mr. Stanton , and Ms. Lee of Nevada ) introduced the following bill; which was referred to the Committee on Appropriations , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo allocate funds for the local law enforcement grant programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Providing Useful Budgets for Localities to Invest in Cops by Substituting Appropriations from Federal Enforcement To Yield Results Act or the PUBLIC SAFETY Act .\n#### 2. Funding for COPS Hiring Program\n##### (a) In general\nSection 100052 of the Act titled An Act to provide for reconciliation pursuant to title II of H. Con. Res. 14 ( Public Law 119\u201321 ) is amended\u2014\n**(1)**\nin the section heading, by striking U.S. Immigration and Customs Enforcement and inserting COPS Hiring Program ;\n**(2)**\nby striking In addition to and inserting (a) In general .\u2014In addition to ; and\n**(3)**\nin subsection (a), as so designated\u2014\n**(A)**\nby striking Secretary of Homeland Security for U.S. Immigration and Customs Enforcement and inserting Attorney General ; and\n**(B)**\nby striking September 30, 2029 and all that follows through removal proceedings and inserting the following: \u201cSeptember 30, 2030, for grants made pursuant to paragraphs (1) and (2) of section 1701(b) of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10381(b) ).\n(b) Waiver For grants made from funds made available under this section, the requirements of section 1701(g) of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10381(g) ) shall be waived for the following jurisdictions: (1) A county, municipality, town, township, village, parish, borough, or other unit of general government below the State level that employs fewer than 175 law enforcement officers. (2) A Tribal government that employs fewer than 175 law enforcement officers. .\n#### 3. Funding for Byrne JAG Program\nSection 90003 of the Act titled An Act to provide for reconciliation pursuant to title II of H. Con. Res. 14 ( Public Law 119\u201321 ) is amended to read as follows:\n90003. Edward Byrne Memorial Justice Assistance Grant Program In addition to any amounts otherwise appropriated, there is appropriated to the Attorney General for the Department of Justice for fiscal year 2025, out of any money in the Treasury not otherwise appropriated, to remain available until September 30, 2029, $45,000,000,000, for the Edward Byrne Memorial Justice Assistance Grant Program. .",
      "versionDate": "2026-01-20",
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
        "actionDate": "2026-01-14",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "3631",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "PUBLIC SAFETY Act",
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
        "name": "Economics and Public Finance",
        "updateDate": "2026-02-18T19:44:56Z"
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
      "date": "2026-01-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7163ih.xml"
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
      "title": "PUBLIC SAFETY Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-10T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PUBLIC SAFETY Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-10T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Providing Useful Budgets for Localities to Invest in Cops by Substituting Appropriations from Federal Enforcement To Yield Results Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-10T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To allocate funds for the local law enforcement grant programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-10T04:48:23Z"
    }
  ]
}
```
