# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5145?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5145
- Title: Bipartisan Premium Tax Credit Extension Act
- Congress: 119
- Bill type: HR
- Bill number: 5145
- Origin chamber: House
- Introduced date: 2025-09-04
- Update date: 2026-01-08T09:07:21Z
- Update date including text: 2026-01-08T09:07:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-09-04: Introduced in House
- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-09-04: Introduced in House

## Actions

- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-04",
    "latestAction": {
      "actionDate": "2025-09-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5145",
    "number": "5145",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "K000399",
        "district": "2",
        "firstName": "Jennifer",
        "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
        "lastName": "Kiggans",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Bipartisan Premium Tax Credit Extension Act",
    "type": "HR",
    "updateDate": "2026-01-08T09:07:21Z",
    "updateDateIncludingText": "2026-01-08T09:07:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-04",
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
      "actionDate": "2025-09-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-04",
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
          "date": "2025-09-04T13:04:20Z",
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
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "NY"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-09-04",
      "state": "PA"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-09-04",
      "state": "AZ"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-09-04",
      "state": "PA"
    },
    {
      "bioguideId": "G000593",
      "district": "28",
      "firstName": "Carlos",
      "fullName": "Rep. Gimenez, Carlos A. [R-FL-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Gimenez",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-09-04",
      "state": "FL"
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
      "sponsorshipDate": "2025-09-04",
      "state": "CA"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-09-04",
      "state": "CA"
    },
    {
      "bioguideId": "H001100",
      "district": "3",
      "firstName": "Jeff",
      "fullName": "Rep. Hurd, Jeff [R-CO-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Hurd",
      "party": "R",
      "sponsorshipDate": "2025-09-04",
      "state": "CO"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-09-04",
      "state": "NJ"
    },
    {
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "ME"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-09-04",
      "state": "NY"
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
      "sponsorshipDate": "2025-09-04",
      "state": "NC"
    },
    {
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "WA"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-09-04",
      "state": "FL"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-09-08",
      "state": "NJ"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "MI"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "CA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "NJ"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "NH"
    },
    {
      "bioguideId": "D000594",
      "district": "15",
      "firstName": "Monica",
      "fullName": "Rep. De La Cruz, Monica [R-TX-15]",
      "isOriginalCosponsor": "False",
      "lastName": "De La Cruz",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "TX"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "NV"
    },
    {
      "bioguideId": "M001216",
      "district": "7",
      "firstName": "Cory",
      "fullName": "Rep. Mills, Cory [R-FL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mills",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "FL"
    },
    {
      "bioguideId": "K000009",
      "district": "9",
      "firstName": "Marcy",
      "fullName": "Rep. Kaptur, Marcy [D-OH-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaptur",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "OH"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "NM"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "CA"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "NY"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "CA"
    },
    {
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "False",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "TX"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "CA"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5145ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5145\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 4, 2025 Mrs. Kiggans of Virginia (for herself, Mr. Suozzi , Mr. Fitzpatrick , Mr. Ciscomani , Mr. Bresnahan , Mr. Gimenez , Mr. Valadao , Mrs. Kim , Mr. Hurd of Colorado , Mr. Kean , Mr. Golden of Maine , Mr. Lawler , Mr. Davis of North Carolina , Ms. Perez , and Ms. Salazar ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to extend the enhanced premium tax credit, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Bipartisan Premium Tax Credit Extension Act .\n#### 2. Extension of enhanced premium tax credit\n##### (a) Extension of rules To increase premium assistance amounts\nClause (iii) of section 36B(b)(3)(A) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin the heading, by striking through 2025 and inserting through 2026 , and\n**(2)**\nin the matter preceding subclause (I), by striking before January 1, 2026 and inserting before January 1, 2027 .\n##### (b) Extension of rule To allow credit to taxpayers whose household income exceeds 400 percent of poverty line\nSubparagraph (E) of section 36B(c)(1) of such Code is amended\u2014\n**(1)**\nin the heading, by striking through 2025 and inserting through 2026 , and\n**(2)**\nby striking before January 1, 2026 and inserting before January 1, 2027 .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-09-04",
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
        "actionDate": "2025-12-11",
        "text": "Cloture on the motion to proceed to the measure not invoked in Senate by Yea-Nay Vote. 51 - 48. Record Vote Number: 644. (CR S8654-8655)"
      },
      "number": "3385",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Lower Health Care Costs Act",
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
        "updateDate": "2025-09-12T16:20:39Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-04",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr5145",
          "measure-number": "5145",
          "measure-type": "hr",
          "orig-publish-date": "2025-09-04",
          "originChamber": "HOUSE",
          "update-date": "2025-09-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5145v00",
            "update-date": "2025-09-18"
          },
          "action-date": "2025-09-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Bipartisan Premium Tax Credit Extension Act</strong></p><p>This bill extends for one year, through 2026, temporary changes enacted by the American Rescue Plan Act of 2021 (ARPA) and the Inflation Reduction Act of 2022 (IRA) that generally expand eligibility for and increase the amount of the premium tax credit.\u00a0</p><p>Currently, eligible taxpayers may be able to claim the premium tax credit, which applies toward the cost of obtaining health insurance through health insurance exchanges. To be eligible for the premium tax credit, a taxpayer\u2019s household income must meet or exceed 100% of the federal poverty level (FPL) and, after 2025, may not exceed 400% of the FPL (maximum income limit). For 2021-2025, the ARPA and IRA eliminated the maximum income limit, which generally expands eligibility for the premium tax credit.</p><p>Further, under current law, the amount of the premium tax credit is (1) generally the plan premium (conditions apply), minus (2) the taxpayer\u2019s household income multiplied by the applicable percentage. The applicable percentage is a specific percentage that varies depending on which of six income ranges (adjusted for inflation after 2025) the taxpayer\u2019s household income falls within. For 2021-2025, the ARPA and IRA lowered the applicable percentages and eliminated the adjustment of the applicable percentages for inflation, which generally increases the amount of the premium tax credit.</p><p>The bill extends for one year, through 2026, the elimination of the 400% maximum income limit, the\u00a0lower applicable percentages, and the elimination of the inflation adjustment for the applicable percentages. </p>"
        },
        "title": "Bipartisan Premium Tax Credit Extension Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5145.xml",
    "summary": {
      "actionDate": "2025-09-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Bipartisan Premium Tax Credit Extension Act</strong></p><p>This bill extends for one year, through 2026, temporary changes enacted by the American Rescue Plan Act of 2021 (ARPA) and the Inflation Reduction Act of 2022 (IRA) that generally expand eligibility for and increase the amount of the premium tax credit.\u00a0</p><p>Currently, eligible taxpayers may be able to claim the premium tax credit, which applies toward the cost of obtaining health insurance through health insurance exchanges. To be eligible for the premium tax credit, a taxpayer\u2019s household income must meet or exceed 100% of the federal poverty level (FPL) and, after 2025, may not exceed 400% of the FPL (maximum income limit). For 2021-2025, the ARPA and IRA eliminated the maximum income limit, which generally expands eligibility for the premium tax credit.</p><p>Further, under current law, the amount of the premium tax credit is (1) generally the plan premium (conditions apply), minus (2) the taxpayer\u2019s household income multiplied by the applicable percentage. The applicable percentage is a specific percentage that varies depending on which of six income ranges (adjusted for inflation after 2025) the taxpayer\u2019s household income falls within. For 2021-2025, the ARPA and IRA lowered the applicable percentages and eliminated the adjustment of the applicable percentages for inflation, which generally increases the amount of the premium tax credit.</p><p>The bill extends for one year, through 2026, the elimination of the 400% maximum income limit, the\u00a0lower applicable percentages, and the elimination of the inflation adjustment for the applicable percentages. </p>",
      "updateDate": "2025-09-18",
      "versionCode": "id119hr5145"
    },
    "title": "Bipartisan Premium Tax Credit Extension Act"
  },
  "summaries": [
    {
      "actionDate": "2025-09-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Bipartisan Premium Tax Credit Extension Act</strong></p><p>This bill extends for one year, through 2026, temporary changes enacted by the American Rescue Plan Act of 2021 (ARPA) and the Inflation Reduction Act of 2022 (IRA) that generally expand eligibility for and increase the amount of the premium tax credit.\u00a0</p><p>Currently, eligible taxpayers may be able to claim the premium tax credit, which applies toward the cost of obtaining health insurance through health insurance exchanges. To be eligible for the premium tax credit, a taxpayer\u2019s household income must meet or exceed 100% of the federal poverty level (FPL) and, after 2025, may not exceed 400% of the FPL (maximum income limit). For 2021-2025, the ARPA and IRA eliminated the maximum income limit, which generally expands eligibility for the premium tax credit.</p><p>Further, under current law, the amount of the premium tax credit is (1) generally the plan premium (conditions apply), minus (2) the taxpayer\u2019s household income multiplied by the applicable percentage. The applicable percentage is a specific percentage that varies depending on which of six income ranges (adjusted for inflation after 2025) the taxpayer\u2019s household income falls within. For 2021-2025, the ARPA and IRA lowered the applicable percentages and eliminated the adjustment of the applicable percentages for inflation, which generally increases the amount of the premium tax credit.</p><p>The bill extends for one year, through 2026, the elimination of the 400% maximum income limit, the\u00a0lower applicable percentages, and the elimination of the inflation adjustment for the applicable percentages. </p>",
      "updateDate": "2025-09-18",
      "versionCode": "id119hr5145"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5145ih.xml"
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
      "title": "Bipartisan Premium Tax Credit Extension Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-09T04:23:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Bipartisan Premium Tax Credit Extension Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-09T04:23:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to extend the enhanced premium tax credit, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-09T04:18:18Z"
    }
  ]
}
```
