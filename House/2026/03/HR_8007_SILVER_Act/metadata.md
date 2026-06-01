# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8007?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8007
- Title: SILVER Act
- Congress: 119
- Bill type: HR
- Bill number: 8007
- Origin chamber: House
- Introduced date: 2026-03-19
- Update date: 2026-04-03T21:07:12Z
- Update date including text: 2026-04-03T21:07:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-19: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2026-03-19: Introduced in House

## Actions

- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-19",
    "latestAction": {
      "actionDate": "2026-03-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8007",
    "number": "8007",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "F000469",
        "district": "1",
        "firstName": "Russ",
        "fullName": "Rep. Fulcher, Russ [R-ID-1]",
        "lastName": "Fulcher",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "SILVER Act",
    "type": "HR",
    "updateDate": "2026-04-03T21:07:12Z",
    "updateDateIncludingText": "2026-04-03T21:07:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-19",
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
      "actionDate": "2026-03-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-19",
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
          "date": "2026-03-19T13:01:20Z",
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
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8007ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8007\nIN THE HOUSE OF REPRESENTATIVES\nMarch 19, 2026 Mr. Fulcher (for himself and Mr. Harris of North Carolina ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Commodity Exchange Act to reduce systemic risk while increasing geographical diversity and competition with respect to depositories for the storage of precious metals, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the System Integrity through Licensed Vault Expansion and Resilience Act or the SILVER Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nPrecious metals exchanges currently require physically traded metals to be stored within close proximity to New York City.\n**(2)**\nGeographic concentration creates systemic risk vulnerabilities, reduces available liquidity, and increases the cost to market participants.\n**(3)**\nRecent liquidity events in global metals markets underscore the need to minimize regulatory barriers that reduce the available supply of metals to the publicly traded marketplace.\n**(4)**\nNotwithstanding the current limited supply, the security standards of existing vaults supporting publicly traded exchanges are outstanding and have enhanced the confidence of market participants.\n**(5)**\nMarket liquidity and participant confidence will be enhanced by the addition of storage vaults of relative scale and commercial importance in the marketplace.\n**(6)**\nAdditional supply in lower-cost markets, especially markets that are near hubs of precious metals activity and interstate transportation networks, would also reduce storage costs, enhance competition in the storage marketplace, and promote greater market access to investors.\n**(7)**\nIt is in the public interest for systemically important financial market utilities to provide a clear and transparent selection process for precious metals storage facilities within their network.\n#### 3. Precious metals depositories used in connection with futures contracts\nSection 5b(c)(2) of the Commodity Exchange Act ( 7 U.S.C. 7a\u20131(c)(2) ) is amended\u2014\n**(1)**\nin subparagraph (E)(vii), by inserting , including risks related to the geographic concentration of depositories for the storage of gold, silver, platinum, and palladium (referred to in this paragraph as precious metals ), after clause (vi) ;\n**(2)**\nin subparagraph (F)\u2014\n**(A)**\nby redesignating clause (iii) as clause (iv); and\n**(B)**\nby inserting after clause (ii) the following:\n(iii) Approval of precious metals depositories (I) In general A derivatives clearing organization shall\u2014 (aa) develop, publish, and employ objective and transparent criteria in evaluating and selecting depositories for the storage of precious metals used in connection with a contract of sale of a commodity for future delivery; and (bb) provide a formal process for those depositories to apply for that selection. (II) Selection factors In selecting depositories under subclause (I), a derivatives clearing organization shall\u2014 (aa) assess and account for, among other factors, geographic diversity, competition, risk management, storage costs to members and participants, and systemic risk implications; and (bb) approve new depositories in the context of a public interest in increased geographic diversity, increased liquidity, market resiliency, market access, competition, and cost efficiency, consistent with appropriate security and quality standards. (III) Geographical requirement (aa) In general A derivatives clearing organization shall select at least 2 depositories described in subclause (I) in each time zone described in item (bb). (bb) Time zone A time zone referred to in item (aa) is each of the following: (AA) Eastern time. (BB) Central time. (CC) Mountain time. (DD) Pacific time. ;\n**(3)**\nin subparagraph (I)\u2014\n**(A)**\nin clause (ii)(II), by striking and at the end;\n**(B)**\nin clause (iii), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(iv) periodically assess the ease of access for market participants with respect to the physical settlement of any commodity, regardless of the geographic location within the United States, to ensure system availability and resiliency. ;\n**(4)**\nin subparagraph (L)(iii)\u2014\n**(A)**\nin subclause (IV), by striking and at the end;\n**(B)**\nby redesignating subclause (V) as subclause (VI); and\n**(C)**\nby inserting after subclause (IV) the following:\n(V) conditions for applying to, and receiving approval from, the derivatives clearing organization as a metal service provider, such as a depository for the storage of precious metals; and ; and\n**(5)**\nin subparagraph (N)(i), by inserting , including with respect to the approval of a metal service provider, such as a depository for the storage of precious metals after trade .",
      "versionDate": "2026-03-19",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2026-04-03T21:07:12Z"
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
      "date": "2026-03-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8007ih.xml"
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
      "title": "SILVER Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-02T05:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SILVER Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-02T05:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "System Integrity through Licensed Vault Expansion and Resilience Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-02T05:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Commodity Exchange Act to reduce systemic risk while increasing geographical diversity and competition with respect to depositories for the storage of precious metals, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-02T05:33:24Z"
    }
  ]
}
```
