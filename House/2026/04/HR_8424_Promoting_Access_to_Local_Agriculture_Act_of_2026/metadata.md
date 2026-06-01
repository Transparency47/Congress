# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8424?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8424
- Title: Promoting Access to Local Agriculture Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8424
- Origin chamber: House
- Introduced date: 2026-04-21
- Update date: 2026-05-29T15:49:18Z
- Update date including text: 2026-05-29T15:49:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-04-21: Introduced in House
- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-21 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-04-21: Introduced in House

## Actions

- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-21 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-21",
    "latestAction": {
      "actionDate": "2026-04-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8424",
    "number": "8424",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "S001221",
        "district": "3",
        "firstName": "Hillary",
        "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
        "lastName": "Scholten",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Promoting Access to Local Agriculture Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-29T15:49:18Z",
    "updateDateIncludingText": "2026-05-29T15:49:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-21",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-21",
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
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-21",
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
          "date": "2026-04-21T14:00:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-04-21T14:00:05Z",
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
      "sponsorshipDate": "2026-04-21",
      "state": "CA"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "MI"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8424ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8424\nIN THE HOUSE OF REPRESENTATIVES\nApril 21, 2026 Ms. Scholten (for herself and Mr. Valadao ) introduced the following bill; which was referred to the Committee on Agriculture , and in addition to the Committee on Education and Workforce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require the Secretary of Agriculture to streamline applications from farmers to be vendors under certain nutrition programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Promoting Access to Local Agriculture Act of 2026 .\n#### 2. Streamlining applications for farmers\n##### (a) Definitions\nIn this section:\n**(1) Covered nutrition program**\nThe term covered nutrition program means\u2014\n**(A)**\nthe supplemental nutrition assistance program established under the Food and Nutrition Act of 2008 ( 7 U.S.C. 2011 et seq. );\n**(B)**\nthe senior farmers\u2019 market nutrition program established under section 4402 of the Farm Security and Rural Investment Act of 2002 ( 7 U.S.C. 3007 );\n**(C)**\nthe special supplemental nutrition program for women, infants, and children established by section 17 of the Child Nutrition Act of 1966 ( 42 U.S.C. 1786 ), including the farmers\u2019 market nutrition program under that program; and\n**(D)**\nthe Gus Schumacher Nutrition Incentive Program established under section 4405 of the Food, Conservation, and Energy Act of 2008 ( 7 U.S.C. 7517 ), as practicable with respect to the activities carried out by the Secretary under subsections (b) and (c).\n**(2) Secretary**\nThe term Secretary means the Secretary of Agriculture.\n##### (b) Streamlined application process\n**(1) In general**\nThe Secretary shall establish a streamlined application process\u2014\n**(A)**\nfor direct marketing farmers and ranchers to apply to be vendors under each of the covered nutrition programs; and\n**(B)**\nby\u2014\n**(i)**\ndeveloping a single application that a direct marketing farmer or rancher may use to apply to each of the covered nutrition programs; or\n**(ii)**\ndeveloping an information sharing system that\u2014\n**(I)**\nshares the information of a direct marketing farmer or rancher who is approved as an authorized vendor under a covered nutrition program with each of the other covered nutrition programs; and\n**(II)**\ndeems that direct marketing farmer or rancher as a prequalified eligible vendor for those other covered nutrition programs.\n**(2) Report**\nNot later than 1 year after the date of enactment of this Act, the Secretary shall submit to the Committee on Agriculture, Nutrition, and Forestry of the Senate and the Committee on Agriculture of the House of Representatives a report describing progress made in carrying out paragraph (1).\n##### (c) Streamlined processing of benefits\nThe Secretary shall establish a streamlined process for direct marketing farmers and ranchers that are vendors under any of the covered nutrition programs to process benefits under those programs through the use of standardized technology, such as a single piece of equipment or a mobile application.\n#### 3. Support for wireless and mobile equipment for certain entities\nSection 7(f)(2) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2016(f)(2) ) is amended\u2014\n**(1)**\nby redesignating subparagraph (C) as subparagraph (D); and\n**(2)**\nby inserting after subparagraph (B) the following:\n(C) Requirement The Secretary shall ensure that equipment or systems made available to entities described in clauses (i) and (ii) of subparagraph (B) by a State agency or an implementing partner of a State agency is appropriate for the entity, including, with respect to farmers markets and other direct-to-consumer markets, wireless or mobile processing equipment and technology systems. .",
      "versionDate": "2026-04-21",
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
        "actionDate": "2026-05-11",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "4483",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Promoting Access to Local Agriculture Act of 2026",
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
        "updateDate": "2026-05-04T20:34:46Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-04-21",
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
          "measure-id": "id119hr8424",
          "measure-number": "8424",
          "measure-type": "hr",
          "orig-publish-date": "2026-04-21",
          "originChamber": "HOUSE",
          "update-date": "2026-05-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr8424v00",
            "update-date": "2026-05-06"
          },
          "action-date": "2026-04-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Promoting Access to Local Agriculture Act of 2026</strong></p><p>This bill directs the Department of Agriculture (USDA) to establish a streamlined process for farmers and ranchers to provide benefits under certain federal nutrition programs. These programs include\u00a0the Supplemental Nutrition Assistance Program (SNAP); the Senior Farmers Market Nutrition Program (SFMNP); the Special Supplemental Nutrition Program for Women, Infants, and Children (WIC); and the Gus Schumacher Nutrition Incentive Program (GusNIP).</p><p>Specifically, USDA must establish a streamlined application process\u00a0for farmers and ranchers to apply to be vendors under the nutrition programs, including by developing a single application for the programs or an information sharing system. USDA must also develop a streamlined process for these vendors to use standardized technology\u00a0to process program benefits\u00a0(such as a single piece of equipment or a mobile application).</p><p>Further, USDA must ensure that the program benefit processing equipment and systems made available by a state agency are appropriate for the entity. For example, this includes ensuring wireless or mobile processing equipment and technology systems are appropriate\u00a0for farmers markets and other direct-to-consumer markets.</p>"
        },
        "title": "Promoting Access to Local Agriculture Act of 2026"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr8424.xml",
    "summary": {
      "actionDate": "2026-04-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Promoting Access to Local Agriculture Act of 2026</strong></p><p>This bill directs the Department of Agriculture (USDA) to establish a streamlined process for farmers and ranchers to provide benefits under certain federal nutrition programs. These programs include\u00a0the Supplemental Nutrition Assistance Program (SNAP); the Senior Farmers Market Nutrition Program (SFMNP); the Special Supplemental Nutrition Program for Women, Infants, and Children (WIC); and the Gus Schumacher Nutrition Incentive Program (GusNIP).</p><p>Specifically, USDA must establish a streamlined application process\u00a0for farmers and ranchers to apply to be vendors under the nutrition programs, including by developing a single application for the programs or an information sharing system. USDA must also develop a streamlined process for these vendors to use standardized technology\u00a0to process program benefits\u00a0(such as a single piece of equipment or a mobile application).</p><p>Further, USDA must ensure that the program benefit processing equipment and systems made available by a state agency are appropriate for the entity. For example, this includes ensuring wireless or mobile processing equipment and technology systems are appropriate\u00a0for farmers markets and other direct-to-consumer markets.</p>",
      "updateDate": "2026-05-06",
      "versionCode": "id119hr8424"
    },
    "title": "Promoting Access to Local Agriculture Act of 2026"
  },
  "summaries": [
    {
      "actionDate": "2026-04-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Promoting Access to Local Agriculture Act of 2026</strong></p><p>This bill directs the Department of Agriculture (USDA) to establish a streamlined process for farmers and ranchers to provide benefits under certain federal nutrition programs. These programs include\u00a0the Supplemental Nutrition Assistance Program (SNAP); the Senior Farmers Market Nutrition Program (SFMNP); the Special Supplemental Nutrition Program for Women, Infants, and Children (WIC); and the Gus Schumacher Nutrition Incentive Program (GusNIP).</p><p>Specifically, USDA must establish a streamlined application process\u00a0for farmers and ranchers to apply to be vendors under the nutrition programs, including by developing a single application for the programs or an information sharing system. USDA must also develop a streamlined process for these vendors to use standardized technology\u00a0to process program benefits\u00a0(such as a single piece of equipment or a mobile application).</p><p>Further, USDA must ensure that the program benefit processing equipment and systems made available by a state agency are appropriate for the entity. For example, this includes ensuring wireless or mobile processing equipment and technology systems are appropriate\u00a0for farmers markets and other direct-to-consumer markets.</p>",
      "updateDate": "2026-05-06",
      "versionCode": "id119hr8424"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-04-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8424ih.xml"
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
      "title": "Promoting Access to Local Agriculture Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-29T05:08:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Promoting Access to Local Agriculture Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-29T05:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Agriculture to streamline applications from farmers to be vendors under certain nutrition programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-29T05:03:42Z"
    }
  ]
}
```
