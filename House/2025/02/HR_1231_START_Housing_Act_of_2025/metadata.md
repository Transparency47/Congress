# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1231?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1231
- Title: START Housing Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1231
- Origin chamber: House
- Introduced date: 2025-02-12
- Update date: 2025-12-18T09:07:25Z
- Update date including text: 2025-12-18T09:07:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-12: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-02-12: Introduced in House

## Actions

- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-12",
    "latestAction": {
      "actionDate": "2025-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1231",
    "number": "1231",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "B001278",
        "district": "1",
        "firstName": "Suzanne",
        "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
        "lastName": "Bonamici",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "START Housing Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-18T09:07:25Z",
    "updateDateIncludingText": "2025-12-18T09:07:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-12",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-12",
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
          "date": "2025-02-12T15:08:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "PA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "DC"
    },
    {
      "bioguideId": "G000551",
      "district": "7",
      "firstName": "Ra\u00fal",
      "fullName": "Rep. Grijalva, Ra\u00fal M. [D-AZ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Grijalva",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "AZ"
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
      "sponsorshipDate": "2025-02-12",
      "state": "LA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "NE"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "NM"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "OH"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "IL"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1231ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1231\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2025 Ms. Bonamici (for herself, Mr. Fitzpatrick , Ms. Norton , Mr. Grijalva , and Mr. Carter of Louisiana ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo reauthorize and expand the pilot program to help individuals in recovery from a substance use disorder become stably housed, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Supporting Transition And Recovery Through Housing Act of 2025 or the START Housing Act of 2025 .\n#### 2. Reauthorization of Recovery Housing Program\nSection 8071 of the SUPPORT for Patients and Communities Act ( 42 U.S.C. 5301 note) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby striking 2019 through 2023 and inserting 2026 through 2031 ;\n**(B)**\nby striking for a period of not more than 2 years or ; and\n**(C)**\nby striking , whichever is earlier ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1), by inserting , acting through the Office of Community Planning and Development in consultation with the Office of Special Needs Assistance, before not later than ; and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (A), by striking allocated to and inserting prioritized for ; and\n**(ii)**\nby striking subparagraph (B) and inserting the following new subparagraph:\n(B) Priority Among the States, priority shall be given to States with the greatest need, as such need is determined by the Secretary based on the following factors: (i) The highest average rates of unemployment based on data provided by the Bureau of Labor Statistics for calendar years 2019 through 2023. (ii) The lowest average labor force participation rates based on data provided by the Bureau of Labor Statistics for calendar years 2019 through 2023. (iii) The highest age-adjusted rates of drug overdose deaths based on data from the Centers for Disease Control and Prevention. (iv) The highest rates of unsheltered homelessness as determined by the most recent annual point-in-time count of persons experiencing homelessness required by the Secretary of Housing and Urban Development under title IV of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11360 et seq. ). ;\n**(3)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (2)\u2014\n**(i)**\nby inserting , low-barrier after effective ; and\n**(ii)**\nby inserting before the period at the end the following: with an expectation that persons participating in the program have access to stable housing upon exiting the program ; and\n**(B)**\nby adding at the end the following new paragraphs:\n(4) Supplement not supplant As a condition of receiving funds under this section, a State shall use such funds received under this section only to supplement the level of State or local funds that would, in the absence of the receipt of funds under this section, be made available for related housing and recovery services. (5) Consultation Each State that receives amounts pursuant to this section shall consult with continuums of care and public housing agencies to assess needs for implementing funds and developing a plan to support individuals receiving stable housing in connection with funding under this section with transfer to other housing at the end of the individuals\u2019 eligibility. ; and\n**(4)**\nby striking subsection (f) and inserting the following new subsection:\n(f) Technical assistance The Secretary may use not more than 2 percent of the funds made available under this section for technical assistance, to publish best practices, and to conduct outreach to grantees or potentially eligible participants. .",
      "versionDate": "2025-02-12",
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
            "name": "Drug, alcohol, tobacco use",
            "updateDate": "2025-04-23T17:43:24Z"
          },
          {
            "name": "Homelessness and emergency shelter",
            "updateDate": "2025-04-23T17:43:24Z"
          },
          {
            "name": "Low- and moderate-income housing",
            "updateDate": "2025-04-23T17:43:24Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2025-04-23T17:43:24Z"
          },
          {
            "name": "Public housing",
            "updateDate": "2025-04-23T17:43:24Z"
          },
          {
            "name": "Unemployment",
            "updateDate": "2025-04-23T17:43:24Z"
          }
        ]
      },
      "policyArea": {
        "name": "Housing and Community Development",
        "updateDate": "2025-03-13T12:48:23Z"
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
      "date": "2025-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1231ih.xml"
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
      "title": "START Housing Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T11:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "START Housing Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T11:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Supporting Transition And Recovery Through Housing Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T11:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To reauthorize and expand the pilot program to help individuals in recovery from a substance use disorder become stably housed, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T11:18:24Z"
    }
  ]
}
```
