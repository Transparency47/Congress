# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5111?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5111
- Title: CRP Improvement and Flexibility Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5111
- Origin chamber: House
- Introduced date: 2025-09-03
- Update date: 2026-05-16T08:07:53Z
- Update date including text: 2026-05-16T08:07:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-03: Introduced in House
- 2025-09-03 - IntroReferral: Introduced in House
- 2025-09-03 - IntroReferral: Introduced in House
- 2025-09-03 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.
- Latest action: 2025-09-03: Introduced in House

## Actions

- 2025-09-03 - IntroReferral: Introduced in House
- 2025-09-03 - IntroReferral: Introduced in House
- 2025-09-03 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-03",
    "latestAction": {
      "actionDate": "2025-09-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5111",
    "number": "5111",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "C001059",
        "district": "21",
        "firstName": "Jim",
        "fullName": "Rep. Costa, Jim [D-CA-21]",
        "lastName": "Costa",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "CRP Improvement and Flexibility Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:53Z",
    "updateDateIncludingText": "2026-05-16T08:07:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Conservation, Research, and Biotechnology.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-03",
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
      "actionDate": "2025-09-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-03",
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
          "date": "2025-09-03T14:00:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-13T19:53:21Z",
              "name": "Referred to"
            }
          },
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
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
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "IA"
    },
    {
      "bioguideId": "J000301",
      "district": "0",
      "firstName": "Dusty",
      "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2026-01-22",
      "state": "SD"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5111ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5111\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 3, 2025 Mr. Costa (for himself and Mr. Feenstra ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food Security Act of 1985 to improve the conservation reserve program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the CRP Improvement and Flexibility Act of 2025 .\n#### 2. Conservation reserve program improvements\n##### (a) State acres for wildlife enhancement continuous enrollment\nSection 1231(d)(6)(A)(i) of the Food Security Act of 1985 ( 16 U.S.C. 3831(d)(6)(A)(i) ) is amended\u2014\n**(1)**\nin subclause (II), by striking and at the end; and\n**(2)**\nby adding at the end the following:\n(IV) land that will be enrolled under the State acres for wildlife enhancement practice established by the Secretary; and .\n##### (b) Emergency haying during the primary nesting season; conditions on haying and grazing\nSection 1233(b) of the Food Security Act of 1985 ( 16 U.S.C. 3833(b) ) is amended\u2014\n**(1)**\nin paragraph (1)(B)(i)\u2014\n**(A)**\nby redesignating subclauses (I) through (VI) as subclauses (II) through (VII), respectively;\n**(B)**\nby inserting before subclause (II) (as so redesignated) the following:\n(I) emergency haying in response to a localized or regional drought, flooding, wildfire, or other emergency, on all practices, during the final 2 weeks of, and outside of, the primary nesting season, on not more than 50 percent of contract acres, as identified in the site-specific plan, when\u2014 (aa) the county is designated as D2 (severe drought) or greater according to the United States Drought Monitor; (bb) there is at least a 40 percent loss in forage production in the county; or (cc) the Secretary, in coordination with the State technical committee, determines that the program can assist in the response to a natural disaster event without permanent damage to the established cover; ;\n**(C)**\nin subclause (II) (as so redesignated), in the matter preceding item (aa), by striking emergency haying, emergency grazing, or other emergency use and inserting emergency grazing or other emergency use ; and\n**(D)**\nin subclause (III) (as so redesignated), by striking payments and inserting the conditions described in item (aa), (bb), or (cc) of subclause (I) are met or payments ; and\n**(2)**\nin paragraph (2)(B)\u2014\n**(A)**\nby redesignating clause (ii) as clause (iii); and\n**(B)**\nby inserting after clause (i) the following:\n(ii) Damage to cover for wildlife populations Haying or grazing described in paragraph (1) shall not be permitted on land subject to a contract under the conservation reserve program, or under a particular practice, if haying or grazing during the final 2 weeks of the primary nesting season under that practice, as applicable, would cause long-term damage to vegetative cover for wildlife populations supported by the applicable practice on that land. .\n##### (c) Cost sharing payments for establishment of grazing infrastructure\n**(1) Cost sharing payments; other Federal cost share assistance**\nSection 1234(b) of the Food Security Act of 1985 ( 16 U.S.C. 3834(b) ) is amended\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby striking establishing water and inserting the following: \u201cestablishing\u2014\n(A) water ;\n**(ii)**\nin subparagraph (A) (as so designated), by striking the period at the end and inserting ; and ; and\n**(iii)**\nby adding at the end the following:\n(B) grazing infrastructure, including interior cross fencing, perimeter fencing, and water infrastructure (such as rural water connections, water wells, pipelines, and water tanks), under each contract, for all practices, if grazing is included in the conservation plan and addresses a resource concern. ; and\n**(B)**\nin paragraph (3), by striking land and inserting activities required by the contract entered into under this subchapter .\n**(2) Reenrollment of land with grazing infrastructure**\nSection 1231(h) of the Food Security Act of 1985 ( 16 U.S.C. 3831(h) ) is amended by adding at the end the following:\n(3) Land with grazing infrastructure On the expiration of a contract entered into under this subchapter that covers land that includes grazing infrastructure established with cost sharing assistance under section 1234(b)(1)(B)\u2014 (A) the Secretary shall consider that land to be planted for purposes of subsection (b)(1)(B); and (B) that land shall be eligible for reenrollment in the conservation reserve, subject to the requirements of this subchapter. .\n##### (d) Mid-Contract management for activities not relating to haying or grazing\n**(1) Definition of management**\nSection 1232(a)(5) of the Food Security Act of 1985 ( 16 U.S.C. 3832(a)(5) ) is amended by inserting (as defined in section 1231A(a)) after management .\n**(2) Management payments**\nSection 1234(b)(2) of the Food Security Act of 1985 ( 16 U.S.C. 3834(b)(2) ) is amended by striking subparagraph (B) and inserting the following:\n(B) Management payments The Secretary shall make cost sharing payments to an owner or operator under this subchapter for any management activity described in section 1232(a)(5), except for those management activities relating to haying or grazing. .\n##### (e) Payment limitation for rental payments\nSection 1234(g)(1) of the Food Security Act of 1985 ( 16 U.S.C. 3834(g)(1) ) is amended by striking $50,000 and inserting $125,000 .",
      "versionDate": "2025-09-03",
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
        "actionDate": "2025-07-31",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S4999)"
      },
      "number": "2608",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "CRP Improvement and Flexibility Act of 2025",
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
        "updateDate": "2025-09-11T15:38:36Z"
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
      "date": "2025-09-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5111ih.xml"
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
      "title": "CRP Improvement and Flexibility Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-06T07:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CRP Improvement and Flexibility Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-06T07:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food Security Act of 1985 to improve the conservation reserve program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-06T07:33:34Z"
    }
  ]
}
```
