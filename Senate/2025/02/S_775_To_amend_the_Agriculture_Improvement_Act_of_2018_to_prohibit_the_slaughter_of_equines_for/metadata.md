# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/775?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/775
- Title: SAFE Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 775
- Origin chamber: Senate
- Introduced date: 2025-02-27
- Update date: 2026-05-15T11:03:24Z
- Update date including text: 2026-05-15T11:03:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in Senate
- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-02-27: Introduced in Senate

## Actions

- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/775",
    "number": "775",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "G000359",
        "district": "",
        "firstName": "Lindsey",
        "fullName": "Sen. Graham, Lindsey [R-SC]",
        "lastName": "Graham",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "SAFE Act of 2025",
    "type": "S",
    "updateDate": "2026-05-15T11:03:24Z",
    "updateDateIncludingText": "2026-05-15T11:03:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-27",
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
      "actionDate": "2025-02-27",
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
            "date": "2025-02-27T17:05:41Z",
            "name": "Referred To"
          },
          {
            "date": "2025-02-27T17:05:41Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "NM"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "ME"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "LA"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "PA"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "FL"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "RI"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "OR"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s775is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 775\nIN THE SENATE OF THE UNITED STATES\nFebruary 27, 2025 Mr. Graham (for himself and Mr. Luj\u00e1n ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Agriculture Improvement Act of 2018 to prohibit the slaughter of equines for human consumption.\n#### 1. Short title\nThis Act may be cited as the Save America\u2019s Forgotten Equines Act of 2025 or the SAFE Act of 2025 .\n#### 2. Prohibition on slaughter of equines for human consumption\nSection 12515 of the Agriculture Improvement Act of 2018 ( 7 U.S.C. 2160 ) is amended\u2014\n**(1)**\nin the section heading, by striking dogs and cats and inserting dogs, cats, and equines ; and\n**(2)**\nin subsection (a), by striking a dog or cat each place it appears and inserting a dog, cat, or equine .",
      "versionDate": "2025-02-27",
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
        "actionDate": "2025-03-28",
        "text": "Referred to the Subcommittee on Livestock, Dairy, and Poultry."
      },
      "number": "1661",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "SAFE Act of 2025",
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
        "updateDate": "2025-03-28T15:18:08Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-27",
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
          "measure-id": "id119s775",
          "measure-number": "775",
          "measure-type": "s",
          "orig-publish-date": "2025-02-27",
          "originChamber": "SENATE",
          "update-date": "2025-03-31"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s775v00",
            "update-date": "2025-03-31"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Save America's Forgotten Equines Act of 2025 or the SAFE Act of 2025</strong></p><p>This bill permanently prohibits the slaughter of equines (e.g., horses and mules) for human consumption.\u00a0(Current law prohibits the slaughter of dogs and cats for human consumption. This bill extends the prohibition to equines.)\u00a0</p><p>Specifically, this bill prohibits a person from knowingly (1)\u00a0slaughtering an equine for human consumption; or\u00a0(2) shipping, transporting, possessing, purchasing, selling, or donating an equine to be slaughtered for human consumption or equine parts for human consumption.</p><p>The bill subjects a violator to a fine.</p><p>The bill applies to conduct in or affecting interstate or foreign commerce or within the special maritime and territorial jurisdiction of the United States. However, it does not apply to an activity carried out by an Indian for a religious ceremony.</p><p>As background, in recent years, the appropriations acts have prohibited the Department of Agriculture (USDA) from using federal funds to inspect horses before they are slaughtered for human consumption. Therefore, there are currently no USDA-inspected horse slaughter facilities in the United States.</p>"
        },
        "title": "SAFE Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s775.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Save America's Forgotten Equines Act of 2025 or the SAFE Act of 2025</strong></p><p>This bill permanently prohibits the slaughter of equines (e.g., horses and mules) for human consumption.\u00a0(Current law prohibits the slaughter of dogs and cats for human consumption. This bill extends the prohibition to equines.)\u00a0</p><p>Specifically, this bill prohibits a person from knowingly (1)\u00a0slaughtering an equine for human consumption; or\u00a0(2) shipping, transporting, possessing, purchasing, selling, or donating an equine to be slaughtered for human consumption or equine parts for human consumption.</p><p>The bill subjects a violator to a fine.</p><p>The bill applies to conduct in or affecting interstate or foreign commerce or within the special maritime and territorial jurisdiction of the United States. However, it does not apply to an activity carried out by an Indian for a religious ceremony.</p><p>As background, in recent years, the appropriations acts have prohibited the Department of Agriculture (USDA) from using federal funds to inspect horses before they are slaughtered for human consumption. Therefore, there are currently no USDA-inspected horse slaughter facilities in the United States.</p>",
      "updateDate": "2025-03-31",
      "versionCode": "id119s775"
    },
    "title": "SAFE Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Save America's Forgotten Equines Act of 2025 or the SAFE Act of 2025</strong></p><p>This bill permanently prohibits the slaughter of equines (e.g., horses and mules) for human consumption.\u00a0(Current law prohibits the slaughter of dogs and cats for human consumption. This bill extends the prohibition to equines.)\u00a0</p><p>Specifically, this bill prohibits a person from knowingly (1)\u00a0slaughtering an equine for human consumption; or\u00a0(2) shipping, transporting, possessing, purchasing, selling, or donating an equine to be slaughtered for human consumption or equine parts for human consumption.</p><p>The bill subjects a violator to a fine.</p><p>The bill applies to conduct in or affecting interstate or foreign commerce or within the special maritime and territorial jurisdiction of the United States. However, it does not apply to an activity carried out by an Indian for a religious ceremony.</p><p>As background, in recent years, the appropriations acts have prohibited the Department of Agriculture (USDA) from using federal funds to inspect horses before they are slaughtered for human consumption. Therefore, there are currently no USDA-inspected horse slaughter facilities in the United States.</p>",
      "updateDate": "2025-03-31",
      "versionCode": "id119s775"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s775is.xml"
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
      "title": "SAFE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-15T11:03:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SAFE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Save America\u2019s Forgotten Equines Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Agriculture Improvement Act of 2018 to prohibit the slaughter of equines for human consumption.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:03:59Z"
    }
  ]
}
```
