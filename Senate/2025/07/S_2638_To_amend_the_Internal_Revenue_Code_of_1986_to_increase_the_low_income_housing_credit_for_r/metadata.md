# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2638?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2638
- Title: Energy Efficiency for Affordable Housing Act
- Congress: 119
- Bill type: S
- Bill number: 2638
- Origin chamber: Senate
- Introduced date: 2025-07-31
- Update date: 2025-09-05T19:31:00Z
- Update date including text: 2025-09-05T19:31:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-31: Introduced in Senate
- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-07-31: Introduced in Senate

## Actions

- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-31",
    "latestAction": {
      "actionDate": "2025-07-31",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2638",
    "number": "2638",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Energy Efficiency for Affordable Housing Act",
    "type": "S",
    "updateDate": "2025-09-05T19:31:00Z",
    "updateDateIncludingText": "2025-09-05T19:31:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-31",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-31",
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
          "date": "2025-08-01T01:26:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "sponsorshipDate": "2025-07-31",
      "state": "MA"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
      "state": "MN"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-07-31",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2638is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2638\nIN THE SENATE OF THE UNITED STATES\nJuly 31, 2025 Ms. Klobuchar (for herself, Ms. Warren , Ms. Smith , and Mr. Van Hollen ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to increase the low-income housing credit for rehabilitation expenditures for buildings achieving enhanced energy performance, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Energy Efficiency for Affordable Housing Act .\n#### 2. Increase of credit\n##### (a) In general\nParagraph (2) of section 42(e) of the Internal Revenue Code of 1986 is amended by adding at the end the following new subparagraph:\n(C) Increase in credit for buildings achieving enhanced energy performance (i) In general In the case of any existing building to which subsection (b)(2) does not apply which achieves enhanced energy performance, the rehabilitation expenditures taken into account under subparagraph (A) shall be 130 percent of such expenditures determined without regard to this subparagraph. (ii) Enhanced energy performance For purposes of clause (i), a building achieves enhanced energy performance if it meets either of the following: (I) The minimum requirements of an advanced building construction standard which shall be determined by the Secretary of Energy using prescriptive or performance methods of calculation and promulgated by the Secretary of Energy within 180 days of the date of the enactment of this subparagraph. (II) In the case of a taxpayer which elects (at such time and in such manner as the Secretary may provide) the application of this subclause with respect to the building, a qualified retrofit plan. (iii) Definitions For purposes of this subparagraph\u2014 (I) Qualified retrofit plan The term qualified retrofit plan means a written plan prepared and stamped by a qualified professional which specifies modifications to a building which, in the aggregate, are expected to reduce such building\u2019s site energy usage intensity by 50 percent or more in comparison to the baseline energy usage intensity of such building. Such plan shall require a qualified professional to certify\u2014 (aa) the baseline energy usage intensity of the building, (bb) that the modifications are expected to reduce such building\u2019s site energy usage intensity by 50 percent or more in comparison to the baseline energy usage intensity of such building, and (cc) as of any date following installation of building modifications, that such modifications have been installed. (II) Baseline energy usage intensity The term baseline energy usage intensity means the site energy usage intensity as of any date during the 24-month period immediately preceding the building modifications described in the qualified retrofit plan. (III) Site energy usage intensity The site energy usage intensity shall be determined for the entire building in accordance with such regulations or other guidance as the Secretary may provide and measured in British thermal units per square foot per year. (IV) Qualified professional The term qualified professional means an individual who is a licensed architect or a licensed engineer or meets such other requirements as the Secretary of Energy may provide. .\n##### (b) Increase for buildings in high-Cost areas\nParagraph (2) of section 42(e) of the Internal Revenue Code of 1986, as amended by subsection (a), is further amended by adding at the end the following new subparagraph:\n(D) Special rule for buildings in high-cost areas which achieve enhanced energy performance In the case of an existing building to which both subparagraph (C) and subsection (d)(5)(B) apply (but for this subparagraph)\u2014 (i) subsection (d)(5)(B)(i)(II) shall not apply, and (ii) the rehabilitation expenditures taken into account under subparagraph (A) shall be 160 percent of such expenditures determined without regard to this subparagraph. .\n##### (c) Effective date\n**(1) In general**\nExcept as provided in paragraph (2), the amendments made by this section shall apply to buildings with respect to which housing credit dollar amounts are allocated after December 31, 2025.\n**(2) Bond-financed projects**\nIn the case of any building some portion of which, or of the land on which the building is located, is financed by an obligation which is described in section 42(h)(4)(A) of the Internal Revenue Code of 1986, the amendments made by this section shall apply to any such building financed by such an obligation which is part of an issue the issue date of which is after December 31, 2025.",
      "versionDate": "2025-07-31",
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
        "name": "Taxation",
        "updateDate": "2025-09-05T19:31:00Z"
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
      "date": "2025-07-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2638is.xml"
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
      "title": "Energy Efficiency for Affordable Housing Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-12T03:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Energy Efficiency for Affordable Housing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-12T03:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to increase the low-income housing credit for rehabilitation expenditures for buildings achieving enhanced energy performance, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-12T03:18:27Z"
    }
  ]
}
```
