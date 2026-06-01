# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2518?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2518
- Title: Protecting Air Ambulance Services for Americans Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2518
- Origin chamber: Senate
- Introduced date: 2025-07-29
- Update date: 2026-03-12T11:03:18Z
- Update date including text: 2026-03-12T11:03:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-07-29: Introduced in Senate
- 2025-07-29 - IntroReferral: Introduced in Senate
- 2025-07-29 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-07-29: Introduced in Senate

## Actions

- 2025-07-29 - IntroReferral: Introduced in Senate
- 2025-07-29 - IntroReferral: Read twice and referred to the Committee on Finance.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2518",
    "number": "2518",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001267",
        "district": "",
        "firstName": "Michael",
        "fullName": "Sen. Bennet, Michael F. [D-CO]",
        "lastName": "Bennet",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Protecting Air Ambulance Services for Americans Act of 2025",
    "type": "S",
    "updateDate": "2026-03-12T11:03:18Z",
    "updateDateIncludingText": "2026-03-12T11:03:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-29",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-29",
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
            "date": "2025-07-29T21:02:58Z",
            "name": "Referred To"
          },
          {
            "date": "2025-07-29T21:02:58Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "TN"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-10-27",
      "state": "NV"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-10-27",
      "state": "HI"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-10-27",
      "state": "NC"
    },
    {
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-10-27",
      "state": "SC"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-10-27",
      "state": "MT"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-10-27",
      "state": "NM"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-01-29",
      "state": "VA"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2026-01-29",
      "state": "MT"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-03-11",
      "state": "NM"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-03-11",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2518is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2518\nIN THE SENATE OF THE UNITED STATES\nJuly 29, 2025 Mr. Bennet (for himself and Mrs. Blackburn ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to revise payment for air ambulance services under the Medicare program.\n#### 1. Short title\nThis Act may be cited as the Protecting Air Ambulance Services for Americans Act of 2025 .\n#### 2. Improvements to Medicare payment system for air ambulance services\nSection 1834(l) of the Social Security Act (42 U.S.C. 1395m(l)) is amended by adding at the end the following new paragraph:\n(18) Improvements to medicare payment system for air ambulance services (A) In general The Secretary may revise the fee schedule otherwise established under this subsection for air ambulance services based on data described in subparagraph (B) and data collected under subparagraph (C). (B) Data described For purposes of subparagraph (A), the data described in this subparagraph is data collected pursuant to the provisions of, and amendments made by, section 106 of division BB of the Consolidated Appropriations Act, 2021 (Public Law 116\u2013260). (C) Additional data collection The Secretary shall require, once every 3 years, providers of services and suppliers furnishing air ambulance services to submit to the Secretary\u2014 (i) data relating to the fixed and operated costs per air ambulance base attributable to furnishing air ambulance services to individuals enrolled under this part and data relating to the utilization of such services by such individuals; (ii) data relating to the revenue obtained by such providers and suppliers under this part attributable to the furnishing of such services; and (iii) any other information determined appropriate by the Secretary. (D) Consultation In the case that the Secretary elects to revise the fee schedule for air ambulance services under subparagraph (A), the Secretary shall consider stakeholder input in a process that is transparent and appropriately considers data described in subparagraph (B) and data collected under subparagraph (C). .\n#### 3. Timely finalization of air ambulance data collection rule\nNot later than 6 months after the date of enactment of this Act, the Secretary of Health and Human Services shall finalize and publish a final rule implementing the air ambulance data collection requirements under section 106 of division BB of the Consolidated Appropriations Act, 2021 (Public Law 116\u2013260).\n#### 4. GAO study on emergency air ambulance costs\nNot later than 1 year after the date on which data begins to be collected pursuant to the provisions of, and amendments made by, section 106 of division BB of the Consolidated Appropriations Act, 2021 (Public Law 116\u2013260), the Comptroller General of the United States shall submit to the Committee on Finance of the Senate and the Committee on Ways and Means and the Committee on Energy and Commerce of the House of Representatives, a report detailing\u2014\n**(1)**\nthe average annual operating costs per air ambulance base;\n**(2)**\nthe average cost per transport by air ambulance;\n**(3)**\nthe payor mix for air ambulance services;\n**(4)**\nthe adequacy of Medicare payments for such services;\n**(5)**\ngeographic variations in the cost of furnishing such services; and\n**(6)**\nrecommendations on improving the fee schedule under section 1834(l) of the Social Security Act (42 U.S.C. 1395m(l)) for air ambulance services.",
      "versionDate": "",
      "versionType": "Introduced in Senate"
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
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4792",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Protecting Air Ambulance Services for Americans Act of 2025",
      "type": "HR"
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
        "updateDate": "2025-09-16T13:34:59Z"
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
    "originChamber": "Senate",
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
          "measure-id": "id119s2518",
          "measure-number": "2518",
          "measure-type": "s",
          "orig-publish-date": "2025-07-29",
          "originChamber": "SENATE",
          "update-date": "2025-12-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2518v00",
            "update-date": "2025-12-02"
          },
          "action-date": "2025-07-29",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Protecting Air Ambulance Services for Americans Act of 2025</strong></p><p>This bill authorizes payment changes under Medicare for air ambulance services based on certain collected data and requires additional reporting from providers of these services.</p><p>Current law requires providers of air ambulance services to report certain information regarding general costs and utilization to the Department of Health and Human Services; private health insurers are also required to report information relating to coverage of these services. The bill authorizes the Centers for Medicare & Medicaid Services to revise payment rates under Medicare for air ambulance services based on this data, and it requires providers of air ambulance services to specifically report information relating to costs and utilization under Medicare.</p><p>The bill also requires the Government Accountability Office to report on the data that is collected under current law requirements and to recommend changes to Medicare payment rates accordingly.</p>"
        },
        "title": "Protecting Air Ambulance Services for Americans Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2518.xml",
    "summary": {
      "actionDate": "2025-07-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting Air Ambulance Services for Americans Act of 2025</strong></p><p>This bill authorizes payment changes under Medicare for air ambulance services based on certain collected data and requires additional reporting from providers of these services.</p><p>Current law requires providers of air ambulance services to report certain information regarding general costs and utilization to the Department of Health and Human Services; private health insurers are also required to report information relating to coverage of these services. The bill authorizes the Centers for Medicare & Medicaid Services to revise payment rates under Medicare for air ambulance services based on this data, and it requires providers of air ambulance services to specifically report information relating to costs and utilization under Medicare.</p><p>The bill also requires the Government Accountability Office to report on the data that is collected under current law requirements and to recommend changes to Medicare payment rates accordingly.</p>",
      "updateDate": "2025-12-02",
      "versionCode": "id119s2518"
    },
    "title": "Protecting Air Ambulance Services for Americans Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-07-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting Air Ambulance Services for Americans Act of 2025</strong></p><p>This bill authorizes payment changes under Medicare for air ambulance services based on certain collected data and requires additional reporting from providers of these services.</p><p>Current law requires providers of air ambulance services to report certain information regarding general costs and utilization to the Department of Health and Human Services; private health insurers are also required to report information relating to coverage of these services. The bill authorizes the Centers for Medicare & Medicaid Services to revise payment rates under Medicare for air ambulance services based on this data, and it requires providers of air ambulance services to specifically report information relating to costs and utilization under Medicare.</p><p>The bill also requires the Government Accountability Office to report on the data that is collected under current law requirements and to recommend changes to Medicare payment rates accordingly.</p>",
      "updateDate": "2025-12-02",
      "versionCode": "id119s2518"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2518is.xml"
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
      "title": "Protecting Air Ambulance Services for Americans Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-12T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting Air Ambulance Services for Americans Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-08T04:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to revise payment for air ambulance services under the Medicare program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-08T04:33:25Z"
    }
  ]
}
```
