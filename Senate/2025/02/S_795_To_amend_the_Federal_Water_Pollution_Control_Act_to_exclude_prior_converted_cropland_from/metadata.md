# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/795?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/795
- Title: Farmers Freedom Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 795
- Origin chamber: Senate
- Introduced date: 2025-02-27
- Update date: 2026-03-02T20:19:53Z
- Update date including text: 2026-03-02T20:19:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in Senate
- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-02-27: Introduced in Senate

## Actions

- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/795",
    "number": "795",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "R000605",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Rounds, Mike [R-SD]",
        "lastName": "Rounds",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "Farmers Freedom Act of 2025",
    "type": "S",
    "updateDate": "2026-03-02T20:19:53Z",
    "updateDateIncludingText": "2026-03-02T20:19:53Z"
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
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
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
        "item": {
          "date": "2025-02-27T18:49:28Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "WY"
    },
    {
      "bioguideId": "T000250",
      "firstName": "John",
      "fullName": "Sen. Thune, John [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Thune",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "SD"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "ND"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "KS"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-04-11",
      "state": "IA"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-04-11",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s795is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 795\nIN THE SENATE OF THE UNITED STATES\nFebruary 27, 2025 Mr. Rounds (for himself, Mr. Barrasso , Mr. Thune , Mr. Hoeven , and Mr. Marshall ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo amend the Federal Water Pollution Control Act to exclude prior converted cropland from the definition of navigable waters , and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Farmers Freedom Act of 2025 .\n#### 2. Prior converted cropland\n##### (a) In general\nSection 502 of the Federal Water Pollution Control Act ( 33 U.S.C. 1362 ) is amended by striking paragraph (7) and inserting the following:\n(7) Navigable waters (A) In general The term navigable waters means the waters of the United States, including the territorial seas. (B) Exclusion The term navigable waters does not include prior converted cropland. (C) Associated definitions For purposes of this paragraph: (i) Abandoned The term abandoned , with respect to an area that was prior converted cropland, means that the area was not used for, or in support of, agricultural purposes at least once in the immediately preceding 5-year period, as determined by the Administrator. (ii) Agricultural purpose The term agricultural purpose includes land use that makes the production of an agricultural product possible, including\u2014 (I) grazing and haying; (II) idling land for conservation use, such as habitat management, pollinator and wildlife management, water storage and supply management, and flood management; (III) irrigation tailwater storage; (IV) farm-raised fish production; (V) cranberry bogs; (VI) nutrient retention; and (VII) idling land for soil recovery after natural disasters such as hurricanes and drought. (iii) Prior converted cropland (I) In general The term prior converted cropland means any area that, prior to December 23, 1985, was drained or otherwise manipulated for the purpose, or having the effect, of making production of an agricultural product possible, including such areas that are designated as prior converted cropland by the Secretary of Agriculture. (II) Exclusion The term prior converted cropland does not include an area that is abandoned and has reverted to wetlands. (iv) Wetlands The term wetlands means an area that is inundated or saturated by surface or ground water at a frequency and duration sufficient to support, and that under normal circumstances do support, a prevalence of vegetation typically adapted for life in saturated soil conditions, including swamps, marshes, bogs, and similar areas. .\n##### (b) Prohibition on change in use policy\nIn carrying out the amendments made by this section, the Administrator of the Environmental Protection Agency and the Secretary of the Army, acting through the Chief of Engineers, may not, with respect to prior converted cropland, carry out the change in use policy described in the final rule of the Environmental Protection Agency and the Corps of Engineers entitled Revised Definition of Waters of the United States (88 Fed. Reg. 3004 (January 18, 2023)) or a substantially similar policy.",
      "versionDate": "2025-02-27",
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
        "name": "Environmental Protection",
        "updateDate": "2025-03-28T11:22:46Z"
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
          "measure-id": "id119s795",
          "measure-number": "795",
          "measure-type": "s",
          "orig-publish-date": "2025-02-27",
          "originChamber": "SENATE",
          "update-date": "2026-03-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s795v00",
            "update-date": "2026-03-02"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Farmers Freedom Act of 2025</strong></p><p>This bill\u00a0excludes certain prior converted cropland from permit requirements under the Clean Water Act, including Section 404 permits for discharges of dredged materials into waters of the United States (WOTUS). The exclusion applies to areas that were converted to cropland prior to December 23, 1985. However, the bill does not exclude an area that has reverted to wetlands and has not been used for agricultural purposes in five years.</p><p>In recent years, there has not been regulatory consistency about which cropland, such as cropland that has reverted to wetlands, is protected under the scope of the act as WOTUS.\u00a0In 2020, the Environmental Protection Agency (EPA) and the U.S. Army Corps of Engineers issued the <em>Navigable Waters Protection Rule</em> that, among other provisions,\u00a0defined\u00a0<em>prior converted cropland</em> in order to specify which cropland is excluded from the scope of the act.\u00a0However, the U.S. District Court for the District of Arizona vacated the rule in <em>Pascua Yaqui Tribe v. EPA</em>. In 2023, the EPA and the Army Corps of Engineers issued another rule that excluded prior converted cropland from the scope of the act, but they defined the exclusion more narrowly than the exclusion in the 2020 rule.\u00a0</p><p>Similar to the 2020 rule, this bill broadens the exclusion. The bill determines the scope of the exclusion by defining the term <em>prior converted cropland</em> in statute<em>.\u00a0</em></p>"
        },
        "title": "Farmers Freedom Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s795.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Farmers Freedom Act of 2025</strong></p><p>This bill\u00a0excludes certain prior converted cropland from permit requirements under the Clean Water Act, including Section 404 permits for discharges of dredged materials into waters of the United States (WOTUS). The exclusion applies to areas that were converted to cropland prior to December 23, 1985. However, the bill does not exclude an area that has reverted to wetlands and has not been used for agricultural purposes in five years.</p><p>In recent years, there has not been regulatory consistency about which cropland, such as cropland that has reverted to wetlands, is protected under the scope of the act as WOTUS.\u00a0In 2020, the Environmental Protection Agency (EPA) and the U.S. Army Corps of Engineers issued the <em>Navigable Waters Protection Rule</em> that, among other provisions,\u00a0defined\u00a0<em>prior converted cropland</em> in order to specify which cropland is excluded from the scope of the act.\u00a0However, the U.S. District Court for the District of Arizona vacated the rule in <em>Pascua Yaqui Tribe v. EPA</em>. In 2023, the EPA and the Army Corps of Engineers issued another rule that excluded prior converted cropland from the scope of the act, but they defined the exclusion more narrowly than the exclusion in the 2020 rule.\u00a0</p><p>Similar to the 2020 rule, this bill broadens the exclusion. The bill determines the scope of the exclusion by defining the term <em>prior converted cropland</em> in statute<em>.\u00a0</em></p>",
      "updateDate": "2026-03-02",
      "versionCode": "id119s795"
    },
    "title": "Farmers Freedom Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Farmers Freedom Act of 2025</strong></p><p>This bill\u00a0excludes certain prior converted cropland from permit requirements under the Clean Water Act, including Section 404 permits for discharges of dredged materials into waters of the United States (WOTUS). The exclusion applies to areas that were converted to cropland prior to December 23, 1985. However, the bill does not exclude an area that has reverted to wetlands and has not been used for agricultural purposes in five years.</p><p>In recent years, there has not been regulatory consistency about which cropland, such as cropland that has reverted to wetlands, is protected under the scope of the act as WOTUS.\u00a0In 2020, the Environmental Protection Agency (EPA) and the U.S. Army Corps of Engineers issued the <em>Navigable Waters Protection Rule</em> that, among other provisions,\u00a0defined\u00a0<em>prior converted cropland</em> in order to specify which cropland is excluded from the scope of the act.\u00a0However, the U.S. District Court for the District of Arizona vacated the rule in <em>Pascua Yaqui Tribe v. EPA</em>. In 2023, the EPA and the Army Corps of Engineers issued another rule that excluded prior converted cropland from the scope of the act, but they defined the exclusion more narrowly than the exclusion in the 2020 rule.\u00a0</p><p>Similar to the 2020 rule, this bill broadens the exclusion. The bill determines the scope of the exclusion by defining the term <em>prior converted cropland</em> in statute<em>.\u00a0</em></p>",
      "updateDate": "2026-03-02",
      "versionCode": "id119s795"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s795is.xml"
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
      "title": "Farmers Freedom Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-12T11:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Farmers Freedom Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T01:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Water Pollution Control Act to exclude prior converted cropland from the definition of \"navigable waters\", and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T01:48:22Z"
    }
  ]
}
```
