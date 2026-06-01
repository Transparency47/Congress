# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1951?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1951
- Title: Strengthening Rural Cooperatives and Communities Act
- Congress: 119
- Bill type: HR
- Bill number: 1951
- Origin chamber: House
- Introduced date: 2025-03-06
- Update date: 2025-07-28T16:48:28Z
- Update date including text: 2025-07-28T16:48:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-06: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-03-28 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.
- Latest action: 2025-03-06: Introduced in House

## Actions

- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-03-28 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1951",
    "number": "1951",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "R000622",
        "district": "19",
        "firstName": "Josh",
        "fullName": "Rep. Riley, Josh [D-NY-19]",
        "lastName": "Riley",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Strengthening Rural Cooperatives and Communities Act",
    "type": "HR",
    "updateDate": "2025-07-28T16:48:28Z",
    "updateDateIncludingText": "2025-07-28T16:48:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-28",
      "committees": {
        "item": {
          "name": "Commodity Markets, Digital Assets, and Rural Development Subcommittee",
          "systemCode": "hsag22"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-06",
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
      "actionDate": "2025-03-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-06",
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
          "date": "2025-03-06T14:00:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-28T20:52:16Z",
              "name": "Referred to"
            }
          },
          "name": "Commodity Markets, Digital Assets, and Rural Development Subcommittee",
          "systemCode": "hsag22"
        }
      },
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
      "sponsorshipDate": "2025-03-06",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1951ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1951\nIN THE HOUSE OF REPRESENTATIVES\nMarch 6, 2025 Mr. Riley of New York (for himself and Mr. Valadao ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Consolidated Farm and Rural Development Act to reauthorize rural cooperative development grants.\n#### 1. Short title\nThis Act may be cited as the Strengthening Rural Cooperatives and Communities Act .\n#### 2. Reauthorization of rural cooperative development grants\nSection 310B(e) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1932(e) ) is amended\u2014\n**(1)**\nin paragraph (1), by adding at the end the following:\n(C) Cooperative development The term cooperative development means activities including outreach, education, training, and technical assistance, to support the startup, expansion, or ongoing sustainability of new and existing cooperatives. ;\n**(2)**\nin paragraph (4), by inserting , and award maximum points in scoring criteria to applicants that satisfy the requirements of paragraph (5)(F), before if the plan ;\n**(3)**\nin paragraph (5), by striking subparagraph (D) and inserting the following:\n(D) commit to providing technical assistance and other services to socially vulnerable, underserved, or distressed communities; ;\n**(4)**\nin paragraph (6)(B), by striking If the Secretary determines it to be in the best interest of the program, the and inserting The ;\n**(5)**\nin paragraph (10), by adding at the end the following: The Secretary shall analyze the data resulting from the research, and include the data and the analysis in the annual report submitted by the interagency working group under paragraph (12). ;\n**(6)**\nin paragraph (12), by adding at the end the following: Not later than 180 days after the date of the enactment of this sentence and annually thereafter, the interagency working group shall submit to the Congress a report describing the activities carried out by the working group. ; and\n**(7)**\nin paragraph (13), by striking 2014 through 2023 and inserting 2025 through 2029 .",
      "versionDate": "2025-03-06",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-04-29T15:39:26Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-06",
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
          "measure-id": "id119hr1951",
          "measure-number": "1951",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-06",
          "originChamber": "HOUSE",
          "update-date": "2025-07-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1951v00",
            "update-date": "2025-07-28"
          },
          "action-date": "2025-03-06",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Strengthening Rural Cooperatives and Communities Act</strong></p><p>This bill reauthorizes through FY2029 and modifies the Rural Cooperative Development Grant (RCDG) Program. This Department of Agriculture (USDA) program provides grants to nonprofit institutions to help individuals and businesses start, expand, or improve rural cooperatives and other mutually-owned businesses through Rural Cooperative Development Centers.</p><p>USDA must give preference to grants that commit to providing technical assistance and other services to socially vulnerable,\u00a0underserved, or distressed communities. Under current law,\u00a0USDA must give preference to underserved and economically distressed areas in rural areas.</p><p>In addition, USDA may give an additional\u00a0preference to applications that commit to providing a 25% matching contribution for the center with private funds and in-kind contributions.\u00a0Specifically, USDA\u00a0may\u00a0award the maximum points in application scoring criteria to applicants that satisfy this requirement.</p><p>Under the bill, cooperative development includes activities (e.g., outreach, education, training, and technical assistance) to support the startup, expansion, or ongoing sustainability of new and existing cooperatives. Current law does not define cooperative development.</p><p>The bill directs the RCDG interagency working group to submit an annual report to Congress on its activities.</p><p>Finally, the program currently includes cooperative research program requirements to collect data on the effects of all types of cooperatives on the national economy. Under the bill, USDA must analyze the data resulting from the research and include the data and analysis in the annual report to Congress.</p>"
        },
        "title": "Strengthening Rural Cooperatives and Communities Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1951.xml",
    "summary": {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Strengthening Rural Cooperatives and Communities Act</strong></p><p>This bill reauthorizes through FY2029 and modifies the Rural Cooperative Development Grant (RCDG) Program. This Department of Agriculture (USDA) program provides grants to nonprofit institutions to help individuals and businesses start, expand, or improve rural cooperatives and other mutually-owned businesses through Rural Cooperative Development Centers.</p><p>USDA must give preference to grants that commit to providing technical assistance and other services to socially vulnerable,\u00a0underserved, or distressed communities. Under current law,\u00a0USDA must give preference to underserved and economically distressed areas in rural areas.</p><p>In addition, USDA may give an additional\u00a0preference to applications that commit to providing a 25% matching contribution for the center with private funds and in-kind contributions.\u00a0Specifically, USDA\u00a0may\u00a0award the maximum points in application scoring criteria to applicants that satisfy this requirement.</p><p>Under the bill, cooperative development includes activities (e.g., outreach, education, training, and technical assistance) to support the startup, expansion, or ongoing sustainability of new and existing cooperatives. Current law does not define cooperative development.</p><p>The bill directs the RCDG interagency working group to submit an annual report to Congress on its activities.</p><p>Finally, the program currently includes cooperative research program requirements to collect data on the effects of all types of cooperatives on the national economy. Under the bill, USDA must analyze the data resulting from the research and include the data and analysis in the annual report to Congress.</p>",
      "updateDate": "2025-07-28",
      "versionCode": "id119hr1951"
    },
    "title": "Strengthening Rural Cooperatives and Communities Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Strengthening Rural Cooperatives and Communities Act</strong></p><p>This bill reauthorizes through FY2029 and modifies the Rural Cooperative Development Grant (RCDG) Program. This Department of Agriculture (USDA) program provides grants to nonprofit institutions to help individuals and businesses start, expand, or improve rural cooperatives and other mutually-owned businesses through Rural Cooperative Development Centers.</p><p>USDA must give preference to grants that commit to providing technical assistance and other services to socially vulnerable,\u00a0underserved, or distressed communities. Under current law,\u00a0USDA must give preference to underserved and economically distressed areas in rural areas.</p><p>In addition, USDA may give an additional\u00a0preference to applications that commit to providing a 25% matching contribution for the center with private funds and in-kind contributions.\u00a0Specifically, USDA\u00a0may\u00a0award the maximum points in application scoring criteria to applicants that satisfy this requirement.</p><p>Under the bill, cooperative development includes activities (e.g., outreach, education, training, and technical assistance) to support the startup, expansion, or ongoing sustainability of new and existing cooperatives. Current law does not define cooperative development.</p><p>The bill directs the RCDG interagency working group to submit an annual report to Congress on its activities.</p><p>Finally, the program currently includes cooperative research program requirements to collect data on the effects of all types of cooperatives on the national economy. Under the bill, USDA must analyze the data resulting from the research and include the data and analysis in the annual report to Congress.</p>",
      "updateDate": "2025-07-28",
      "versionCode": "id119hr1951"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1951ih.xml"
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
      "title": "Strengthening Rural Cooperatives and Communities Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-22T05:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Strengthening Rural Cooperatives and Communities Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-22T05:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Consolidated Farm and Rural Development Act to reauthorize rural cooperative development grants.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-22T05:48:27Z"
    }
  ]
}
```
