# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1871?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1871
- Title: Water Conservation Rebate Tax Parity Act
- Congress: 119
- Bill type: HR
- Bill number: 1871
- Origin chamber: House
- Introduced date: 2025-03-05
- Update date: 2026-04-22T08:07:17Z
- Update date including text: 2026-04-22T08:07:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-05: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-03-05: Introduced in House

## Actions

- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1871",
    "number": "1871",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "H001068",
        "district": "2",
        "firstName": "Jared",
        "fullName": "Rep. Huffman, Jared [D-CA-2]",
        "lastName": "Huffman",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Water Conservation Rebate Tax Parity Act",
    "type": "HR",
    "updateDate": "2026-04-22T08:07:17Z",
    "updateDateIncludingText": "2026-04-22T08:07:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-05",
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
      "actionDate": "2025-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-05",
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
          "date": "2025-03-05T15:06:15Z",
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
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "UT"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "PA"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "CA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "IA"
    },
    {
      "bioguideId": "R000599",
      "district": "25",
      "firstName": "Raul",
      "fullName": "Rep. Ruiz, Raul [D-CA-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Ruiz",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "CA"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "CA"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "CA"
    },
    {
      "bioguideId": "T000474",
      "district": "35",
      "firstName": "Norma",
      "fullName": "Rep. Torres, Norma J. [D-CA-35]",
      "isOriginalCosponsor": "False",
      "lastName": "Torres",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "CA"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "CA"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "False",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
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
      "sponsorshipDate": "2026-04-21",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1871ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1871\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2025 Mr. Huffman (for himself, Mr. Moore of Utah , and Ms. Chu ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to expand the exclusion for certain conservation subsidies to include subsidies for water conservation or efficiency measures, storm water management measures, and wastewater management measures.\n#### 1. Short title\nThis Act may be cited as the Water Conservation Rebate Tax Parity Act .\n#### 2. Modifications to income exclusion for conservation subsidies\n##### (a) In general\nSubsection (a) of section 136 of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking any subsidy provided and inserting\nany subsidy\u2014 (1) provided ,\n**(2)**\nby striking the period at the end and inserting a comma, and\n**(3)**\nby adding at the end the following new paragraphs:\n(2) provided (directly or indirectly) by a public utility to a customer, or by a State or local government to a resident of such State or locality, for the purchase or installation of any water conservation or efficiency measure, (3) provided (directly or indirectly) by a storm water management provider to a customer, or by a State or local government to a resident of such State or locality, for the purchase or installation of any storm water management measure, or (4) provided (directly or indirectly) by a State or local government to a resident of such State or locality for the purchase or installation of any wastewater management measure, but only if such measure is with respect to the taxpayer\u2019s principal residence. .\n##### (b) Conforming amendments\n**(1) Definition of water conservation or efficiency measure and storm water management measure**\nSection 136(c) of the Internal Revenue Code of 1986 is amended\u2014\n**(A)**\nby striking Energy conservation measure in the heading thereof and inserting Definitions ,\n**(B)**\nby striking In general in the heading of paragraph (1) and inserting Energy conservation measure , and\n**(C)**\nby redesignating paragraph (2) as paragraph (5) and by inserting after paragraph (1) the following:\n(2) Water conservation or efficiency measure For purposes of this section, the term water conservation or efficiency measure means any evaluation of water use, or any installation or modification of property, the primary purpose of which is to reduce consumption of water or to improve the management of water demand with respect to one or more dwelling units. (3) Storm water management measure For purposes of this section, the term storm water management measure means any installation or modification of property primarily designed to reduce or manage amounts of storm water with respect to one or more dwelling units, including an installation or modification to prevent or reduce the impacts of storm water-caused flooding to such property. (4) Wastewater management measure For purposes of this section, the term wastewater management measure means any installation or modification of property primarily designed to manage wastewater (including septic tanks and cesspools) with respect to one or more dwelling units. .\n**(2) Definition of public utility**\nSection 136(c)(5) of such Code (as redesignated by paragraph (1)(C)) is amended by striking subparagraph (B) and inserting the following:\n(B) Public utility The term public utility means a person engaged in the sale of electricity, natural gas, or water to residential, commercial, or industrial customers for use by such customers. (C) Storm water management provider The term storm water management provider means a person engaged in the provision of storm water management measures to the public. (D) Person For purposes of subparagraphs (B) and (C), the term person includes the Federal Government, a State or local government or any political subdivision thereof, or any instrumentality of any of the foregoing. .\n**(3) Clerical amendments**\n**(A)**\nThe heading of section 136 of such Code is amended\u2014\n**(i)**\nby inserting and water after energy , and\n**(ii)**\nby striking provided by public utilities .\n**(B)**\nThe item relating to section 136 in the table of sections of part III of subchapter B of chapter 1 of such Code is amended\u2014\n**(i)**\nby inserting and water after energy , and\n**(ii)**\nby striking provided by public utilities .\n##### (c) Effective date\nThe amendments made by this section shall apply to amounts received after December 31, 2021.\n##### (d) No inference\nNothing in this Act or the amendments made by this Act shall be construed to create any inference with respect to the proper tax treatment of any subsidy received directly or indirectly from a public utility, a storm water management provider, or a State or local government for any water conservation or efficiency measure, storm water management measure, or wastewaster management measure before January 1, 2022.",
      "versionDate": "2025-03-05",
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
        "actionDate": "2025-03-05",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "857",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Water Conservation Rebate Tax Parity Act",
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
        "name": "Taxation",
        "updateDate": "2025-05-08T18:47:47Z"
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
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1871ih.xml"
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
      "title": "Water Conservation Rebate Tax Parity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-24T13:53:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Water Conservation Rebate Tax Parity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-24T13:53:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to expand the exclusion for certain conservation subsidies to include subsidies for water conservation or efficiency measures, storm water management measures, and wastewater management measures.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-24T13:48:29Z"
    }
  ]
}
```
