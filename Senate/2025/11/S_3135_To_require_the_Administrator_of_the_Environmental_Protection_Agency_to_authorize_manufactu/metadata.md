# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3135?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3135
- Title: Cold Weather Diesel Reliability Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3135
- Origin chamber: Senate
- Introduced date: 2025-11-06
- Update date: 2026-05-04T20:21:55Z
- Update date including text: 2026-05-04T20:21:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-06: Introduced in Senate
- 2025-11-06 - IntroReferral: Introduced in Senate
- 2025-11-06 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- 2026-03-11 - Committee: Committee on Environment and Public Works. Hearings held.
- Latest action: 2025-11-06: Introduced in Senate

## Actions

- 2025-11-06 - IntroReferral: Introduced in Senate
- 2025-11-06 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- 2026-03-11 - Committee: Committee on Environment and Public Works. Hearings held.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3135",
    "number": "3135",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "S001198",
        "district": "",
        "firstName": "Dan",
        "fullName": "Sen. Sullivan, Dan [R-AK]",
        "lastName": "Sullivan",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "Cold Weather Diesel Reliability Act of 2025",
    "type": "S",
    "updateDate": "2026-05-04T20:21:55Z",
    "updateDateIncludingText": "2026-05-04T20:21:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-11",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Environment and Public Works. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-11-06",
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
            "date": "2026-03-11T14:30:00Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-11-06T19:32:49Z",
            "name": "Referred To"
          },
          {
            "date": "2025-11-06T19:32:49Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-11-06",
      "state": "WY"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2026-02-26",
      "state": "UT"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2026-03-02",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3135is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3135\nIN THE SENATE OF THE UNITED STATES\nNovember 6, 2025 Mr. Sullivan (for himself and Ms. Lummis ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo require the Administrator of the Environmental Protection Agency to authorize manufacturers of certain vehicles to suspend engine derate or shutdown functions in prolonged cold weather conditions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Cold Weather Diesel Reliability Act of 2025 .\n#### 2. Findings\nCongress finds that\u2014\n**(1)**\ndiesel vehicles are vital for critical transportation and emergency services in cold weather regions;\n**(2)**\nin rural regions with prolonged freezing conditions, diesel exhaust fluid storage, supply, and system functionality are frequently unreliable and logistically impractical on a year-round basis;\n**(3)**\nautomatic engine shutdowns and power reductions due to emissions control malfunctions in extreme cold pose serious, life-threatening risks; and\n**(4)**\nemissions safeguards under the Clean Air Act ( 42 U.S.C. 7401 et seq. ) were never intended to jeopardize human safety or impede critical mobility.\n#### 3. Definitions\nIn this Act:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Environmental Protection Agency.\n**(2) Covered manufacturer**\nThe term covered manufacturer means the manufacturer (as defined in section 216 of the Clean Air Act ( 42 U.S.C. 7550 )) of a covered vehicle or an engine of a covered vehicle.\n**(3) Covered vehicle**\nThe term covered vehicle means an on-highway diesel vehicle or nonroad diesel equipment.\n#### 4. Diesel engine emissions relief in cold weather regions\n##### (a) Cold weather sensor mitigation measures\nNot later than 180 days after the date of enactment of this Act, the Administrator shall revise any applicable regulation under the Clean Air Act ( 42 U.S.C. 7401 et seq. ) that applies to covered vehicles or engines used in covered vehicles to authorize covered manufacturers to suspend inducement-related engine derate or shutdown functions that are triggered by emissions control system faults when ambient temperatures are at or below zero degrees Centigrade and to specify that no party other than a covered manufacturer shall suspend those inducement-related derate or shutdown functions, subject to the conditions that\u2014\n**(1)**\nthe engine returns to normal emission control operation, including inducement enforcement, once ambient temperatures rise above zero degrees Centigrade; and\n**(2)**\ncontinued maximum engine performance when ambient temperatures are at or below zero degrees Centigrade is necessary to prevent occupational danger, equipment failure, or loss of essential transportation functionality in remote areas with limited roadside support or emergency communications access.\n##### (b) Relief to regions with prolonged freezing conditions\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, the Administrator shall revise any applicable regulation under the Clean Air Act ( 42 U.S.C. 7401 et seq. ) to grant a year-round exemption from diesel exhaust fluid system requirements any covered vehicle that\u2014\n**(A)**\nis primarily operated north of 59 degrees north latitude, as demonstrated by documentation of commercial operation, domicile location, or maintenance and dispatch records; or\n**(B)**\nencounters operational or logistical conditions characterized by prolonged ambient temperatures that\u2014\n**(i)**\nare below the freezing point of diesel exhaust fluid; or\n**(ii)**\notherwise make the use of the diesel exhaust fluid system impractical.\n**(2) Scope of relief**\nIn carrying out paragraph (1), the Administrator shall grant to a covered vehicle described in subparagraph (A) or (B) of that paragraph an exemption from any requirement to include an engine derate or shutdown function that is triggered by the absence, degradation, malfunction, or fault of a diesel exhaust fluid system, including any associated sensors or electronic control modules.\n#### 5. Rule of construction\nNothing in this Act waives compliance with any emissions standard under the Clean Air Act ( 42 U.S.C. 7401 et seq. ) outside of\u2014\n**(1)**\nthe temporary cold-weather operational mode authorized under section 4(a); and\n**(2)**\nthe exemption from diesel exhaust fluid system requirements under section 4(b).",
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
        "actionDate": "2025-11-21",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "6250",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Cold Weather Diesel Reliability Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2026-05-04T20:21:47Z"
          },
          {
            "name": "Atmospheric science and weather",
            "updateDate": "2026-05-04T20:21:40Z"
          },
          {
            "name": "Environmental Protection Agency (EPA)",
            "updateDate": "2026-05-04T20:21:54Z"
          },
          {
            "name": "Manufacturing",
            "updateDate": "2026-05-04T20:21:30Z"
          },
          {
            "name": "Motor vehicles",
            "updateDate": "2026-05-04T20:21:22Z"
          }
        ]
      },
      "policyArea": {
        "name": "Environmental Protection",
        "updateDate": "2025-11-19T15:16:11Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3135is.xml"
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
      "title": "Cold Weather Diesel Reliability Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-12T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Cold Weather Diesel Reliability Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-13T12:08:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Administrator of the Environmental Protection Agency to authorize manufacturers of certain vehicles to suspend engine derate or shutdown functions in prolonged cold weather conditions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-13T12:03:25Z"
    }
  ]
}
```
