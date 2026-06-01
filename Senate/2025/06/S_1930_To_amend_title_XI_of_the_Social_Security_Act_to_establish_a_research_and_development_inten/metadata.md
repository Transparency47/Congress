# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1930?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1930
- Title: Small Biotech Innovation Act
- Congress: 119
- Bill type: S
- Bill number: 1930
- Origin chamber: Senate
- Introduced date: 2025-06-03
- Update date: 2025-12-05T22:50:19Z
- Update date including text: 2025-12-05T22:50:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-03: Introduced in Senate
- 2025-06-03 - IntroReferral: Introduced in Senate
- 2025-06-03 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-06-03: Introduced in Senate

## Actions

- 2025-06-03 - IntroReferral: Introduced in Senate
- 2025-06-03 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-03",
    "latestAction": {
      "actionDate": "2025-06-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1930",
    "number": "1930",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Small Biotech Innovation Act",
    "type": "S",
    "updateDate": "2025-12-05T22:50:19Z",
    "updateDateIncludingText": "2025-12-05T22:50:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-03",
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
      "actionDate": "2025-06-03",
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
          "date": "2025-06-03T16:22:27Z",
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
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-09-11",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1930is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1930\nIN THE SENATE OF THE UNITED STATES\nJune 3, 2025 Mr. Cassidy introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XI of the Social Security Act to establish a research and development-intensive small biotech manufacturer exception from the Medicare drug price negotiation program.\n#### 1. Short title\nThis Act may be cited as the Small Biotech Innovation Act .\n#### 2. Research and development-intensive small biotech manufacturer exception from Medicare drug price negotiation program\nSection 1192(d)(2) of the Social Security Act ( 42 U.S.C. 1320f\u20131(d)(2) ) is amended by adding at the end the following new subparagraph:\n(D) Research and development-intensive small biotech manufacturer exception for 2029 and subsequent years (i) In general With respect to initial price applicability years (beginning with initial price applicability year 2029), subject to the succeeding provisions of this subparagraph, the term negotiation eligible drug shall not include a qualifying single source drug (as defined in subsection (e)) of a research and development-intensive small biotech manufacturer (as defined in clause (ii)). (ii) Definitions In this subparagraph: (I) Applicable percent The term applicable percent means\u2014 (aa) in the case of a small biotech manufacturer that has 1 qualifying single source drug, 30 percent; (bb) in the case of a small biotech manufacturer that has 2 qualifying single source drugs, 40 percent; (cc) in the case of a small biotech manufacturer that has 3 qualifying single source drugs, 50 percent; (dd) in the case of a small biotech manufacturer that has 4 qualifying single source drugs, 60 percent; and (ee) in the case of a small biotech manufacturer that has 5 qualifying single source drugs, 70 percent. (II) Small biotech manufacturer defined The term small biotech manufacturer means a manufacturer that\u2014 (aa) has 5 or less qualifying single source drugs; and (bb) is not owned by, controlled by, or subject to the jurisdiction or direction of a government of a foreign country, or organized under the laws of a foreign country that is a covered nation (as defined in section 4872(f) of title 10, United States Code). (III) Research and development-intensive small biotech manufacturer defined The term research and development-intensive small biotech manufacturer means a small biotech manufacturer that invests at least the applicable percent of their net revenue from the average of the previous three years in research and development (determined based on generally accepted accounting principles). (iii) Treatment in case of acquisition A drug shall not be considered to be a qualifying single source drug of a research and development-intensive small biotech manufacturer if the manufacturer of such drug is acquired after 2029 by another manufacturer that does not meet the definition of a research and development-intensive small biotech manufacturer, effective at the beginning of the plan year immediately following such acquisition. (iv) Annual application In order for a qualifying single source drug of a research and development-intensive small biotech manufacturer to be eligible for the exception under this subparagraph with respect to an initial price applicability year (beginning with initial price applicability year 2029), the manufacturer shall submit an application to the Secretary (at a time specified by the Secretary) containing\u2014 (I) information on the net product revenue and research and development expenditures of the manufacturer during the relevant time period; (II) a certification that the information submitted by the manufacturer under subclause (I) is accurate and complete to the best of the manufacturer\u2019s knowledge; and (III) such other information as the Secretary may specify. (v) Dispute Resolution The Secretary shall develop a process under which a manufacturer may appeal a determination by the Secretary that the manufacturer is not a research and development-intensive small biotech manufacturer. Such process shall conclude, with respect to a manufacturer, not later than the selected drug publication date with respect to the initial price applicability year for which the manufacturer submitted an application under clause (iv). .",
      "versionDate": "2025-06-03",
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
        "actionDate": "2025-06-04",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3731",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Small Biotech Innovation Act",
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
        "name": "Health",
        "updateDate": "2025-06-18T14:13:03Z"
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
      "date": "2025-06-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1930is.xml"
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
      "title": "Small Biotech Innovation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-12T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XI of the Social Security Act to establish a research and development-intensive small biotech manufacturer exemption from the Medicare drug price negotiation program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-12T10:56:35Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Small Biotech Innovation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-07T04:23:18Z"
    }
  ]
}
```
