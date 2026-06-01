# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/231?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/231
- Title: WEATHER Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 231
- Origin chamber: Senate
- Introduced date: 2025-01-23
- Update date: 2025-05-06T17:18:26Z
- Update date including text: 2025-05-06T17:18:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in Senate
- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-01-23: Introduced in Senate

## Actions

- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/231",
    "number": "231",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "W000800",
        "district": "",
        "firstName": "Peter",
        "fullName": "Sen. Welch, Peter [D-VT]",
        "lastName": "Welch",
        "party": "D",
        "state": "VT"
      }
    ],
    "title": "WEATHER Act of 2025",
    "type": "S",
    "updateDate": "2025-05-06T17:18:26Z",
    "updateDateIncludingText": "2025-05-06T17:18:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-23",
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
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T20:34:06Z",
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
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "MA"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "CT"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "CT"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "CA"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernard",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-01-23",
      "state": "VT"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s231is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 231\nIN THE SENATE OF THE UNITED STATES\nJanuary 23, 2025 Mr. Welch (for himself, Ms. Warren , Mr. Blumenthal , Mr. Murphy , Mr. Padilla , Mr. Sanders , and Mr. Van Hollen ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Federal Crop Insurance Act to authorize the Federal Crop Insurance Corporation to carry out research and development on a single index insurance policy, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Withstanding Extreme Agricultural Threats by Harvesting Economic Resilience Act of 2025 or the WEATHER Act of 2025 .\n#### 2. Single index insurance policy\n##### (a) In general\nSection 522(c) of the Federal Crop Insurance Act ( 7 U.S.C. 1522(c) ) is amended by adding at the end the following:\n(20) Single index insurance policy (A) Definitions In this paragraph: (i) Covered crop or commodity The term covered crop or commodity means any crop or commodity (including a specialty crop) on a farm except timber, forest products, animals for sport or show, and pets. (ii) Covered policy The term covered policy means the single index insurance policy described in subparagraph (B)(i). (iii) Covered weather condition (I) In general The term covered weather condition means any of the following weather conditions that are found to be closely correlated with agricultural income losses: (aa) High winds. (bb) Excessive moisture and flooding. (cc) Extreme heat. (dd) Abnormal freeze conditions. (ee) Wildfire. (ff) Hail. (gg) Drought. (hh) Any other severe weather or growing conditions applicable to small-scale farmers, as determined by the Secretary. (II) Data The existence of a weather condition described in subclause (I) shall be determined by indices that prioritize using data from the National Oceanic and Atmospheric Administration, as available, but may use other federally or State certified weather data sources, public and private satellite data, and weather and climate data and models, if necessary, as determined by the Secretary. (B) Policy (i) In general The Corporation shall carry out research and development, or offer to enter into 1 or more contracts with 1 or more qualified persons to carry out research and development, to develop a single index policy to insure against agricultural income losses due to 1 or more covered weather conditions. (ii) Coverage Research and development on the covered policy under clause (i) shall require that coverage is available in all 50 States (including Indian Tribes), the District of Columbia, American Samoa, Guam, the Commonwealth of the Northern Mariana Islands, the Commonwealth of Puerto Rico, and the Virgin Islands of the United States. (iii) Option to buy-up or buy-down (I) In general Research and development on the covered policy under clause (i) shall consider permitting a holder of the covered policy to elect to buy-up to 150 percent, subject to subclause (II), or buy-down to 5 percent, of the median county-level adjusted gross income for farms, in 5-percent increments, to reflect the income of the individual farm business of the holder insured under the covered policy. (II) Limitation A holder of a covered policy may buy-up under subclause (I) only if the farms of the holder insured under the covered policy have at least 3 covered crops or commodities. (iv) Priority features of policy In carrying out research and development on the covered policy under clause (i), the following features may be given priority: (I) Agricultural income losses under the covered policy include\u2014 (aa) losses for all covered crops or commodities; and (bb) losses to the value of packing, packaging, or any other similar on-farm activity that the Corporation determines necessary to remove a covered crop or commodity from the field. (II) Payments are made under the covered policy not later than 30 days after the occurrence of a covered weather condition in the county in which the applicable farm of the farmer is located or an adjacent county. (III) Provision of seasonal coverage periods. (IV) Provision of special consideration to concerns facing individual farm businesses\u2014 (aa) that have less than $350,000 in adjusted gross income; and (bb) with respect to which a farmer is an underserved producer (as defined in section 508(a)(7)(A)). (V) Paperwork requirements are reduced for farmers seeking to obtain a covered policy. (v) Consultation In carrying out research and development on the covered policy under clause (i), the Corporation\u2014 (I) shall hold stakeholder meetings to solicit producer and agent feedback; and (II) may consult with licensed actuaries with experience developing index policies insuring agricultural production. (C) Report Not later than 1 year after the date of enactment of this paragraph, the Corporation shall make publicly available a report that describes\u2014 (i) the results of the research and development carried out under this paragraph; and (ii) recommendations to Congress with respect to those results, including\u2014 (I) any challenges to developing the covered policy; and (II) options to address those challenges. .\n##### (b) Technical amendment\nSection 531(a)(18) of the Federal Crop Insurance Act ( 7 U.S.C. 1531(a)(18) ) is amended by striking section 2501(e) of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 2279(e) ) and inserting section 2501(a) of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 2279(a) ). .",
      "versionDate": "2025-01-23",
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
        "actionDate": "2025-04-18",
        "text": "Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit."
      },
      "number": "2435",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Save Our Small Farms Act of 2025",
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
        "updateDate": "2025-02-25T18:28:06Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
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
          "measure-id": "id119s231",
          "measure-number": "231",
          "measure-type": "s",
          "orig-publish-date": "2025-01-23",
          "originChamber": "SENATE",
          "update-date": "2025-04-22"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s231v00",
            "update-date": "2025-04-22"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Withstanding Extreme Agricultural Threats by Harvesting Economic Resilience Act of 2025 or the WEATHER Act of 2025</strong></p><p>This bill requires the federal crop insurance program (FCIP) to provide for the research and development of a single index insurance policy to insure against agricultural income losses due to covered weather conditions.</p><p>Specifically, the FCIP must develop a single index policy that is available in every state, each U.S. territory, and the District of Columbia to insure against agricultural income losses due to one or more covered weather conditions. <em>Covered weather conditions</em> are those\u00a0found to be closely correlated with agricultural income losses, including high winds, excessive moisture and flooding, extreme heat, abnormal freeze conditions, wildfire, hail, drought, and any other severe weather or growing conditions applicable to small-scale farmers.</p><p>Under an index policy, claim payments are generally triggered based on a predetermined index that is entirely independent of the individual farm operation (e.g., rainfall level). Under such a policy, the payments are automatically triggered when the index reaches a certain level rather than when an insured farmer files a claim.\u00a0</p><p>In carrying out the research and development, the\u00a0FCIP\u00a0must hold stakeholder meetings to solicit producer and agent feedback.</p><p>In addition, the FCIP must make publicly available a report on the results of the research and development, and any recommendations to Congress with respect to those results.\u00a0</p>"
        },
        "title": "WEATHER Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s231.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Withstanding Extreme Agricultural Threats by Harvesting Economic Resilience Act of 2025 or the WEATHER Act of 2025</strong></p><p>This bill requires the federal crop insurance program (FCIP) to provide for the research and development of a single index insurance policy to insure against agricultural income losses due to covered weather conditions.</p><p>Specifically, the FCIP must develop a single index policy that is available in every state, each U.S. territory, and the District of Columbia to insure against agricultural income losses due to one or more covered weather conditions. <em>Covered weather conditions</em> are those\u00a0found to be closely correlated with agricultural income losses, including high winds, excessive moisture and flooding, extreme heat, abnormal freeze conditions, wildfire, hail, drought, and any other severe weather or growing conditions applicable to small-scale farmers.</p><p>Under an index policy, claim payments are generally triggered based on a predetermined index that is entirely independent of the individual farm operation (e.g., rainfall level). Under such a policy, the payments are automatically triggered when the index reaches a certain level rather than when an insured farmer files a claim.\u00a0</p><p>In carrying out the research and development, the\u00a0FCIP\u00a0must hold stakeholder meetings to solicit producer and agent feedback.</p><p>In addition, the FCIP must make publicly available a report on the results of the research and development, and any recommendations to Congress with respect to those results.\u00a0</p>",
      "updateDate": "2025-04-22",
      "versionCode": "id119s231"
    },
    "title": "WEATHER Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Withstanding Extreme Agricultural Threats by Harvesting Economic Resilience Act of 2025 or the WEATHER Act of 2025</strong></p><p>This bill requires the federal crop insurance program (FCIP) to provide for the research and development of a single index insurance policy to insure against agricultural income losses due to covered weather conditions.</p><p>Specifically, the FCIP must develop a single index policy that is available in every state, each U.S. territory, and the District of Columbia to insure against agricultural income losses due to one or more covered weather conditions. <em>Covered weather conditions</em> are those\u00a0found to be closely correlated with agricultural income losses, including high winds, excessive moisture and flooding, extreme heat, abnormal freeze conditions, wildfire, hail, drought, and any other severe weather or growing conditions applicable to small-scale farmers.</p><p>Under an index policy, claim payments are generally triggered based on a predetermined index that is entirely independent of the individual farm operation (e.g., rainfall level). Under such a policy, the payments are automatically triggered when the index reaches a certain level rather than when an insured farmer files a claim.\u00a0</p><p>In carrying out the research and development, the\u00a0FCIP\u00a0must hold stakeholder meetings to solicit producer and agent feedback.</p><p>In addition, the FCIP must make publicly available a report on the results of the research and development, and any recommendations to Congress with respect to those results.\u00a0</p>",
      "updateDate": "2025-04-22",
      "versionCode": "id119s231"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s231is.xml"
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
      "title": "WEATHER Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-22T06:23:50Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "WEATHER Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Withstanding Extreme Agricultural Threats by Harvesting Economic Resilience Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Crop Insurance Act to authorize the Federal Crop Insurance Corporation to carry out research and development on a single index insurance policy, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:18:40Z"
    }
  ]
}
```
