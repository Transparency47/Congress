# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4067?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4067
- Title: Land Grant Research Prioritization Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4067
- Origin chamber: Senate
- Introduced date: 2026-03-11
- Update date: 2026-04-06T13:14:01Z
- Update date including text: 2026-04-06T13:14:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-03-11: Introduced in Senate
- 2026-03-11 - IntroReferral: Introduced in Senate
- 2026-03-11 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2026-03-11: Introduced in Senate

## Actions

- 2026-03-11 - IntroReferral: Introduced in Senate
- 2026-03-11 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-11",
    "latestAction": {
      "actionDate": "2026-03-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4067",
    "number": "4067",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "O000174",
        "district": "",
        "firstName": "Jon",
        "fullName": "Sen. Ossoff, Jon [D-GA]",
        "lastName": "Ossoff",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Land Grant Research Prioritization Act of 2026",
    "type": "S",
    "updateDate": "2026-04-06T13:14:01Z",
    "updateDateIncludingText": "2026-04-06T13:14:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-11",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-11",
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
        "item": {
          "date": "2026-03-11T22:58:51Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2026-03-11",
      "state": "FL"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2026-03-11",
      "state": "GA"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-03-11",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4067is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4067\nIN THE SENATE OF THE UNITED STATES\nMarch 11, 2026 Mr. Ossoff (for himself, Mrs. Moody , Mr. Warnock , and Mr. Scott of Florida ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Food, Agriculture, Conservation, and Trade Act of 1990 to establish research and extension grant priorities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Land Grant Research Prioritization Act of 2026 .\n#### 2. Research and extension priorities\nSection 1672(d) of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 5925(d) ) is amended by adding at the end the following:\n(21) Advanced mechanized harvester technologies research and extension (A) In general Research and extension grants may be made under this section for the purpose of developing and evaluating technologies to mechanize agricultural processes. (B) Emphasis In awarding grants under subparagraph (A), the Secretary may place emphasis on mechanizing the process for harvesting specialty crops. (22) Agricultural application of artificial intelligence research and extension (A) In general Research and extension grants may be made under this section for the purpose of developing and evaluating agricultural uses of artificial intelligence. (B) Emphasis In awarding grants under subparagraph (A), the Secretary may place emphasis on uses of artificial intelligence that improve specialty crop production. (23) Invasive species research and extension Research and extension grants may be made under this section for the purpose of supporting research projects at land-grant colleges and universities (as defined in section 1404 of the National Agricultural Research, Extension, and Teaching Policy Act of 1977 ( 7 U.S.C. 3103 )) to develop and apply methods to manage and eradicate invasive species of plants and animals, including through methods of biocontrol. (24) Aquaculture research and extension Research and extension grants may be made under this section for the purpose of supporting research projects at land-grant colleges and universities (as defined in section 1404 of the National Agricultural Research, Extension, and Teaching Policy Act of 1977 ( 7 U.S.C. 3103 )) to develop and apply aquaculture methods, including through the propagation and rearing of economically and ecologically valuable aquatic and marine species. .",
      "versionDate": "2026-03-11",
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
        "actionDate": "2026-02-26",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "7734",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Land Grant Research Prioritization Act of 2026",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-03-27T21:28:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-03-11",
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
          "measure-id": "id119s4067",
          "measure-number": "4067",
          "measure-type": "s",
          "orig-publish-date": "2026-03-11",
          "originChamber": "SENATE",
          "update-date": "2026-04-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s4067v00",
            "update-date": "2026-04-06"
          },
          "action-date": "2026-03-11",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Land Grant Research Prioritization Act of 2026</strong></p><p>This bill includes additional priorities as Department of Agriculture (USDA) high-priority research and extension areas.</p><p>Under the bill, USDA may award\u00a0grants for developing and evaluating (1) technologies to mechanize agricultural processes (and may emphasize processes for harvesting specialty crops), and (2) agricultural uses of artificial intelligence (and may emphasize uses for improving specialty crop production).</p><p>Further, USDA may award grants\u00a0to support research projects at land-grant colleges and universities to develop and apply</p><ul><li>methods to manage and eradicate invasive species of plants and animals, including through methods of biocontrol; and</li><li>aquaculture methods, including through the propagation and rearing of economically and ecologically valuable aquatic and marine species.\u00a0</li></ul>"
        },
        "title": "Land Grant Research Prioritization Act of 2026"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s4067.xml",
    "summary": {
      "actionDate": "2026-03-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Land Grant Research Prioritization Act of 2026</strong></p><p>This bill includes additional priorities as Department of Agriculture (USDA) high-priority research and extension areas.</p><p>Under the bill, USDA may award\u00a0grants for developing and evaluating (1) technologies to mechanize agricultural processes (and may emphasize processes for harvesting specialty crops), and (2) agricultural uses of artificial intelligence (and may emphasize uses for improving specialty crop production).</p><p>Further, USDA may award grants\u00a0to support research projects at land-grant colleges and universities to develop and apply</p><ul><li>methods to manage and eradicate invasive species of plants and animals, including through methods of biocontrol; and</li><li>aquaculture methods, including through the propagation and rearing of economically and ecologically valuable aquatic and marine species.\u00a0</li></ul>",
      "updateDate": "2026-04-06",
      "versionCode": "id119s4067"
    },
    "title": "Land Grant Research Prioritization Act of 2026"
  },
  "summaries": [
    {
      "actionDate": "2026-03-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Land Grant Research Prioritization Act of 2026</strong></p><p>This bill includes additional priorities as Department of Agriculture (USDA) high-priority research and extension areas.</p><p>Under the bill, USDA may award\u00a0grants for developing and evaluating (1) technologies to mechanize agricultural processes (and may emphasize processes for harvesting specialty crops), and (2) agricultural uses of artificial intelligence (and may emphasize uses for improving specialty crop production).</p><p>Further, USDA may award grants\u00a0to support research projects at land-grant colleges and universities to develop and apply</p><ul><li>methods to manage and eradicate invasive species of plants and animals, including through methods of biocontrol; and</li><li>aquaculture methods, including through the propagation and rearing of economically and ecologically valuable aquatic and marine species.\u00a0</li></ul>",
      "updateDate": "2026-04-06",
      "versionCode": "id119s4067"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4067is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Food, Agriculture, Conservation, and Trade Act of 1990 to establish research and extension grant priorities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-24T05:18:29Z"
    },
    {
      "title": "Land Grant Research Prioritization Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-24T05:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Land Grant Research Prioritization Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-24T05:08:18Z"
    }
  ]
}
```
