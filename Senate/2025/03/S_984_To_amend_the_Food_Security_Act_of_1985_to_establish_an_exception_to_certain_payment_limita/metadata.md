# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/984?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/984
- Title: Fair Access to Agriculture Disaster Programs Act
- Congress: 119
- Bill type: S
- Bill number: 984
- Origin chamber: Senate
- Introduced date: 2025-03-12
- Update date: 2025-05-14T15:01:11Z
- Update date including text: 2025-05-14T15:01:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-12: Introduced in Senate
- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (Sponsor introductory remarks on measure: CR S1706)
- Latest action: 2025-03-12: Introduced in Senate

## Actions

- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (Sponsor introductory remarks on measure: CR S1706)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-12",
    "latestAction": {
      "actionDate": "2025-03-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/984",
    "number": "984",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "P000145",
        "district": "",
        "firstName": "Alex",
        "fullName": "Sen. Padilla, Alex [D-CA]",
        "lastName": "Padilla",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Fair Access to Agriculture Disaster Programs Act",
    "type": "S",
    "updateDate": "2025-05-14T15:01:11Z",
    "updateDateIncludingText": "2025-05-14T15:01:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-12",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (Sponsor introductory remarks on measure: CR S1706)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-12",
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
          "date": "2025-03-12T17:30:47Z",
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
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s984is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 984\nIN THE SENATE OF THE UNITED STATES\nMarch 12, 2025 Mr. Padilla (for himself and Mr. Tillis ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Food Security Act of 1985 to establish an exception to certain payment limitations in the case of person or legal entity that derives income from agriculture, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fair Access to Agriculture Disaster Programs Act .\n#### 2. Exception for income derived from agriculture\nSection 1001D(b) of the Food Security Act of 1985 (7 U.S.C. 1308\u20133a(b)) is amended\u2014\n**(1)**\nin paragraph (1), by striking paragraph (3) and inserting paragraphs (3) and (4) ; and\n**(2)**\nby adding at the end the following:\n(4) Exception (A) In general In the case of a payment or benefit described in subparagraph (B), the limitation established by paragraph (1) shall not apply to a person or legal entity during a crop, fiscal, or program year, as appropriate, if not less than 75 percent of the average adjusted gross income of the person or legal entity derives from farming, ranching, or silviculture activities, including agritourism, direct-to-consumer marketing of agricultural products, the sale of agricultural equipment owned by such person or entity, and other agriculture-related activities, as determined by the Secretary. (B) Payment or benefit described A payment or benefit referred to in subparagraph (A) is\u2014 (i) a payment or benefit under subtitle E of title I of the Agricultural Act of 2014 ( 7 U.S.C. 9081 ); or (ii) a payment or benefit under section 196 of the Federal Agriculture Improvement and Reform Act of 1996 ( 7 U.S.C. 7333 ). .",
      "versionDate": "2025-03-12",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2025-05-06T16:58:11Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-12",
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
          "measure-id": "id119s984",
          "measure-number": "984",
          "measure-type": "s",
          "orig-publish-date": "2025-03-12",
          "originChamber": "SENATE",
          "update-date": "2025-05-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s984v00",
            "update-date": "2025-05-14"
          },
          "action-date": "2025-03-12",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Fair Access to Agriculture Disaster Programs Act</strong></p><p>This bill waives the adjusted gross income limitations for payments or benefits under specific Department of Agriculture (USDA) disaster assistance programs for a person or legal entity that derives a portion of their income from agriculture. Currently, a person or entity is not eligible to receive certain benefits during a crop, fiscal, or program year if their average gross income exceeds $900,000.</p><p>Specifically, in the case of an excepted payment or benefit, the adjusted gross income limitation is waived if 75% or more of the average adjusted gross income for the person or entity is derived from farming, ranching, or silviculture activities. These activities include agritourism, direct-to-consumer marketing of agricultural products, and the sale of agricultural equipment owned by such person or entity.</p><p>The bill applies to the USDA</p><ul><li>Livestock Indemnity Program;</li><li>Livestock Forage Disaster Program;</li><li>Emergency Assistance for Livestock, Honey Bees, and Farm-Raised Fish Program;</li><li>Tree Assistance Program; and</li><li>Noninsured Crop Disaster Assistance Program.</li></ul>"
        },
        "title": "Fair Access to Agriculture Disaster Programs Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s984.xml",
    "summary": {
      "actionDate": "2025-03-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Fair Access to Agriculture Disaster Programs Act</strong></p><p>This bill waives the adjusted gross income limitations for payments or benefits under specific Department of Agriculture (USDA) disaster assistance programs for a person or legal entity that derives a portion of their income from agriculture. Currently, a person or entity is not eligible to receive certain benefits during a crop, fiscal, or program year if their average gross income exceeds $900,000.</p><p>Specifically, in the case of an excepted payment or benefit, the adjusted gross income limitation is waived if 75% or more of the average adjusted gross income for the person or entity is derived from farming, ranching, or silviculture activities. These activities include agritourism, direct-to-consumer marketing of agricultural products, and the sale of agricultural equipment owned by such person or entity.</p><p>The bill applies to the USDA</p><ul><li>Livestock Indemnity Program;</li><li>Livestock Forage Disaster Program;</li><li>Emergency Assistance for Livestock, Honey Bees, and Farm-Raised Fish Program;</li><li>Tree Assistance Program; and</li><li>Noninsured Crop Disaster Assistance Program.</li></ul>",
      "updateDate": "2025-05-14",
      "versionCode": "id119s984"
    },
    "title": "Fair Access to Agriculture Disaster Programs Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Fair Access to Agriculture Disaster Programs Act</strong></p><p>This bill waives the adjusted gross income limitations for payments or benefits under specific Department of Agriculture (USDA) disaster assistance programs for a person or legal entity that derives a portion of their income from agriculture. Currently, a person or entity is not eligible to receive certain benefits during a crop, fiscal, or program year if their average gross income exceeds $900,000.</p><p>Specifically, in the case of an excepted payment or benefit, the adjusted gross income limitation is waived if 75% or more of the average adjusted gross income for the person or entity is derived from farming, ranching, or silviculture activities. These activities include agritourism, direct-to-consumer marketing of agricultural products, and the sale of agricultural equipment owned by such person or entity.</p><p>The bill applies to the USDA</p><ul><li>Livestock Indemnity Program;</li><li>Livestock Forage Disaster Program;</li><li>Emergency Assistance for Livestock, Honey Bees, and Farm-Raised Fish Program;</li><li>Tree Assistance Program; and</li><li>Noninsured Crop Disaster Assistance Program.</li></ul>",
      "updateDate": "2025-05-14",
      "versionCode": "id119s984"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s984is.xml"
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
      "title": "Fair Access to Agriculture Disaster Programs Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-29T02:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fair Access to Agriculture Disaster Programs Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-29T02:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Food Security Act of 1985 to establish an exception to certain payment limitations in the case of person or legal entity that derives income from agriculture, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-29T02:19:12Z"
    }
  ]
}
```
