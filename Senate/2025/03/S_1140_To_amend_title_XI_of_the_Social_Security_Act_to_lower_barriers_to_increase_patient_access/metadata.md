# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1140?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1140
- Title: Health ACCESS Act
- Congress: 119
- Bill type: S
- Bill number: 1140
- Origin chamber: Senate
- Introduced date: 2025-03-26
- Update date: 2026-04-08T13:07:09Z
- Update date including text: 2026-04-08T13:07:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-26: Introduced in Senate
- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-03-26: Introduced in Senate

## Actions

- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-26",
    "latestAction": {
      "actionDate": "2025-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1140",
    "number": "1140",
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
    "title": "Health ACCESS Act",
    "type": "S",
    "updateDate": "2026-04-08T13:07:09Z",
    "updateDateIncludingText": "2026-04-08T13:07:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-26",
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
      "actionDate": "2025-03-26",
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
          "date": "2025-03-26T16:18:20Z",
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1140is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1140\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2025 Mr. Cassidy (for himself and Mr. Padilla ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XI of the Social Security Act to lower barriers to increase patient access to health care.\n#### 1. Short title\nThis Act may be cited as the Health Accelerating Consumer\u2019s Care by Expediting Self-Scheduling Act or the Health ACCESS Act .\n#### 2. Amendments to section 1128B\nSection 1128B(b) of the Social Security Act (42 U.S.C. 1320a\u20137b(b)) is amended\u2014\n**(1)**\nin paragraph (3)\u2014\n**(A)**\nby moving the left margins of subparagraphs (J) and (K) 2 ems to the left;\n**(B)**\nin subparagraph (K), by striking and at the end;\n**(C)**\nin subparagraph (L), by striking the period at the end and inserting ; and ; and\n**(D)**\nby adding at the end the following new subparagraph:\n(M) any remuneration paid by a provider of services (as defined in section 1861(u)) or a supplier (as defined in section 1861(d)) to an information service provider (as defined in paragraph (5)), if\u2014 (i) such information service provider does not\u2014 (I) steer or lead a consumer to select a particular provider of services or supplier based on the amount a provider of services or supplier pays or may pay the information service provider; (II) provide, or represent itself as providing, any medical items or services, diagnostic or counseling services or assessments of illness or injury, or make any promises of cure or guarantees of treatment; (III) provide contact information regarding a consumer (as defined in paragraph (5)) to providers of services or suppliers, except to the specific provider of services or supplier selected by the consumer; (IV) provide or arrange for transportation of an individual to, or from, the location of a provider of services or supplier; (V) provide or arrange for the provision of any other remuneration to a Federal health care program beneficiary other than the inherent convenience of the information service; or (VI) engage in targeted marketing of a particular provider or supplier through phone calls or text messages, with respect to consumers or potential consumers who have not previously interacted with the information service provider or who have opted out; (ii) the methodology for determining compensation paid to the information service provider by a provider of services or supplier is set in advance in writing, and the compensation: (I) does not exceed fair market value; (II) is for services, specified in writing; and (III) does not take into account the value of any items or services payable in whole or in part by a Federal health care program that result from recommendations by the information service provider for the provider of services or supplier; (iii) such information service provider clearly discloses the financial arrangement between it and the providers of services or suppliers participating in such service to consumers; (iv) such information service provider furnishes provider- and supplier-specific information to consumers based only on objective, consumer-centric criteria; (v) such information service provider develops objective criteria for participation in such information service and does not exclude any providers of services or suppliers who meet such criteria from participating therein; and (vi) such information service provider meets such other conditions as may be determined appropriate by the Secretary. ; and\n**(E)**\nby adding at the end the following new paragraph:\n(5) Definition of consumer; information service provider For purposes of paragraph (3)(M): (A) Consumer The term consumer means an individual who uses a web-based platform operated by an information service provider for the purpose of searching providers of services or suppliers. (B) Information service provider The term information service provider means any individual or entity operating a web-based platform that makes information regarding providers of services or suppliers available to consumers. .",
      "versionDate": "2025-03-26",
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
        "actionDate": "2025-11-18",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6100",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Health ACCESS Act",
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
        "updateDate": "2025-04-10T13:27:58Z"
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
      "date": "2025-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1140is.xml"
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
      "title": "Health ACCESS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-10T01:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Health ACCESS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-10T01:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Health Accelerating Consumer\u2019s Care by Expediting Self-Scheduling Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-10T01:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XI of the Social Security Act to lower barriers to increase patient access to health care.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-10T01:48:27Z"
    }
  ]
}
```
