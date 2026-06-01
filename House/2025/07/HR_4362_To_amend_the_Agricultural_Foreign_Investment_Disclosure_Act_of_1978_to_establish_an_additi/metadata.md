# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4362?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4362
- Title: AFIDA Improvements Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4362
- Origin chamber: House
- Introduced date: 2025-07-14
- Update date: 2026-03-04T09:05:49Z
- Update date including text: 2026-03-04T09:05:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-14: Introduced in House
- 2025-07-14 - IntroReferral: Introduced in House
- 2025-07-14 - IntroReferral: Introduced in House
- 2025-07-14 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-07-14: Introduced in House

## Actions

- 2025-07-14 - IntroReferral: Introduced in House
- 2025-07-14 - IntroReferral: Introduced in House
- 2025-07-14 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-14",
    "latestAction": {
      "actionDate": "2025-07-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4362",
    "number": "4362",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "B001298",
        "district": "2",
        "firstName": "Don",
        "fullName": "Rep. Bacon, Don [R-NE-2]",
        "lastName": "Bacon",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "AFIDA Improvements Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-04T09:05:49Z",
    "updateDateIncludingText": "2026-03-04T09:05:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-14",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-14",
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
          "date": "2025-07-14T16:00:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "MO"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "IL"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "MN"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "IA"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "WA"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "PA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "CA"
    },
    {
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "TX"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "CA"
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
      "sponsorshipDate": "2025-07-29",
      "state": "VA"
    },
    {
      "bioguideId": "M001216",
      "district": "7",
      "firstName": "Cory",
      "fullName": "Rep. Mills, Cory [R-FL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mills",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "FL"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4362ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4362\nIN THE HOUSE OF REPRESENTATIVES\nJuly 14, 2025 Mr. Bacon (for himself, Mr. Alford , Mr. Bost , Mr. Finstad , Mrs. Hinson , Mr. Newhouse , Ms. Houlahan , Mr. Panetta , Mr. Cuellar , and Mr. Carbajal ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Agricultural Foreign Investment Disclosure Act of 1978 to establish an additional reporting requirement, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the AFIDA Improvements Act of 2025 .\n#### 2. Reporting; enforcement\n##### (a) Reporting requirement\nSection 2 of the Agricultural Foreign Investment Disclosure Act of 1978 ( 7 U.S.C. 3501 ) is amended by adding at the end the following:\n(g) Minimum ownership In the case of agricultural land in which more than 1 foreign person acquires or transfers any interest, other than a security interest, the reporting requirements under this section shall apply to each foreign person who holds at least a 1 percent interest in that land\u2014 (1) directly through the first tier of ownership; or (2) in the aggregate through an interest in other entities at various tiers. .\n##### (b) Enforcement\nSection 4 of the Agricultural Foreign Investment Disclosure Act of 1978 ( 7 U.S.C. 3503 ) is amended\u2014\n**(1)**\nby striking the section designation and all that follows through The Secretary and inserting the following:\n4. Investigative actions (a) In general The Secretary ; and\n**(2)**\nby adding at the end the following:\n(b) Actions by FPAC\u2013BC As part of the actions taken under subsection (a), the Farm Production and Conservation Business Center shall\u2014 (1) take such actions as are necessary to validate the data collected under section 2, including revising and validating information throughout the data collection process; (2) take such actions as are necessary to ensure compliance with section 2(g); and (3) in coordination with the Farm Service Agency, to the maximum extent practicable, identify persons that have carried out an activity subject to a civil penalty described in paragraph (1) or (2) of section 3(a). .\n#### 3. Agricultural foreign investment disclosure improvements\n##### (a) Definitions\nIn this section:\n**(1) AFIDA**\nThe term AFIDA means the Agricultural Foreign Investment Disclosure Act of 1978 ( 7 U.S.C. 3501 et seq. ).\n**(2) FPAC\u2013BC**\nThe term FPAC\u2013BC means the Farm Production and Conservation Business Center.\n**(3) Secretary**\nThe term Secretary means the Secretary of Agriculture.\n##### (b) MOU with CFIUS\nNot later than 1 year after the date of enactment of this Act, the Secretary shall enter into 1 or more memoranda of understanding with the Committee on Foreign Investment in the United States under which the Secretary shall provide the Committee with all relevant information relating to reports on foreign ownership of United States agricultural land submitted to the Secretary under section 2 of AFIDA ( 7 U.S.C. 3501 ), including information on\u2014\n**(1)**\neach report submitted to the Secretary; and\n**(2)**\nwith respect to each such report, the identity of the person submitting the report and the date of submission.\n##### (c) AFIDA handbook updates\n**(1) First update**\nNot later than 1 year after the date of enactment of this Act, the Secretary shall update the most recent version of the Farm Service Agency handbook entitled Foreign Investment Disclosure as determined necessary by the Secretary for the effective implementation of AFIDA, which update shall incorporate recommendations made by the report of the Government Accountability Office entitled Foreign Investments in U.S. Agricultural Land: Enhancing Efforts to Collect, Track, and Share Key Information Could Better Identify National Security Risks and dated January 18, 2024.\n**(2) Subsequent updates**\nAfter updating the handbook described in paragraph (1) under that paragraph, the Secretary shall carry out an update of that handbook every 10 years thereafter, including by incorporating any recommendations of the Government Accountability Office.\n##### (d) Analysis of streamlined process for electronic submission and retention of reports under AFIDA\n**(1) Definition of covered process**\nIn this subsection, the term covered process means the streamlined process for electronic submission and retention of disclosures made under AFIDA required under section 773 of division A of the Consolidated Appropriations Act, 2023 ( 7 U.S.C. 3501 note; 136 Stat. 4509).\n**(2) Analysis**\nUnless the covered process is established by not later than 1 year after the date of enactment of this Act, the FPAC\u2013BC, in coordination with the Farm Service Agency, shall, by that date\u2014\n**(A)**\ncarry out an analysis of the specific steps required to establish that process and the elements of that process; and\n**(B)**\ndevelop a timeline for specific implementation benchmarks to be met.\n**(3) Report**\nThe Secretary shall submit to the Committee on Agriculture, Nutrition, and Forestry of the Senate and the Committee on Agriculture of the House of Representatives a report describing the analysis and implementation timeline under paragraph (2), if applicable.",
      "versionDate": "2025-07-14",
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
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "1969",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "AFIDA Improvements Act of 2025",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-07-29T21:00:15Z"
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
      "date": "2025-07-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4362ih.xml"
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
      "title": "AFIDA Improvements Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:52:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "AFIDA Improvements Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-24T05:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Agricultural Foreign Investment Disclosure Act of 1978 to establish an additional reporting requirement, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-24T05:18:43Z"
    }
  ]
}
```
