# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7670?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7670
- Title: Specialty CROP Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7670
- Origin chamber: House
- Introduced date: 2026-02-25
- Update date: 2026-04-28T08:06:18Z
- Update date including text: 2026-04-28T08:06:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-02-25: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2026-02-25: Introduced in House

## Actions

- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-25",
    "latestAction": {
      "actionDate": "2026-02-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7670",
    "number": "7670",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
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
    "title": "Specialty CROP Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-28T08:06:18Z",
    "updateDateIncludingText": "2026-04-28T08:06:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-25",
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
      "actionDate": "2026-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-25",
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
          "date": "2026-02-25T14:02:50Z",
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
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2026-02-25",
      "state": "CA"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "CA"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "OR"
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
      "sponsorshipDate": "2026-03-03",
      "state": "PA"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7670ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7670\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2026 Ms. Bonamici (for herself, Mr. Valadao , Mr. Costa , and Ms. Salinas ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo require a report on the competitiveness of United States exports of specialty crops.\n#### 1. Short title\nThis Act may be cited as the Specialty Crops Reporting on Opportunities and Promotion Act of 2026 or the Specialty CROP Act of 2026 .\n#### 2. Report on competitiveness of United States exports of specialty crops\nSection 203(e)(7) of the Agricultural Trade Act of 1978 ( 7 U.S.C. 5623(e)(7) ) is amended to read as follows:\n(7) Annual report (A) In general Each year, the Secretary, in consultation with the United States Trade Representative, shall submit to the appropriate committees of Congress a report detailing the competitiveness of United States exports of specialty crops. (B) Elements The report required by subparagraph (A) shall\u2014 (i) identify and analyze acts, policies, or practices of foreign countries that constitute significant barriers to, or distortions of United States exports of specialty crops, including the imposition of\u2014 (I) tariffs (including retaliatory tariffs) and quotas (including tariff-rate quotas); and (II) nontariff barriers, including technical barriers to trade, sanitary and phytosanitary measures, import licensing procedures, and subsidies; (ii) make an estimate\u2014 (I) of the impacts on the competitiveness of United States exports of specialty crops of any act, policy, or practice identified under clause (i); and (II) if feasible, of the value of additional specialty crops that would, during the year preceding submission of the report, have been exported from the United States to each foreign country an act, policy, or practice of which is identified under clause (i) if each such act, policy, or practice of that country did not exist; (iii) assess the extent to which each act, policy, or practice identified under clause (i) is subject to international agreements to which the United States is a party; (iv) include information with respect to any action taken by the executive branch during the year preceding submission of the report, or expected to be taken after submission of the report, to eliminate any act, policy, or practice identified under clause (i), including\u2014 (I) any action under section 301; (II) negotiations or consultations with foreign governments, which may include engagement through the standing committee on sanitary and phytosanitary matters established under a free trade agreement to which the United States is a party; and (III) action at the World Trade Organization, including dispute settlement actions, consultations, or negotiations; and (v) a description of\u2014 (I) any funds provided under subsection (f)(3)(A)(iv) that were not obligated in the fiscal year preceding submission of the report; and (II) the reason such funds were not obligated. (C) Comment period Before preparing the report required by subparagraph (A), the Secretary, in coordination with the United States Trade Representative, shall\u2014 (i) seek comment from the public and the Agricultural Technical Advisory Committee for Trade in Fruits and Vegetables; and (ii) take such comments into account in preparing the report. (D) Form of report (i) In general The report required by subparagraph (A) shall be submitted in unclassified form, but may include a classified annex. (ii) Public availability The unclassified portion of the report required by subparagraph (A) shall be made available to the public in machine-readable format. .",
      "versionDate": "2026-02-25",
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
        "actionDate": "2026-02-25",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "3915",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Specialty CROP Act of 2026",
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
        "updateDate": "2026-03-17T18:21:33Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-02-25",
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
          "measure-id": "id119hr7670",
          "measure-number": "7670",
          "measure-type": "hr",
          "orig-publish-date": "2026-02-25",
          "originChamber": "HOUSE",
          "update-date": "2026-04-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr7670v00",
            "update-date": "2026-04-07"
          },
          "action-date": "2026-02-25",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Specialty Crops Reporting on Opportunities and Promotion Act of 2026 or the Specialty CROP Act of 2026</strong></p><p>This bill expands the annual\u00a0reporting requirements for the Technical Assistance for Specialty Crops program to require the Department of Agriculture\u00a0(USDA) to provide specific information on the competitiveness of U.S. exports of specialty crops.</p><p>Specifically, the bill modifies the requirements for\u00a0a congressionally mandated\u00a0annual report on U.S. specialty crop trade issues to require USDA to report specific information on acts, policies, and practices of foreign countries that constitute significant barriers to, or distortions of, U.S. exports of specialty crops.</p><p>Further, USDA must consult with the Office of the United States Trade Representative (USTR) on the report. Before preparing the report, USDA, in coordination with the USTR,\u00a0must seek comments from the public and the Agricultural Technical Advisory Committee for Trade in Fruits and Vegetables.</p><p>Under the bill, USDA must submit the report to Congress in an unclassified form, but may include a classified annex. The unclassified portion of the report must be publicly available.</p>"
        },
        "title": "Specialty CROP Act of 2026"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr7670.xml",
    "summary": {
      "actionDate": "2026-02-25",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Specialty Crops Reporting on Opportunities and Promotion Act of 2026 or the Specialty CROP Act of 2026</strong></p><p>This bill expands the annual\u00a0reporting requirements for the Technical Assistance for Specialty Crops program to require the Department of Agriculture\u00a0(USDA) to provide specific information on the competitiveness of U.S. exports of specialty crops.</p><p>Specifically, the bill modifies the requirements for\u00a0a congressionally mandated\u00a0annual report on U.S. specialty crop trade issues to require USDA to report specific information on acts, policies, and practices of foreign countries that constitute significant barriers to, or distortions of, U.S. exports of specialty crops.</p><p>Further, USDA must consult with the Office of the United States Trade Representative (USTR) on the report. Before preparing the report, USDA, in coordination with the USTR,\u00a0must seek comments from the public and the Agricultural Technical Advisory Committee for Trade in Fruits and Vegetables.</p><p>Under the bill, USDA must submit the report to Congress in an unclassified form, but may include a classified annex. The unclassified portion of the report must be publicly available.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hr7670"
    },
    "title": "Specialty CROP Act of 2026"
  },
  "summaries": [
    {
      "actionDate": "2026-02-25",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Specialty Crops Reporting on Opportunities and Promotion Act of 2026 or the Specialty CROP Act of 2026</strong></p><p>This bill expands the annual\u00a0reporting requirements for the Technical Assistance for Specialty Crops program to require the Department of Agriculture\u00a0(USDA) to provide specific information on the competitiveness of U.S. exports of specialty crops.</p><p>Specifically, the bill modifies the requirements for\u00a0a congressionally mandated\u00a0annual report on U.S. specialty crop trade issues to require USDA to report specific information on acts, policies, and practices of foreign countries that constitute significant barriers to, or distortions of, U.S. exports of specialty crops.</p><p>Further, USDA must consult with the Office of the United States Trade Representative (USTR) on the report. Before preparing the report, USDA, in coordination with the USTR,\u00a0must seek comments from the public and the Agricultural Technical Advisory Committee for Trade in Fruits and Vegetables.</p><p>Under the bill, USDA must submit the report to Congress in an unclassified form, but may include a classified annex. The unclassified portion of the report must be publicly available.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hr7670"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7670ih.xml"
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
      "title": "Specialty CROP Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-12T04:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Specialty CROP Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-12T04:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Specialty Crops Reporting on Opportunities and Promotion Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-12T04:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require a report on the competitiveness of United States exports of specialty crops.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-12T04:18:25Z"
    }
  ]
}
```
