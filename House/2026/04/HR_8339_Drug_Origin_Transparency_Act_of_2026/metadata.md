# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8339?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8339
- Title: Drug Origin Transparency Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8339
- Origin chamber: House
- Introduced date: 2026-04-16
- Update date: 2026-04-30T18:17:10Z
- Update date including text: 2026-04-30T18:17:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-16: Introduced in House
- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-04-16: Introduced in House

## Actions

- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-16",
    "latestAction": {
      "actionDate": "2026-04-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8339",
    "number": "8339",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001163",
        "district": "7",
        "firstName": "Doris",
        "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
        "lastName": "Matsui",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Drug Origin Transparency Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-30T18:17:10Z",
    "updateDateIncludingText": "2026-04-30T18:17:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-16",
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
      "actionDate": "2026-04-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-16",
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
          "date": "2026-04-16T14:06:05Z",
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
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "TX"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "WA"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8339ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8339\nIN THE HOUSE OF REPRESENTATIVES\nApril 16, 2026 Ms. Matsui (for herself, Mr. Crenshaw , Ms. Schrier , and Mrs. Hinson ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act to enhance drug manufacturing amount information reporting, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Drug Origin Transparency Act of 2026 .\n#### 2. Enhanced drug manufacturing amount information reporting\n##### (a) In general\nSection 510(j)(3) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360(j)(3) ) is amended\u2014\n**(1)**\nin subparagraph (A), by adding or (2) after paragraph (1) ; and\n**(2)**\nby adding at the end the following:\n(C) Each report submitted pursuant to subparagraph (A) with respect to a drug shall\u2014 (i) include additional information as may be specified by the Secretary in regulation or guidance regarding the supply chain for such drug, such as\u2014 (I) the identity of the respective suppliers of each active pharmaceutical ingredient, active pharmaceutical ingredient intermediate, and in-process material used in such manufacture, preparation, propagation, compounding, or processing of the drug; and (II) the respective amounts of such drug that were manufactured, prepared, propagated, compounded, or processed using an active pharmaceutical ingredient, active pharmaceutical ingredient intermediate, and in-process material from each such identified supplier; and (ii) be submitted more frequently than annually, in accordance with a reporting schedule as may be specified by the Secretary in such regulation or guidance, but not more frequently than 4 times per year. (D) Any additional information specified in regulation or guidance pursuant to subparagraph (C) shall be a required element of reports under this paragraph not earlier than 6 months after the date on which such regulation or guidance is issued in final form (and in no event shall the absence of any regulation or guidance issued under subparagraph (C) affect the requirement to report as described in subparagraph (A)). .\n##### (b) Conforming amendment\nSection 510(j)(3)(B) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 510(j)(3)(B) ) is amended by striking subparagraph (A) and inserting this paragraph .\n#### 3. Require drug labeling to include original manufacturer and supply chain information\nSection 502 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 352 ) is amended\u2014\n**(1)**\nin paragraph (b)\u2014\n**(A)**\nby striking (b) If in a package and inserting (b)(1) If in a package ;\n**(B)**\nby striking a label containing (1) the name and place and inserting\na label containing\u2014 (A) the name and place ;\n**(C)**\nby striking or distributor; and (2) an accurate statement and inserting\nor distributor; and (B) an accurate statement ;\n**(D)**\nby striking under clause (2) of this paragraph and inserting under this clause ; and\n**(E)**\nby inserting at the end the following:\n(2) (A) Subject to clause (C), if it is a drug, including an active pharmaceutical ingredient, unless it bears a label containing the name and place of business, and unique facility identifier of the original manufacturer of such drug or active pharmaceutical ingredient, except that the Secretary may provide, by regulation, for reasonable variations in the implementation of such labeling requirements. (B) Subject to clause (C), if it is a drug that is an active pharmaceutical ingredient, unless any accompanying certificate of analysis contains the name and place of business, and unique facility identifier of the original manufacturer of the active pharmaceutical ingredient. (C) The Secretary may provide, by regulation, for reasonable variations in the implementation of labeling requirements specified in this subparagraph. ; and\n**(2)**\nby inserting after paragraph (c) the following:\n(d) (1) Subject to subparagraph (2), if it is a drug, including an active pharmaceutical ingredient, unless it bears labeling containing the name and place of business of\u2014 (A) the original manufacturer of each active pharmaceutical ingredient; (B) each manufacturer, if different from the original manufacturer; and (C) the packer or distributor, if any. (2) The Secretary may provide, by regulation, for reasonable variations or an alternative placement for the labeling requirements specified in subparagraph (1), including by electronic means. .",
      "versionDate": "2026-04-16",
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
        "updateDate": "2026-04-30T18:17:10Z"
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
      "date": "2026-04-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8339ih.xml"
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
      "title": "Drug Origin Transparency Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-23T09:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Drug Origin Transparency Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-23T09:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Food, Drug, and Cosmetic Act to enhance drug manufacturing amount information reporting, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-23T09:33:34Z"
    }
  ]
}
```
