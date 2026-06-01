# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5907?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5907
- Title: To authorize the Secretary of Housing and Urban Development to award grants to eligible entities to select pre-reviewed designs of covered structures of mixed-income housing for use in the jurisdiction of the eligible entity, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 5907
- Origin chamber: House
- Introduced date: 2025-11-04
- Update date: 2026-03-10T08:05:34Z
- Update date including text: 2026-03-10T08:05:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-04: Introduced in House
- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-11-04: Introduced in House

## Actions

- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Introduced in House
- 2025-11-04 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-04",
    "latestAction": {
      "actionDate": "2025-11-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5907",
    "number": "5907",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "B001326",
        "district": "5",
        "firstName": "Janelle",
        "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
        "lastName": "Bynum",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "To authorize the Secretary of Housing and Urban Development to award grants to eligible entities to select pre-reviewed designs of covered structures of mixed-income housing for use in the jurisdiction of the eligible entity, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-03-10T08:05:34Z",
    "updateDateIncludingText": "2026-03-10T08:05:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-04",
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
      "actionDate": "2025-11-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-04",
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
          "date": "2025-11-04T19:00:45Z",
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
      "bioguideId": "S001213",
      "district": "1",
      "firstName": "Bryan",
      "fullName": "Rep. Steil, Bryan [R-WI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Steil",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "WI"
    },
    {
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "sponsorshipWithdrawnDate": "2026-01-12",
      "state": "WI"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "NH"
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
      "sponsorshipDate": "2025-11-07",
      "state": "PA"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
      "state": "NC"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-12-05",
      "state": "DE"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-01-20",
      "state": "NY"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "NH"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5907ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5907\nIN THE HOUSE OF REPRESENTATIVES\nNovember 4, 2025 Ms. Bynum (for herself, Mr. Steil , Mr. Fitzgerald , and Mr. Pappas ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo authorize the Secretary of Housing and Urban Development to award grants to eligible entities to select pre-reviewed designs of covered structures of mixed-income housing for use in the jurisdiction of the eligible entity, and for other purposes.\n#### 1. Accelerating home building act\n##### (a) Definitions\nIn this section:\n**(1) Affordable housing**\nThe term affordable housing means housing for which the total monthly housing cost payment is not more than 30 percent of the monthly household income for a household earning not more than 80 percent of the area median income.\n**(2) Covered structure**\nThe term covered structure means\u2014\n**(A)**\na low-rise or mid-rise structure with not more than 25 dwelling units; and\n**(B)**\nincludes\u2014\n**(i)**\nan accessory dwelling unit;\n**(ii)**\ninfill development;\n**(iii)**\na duplex;\n**(iv)**\na triplex;\n**(v)**\na fourplex;\n**(vi)**\na cottage court;\n**(vii)**\na courtyard building;\n**(viii)**\na townhouse;\n**(ix)**\na multiplex; and\n**(x)**\nany other structure with not less than 2 dwelling units that the Secretary considers appropriate.\n**(3) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\na unit of general local government, as defined in section 102(a) of the Housing and Community Development Act of 1974 ( 42 U.S.C. 5302(a) );\n**(B)**\na municipal membership organization; and\n**(C)**\nan Indian tribe, as defined in section 102(a) of the Housing and Community Development Act of 1974 ( 42 U.S.C. 5302(a) ).\n**(4) High opportunity area**\nThe term high opportunity area has the meaning given the term in section 1282.1 of title 12, Code of Federal Regulations, or any successor regulation.\n**(5) Infill development**\nThe term infill development means residential development on small parcels in previously established areas for replacement by new or refurbished housing that utilizes existing utilities and infrastructure.\n**(6) Mixed-income housing**\nThe term mixed-income housing means a housing development that is comprised of housing units that promote differing levels of affordability in the community.\n**(7) Pre-reviewed designs**\nThe term pre-reviewed designs , also known as pattern books, means sets of construction plans that are assessed and approved by localities for compliance with local building and permitting standards to streamline and expedite approval pathways for housing construction.\n**(8) Rural area**\nThe term rural area means any area other than a city or town that has a population of less than 50,000 inhabitants.\n**(9) Secretary**\nThe term Secretary means the Secretary of Housing and Urban Development.\n##### (b) Authority\nThe Secretary may award grants to eligible entities to select pre-reviewed designs of covered structures of mixed-income housing for use in the jurisdiction of the eligible entity, except that such grant awards may not be used for construction, alteration, or repair work.\n##### (c) Considerations\nIn reviewing applications submitted by eligible entities for a grant under this section, the Secretary shall consider\u2014\n**(1)**\nthe need for affordable housing by the eligible entity;\n**(2)**\nthe presence of high opportunity areas in the jurisdiction of the eligible entity;\n**(3)**\ncoordination between the eligible entity and a State agency; and\n**(4)**\ncoordination between the eligible entity and State, local, and regional transportation planning authorities.\n##### (d) Set-aside for rural areas\nOf the amount made available in each fiscal year for grants under this section, the Secretary shall ensure that not less than 10 percent shall be used for grants to eligible entities that are located in rural areas.\n##### (e) Reports\nThe Secretary shall require eligible entities receiving grants under this section to report on\u2014\n**(1)**\nthe impacts of the activities carried out using the grant amounts in improving the production and supply of affordable housing;\n**(2)**\nthe pre-reviewed designs selected using the grant amounts in their communities;\n**(3)**\nthe number of permits issued for housing development utilizing pre-reviewed designs; and\n**(4)**\nthe number of housing units produced in developments utilizing the pre-reviewed designs.\n##### (f) Availability of information\nThe Secretary shall\u2014\n**(1)**\nto the extent possible, encourage localities to make publicly available through a website information on the pre-reviewed designs selected and submitted to the Secretary by eligible entities receiving grants under this section, including information on the benefits of use of those designs; and\n**(2)**\ncollect, identify, and disseminate best practices regarding such designs and make such information publicly available on the website of the Department of Housing and Urban Development.\n##### (g) Design adoption and repayment\nThe Secretary may require an eligible entity to return to the Secretary any grant funds received under this section if the selected pre-reviewed designs submitted under this section have not been adopted during the 5-year period following receipt of the grant, unless that period is extended by the Secretary.\n##### (h) Authorization of appropriations\n**(1) In general**\nThere is authorized to be appropriated to the Secretary such sums as are necessary to carry out this section.\n**(2) Technical assistance**\nThe Secretary may set aside not more than 5 percent of amounts appropriated under paragraph (1) in a fiscal year to provide technical assistance to grant recipients under this section and pre-grant technical assistance for prospective applicants.",
      "versionDate": "2025-11-04",
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
        "name": "Housing and Community Development",
        "updateDate": "2025-11-25T17:20:48Z"
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
      "date": "2025-11-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5907ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Secretary of Housing and Urban Development to award grants to eligible entities to select pre-reviewed designs of covered structures of mixed-income housing for use in the jurisdiction of the eligible entity, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-05T09:18:15Z"
    },
    {
      "title": "To authorize the Secretary of Housing and Urban Development to award grants to eligible entities to select pre-reviewed designs of covered structures of mixed-income housing for use in the jurisdiction of the eligible entity, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-05T09:05:46Z"
    }
  ]
}
```
