# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3145?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3145
- Title: CARE Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3145
- Origin chamber: Senate
- Introduced date: 2025-11-06
- Update date: 2026-04-30T11:03:20Z
- Update date including text: 2026-04-30T11:03:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-06: Introduced in Senate
- 2025-11-06 - IntroReferral: Introduced in Senate
- 2025-11-06 - IntroReferral: Read twice and referred to the Committee on Finance. (Sponsor introductory remarks on measure: CR S7964)
- Latest action: 2025-11-06: Introduced in Senate

## Actions

- 2025-11-06 - IntroReferral: Introduced in Senate
- 2025-11-06 - IntroReferral: Read twice and referred to the Committee on Finance. (Sponsor introductory remarks on measure: CR S7964)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-06",
    "latestAction": {
      "actionDate": "2025-11-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3145",
    "number": "3145",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001035",
        "district": "",
        "firstName": "Susan",
        "fullName": "Sen. Collins, Susan M. [R-ME]",
        "lastName": "Collins",
        "party": "R",
        "state": "ME"
      }
    ],
    "title": "CARE Act of 2025",
    "type": "S",
    "updateDate": "2026-04-30T11:03:20Z",
    "updateDateIncludingText": "2026-04-30T11:03:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-06",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance. (Sponsor introductory remarks on measure: CR S7964)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-06",
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
            "date": "2025-11-06T22:10:06Z",
            "name": "Referred To"
          },
          {
            "date": "2025-11-06T22:10:06Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "VT"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-12-08",
      "state": "MN"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-12-08",
      "state": "LA"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "WV"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "RI"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2026-01-05",
      "state": "NJ"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-01-05",
      "state": "WV"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "DE"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3145is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3145\nIN THE SENATE OF THE UNITED STATES\nNovember 6, 2025 Ms. Collins (for herself and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XI of the Social Security Act to require the Center for Medicare and Medicaid Innovation to test a comprehensive alternative response for emergencies model under the Medicare program.\n#### 1. Short title\nThis Act may be cited as the Comprehensive Alternative Response for Emergencies Act of 2025 or the CARE Act of 2025 .\n#### 2. Requiring the Center for Medicare and Medicaid Innovation to test a comprehensive alternative response for emergencies model under the Medicare program\n##### (a) In general\nSection 1115A of the Social Security Act ( 42 U.S.C. 1315a ) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (2)(A), in the third sentence, by inserting , and, beginning not later than the date that is 2 years after the date of the enactment of the CARE Act of 2025, shall include the Comprehensive Alternative Response for Emergencies Model described in subsection (h) before the period at the end; and\n**(B)**\nin paragraph (3)(B), by striking The Secretary and inserting Except in the case of the model described in subsection (h), the Secretary ; and\n**(2)**\nby adding at the end the following new subsection:\n(h) Comprehensive alternative response for emergencies model (1) In general For purposes of subsection (b)(2)(A), the Comprehensive Alternative Response for Emergencies Model described in this subsection is a model under which payment is made under part B of title XVIII for treatment of services furnished to an individual enrolled under such part by a provider or supplier of ground ambulance services (as described in section 1834(l)), or by an entity under arrangement with such a provider, when such services\u2014 (A) include the dispatch of a ground ambulance vehicle but do not include a corresponding transport payable under such section; (B) are so furnished in response to an emergency medical call (as specified by the Secretary) made with respect to such individual; and (C) are so furnished in accordance with State and local licensure requirements and protocols (which may include online medical direction through the use of audiovisual telecommunications technology). (2) Payment (A) In general The Secretary shall set payment rates for services furnished under the model described in paragraph (1) in a manner that generally aligns such payments with the payments that would have been made for such services had such services resulted in a transport payable under section 1834(l). (B) Originating site fee In the case of a telehealth service payable under section 1834(m) that is furnished in conjunction with treatment services furnished under the model described in paragraph (1), the site where the individual receiving such telehealth service is located shall be treated as an originating site that is described in paragraph (4)(C)(ii)(V) of such section for purposes of applying paragraph (2)(B) of such section. (3) Duration The model described in paragraph (1) shall be carried out for a period of 5 years. .\n##### (b) Report\nNot later than 4 years after the date on which the Comprehensive Alternative Response for Emergencies Model (as described in section 1115A(h) of the Social Security Act, as added by subsection (a)) is implemented, the Comptroller General of the United States shall submit to the Committee on Ways and Means of the House of Representatives and the Committee on Finance of the Senate a report that, taking into account stakeholder input and to the extent data is available\u2014\n**(1)**\nanalyzes various aspects of Medicare beneficiaries\u2019 access to emergency medical services, including an evaluation of the impact of such model on beneficiary outcomes and resource utilization;\n**(2)**\ncompares beneficiary outcomes under such model with beneficiary outcomes using traditional emergency transportation;\n**(3)**\nassesses the impact of regional variations and demographics on the availability of emergency medical services;\n**(4)**\nidentifies best practices and potential challenges in implementing such model; and\n**(5)**\nincludes recommendations for improving emergency medical services.",
      "versionDate": "2025-11-06",
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
        "actionDate": "2025-04-01",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "2538",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "CARE Act of 2025",
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
        "updateDate": "2025-11-19T15:17:23Z"
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
      "date": "2025-11-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3145is.xml"
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
      "title": "CARE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T11:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "CARE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-13T12:08:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Comprehensive Alternative Response for Emergencies Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-13T12:08:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XI of the Social Security Act to require the Center for Medicare and Medicaid Innovation to test a comprehensive alternative response for emergencies model under the Medicare program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-13T12:03:23Z"
    }
  ]
}
```
