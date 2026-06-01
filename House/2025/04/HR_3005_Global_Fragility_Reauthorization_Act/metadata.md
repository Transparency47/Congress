# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3005?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3005
- Title: Global Fragility Reauthorization Act
- Congress: 119
- Bill type: HR
- Bill number: 3005
- Origin chamber: House
- Introduced date: 2025-04-24
- Update date: 2025-09-03T08:05:57Z
- Update date including text: 2025-09-03T08:05:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-24: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-04-24: Introduced in House

## Actions

- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-24",
    "latestAction": {
      "actionDate": "2025-04-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3005",
    "number": "3005",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "J000305",
        "district": "51",
        "firstName": "Sara",
        "fullName": "Rep. Jacobs, Sara [D-CA-51]",
        "lastName": "Jacobs",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Global Fragility Reauthorization Act",
    "type": "HR",
    "updateDate": "2025-09-03T08:05:57Z",
    "updateDateIncludingText": "2025-09-03T08:05:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-24",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-24",
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
          "date": "2025-04-24T15:02:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "M001157",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. McCaul, Michael T. [R-TX-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McCaul",
      "middleName": "T.",
      "party": "R",
      "sponsorshipDate": "2025-04-24",
      "state": "TX"
    },
    {
      "bioguideId": "J000307",
      "district": "10",
      "firstName": "John",
      "fullName": "Rep. James, John [R-MI-10]",
      "isOriginalCosponsor": "False",
      "lastName": "James",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "MI"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "HI"
    },
    {
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "OH"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "ME"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3005ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3005\nIN THE HOUSE OF REPRESENTATIVES\nApril 24, 2025 Ms. Jacobs (for herself and Mr. McCaul ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo reauthorize the Global Fragility Act of 2019, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Global Fragility Reauthorization Act .\n#### 2. Annual Global Fragility Act Steering Committee Meeting on Policy Alignment\n##### (a) In general\nSection 506 of the Global Fragility Act of 2019 ( 22 U.S.C. 9805 ) is amended\u2014\n**(1)**\nby striking Not later than and inserting (a) In general .\u2014Not later than ; and\n**(2)**\nby adding at the end the following:\n(b) Annual meetings (1) In general The senior Federal officials referred to in paragraph (2) shall convene an annual meeting\u2014 (A) to evaluate the extent to which the strategic approach and objectives of priority country and regional plans described in section 506 align to current United States policy priorities in the relevant countries and regions; (B) to assess the elements described in paragraphs (1) through (11) of subsection (a) and consider steps to address any deficiencies in such elements; (C) to determine any beneficial updates or amendments to the priority country and region plans or United States policy priorities to ensure effective short and long-term alignment; and (D) to consider any beneficial steps to increase alignment of relevant diplomatic, development, and security assistance and cooperation activities with the objectives of such plans and priorities. (2) Participants Each meeting described in paragraph (1) shall be chaired by a position not lower than the Deputy Secretary of State or the Deputy National Security Advisor and include the participation of\u2014 (A) the Under Secretary of State for Civilian Security, Democracy, and Human Rights; (B) the Under Secretary of State for Political Affairs; (C) the Administrator of the United States Agency for International Development (USAID); (D) the Deputy Administrator of USAID for Policy and Programming; (E) the Under Secretary of Defense for Policy; (F) the Under Secretary of the Treasury for International Affairs; (G) each relevant Assistant Secretary, Assistant Administrator, National Security Counsel Senior Director, and relevant equivalent level official with regional or functional responsibility for planning, coordination, or implementation of diplomatic, development, or security cooperation or assistance activities in a priority country; and (H) equivalent level participation from all other relevant Federal departments and agencies with activities relevant to conflict prevention or stabilization in a priority county or region. .\n##### (b) Conforming amendments\nThe Global Fragility Act of 2019 ( 22 U.S.C. 9801 et seq. ) is amended\u2014\n**(1)**\nin section 507(1), by striking section 506 and inserting section 506(a) ; and\n**(2)**\nin section 508(a), by striking section 506 and inserting section 506(a) .\n#### 3. Reauthorization of the Prevention and Stabilization Fund\nSection 509(a) of the Global Fragility Act of 2019 ( 22 U.S.C. 9807(a) ) is amended\u2014\n**(1)**\nin paragraph (2), by striking 2024 and inserting 2030 ; and\n**(2)**\nin paragraph (3)(A), by adding at the end the following:\n(iii) for administrative and other expenses related to the operation, management, and monitoring, evaluation, and learning for programs and activities related to the implementation of the Global Fragility Strategy established pursuant to section 504, including diplomatic and other operational activities carried out to implement such strategy in countries and regions selected by the President, pursuant to section 505(a), notwithstanding any other provision of law. .\n#### 4. Reauthorization of the Complex Crises Fund\nSection 509(b)(2) of the Global Fragility Act of 2019 ( 22 U.S.C. 9807 ) is amended by striking 2024 and inserting 2030 .\n#### 5. Use of Economic Support Fund to support monitoring, evaluation, and learning activities\nFunds authorized to be appropriated or otherwise made available to carry out chapter 4 of part II of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2346 et seq. ; relating to the Economic Support Fund) are authorized to be made available for monitoring, evaluation, and learning activities in countries and regions selected by the President, pursuant to section 505(a) of the Global Fragility Act of 2019 ( 22 U.S.C. 9804 ), notwithstanding any other provision of law for any program funded from amounts available for the Prevention and Stabilization Fund established under section 509(a) of such Act ( 22 U.S.C. 9808(a) ) in any fiscal year and related programs funded by other agencies to implement the Global Fragility Strategy established pursuant to section 504 of such Act ( 22 U.S.C. 9803 ).",
      "versionDate": "2025-04-24",
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
        "name": "International Affairs",
        "updateDate": "2025-05-23T12:21:57Z"
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
      "date": "2025-04-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3005ih.xml"
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
      "title": "Global Fragility Reauthorization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-07T04:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Global Fragility Reauthorization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-07T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To reauthorize the Global Fragility Act of 2019, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-07T04:18:29Z"
    }
  ]
}
```
