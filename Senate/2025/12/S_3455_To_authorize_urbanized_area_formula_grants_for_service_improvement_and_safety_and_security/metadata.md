# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3455?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3455
- Title: Moving Transit Forward Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3455
- Origin chamber: Senate
- Introduced date: 2025-12-11
- Update date: 2026-03-19T11:03:28Z
- Update date including text: 2026-03-19T11:03:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in Senate
- 2025-12-11 - IntroReferral: Introduced in Senate
- 2025-12-11 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-12-11: Introduced in Senate

## Actions

- 2025-12-11 - IntroReferral: Introduced in Senate
- 2025-12-11 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3455",
    "number": "3455",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "V000128",
        "district": "",
        "firstName": "Chris",
        "fullName": "Sen. Van Hollen, Chris [D-MD]",
        "lastName": "Van Hollen",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "Moving Transit Forward Act of 2025",
    "type": "S",
    "updateDate": "2026-03-19T11:03:28Z",
    "updateDateIncludingText": "2026-03-19T11:03:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
            "date": "2025-12-11T19:02:36Z",
            "name": "Referred To"
          },
          {
            "date": "2025-12-11T19:02:36Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "PA"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "DE"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "NY"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "MA"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "MD"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "MA"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "IL"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "NJ"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "CT"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "CA"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "MN"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3455is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3455\nIN THE SENATE OF THE UNITED STATES\nDecember 11, 2025 Mr. Van Hollen (for himself, Mr. Fetterman , Ms. Blunt Rochester , Mrs. Gillibrand , Ms. Warren , Ms. Alsobrooks , Mr. Markey , Ms. Duckworth , Mr. Booker , and Mr. Blumenthal ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo authorize urbanized area formula grants for service improvement and safety and security enhancement, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Moving Transit Forward Act of 2025 .\n#### 2. Urbanized area formula grants for service improvement and safety and security enhancement\n##### (a) In general\nChapter 53 of title 49, United States Code, is amended by inserting after section 5307 the following:\n5308. Urbanized area formula grants for service improvement and safety and security enhancement (a) General authority The Secretary may make grants under this section for\u2014 (1) operating costs of equipment and facilities for use in public transportation in an urbanized area, if such costs increase or support the quality, frequency, or geographic availability of service; (2) planning of service adjustments to increase the quality, frequency, or geographic availability of service; (3) capital projects or operating costs to increase the security of an existing or planned public transportation system, including costs of law enforcement or security personnel; or (4) capital projects for safety risk mitigations that are identified and recommended by the safety committee of a recipient under section 5329. (b) Apportionments (1) In general The Secretary shall apportion the amounts made available for each fiscal year to carry out this section so that each urbanized area is entitled to receive an amount equal to the amount apportioned under this section multiplied by a ratio equal to the urbanized area\u2019s operating expenses for the most recent year reported to the Secretary under section 5335, divided by the total operating expenses attributable to all urbanized areas. (2) Additional amounts Amounts apportioned to each urbanized area shall be added to amounts apportioned to that urbanized area under section 5336 and made available for eligible activities under this section in accordance with the requirements of section 5307, except as modified under this section. (c) Grant requirements (1) Certifications (A) Grants for operating costs of equipment and facilities to increase or support service A recipient of assistance for operating costs under subsection (a)(1) shall certify to the Secretary that the recipient will\u2014 (i) utilize the operating assistance to increase or support the total level of vehicle revenue service provided by the recipient; and (ii) ensure that the amount of non-Federal expenditures for operating expenses for each of the fiscal years for which the recipient proposes to use the operating assistance to increase or support vehicle revenue service is not less than the amount of non-Federal expenditures of the recipient for operating expenses for the most recent fiscal year. (B) Grants for capital projects or operating costs to increase security A recipient of assistance for capital projects or operating costs under subsection (a)(3) shall certify to the Secretary that the recipient will ensure that the amount of non-Federal expenditures for security expenses of the recipient for each of the fiscal years for which the recipient proposes to use assistance to increase the security of an existing or planned public transportation system is not less than the amount of non-Federal expenditures for security expenses of the recipient for the most recent fiscal year. (2) Other programs or plans Operating assistance under this section is not required to be included in a transportation improvement program, metropolitan transportation plan, statewide transportation improvement program, or statewide transportation plan under section 5303 or 5304. (3) Prohibition Operating assistance under subsection (a)(1) and assistance for planning under subsection (a)(2) shall not be made available for transitioning fixed route public transportation service provided as of the date of receipt of funds to services offered by a third-party contract provider providing on-demand service. (4) Other amounts Notwithstanding section 5307(a)(1)(D), an urbanized area may use not more than 10 percent of the apportionment for the area under section 5336 as if such amounts were made available originally under this section. (d) Government share of costs for operating expenses (1) In general A grant under this section for operating expenses shall be for 80 percent of the net project cost of the project. (2) Additional matching amounts A recipient of a grant under this section for operating expenses may provide additional local matching amounts beyond the amount required under paragraph (1). .\n##### (b) Technical and conforming amendment\nThe table of sections for chapter 53 of title 49, United States Code, is amended by inserting after the item relating to section 5307 the following:\n5308. Urbanized area formula grants for service improvement and safety and security enhancement. .",
      "versionDate": "2025-12-11",
      "versionType": "Introduced in Senate"
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-01-08T19:41:53Z"
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
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3455is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Moving Transit Forward Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T11:03:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Moving Transit Forward Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:24:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to authorize urbanized area formula grants for service improvement and safety and security enhancement, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-06T06:18:30Z"
    }
  ]
}
```
