# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6250?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6250
- Title: Cold Weather Diesel Reliability Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6250
- Origin chamber: House
- Introduced date: 2025-11-21
- Update date: 2026-04-22T08:06:47Z
- Update date including text: 2026-04-22T08:06:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-21: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-11-21: Introduced in House

## Actions

- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Introduced in House
- 2025-11-21 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-21",
    "latestAction": {
      "actionDate": "2025-11-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6250",
    "number": "6250",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "B001323",
        "district": "",
        "firstName": "Nicholas",
        "fullName": "Rep. Begich, Nicholas J. [R-AK-At Large]",
        "lastName": "Begich",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "Cold Weather Diesel Reliability Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-22T08:06:47Z",
    "updateDateIncludingText": "2026-04-22T08:06:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-21",
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
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-21",
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
          "date": "2025-11-21T14:04:00Z",
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
      "bioguideId": "M001228",
      "district": "2",
      "firstName": "Celeste",
      "fullName": "Rep. Maloy, Celeste [R-UT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Maloy",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6250ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6250\nIN THE HOUSE OF REPRESENTATIVES\nNovember 21, 2025 Mr. Begich introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require the Administrator of the Environmental Protection Agency to authorize manufacturers of certain vehicles to suspend engine derate or shutdown functions in prolonged cold weather conditions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Cold Weather Diesel Reliability Act of 2025 .\n#### 2. Findings\nCongress finds that\u2014\n**(1)**\ndiesel vehicles are vital for critical transportation and emergency services in cold weather regions;\n**(2)**\nin rural regions with prolonged freezing conditions, diesel exhaust fluid storage, supply, and system functionality are frequently unreliable and logistically impractical on a year-round basis;\n**(3)**\nautomatic engine shutdowns and power reductions due to emissions control malfunctions in extreme cold pose serious, life-threatening risks; and\n**(4)**\nemissions safeguards under the Clean Air Act ( 42 U.S.C. 7401 et seq. ) were never intended to jeopardize human safety or impede critical mobility.\n#### 3. Definitions\nIn this Act:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Environmental Protection Agency.\n**(2) Covered manufacturer**\nThe term covered manufacturer means the manufacturer (as defined in section 216 of the Clean Air Act ( 42 U.S.C. 7550 )) of a covered vehicle or an engine of a covered vehicle.\n**(3) Covered vehicle**\nThe term covered vehicle means an on-highway diesel vehicle or nonroad diesel equipment.\n#### 4. Diesel engine emissions relief in cold weather regions\n##### (a) Cold weather sensor mitigation measures\nNot later than 180 days after the date of enactment of this Act, the Administrator shall revise any applicable regulation under the Clean Air Act ( 42 U.S.C. 7401 et seq. ) that applies to covered vehicles or engines used in covered vehicles to authorize covered manufacturers to suspend inducement-related engine derate or shutdown functions that are triggered by emissions control system faults when ambient temperatures are at or below zero degrees Centigrade and to specify that no party other than a covered manufacturer shall suspend those inducement-related derate or shutdown functions, subject to the conditions that\u2014\n**(1)**\nthe engine returns to normal emission control operation, including inducement enforcement, once ambient temperatures rise above zero degrees Centigrade; and\n**(2)**\ncontinued maximum engine performance when ambient temperatures are at or below zero degrees Centigrade is necessary to prevent occupational danger, equipment failure, or loss of essential transportation functionality in remote areas with limited roadside support or emergency communications access.\n##### (b) Relief to regions with prolonged freezing conditions\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, the Administrator shall revise any applicable regulation under the Clean Air Act ( 42 U.S.C. 7401 et seq. ) to grant a year-round exemption from diesel exhaust fluid system requirements any covered vehicle that\u2014\n**(A)**\nis primarily operated north of 59 degrees north latitude, as demonstrated by documentation of commercial operation, domicile location, or maintenance and dispatch records; or\n**(B)**\nencounters operational or logistical conditions characterized by prolonged ambient temperatures that\u2014\n**(i)**\nare below the freezing point of diesel exhaust fluid; or\n**(ii)**\notherwise make the use of the diesel exhaust fluid system impractical.\n**(2) Scope of relief**\nIn carrying out paragraph (1), the Administrator shall grant to a covered vehicle described in subparagraph (A) or (B) of that paragraph an exemption from any requirement to include an engine derate or shutdown function that is triggered by the absence, degradation, malfunction, or fault of a diesel exhaust fluid system, including any associated sensors or electronic control modules.\n#### 5. Rule of construction\nNothing in this Act waives compliance with any emissions standard under the Clean Air Act ( 42 U.S.C. 7401 et seq. ) outside of\u2014\n**(1)**\nthe temporary cold-weather operational mode authorized under section 4(a); and\n**(2)**\nthe exemption from diesel exhaust fluid system requirements under section 4(b).",
      "versionDate": "2025-11-21",
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
        "actionDate": "2026-03-11",
        "text": "Committee on Environment and Public Works. Hearings held."
      },
      "number": "3135",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Cold Weather Diesel Reliability Act of 2025",
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
        "name": "Environmental Protection",
        "updateDate": "2026-04-10T12:43:45Z"
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
      "date": "2025-11-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6250ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Administrator of the Environmental Protection Agency to authorize manufacturers of certain vehicles to suspend engine derate or shutdown functions in prolonged cold weather conditions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-12T17:24:33Z"
    },
    {
      "title": "Cold Weather Diesel Reliability Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-12T14:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Cold Weather Diesel Reliability Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-12T14:23:19Z"
    }
  ]
}
```
