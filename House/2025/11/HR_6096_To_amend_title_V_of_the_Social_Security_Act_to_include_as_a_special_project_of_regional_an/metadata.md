# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6096?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6096
- Title: NEST Act
- Congress: 119
- Bill type: HR
- Bill number: 6096
- Origin chamber: House
- Introduced date: 2025-11-18
- Update date: 2026-03-04T09:06:27Z
- Update date including text: 2026-03-04T09:06:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-18: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-11-18: Introduced in House

## Actions

- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-18",
    "latestAction": {
      "actionDate": "2025-11-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6096",
    "number": "6096",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "L000595",
        "district": "5",
        "firstName": "Julia",
        "fullName": "Rep. Letlow, Julia [R-LA-5]",
        "lastName": "Letlow",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "NEST Act",
    "type": "HR",
    "updateDate": "2026-03-04T09:06:27Z",
    "updateDateIncludingText": "2026-03-04T09:06:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-18",
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
      "actionDate": "2025-11-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-18",
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
          "date": "2025-11-18T15:00:30Z",
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
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "WA"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-11-18",
      "state": "IA"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "CA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-12-05",
      "state": "NE"
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
      "sponsorshipDate": "2025-12-05",
      "state": "DC"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "AZ"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "MA"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "NY"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "AL"
    },
    {
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "VA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "NY"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "FL"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "NH"
    },
    {
      "bioguideId": "L000597",
      "district": "15",
      "firstName": "Laurel",
      "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "FL"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "PA"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "LA"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "NJ"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "IL"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "CA"
    },
    {
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Adams",
      "middleName": "S.",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6096ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6096\nIN THE HOUSE OF REPRESENTATIVES\nNovember 18, 2025 Ms. Letlow (for herself, Ms. Schrier , Mrs. Miller-Meeks , and Ms. Barrag\u00e1n ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title V of the Social Security Act to include as a special project of regional and national significance the purchase, acquisition, and distribution to mothers of newborn infants newborn supply kits, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Newborns Essentials Support Toolkit Act or the NEST Act .\n#### 2. Newborn supply kits\n##### (a) In general\nSection 501(a)(2) of the Social Security Act ( 42 U.S.C. 701(a)(2) ) is amended\u2014\n**(1)**\nby striking and for evidence-based programs and inserting for evidence-based programs ; and\n**(2)**\nby inserting before ; and at the end the following: , and for the purchase, acquisition, and distribution of newborn supply kits distributed in accordance with subsection (d) .\n##### (b) Newborn supply kit defined\nSection 501(b) of the Social Security Act ( 42 U.S.C. 701(b) ) is amended by adding at the end the following:\n(5) The term newborn supply kit means a kit composed of essential goods to help mothers recover from childbirth and care for newborn infants that includes the following items: (A) Diapers, wipes, hygiene items, blankets, and thermometers for newborn infants. (B) Postpartum pads, lotion, cold packs, breastfeeding supplies, information on the National Maternal Mental Health Hotline established under section 399V\u20137 of the Public Health Service Act, information on the National Women\u2019s Health and Breastfeeding Helpline and additional educational material on breastfeeding, information about Federal programs providing support to postpartum women and children, such as the special supplemental nutrition program for women, infants, and children under section 17 of the Child Nutrition Act of 1966, and evidence-based educational material on the use of low-dose aspirin to address hypertension, preeclampsia, and preterm birth. (C) A blood pressure monitor. (D) Other items necessary to support infant and postpartum health (as determined by the Secretary). .\n##### (c) Set-aside\nSection 501(c) of the Social Security Act ( 42 U.S.C. 701(c) ) is amended\u2014\n**(1)**\nby redesignating paragraph (5) as paragraph (6); and\n**(2)**\nby inserting after paragraph (4) the following:\n(5) For each of fiscal years 2026 through 2030, of the funds made available under subsection (a) for a fiscal year, the Secretary may reserve not more than $5,000,000 for the purpose of enabling the Secretary to provide for special projects of regional and national significance for the purchase, acquisition, and distribution of newborn supply kits in accordance with subsection (d). .\n##### (d) Administration\nSection 501 of the Social Security Act ( 42 U.S.C. 701 ) is amended by adding at the end the following:\n(d) (1) In purchasing or acquiring newborn supply kits using funds made available under subsection (c)(5), the Secretary shall make grants or enter into cooperative agreements with nonprofit entities that have a multi-state presence to procure such newborn supply kits for new mothers, such as community-based organizations, Federally qualified health centers (as defined in section 1861(aa)), Tribal organizations (as defined in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 )), and birthing hospitals. (2) In distributing newborn supply kits purchased or acquired using funds made available under subsection (c)(5), the entity that distributes such kits shall, as a condition on the receipt of such funds\u2014 (A) partner with a local organizations that serve the locations where such newborn supply kits are to be distributed; (B) to the maximum extent practicable, ensure the geographical diversity of the recipients of such newborn supply kits; (C) give priority to geographic areas with the greatest need, such as maternity care deserts, rural communities, and communities with the highest maternal mortality rates (such as the Delta region); and (D) give priority to mothers or newborn infants whose family income does not exceed 185 percent of the poverty line (as defined in section 673(2) of the Community Services Block Grant Act ( 42 U.S.C. 9902(2) )) for a family of the size involved. .\n##### (e) Report\n**(1) In general**\nNot later than one year after the date on which the first grant or cooperative agreement is awarded pursuant to the amendment made by subsection (a), t he Secretary shall submit to the appropriate committees of Congress a report on the progress of the grants or cooperative agreements so awarded, including\u2014\n**(A)**\nthe number of mothers served under the grants or cooperative agreements during the period covered by the report (disaggregated by race, family income level, and number of individuals in the household);\n**(B)**\nthe regions in the United States in which newborn supply kits are being distributed through such grants or cooperative agreements;\n**(C)**\nfeedback from mothers who have received newborn supply kits through such grants or cooperative agreements; and\n**(D)**\nsuch other information, as determined necessary by the Secretary.\n**(2) Final report**\nNot later than 180 days after the date on which the last grant or cooperative agreement is awarded pursuant to the amendment made by subsection (a) for fiscal year 2030, the Secretary shall submit to the appropriate committees of Congress a report on the results of the grants or cooperative agreements awarded pursuant to the amendment made by subsection (a) with respect to maternal and infant health outcomes.\n**(3) Appropriate committees of Congress defined**\nIn this subsection, the term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Energy and Commerce of the House of Representatives;\n**(B)**\nthe Committee on Health, Education, Labor, and Pensions of the Senate;\n**(C)**\nthe Committee on Appropriations of the House of Representatives; and\n**(D)**\nthe Committee on Appropriations of the Senate.",
      "versionDate": "2025-11-18",
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
        "name": "Health",
        "updateDate": "2026-01-14T16:47:31Z"
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
      "date": "2025-11-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6096ih.xml"
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
      "title": "NEST Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-19T10:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "NEST Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-19T10:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Newborns Essentials Support Toolkit Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-19T10:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title V of the Social Security Act to include as a special project of regional and national significance the purchase, acquisition, and distribution to mothers of newborn infants newborn supply kits, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-19T10:03:26Z"
    }
  ]
}
```
