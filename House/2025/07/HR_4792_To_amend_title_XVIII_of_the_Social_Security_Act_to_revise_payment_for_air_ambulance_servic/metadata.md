# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4792?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4792
- Title: Protecting Air Ambulance Services for Americans Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4792
- Origin chamber: House
- Introduced date: 2025-07-29
- Update date: 2026-05-13T08:06:25Z
- Update date including text: 2026-05-13T08:06:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-07-29: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-29 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-07-29: Introduced in House

## Actions

- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-29 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-29",
    "latestAction": {
      "actionDate": "2025-07-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4792",
    "number": "4792",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "E000298",
        "district": "4",
        "firstName": "Ron",
        "fullName": "Rep. Estes, Ron [R-KS-4]",
        "lastName": "Estes",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Protecting Air Ambulance Services for Americans Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:25Z",
    "updateDateIncludingText": "2026-05-13T08:06:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-29",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-29",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-29",
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
          "date": "2025-07-29T21:04:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-07-29T21:04:25Z",
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
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "WA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "CA"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "FL"
    },
    {
      "bioguideId": "C001121",
      "district": "6",
      "firstName": "Jason",
      "fullName": "Rep. Crow, Jason [D-CO-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Crow",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "CO"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "KS"
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
      "sponsorshipDate": "2025-11-18",
      "state": "AL"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2025-11-18",
      "state": "TX"
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
      "sponsorshipDate": "2025-11-18",
      "state": "VA"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "NY"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CO"
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
      "sponsorshipDate": "2026-01-15",
      "state": "DC"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "CA"
    },
    {
      "bioguideId": "R000599",
      "district": "25",
      "firstName": "Raul",
      "fullName": "Rep. Ruiz, Raul [D-CA-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Ruiz",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "CA"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "IN"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "WV"
    },
    {
      "bioguideId": "D000628",
      "district": "2",
      "firstName": "Neal",
      "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Dunn",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "FL"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4792ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4792\nIN THE HOUSE OF REPRESENTATIVES\nJuly 29, 2025 Mr. Estes (for himself and Ms. DelBene ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to revise payment for air ambulance services under the Medicare program.\n#### 1. Short title\nThis Act may be cited as the Protecting Air Ambulance Services for Americans Act of 2025 .\n#### 2. Improvements to Medicare payment system for air ambulance services\nSection 1834(l) of the Social Security Act ( 42 U.S.C. 1395m(l) ) is amended by adding at the end the following new paragraph:\n(18) Improvements to Medicare payment system for air ambulance services (A) In general The Secretary may revise the fee schedule otherwise established under this subsection for air ambulance services based on data described in subparagraph (B) and data collected under subparagraph (C). (B) Data described For purposes of subparagraph (A), the data described in this subparagraph is data collected pursuant to the provisions of, and amendments made by, section 106 of division BB of the Consolidated Appropriations Act, 2021 ( Public Law 116\u2013260 ). (C) Additional data collection The Secretary shall require, once every 3 years, providers of services and suppliers furnishing air ambulance services to submit to the Secretary\u2014 (i) data relating to the fixed and operated costs per air ambulance base attributable to furnishing air ambulance services to individuals enrolled under this part and data relating to the utilization of such services by such individuals; (ii) data relating to the revenue obtained by such providers and suppliers under this part attributable to the furnishing of such services; and (iii) any other information determined appropriate by the Secretary. (D) Consultation In the case that the Secretary elects to revise the fee schedule for air ambulance services under subparagraph (A), the Secretary shall consider stakeholder input in a process that is transparent and appropriately considers data described in subparagraph (B) and data collected under subparagraph (C). .\n#### 3. Timely finalization of air ambulance data collection rule\nNot later than 6 months after the date of enactment of this Act, the Secretary of Health and Human Services shall finalize and publish a final rule implementing the air ambulance data collection requirements under section 106 of division BB of the Consolidated Appropriations Act, 2021 ( Public Law 116\u2013260 ).\n#### 4. GAO study on emergency air ambulance costs\nNot later than 1 year after the date on which data begins to be collected pursuant to the provisions of, and amendments made by, section 106 of division BB of the Consolidated Appropriations Act, 2021 ( Public Law 116\u2013260 ), the Comptroller General of the United States shall submit to the Committee on Finance of the Senate and the Committee on Ways and Means and the Committee on Energy and Commerce of the House of Representatives, a report detailing\u2014\n**(1)**\nthe average annual operating costs per air ambulance base;\n**(2)**\nthe average cost per transport by air ambulance;\n**(3)**\nthe payor mix for air ambulance services;\n**(4)**\nthe adequacy of Medicare payments for such services;\n**(5)**\ngeographic variations in the cost of furnishing such services; and\n**(6)**\nrecommendations on improving the fee schedule under section 1834(l) of the Social Security Act ( 42 U.S.C. 1395m(l) ) for air ambulance services.",
      "versionDate": "2025-07-29",
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
        "actionDate": "2025-07-29",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "2518",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Protecting Air Ambulance Services for Americans Act of 2025",
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
        "updateDate": "2025-09-16T13:34:22Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-29",
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
          "measure-id": "id119hr4792",
          "measure-number": "4792",
          "measure-type": "hr",
          "orig-publish-date": "2025-07-29",
          "originChamber": "HOUSE",
          "update-date": "2025-12-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4792v00",
            "update-date": "2025-12-02"
          },
          "action-date": "2025-07-29",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Protecting Air Ambulance Services for Americans Act of 2025</strong></p><p>This bill authorizes payment changes under Medicare for air ambulance services based on certain collected data and requires additional reporting from providers of these services.</p><p>Current law requires providers of air ambulance services to report certain information regarding general costs and utilization to the Department of Health and Human Services; private health insurers are also required to report information relating to coverage of these services. The bill authorizes the Centers for Medicare & Medicaid Services to revise payment rates under Medicare for air ambulance services based on this data, and it requires providers of air ambulance services to specifically report information relating to costs and utilization under Medicare.</p><p>The bill also requires the Government Accountability Office to report on the data that is collected under current law requirements and to recommend changes to Medicare payment rates accordingly.</p>"
        },
        "title": "Protecting Air Ambulance Services for Americans Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4792.xml",
    "summary": {
      "actionDate": "2025-07-29",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Air Ambulance Services for Americans Act of 2025</strong></p><p>This bill authorizes payment changes under Medicare for air ambulance services based on certain collected data and requires additional reporting from providers of these services.</p><p>Current law requires providers of air ambulance services to report certain information regarding general costs and utilization to the Department of Health and Human Services; private health insurers are also required to report information relating to coverage of these services. The bill authorizes the Centers for Medicare & Medicaid Services to revise payment rates under Medicare for air ambulance services based on this data, and it requires providers of air ambulance services to specifically report information relating to costs and utilization under Medicare.</p><p>The bill also requires the Government Accountability Office to report on the data that is collected under current law requirements and to recommend changes to Medicare payment rates accordingly.</p>",
      "updateDate": "2025-12-02",
      "versionCode": "id119hr4792"
    },
    "title": "Protecting Air Ambulance Services for Americans Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-07-29",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Air Ambulance Services for Americans Act of 2025</strong></p><p>This bill authorizes payment changes under Medicare for air ambulance services based on certain collected data and requires additional reporting from providers of these services.</p><p>Current law requires providers of air ambulance services to report certain information regarding general costs and utilization to the Department of Health and Human Services; private health insurers are also required to report information relating to coverage of these services. The bill authorizes the Centers for Medicare & Medicaid Services to revise payment rates under Medicare for air ambulance services based on this data, and it requires providers of air ambulance services to specifically report information relating to costs and utilization under Medicare.</p><p>The bill also requires the Government Accountability Office to report on the data that is collected under current law requirements and to recommend changes to Medicare payment rates accordingly.</p>",
      "updateDate": "2025-12-02",
      "versionCode": "id119hr4792"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4792ih.xml"
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
      "title": "Protecting Air Ambulance Services for Americans Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-05T12:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Air Ambulance Services for Americans Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-05T12:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to revise payment for air ambulance services under the Medicare program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-05T12:18:22Z"
    }
  ]
}
```
