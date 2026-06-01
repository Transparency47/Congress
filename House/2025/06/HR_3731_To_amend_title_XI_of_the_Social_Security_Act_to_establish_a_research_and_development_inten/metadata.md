# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3731?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3731
- Title: Small Biotech Innovation Act
- Congress: 119
- Bill type: HR
- Bill number: 3731
- Origin chamber: House
- Introduced date: 2025-06-04
- Update date: 2026-04-15T08:06:17Z
- Update date including text: 2026-04-15T08:06:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-04: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-04 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-06-04: Introduced in House

## Actions

- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Introduced in House
- 2025-06-04 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-04 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-04",
    "latestAction": {
      "actionDate": "2025-06-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3731",
    "number": "3731",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "P000048",
        "district": "11",
        "firstName": "August",
        "fullName": "Rep. Pfluger, August [R-TX-11]",
        "lastName": "Pfluger",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Small Biotech Innovation Act",
    "type": "HR",
    "updateDate": "2026-04-15T08:06:17Z",
    "updateDateIncludingText": "2026-04-15T08:06:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-04",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-04",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-04",
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
          "date": "2025-06-04T14:06:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-06-04T14:05:50Z",
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
      "bioguideId": "K000392",
      "district": "8",
      "firstName": "David",
      "fullName": "Rep. Kustoff, David [R-TN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Kustoff",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "TN"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-12-19",
      "state": "NY"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3731ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3731\nIN THE HOUSE OF REPRESENTATIVES\nJune 4, 2025 Mr. Pfluger (for himself and Mr. Kustoff ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XI of the Social Security Act to establish a research and development-intensive small biotech manufacturer exception from the Medicare drug price negotiation program.\n#### 1. Short title\nThis Act may be cited as the Small Biotech Innovation Act .\n#### 2. Research and development-intensive small biotech manufacturer exception from Medicare drug price negotiation program\nSection 1192(d)(2) of the Social Security Act ( 42 U.S.C. 1320f\u20131(d)(2) ) is amended by adding at the end the following new subparagraph:\n(D) Research and development-intensive small biotech manufacturer exception for 2029 and subsequent years (i) In general With respect to initial price applicability years (beginning with initial price applicability year 2029), subject to the succeeding provisions of this subparagraph, the term negotiation eligible drug shall not include a qualifying single source drug (as defined in subsection (e)) of a research and development-intensive small biotech manufacturer (as defined in clause (ii)). (ii) Definitions In this subparagraph: (I) Applicable percent The term applicable percent means\u2014 (aa) in the case of a small biotech manufacturer that has 1 qualifying single source drug, 30 percent; (bb) in the case of a small biotech manufacturer that has 2 qualifying single source drugs, 40 percent; (cc) in the case of a small biotech manufacturer that has 3 qualifying single source drugs, 50 percent; (dd) in the case of a small biotech manufacturer that has 4 qualifying single source drugs, 60 percent; and (ee) in the case of a small biotech manufacturer that has 5 qualifying single source drugs, 70 percent. (II) Small biotech manufacturer defined The term small biotech manufacturer means a manufacturer that\u2014 (aa) has 5 or less qualifying single source drugs; and (bb) is not owned by, controlled by, or subject to the jurisdiction or direction of a government of a foreign country, or organized under the laws of a foreign country that is a covered nation (as defined in section 4872(f) of title 10, United States Code). (III) Research and development-intensive small biotech manufacturer defined The term research and development-intensive small biotech manufacturer means a small biotech manufacturer that invests at least the applicable percent of their net revenue from the average of the previous three years in research and development (determined based on generally accepted accounting principles). (iii) Treatment in case of acquisition A drug shall not be considered to be a qualifying single source drug of a research and development-intensive small biotech manufacturer if the manufacturer of such drug is acquired after 2029 by another manufacturer that does not meet the definition of a research and development-intensive small biotech manufacturer, effective at the beginning of the plan year immediately following such acquisition. (iv) Annual application In order for a qualifying single source drug of a research and development-intensive small biotech manufacturer to be eligible for the exception under this subparagraph with respect to an initial price applicability year (beginning with initial price applicability year 2029), the manufacturer shall submit an application to the Secretary (at a time specified by the Secretary) containing\u2014 (I) information on the net product revenue and research and development expenditures of the manufacturer during the relevant time period; (II) a certification that the information submitted by the manufacturer under subclause (I) is accurate and complete to the best of the manufacturer\u2019s knowledge; and (III) such other information as the Secretary may specify. (v) Dispute Resolution The Secretary shall develop a process under which a manufacturer may appeal a determination by the Secretary that the manufacturer is not a research and development-intensive small biotech manufacturer. Such process shall conclude, with respect to a manufacturer, not later than the selected drug publication date with respect to the initial price applicability year for which the manufacturer submitted an application under clause (iv). .",
      "versionDate": "2025-06-04",
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
        "actionDate": "2025-06-03",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1930",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Small Biotech Innovation Act",
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
        "name": "Health",
        "updateDate": "2025-06-24T13:03:21Z"
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
      "date": "2025-06-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3731ih.xml"
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
      "title": "Small Biotech Innovation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-11T06:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Small Biotech Innovation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-11T06:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XI of the Social Security Act to establish a research and development-intensive small biotech manufacturer exception from the Medicare drug price negotiation program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-11T06:48:50Z"
    }
  ]
}
```
